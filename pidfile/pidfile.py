import os


class PIDFile(object):
    __slots__ = ('__file', '__checked')

    def __init__(self, pid_file):
        self.__file = pid_file
        self.__checked = None

    def __check_pid(self):
        if not os.path.exists(self.__file):
            self.__checked = True
            return

        with open(self.__file, "r") as f:
            pid = int(f.read().strip())

            try:
                os.kill(pid, 0)
            except OSError:
                self.__checked = True
                return
            else:
                self.__checked = False
                return

    def __enter__(self):
        self.__check_pid()

        if not self.__checked:
            raise RuntimeError("Program already running.")

        with open(self.__file, "w+") as f:
            f.write(str(os.getpid()))
            f.flush()

    def __exit__(self, *args):
        if self.__checked and os.path.exists(self.__file):
            try:
                os.unlink(self.__file)
            except:
                pass

__all__ = ("PIDFile",)
