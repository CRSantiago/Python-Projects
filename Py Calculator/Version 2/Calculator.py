class Calculator():

    def __init__(self,numbers):
        self.numbers = numbers

    def add(self):
        sum = 0
        for num in self.numbers:
            sum += num
        return sum

    def subtract(self):
        sum = self.numbers[0]
        for num in self.numbers[1:]:
            sum -= num
        return sum

    def multiply(self):
        product = 1
        for num in self.numbers:
            product *= num
        return product

    def division(self):
        qoutient = self.numbers[0]
        for num in self.numbers[1:]:
            qoutient /= num
        return qoutient