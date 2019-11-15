from Calculator import Calculator

def Mean(list):
    # Make this actually do the mean math
    # https://www.tutorialspoint.com/finding-mean-median-mode-in-python-without-libraries
    num_sum = sum(list)
    answer = num_sum / len(list)
    return answer

def PopVariance(list):
    mu = Mean(list)
    for number in list:
        answer =  (Calculator.square(Calculator.subtract(number, mu))) / len(list)
        return answer

def StandardDeviation(list):
    mu = Mean(list)
    for number in list:
        answer =  Calculator.squareRoot((Calculator.square(Calculator.subtract(number, mu))) / len(list))
        return answer

    class Statistics(Calculator):
        result = 0

        def __init__(self):
            pass

        def Mean(self, list):
            self.result = Mean(list)
            return self.result

        def PopVariance(self, list):
            self.result = PopVariance(list)
            return self.result

        def StandardDeviation(self, list):
            self.result = StandardDeviation(list)
            return self.result