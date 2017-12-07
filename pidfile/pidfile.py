import os

import psutil


class PIDFile(object):
    __slots__ = ('__file', '__checked', '__process')

    def __init__(self, pid_file):
        self.__file = pid_file
        self.__checked = None
        self.__process = psutil.Process(os.getppid())

    def check_process(self, pid):
        try:
            cmd1 = psutil.Process(pid).cmdline()[:1]
            cmd2 = self.__process.cmdline()[:1]
            return cmd1 != cmd2
        except psutil.AccessDenied:
            return False

    def check_pid(self):
        """
        Returns `True` if process which created pid-file is
        already dead or has different script name.

        :return: bool
        """
        if not os.path.exists(self.__file):
            return True

        with open(self.__file, "r") as f:
            try:
                pid = int(f.read().strip())
            except Exception:
                return True

        try:
            os.kill(pid, 0)
        except OSError:
            return True

        return self.check_process(pid)

    def __enter__(self):
        result = self.check_pid()

        if not result:
            raise RuntimeError("Program already running.")

        with open(self.__file, "w+") as f:
            f.write(str(os.getpid()))
            f.flush()

    def __exit__(self, *args):
        if self.__checked and os.path.exists(self.__file):
            try:
                os.unlink(self.__file)
            except Exception:
                pass


__all__ = ("PIDFile",)
