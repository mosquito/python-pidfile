import atexit
import os
from typing import Any

import psutil


class AlreadyRunningError(Exception):
    pass


class PIDFile(object):
    def __init__(self, filename: Any = "pidfile"):
        self._process_name = psutil.Process(os.getpid()).cmdline()[0]
        self._file = str(filename)

    @property
    def is_running(self) -> bool:
        if not os.path.exists(self._file):
            return False

        with open(self._file, "r") as f:
            try:
                pid = int(f.read())
            except (OSError, ValueError):
                return False

        if not psutil.pid_exists(pid):
            return False

        try:
            cmd1 = psutil.Process(pid).cmdline()[0]
            return cmd1 == self._process_name
        except psutil.AccessDenied:
            return False

    def close(self) -> None:
        if os.path.exists(self._file):
            try:
                os.unlink(self._file)
            except OSError:
                pass

    def __enter__(self) -> "PIDFile":
        if self.is_running:
            raise AlreadyRunningError

        with open(self._file, "w") as f:
            f.write(str(os.getpid()))

        atexit.register(self.close)

        return self

    def __exit__(self, *_) -> None:
        self.close()
        atexit.unregister(self.close)
