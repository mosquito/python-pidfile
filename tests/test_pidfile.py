from unittest import TestCase

try:
    from mock import patch, mock_open
except ImportError:
    from unittest.mock import patch, mock_open

import pidfile
import os
import psutil

class PIDFileTestCase(TestCase):
    @patch('builtins.open', mock_open(read_data='1'))
    @patch('psutil.pid_exists')
    @patch('os.path.exists')
    def test_pidfile_not_exists(self, exists_mock, pid_exists_mock):
        exists_mock.return_value = False
        with pidfile.PIDFile():
            assert True


    @patch('builtins.open', mock_open(read_data='1'))
    @patch('psutil.pid_exists')
    @patch('psutil.Process')
    @patch('os.path.exists')
    def test_pidfile_exists_process_running(self, exists_mock, Process_mock, pid_exists_mock):
        exists_mock.return_value = True
        Process_mock.return_value = psutil.Process(os.getpid())
        with self.assertRaises(pidfile.AlreadyRunningError):
            with pidfile.PIDFile():
                assert True


    @patch('builtins.open', mock_open(read_data='1'))
    @patch('psutil.pid_exists')
    @patch('os.path.exists')
    def test_pidfile_exists_process_not_running(self, exists_mock, pid_exists_mock):
        exists_mock.return_value = True
        pid_exists_mock.return_value = False
        with pidfile.PIDFile():
            assert True
