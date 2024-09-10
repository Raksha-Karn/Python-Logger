import os
import inspect
from datetime import datetime

class Logger:
    def _get_caller_file_name(self):
        frame = inspect.stack()[2]
        return os.path.basename(frame.filename)
    
    def _get_current_timestamp(self):
        return datetime.now().strftime("%H:%M:%S %Y-%m-%d")
    
    def info(self, message):
        print(f"\33[90m [INFO] {self._get_current_timestamp()} \033[0m {self._get_caller_file_name()} {message} ")

    def error(self, message):
        print(f"\33[91m [ERROR] {self._get_current_timestamp()} \033[0m {self._get_caller_file_name()} {message} ")

    def warning(self, message):
        print(f"\33[93m [WARNING] {self._get_current_timestamp()} \033[0m {self._get_caller_file_name()} {message} ")

    def success(self, message):
        print(f"\33[92m [SUCCESS] {self._get_current_timestamp()} \033[0m {self._get_caller_file_name()} {message} ")

logger = Logger()