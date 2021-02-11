import sys
import csv


class CsvReaderError(Exception):
    def __init__(self, text=""):
        self.text = text

    def __str__(self):
        return "CsvReader Error\n" + self.text


class CsvReader():
    def __init__(self,
                 filename=None,
                 sep=',',
                 header=False,
                 skip_top=0,
                 skip_bottom=0):
        try:
            if type(filename) is not str\
               or type(sep) is not str\
               or type(header) is not bool\
               or (type(skip_top) is not int and skip_top >= 0)\
               or (type(skip_bottom) is not int and skip_bottom >= 0):
                raise CsvReaderError('CsvReader arguments is wrong.')
            with open(filename, 'r') as f:
                csv_list = list(csv.reader(f,
                                           delimiter=sep,
                                           skipinitialspace=True))
                col_len = len(csv_list[0])
                if list(filter(lambda x: len(x) != col_len, csv_list)):
                    raise FileNotFoundError()
                if [x for x in csv_list if '' in x]:
                    raise FileNotFoundError()
                if header:
                    start_index = 1 + skip_top
                    self.header = csv_list[0]
                else:
                    start_index = skip_top
                    self.header = None
                if skip_bottom > 0:
                    self.data = csv_list[start_index: -skip_bottom]
                else:
                    self.data = csv_list[start_index:]
        except FileNotFoundError:
            self.data = None
        except CsvReaderError as e:
            print(e)
            sys.exit()
        except Exception as e:
            print("{}:".format(e.__class__.__name__), e)
            sys.exit()

    def __enter__(self):
        if self.data is None:
            return None
        return self

    def __exit__(self, exe_type, exe_value, _):
        if exe_type is not None:
            print("{}:".format(exe_type.__name__), exe_value)
            sys.exit()

    def getdata(self):
        return self.data

    def getheader(self):
        return self.header


if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        data = file.getdata()
        header = file.getheader()
        print(header)
        for row in data:
            print(row)

    print()
    with CsvReader('good.csv', header=True, skip_top=2, skip_bottom=3) as file:
        data = file.getdata()
        header = file.getheader()
        print(header)
        for row in data:
            print(row)

    print()
    with CsvReader('bad.csv') as file:
        if file is None:
            print("File is corrupted")

    print()
    with CsvReader('not_file') as file:
        if file is None:
            print("File is corrupted")

    print()
    with CsvReader('csvreader.py') as file:
        if file is None:
            print("File is corrupted")

    # print()
    # with CsvReader('csvreader.py', header=3) as file:
    #     if file is None:
    #         print("File is corrupted")

    # print()
    # with CsvReader('csvreader.py') as file:
    #     int('a')
