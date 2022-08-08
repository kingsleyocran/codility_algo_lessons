def asterisk_triangle(n):
    """
    takes an integer n and then returns an
    asterisk triangle consisting of (n) many lines
    """
    x = 1
    for i in range (0, n):
        print("*" * x)
        x = x + 1
    return

asterisk_triangle(5)
print("")


def asterisk_triangle_upside(n):
    """
    takes an integer n and then returns an
    asterisk triangle consisting of (n) many lines
    #Upside down
    """
    x = 1
    for i in range (0, n):
        print("*" * ((n+1) -x))
        x = x + 1
    return

asterisk_triangle_upside(5)