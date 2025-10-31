import numpy as np

from lib_template.multiplication.helper import multiply
from lib_template.exponents.helper import square


class Math:

    def __init__(self, x: float) -> None:

        self.x = x


    def square(self) -> float:
        return square(self.x)
    

    def multiply(self, y: float) -> float:
        return multiply(self.x, y)
    

    def add(self, y: float) -> float:
        return float(np.add(self.x, y))
    

if __name__ == '__main__':
    m = Math(x=1.2)
    print(m.add(y=2.3))