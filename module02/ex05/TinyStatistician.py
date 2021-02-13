from math import sqrt


class TinyStatistician:
    def __init__(self):
        pass

    def mean(self, x):
        if len(x) == 0:
            return None
        ret = 0
        for value in x:
            ret += float(value)
        return ret / float(len(x))

    def median(self, x):
        s_len = len(x)
        if s_len == 0:
            return None
        sorted_x = sorted(x)
        if s_len % 2 == 1:
            return float(sorted_x[s_len // 2])
        return self.mean(sorted_x[s_len // 2 - 1: s_len // 2 + 1])

    def quartile(self, x, percentile):
        s_len = len(x)
        if s_len == 0:
            return None
        sorted_x = sorted(x)
        odd_flag = 1 if s_len % 2 == 1 else 0
        if percentile in [1, 25]:
            slice_point = s_len // 2 + odd_flag
            target_list = sorted_x[:slice_point]
        elif percentile in [3, 75]:
            slice_point = s_len // 2
            target_list = sorted_x[slice_point:]

        return self.median(target_list)

    def var(self, x):
        s_len = len(x)
        if s_len == 0:
            return None
        x_mean = self.mean(x)
        sigma2 = 0
        for value in x:
            sigma2 += (value - x_mean) * (value - x_mean)
        return float(sigma2 / s_len)

    def std(self, x):
        if len(x) == 0:
            return None
        return sqrt(self.var(x))


if __name__ == '__main__':
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    print(tstat.mean(a))
    print(tstat.median(a))
    print(tstat.quartile(a, 25))
    print(tstat.quartile(a, 75))
    print(tstat.var(a))
    print(tstat.std(a))
