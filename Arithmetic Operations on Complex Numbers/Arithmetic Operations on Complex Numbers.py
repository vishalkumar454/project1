# Mini project : Arithmetic Operation on complex numbers

class complex:
    def __init__(self, real, imag = 0.0):
        self.real = real
        self.imag = imag

    def print_complex_number(self):
        print('(',self.real,',',self.imag,')')

    def __add__(self, other):
        return complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return complex(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other):
        return complex(self.real * other.real
                      - self.imag * other.imag,
                       self.imag * other.real
                       + self.real * other.imag)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __le__(self, other):
        return self.real < other.real and self.imag < other.imag

    def __ge__(self, other):
        return self.real >= other.real and self.imag >= other.imag


C1 = complex(2,1)
print('First complex number is as fallows:')
C1.print_complex_number()

C2 = complex(5,6)
print('Second complex number is as fallows:')
C2.print_complex_number()

print('Addition of two complex number is as fallows:')
C3 = C1 + C2
C3.print_complex_number()

print('Subtraction of two complex number is as fallows:')
C4 = C1 - C2
C4.print_complex_number()

print('Multiplication of two complex number is as fallows:')
C4 = C1 * C2
C4.print_complex_number()

print('Compare of two complex number:')
print((C1 == C2))  # Returns true is equal
# Returns False if not

print('Checking if C1 is greater then C2')
print((C1 >= C2))

print('Checking if C1 is greater then C2')
print((C1 <= C2))