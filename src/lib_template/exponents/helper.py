from lib_template.multiplication.helper import multiply


def square(x: float) -> float:
    return multiply(x, x)


if __name__ == '__main__':
    print(square(2.3))