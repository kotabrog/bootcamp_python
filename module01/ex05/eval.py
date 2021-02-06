class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        try:
            if type(coefs) is not list or type(words) is not list\
               or len(coefs) != len(words):
                raise KeyError
            return sum([len(t[1]) * t[0] for t in zip(coefs, words)])
        except Exception:
            return -1

    @staticmethod
    def enumerate_evaluate(coefs, words):
        try:
            if len(coefs) != len(words):
                raise KeyError
            return sum([len(word) * coefs[i] for i, word in enumerate(words)])
        except Exception:
            return -1


if __name__ == '__main__':
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    # words = ["Le", "Lorem", "Ipsum", "est"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    # coefs = [1.0, 2.0, 1.0, 4.0]
    # coefs = 3
    # coefs = "a"
    value = Evaluator.zip_evaluate(coefs, words)
    value = Evaluator.enumerate_evaluate(coefs, words)
    print(value)
