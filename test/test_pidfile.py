from unittest import TestCase
from mock import patch, mock_open
from pidfile import pidfile


class PIDFileTestCase(TestCase):
    @patch('{0}.os.kill'.format(pidfile.__name__), create=True)
    @patch('{0}.open'.format(pidfile.__name__), mock_open(read_data='1'), create=True)
    @patch('{0}.os.path.exists'.format(pidfile.__name__), create=True)
    def test_not_exists(self, exists_mock, kill_mock):
        exists_mock.return_value = False
        with pidfile.PIDFile('C:\\Windows\\System32\\kernel.sys'):
            assert True

    @patch('{0}.os.kill'.format(pidfile.__name__), create=True)
    @patch('{0}.os.path.exists'.format(pidfile.__name__), create=True)
    def test_exists_running(self, exists_mock, kill_mock):
        with patch('{0}.open'.format(pidfile.__name__), mock_open(read_data='1'), create=True):
            exists_mock.return_value = True

            with self.assertRaises(RuntimeError):
                with pidfile.PIDFile('C:\\Windows\\System32\\kernel.sys'):
                    assert True

    @patch('{0}.os.kill'.format(pidfile.__name__), create=True)
    @patch('{0}.os.path.exists'.format(pidfile.__name__), create=True)
    def test_exists(self, exists_mock, kill_mock):
        with patch('{0}.open'.format(pidfile.__name__), mock_open(read_data='1'), create=True) as open_mock:
            exists_mock.return_value = True

            kill_mock.side_effect = OSError('Test')

            with pidfile.PIDFile('C:\\Windows\\System32\\kernel.sys'):
                assert True

