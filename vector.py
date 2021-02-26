import numpy as np

##This is the Python Part  of the assignment

# (s)
# Using Python and numpy, implement amag(vec)function to return themagnitude (length) of a 2-dimensional vector (as a numpy array)
def mag(vec):
    if isinstance(vec,(np.ndarray,tuple,list)) and len(vec) == 1:
        return None
    vec = np.array(vec)
    ##power of each number
    vec = np.power(vec,2)
    vec = np.sum(vec)
    return np.sqrt(vec)

print("Lengeth of Vector: (3,5)")
print(mag([3,5]))

# (t)
# Likewise, implement aunit(vec)function to return the unit vector of a2-dimensional vector (as a numpy array).
def unit(vec):
    if isinstance(vec,(np.ndarray,tuple,list)) and len(vec) == 1:
        return None
    vec = np.array(vec)
    magnitude = mag(vec)
    return np.divide(vec,magnitude)

print("Unit of Vector: (3,2)")
print(unit([3,2]))

# (u)
#  Rotating a 2D vector 90 degrees counter clockwise is done by swapping xand y, and negating the new x.  Implementrot90(vec).  It must return anew numpy array, that is a 90 degree rotation of thevecinput
def rot90(vec):
    vec = np.array(vec)
    x = vec[0]
    y = vec[1]
    vec[0] = -y
    vec[1] = x
    return vec;

print("Rotated  vector: (3,2)")
print(rot90([3,2]))

#Solve the followingusing Python, given a = (3,2), b = (8,7), c=1,5
#(y)2·~a
a = [3,2]
b = [8,7]
c = [1,5]
print("2*~a gives this vector:")
print(np.multiply(a,2))
#(w)~a+~b-~c
print("a+~b-~c")
print(np.subtract(np.add(a,b), c))
#(x) Usehelp(numpy)(or online documentation) to find out how to find thedotproduct of two vectors.  (hint:  in thehelpprompt, you can search bypressing /, then typing text, thenenter, thennorshift-nto navigatethe search results!)
print("You find the dot product by using np.dot[vec1,vec2], here is an example using vector from assignment q:")
print(np.dot([2,3],[4,6]))
#(y) Using numpy, find~a·~a.  Compare withmag(a)*mag(a)
print("numpy ~a*~a =" + str(np.dot(a,a)) + " my mag function mag(a)*mag(a) = " + str(mag(a)*mag(a)))
#(z) Using numpy, find ~a*~b
print("~a*~b =")
print(np.dot(a,b))
#(æ) Using  your rot90function,  find  the  dot  product  ofaand  its  rotation.(That is, given~ar=rot90(a), find~a·~ar)
print("~a*rot90(a) = ")
print(np.dot(a,rot90(a)))









