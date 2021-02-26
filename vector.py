import numpy as np

##This is the Python Part  of the assignment

# (s)
# Using Python and numpy, implement amag(vec)function to return themagnitude (length) of a 2-dimensional vector (as a numpy array)
def mag(vec):
    vec = np.array(vec)
    ##power of each number
    vec = np.power(vec,2)
    vec = np.sum(vec)
    print(vec)
    return np.sqrt(vec)

print("Lengeth of Vector: (3,5)")
print(mag([3,5]))

# (t)
# Likewise, implement aunit(vec)function to return the unit vector of a2-dimensional vector (as a numpy array).
def unit(vec):
    vec = np.array(vec)
    magnitude = mag(vec)
    vec = np.divide(vec,magnitude)
    return vec

#print("Unit of Vector: (3,2)")
#print(unit([3,2]))
print(mag([7,-2]))
##print(unit([7,-2]))



