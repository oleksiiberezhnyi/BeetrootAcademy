class OpenFile:
    COUNTER = 0
    LOG = []

    def __init__(self, filename: str, option: str = 'r'):
        self._filename = filename
        self._option = option

    @staticmethod
    def get_counter():
        return OpenFile.COUNTER

    @staticmethod
    def get_log():
        return OpenFile.LOG

    def __enter__(self):
        OpenFile.COUNTER += 1
        self.LOG.append([self._filename, self._option])
        try:
            self._file = open(self._filename, self._option)
        except FileNotFoundError:
            raise
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()

# with OpenFile("testfile.txt") as file:
#     print(f'Counter: {OpenFile.get_counter()}')
#     print(f'Log: {OpenFile.get_log()}')
#
# with OpenFile("testfile2.txt", "w+") as file2:
#     print(f'Counter: {OpenFile.get_counter()}')
#     print(f'Log: {OpenFile.get_log()}')
#
# with OpenFile("testfile3.txt", "r") as file3:
#     print(f'Counter: {OpenFile.get_counter()}')
#     print(f'Log: {OpenFile.get_log()}')
