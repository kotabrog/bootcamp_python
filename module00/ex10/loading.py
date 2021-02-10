from time import sleep, perf_counter


class Progress:
    def __init__(self, lst_len):
        self.bar_num = 0
        self.bar = '>                       '
        self.lst_len = lst_len
        self.count = 0
        self.percent = 0
        self.start_time = perf_counter()
        self.eta = 0
        self.elapsed = 0

    def update(self):
        self.count += 1
        self.percent = self.count / self.lst_len
        temp_num = int(self.percent * 100 / 4)
        if temp_num > self.bar_num:
            self.bar_num = temp_num
            self.bar = '=' * min(temp_num, 23)\
                + '>' + ' ' * max(23 - temp_num, 0)
        self.elapsed = perf_counter() - self.start_time
        self.eta = (self.lst_len - self.count) * self.elapsed / self.count

    def print_progress(self):
        print('\rETA: {:.2f}s '.format(self.eta)
              + '[{:4.0%}][{}] '.format(self.percent, self.bar)
              + '{}/{} | '.format(self.count, self.lst_len)
              + 'elapsed time {:.2f}'.format(self.elapsed), end='')

    def print_end(self):
        print('\rETA: 0.00s [100%][========================] '
              + '{}/{} | '.format(self.count, self.lst_len)
              + 'elapsed time {:.2f}s'.format(self.elapsed))


def ft_progress(lst):

    progress = Progress(len(lst))
    for x in lst:
        progress.update()
        progress.print_progress()
        yield x
    progress.print_end()


if __name__ == '__main__':
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)
