import os
from unittest import TestCase
from unittest.mock import mock_open, patch

import psutil

import pidfile


builtins_open = open


def open_patcher(data):
    def patched_open(*args, **kwargs):
        if args[0] == "pidfile":
            return mock_open(read_data=data)(*args, **kwargs)
        else:
            return builtins_open(*args, **kwargs)
    return patched_open


def open_patcher_exception():
    def patched_open(*args, **kwargs):
        if args[0] == "pidfile":
            mo = mock_open()
            mo.return_value.read.side_effect = OSError
            return mo(*args, **kwargs)
        else:
            return builtins_open(*args, **kwargs)
    return patched_open


class PIDFileTestCase(TestCase):
    @patch("builtins.open", new=open_patcher("1"))
    @patch("os.path.exists")
    def test_pidfile_not_exists(self, exists_mock):
        exists_mock.return_value = False
        with pidfile.PIDFile():
            assert True

    @patch("builtins.open", new=open_patcher("1"))
    @patch("psutil.pid_exists")
    @patch("psutil.Process")
    @patch("os.path.exists")
    def test_pidfile_exists_process_running(
        self, exists_mock, Process_mock,
        pid_exists_mock,
    ):
        exists_mock.return_value = True
        pid_exists_mock.return_value = True
        Process_mock.return_value = psutil.Process(os.getpid())
        with self.assertRaises(pidfile.AlreadyRunningError):
            with pidfile.PIDFile():
                assert True

    @patch("builtins.open", new=open_patcher("1"))
    @patch("psutil.pid_exists")
    @patch("os.path.exists")
    def test_pidfile_exists_process_not_running(
        self, exists_mock,
        pid_exists_mock,
    ):
        exists_mock.return_value = True
        pid_exists_mock.return_value = False
        with pidfile.PIDFile():
            assert True

    @patch("builtins.open", new=open_patcher(""))
    @patch("psutil.pid_exists")
    @patch("os.path.exists")
    def test_pidfile_exists_empty(self, exists_mock, pid_exists_mock):
        exists_mock.return_value = True
        pid_exists_mock.return_value = True
        with pidfile.PIDFile():
            assert True

    @patch("builtins.open", new=open_patcher_exception())
    @patch("psutil.pid_exists")
    @patch("os.path.exists")
    def test_pidfile_exists_read_fail(self, exists_mock, pid_exists_mock):
        exists_mock.return_value = True
        pid_exists_mock.return_value = True
        with pidfile.PIDFile():
            assert True
