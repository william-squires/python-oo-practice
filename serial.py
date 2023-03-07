class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """initializes SerialGenerator.
        Start is where we start generating numbers
        Count is how many we have incremented
        Count begins at -1 so our first number generated == count
        """
        self.start = start
        self.count = -1

    def generate(self):
        """increment our counter and return a new serial number"""
        self.count += 1
        return self.start + self.count
    
    def reset(self):
        """reset our count to -1 so our first number == start"""
        self.count = -1