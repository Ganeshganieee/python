a=10
def outer():
  b=20
  def inner():
    non local b
     c=10
     b=100
     print(b)
     print(c)
 print(b) 
 inner()
 print(b)
outer()
