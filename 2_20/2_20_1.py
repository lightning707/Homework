import datetime


class CustomOpen:
    _counter = 0

    def __init__(self, file, mode='r', log_file='logs.txt', log_mode='a'):
        self.mode = mode
        self.file = file
        self.log_file = log_file
        self.log_mode = log_mode

    def __enter__(self):
        self.fd = open(self.file, self.mode)
        self.__class__._counter += 1
        self.write_log()
        return self.fd

    def __exit__(self, exc_type, exc_val, exc_tb):
        return None

    def write_log(self):
        with open(self.log_file, self.log_mode) as logs:
            logs.write(f"{datetime.datetime.now()}: {self.__class__._counter} time(s)\n")


with CustomOpen('text.txt', 'a') as text_file:
    text_file.write('asdasd')

with CustomOpen('text.txt', 'a') as text_file:
    text_file.write('123')

with CustomOpen('text.txt', 'a') as text_file:
    text_file.write('qwe')
