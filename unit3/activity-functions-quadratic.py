import cmath

# quadratic_formula function definition
def quadratic_formula(a,b,c):
    # calculate the discriminant
    d = (b**2) - (4*a*c)
    # find two solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    print('The solution are {0} and {1}'.format(sol1,sol2))
    
    
# call quadratic_formula function   
quadratic_formula(1,2,3)