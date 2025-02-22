import math

def calculate_square_root(num1: float, num2: float, first_number_as_main: bool = True) -> float:
  """
  Calcula la raíz cuadrada de un número con respecto a otro.

  Args:
    num1: El primer número.
    num2: El segundo número.
    first_number_as_main: Si es True, num1 es la base y num2 el exponente. Si es False, num2 es la base y num1 el exponente.

  Returns:
    La raíz cuadrada calculada.
  """
  if first_number_as_main:
    return math.pow(num1, 1 / num2)
  else:
    return math.pow(num2, 1 / num1)

# Ejemplos de uso
print(calculate_square_root(9, 2))  # Raíz cuadrada de 9 (resultado: 3.0)
print(calculate_square_root(27, 3)) # Raíz cúbica de 27 (resultado: 3.0)
print(calculate_square_root(4, 2, first_number_as_main=False)) # 2 elevado a la 1/4 (resultado: 1.189207115002721)