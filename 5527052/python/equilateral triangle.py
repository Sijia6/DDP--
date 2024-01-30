def print_equilateral_triangle(n):
    """Print an equilateral triangle with n lines."""
    for i in range(1, n+1):
        print(' ' * (n - i) + '*' * (2*i - 1))


print_equilateral_triangle(5)
