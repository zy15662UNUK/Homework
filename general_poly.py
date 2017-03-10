def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def x_value(x):
         k = len(L)-1
         out = 0
         for i in range(len(L)):
            out = out + L[i]*x**k
            k = k-1
         return out
    return x_value
        
   
    
    
