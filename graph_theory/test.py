
# adding arrays 
# [1,2,] + [1,3,2,] = [1,2,1,3,2]
# (1,2)+(1,3,) = (1,2,1,3)
# {1,2} + {3} : error unsupported
# [2] + (1) : error

# "*" operator
# *(a for a in range(20)) : 0-19
# *(lambda x: x**x) :error
# *(tuple) : tuple, *(1,2,3) : 1 2 3
# *{1,2,3} = 1 2 3 : unpacks
# *[1,2,3] = 1 2 3
# (1,2,3) * 2 = (1,2,3,1,2,3)
# [1,2,3] * 3 = [1,2,3,1,2,3,1,2,3]
# {} * 2 = error tho

# tuples
# a = 1,2,3 : (1,2,3)
# (1,23)*(2) = (1,23,1,23)
# (1,23)*(2,) : error bcos cannot multiply by tuple

# if you dont know how to cast 
# a = 1,2,3 :tuple
# b = [*a] : convert to list
# c = {*b}

# range() 
# range(start,stop,step)
# *range() unpacks to numbers and can be put in arrays
# {8,*range(5)}

print()
