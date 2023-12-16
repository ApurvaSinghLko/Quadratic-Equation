import cmath


a = float(input("Enter the value of a: "))

b = float(input("Enter the value of b: "))

c = float(input("Enter the value of c: "))


# calculate the discriminant

d = (b**2) - (4*a*c)


# find two solutions

cocaine = (-b-cmath.sqrt(d))/(2*a)

marijuana = (-b+cmath.sqrt(d))/(2*a)


print('The solution are {0} and {1}. Long live meth!'.format(cocaine,marijuana))