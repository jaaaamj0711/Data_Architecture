class adam: 
  def __init__(self):
    print('생성')
    
def sum_two(self, a, b):
  return a + b

def get_biggest(self, x): 
  :param x: list of int 
  :type x: list 
  :return: The biggest int value 
  :rtype: int 
  """ 
  ret = x[0] 
  for i in range(1, len(x)): 
    if x[i] > ret: 
      ret = x[i] 
  return ret
  
a = adam() 
print('sum_two() result = ', a.sum_two(1, 3)) 
print('get_biggest() result = ', a.get_biggest([5,3,4,-10,0]))
