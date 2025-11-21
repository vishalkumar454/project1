# Mini Project: Arithmetic Operations on Complex Numbers (Python)

This project demonstrates how to perform arithmetic and comparison operations on complex numbers using Python classes and operator overloading.  
The custom `complex` class supports addition, subtraction, multiplication, equality check, and comparison between two complex values.

---

## Features

- User-defined **Complex Number Class**
- Function to **display complex numbers**
- Operator overloading for:
  - ➕ Addition (`+`)
  - ➖ Subtraction (`-`)
  - ✖ Multiplication (`*`)
  - 🟰 Equality (`==`)
  - 🔼 Greater than or equal (`>=`)
  - 🔽 Less than or equal (`<=`)

---

## Code Structure

- **Class Definition**
  - `__init__()` → Initialize real & imaginary part
  - `print_complex_number()` → Print complex number in readable form
  - Operator overloaded methods:
    - `__add__(self, other)`
    - `__sub__(self, other)`
    - `__mul__(self, other)`
    - `__eq__(self, other)`
    - `__le__(self, other)`
    - `__ge__(self, other)`

- **Driver Code**
  - Creates two complex numbers
  - Performs arithmetic operations
  - Displays results with output

---

## How to Run

1. Install Python (if not installed)
2. Save the script as `complex_operations.py`
3. Run using terminal or IDE:

```bash
python complex_operations.py
