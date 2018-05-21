from unittest import TestCase

try:
    # Python 2.7
    from mock import patch, mock_open
    open_name = '__builtin__.open'
except ImportError:
    # Python 3.x
    from unittest.mock import patch, mock_open
    open_name = 'builtins.open'

import pidfile
import os
import psutil


builtins_open = open
mocked_open = mock_open(read_data='1')


def patched_open(*args, **kwargs):
    if args[0] == 'pidfile':
        return mocked_open(*args, **kwargs)
    else:
        return builtins_open(*args, **kwargs)


class PIDFileTestCase(TestCase):
    @patch(open_name, new=patched_open)
    @patch('psutil.pid_exists')
    @patch('os.path.exists')
    def test_pidfile_not_exists(self, exists_mock, pid_exists_mock):
        exists_mock.return_value = False
        with pidfile.PIDFile():
            assert True

    @patch(open_name, new=patched_open)
    @patch('psutil.pid_exists')
    @patch('psutil.Process')
    @patch('os.path.exists')
    def test_pidfile_exists_process_running(self, exists_mock, Process_mock, pid_exists_mock):
        exists_mock.return_value = True
        Process_mock.return_value = psutil.Process(os.getpid())
        with self.assertRaises(pidfile.AlreadyRunningError):
            with pidfile.PIDFile():
                assert True

    @patch(open_name, new=patched_open)
    @patch('psutil.pid_exists')
    @patch('os.path.exists')
    def test_pidfile_exists_process_not_running(self, exists_mock, pid_exists_mock):
        exists_mock.return_value = True
        pid_exists_mock.return_value = False
        with pidfile.PIDFile():
            assert True
