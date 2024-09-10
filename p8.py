z=lambda x,y : print(f"default argument {x+y}")
z(6,7)
z=lambda y,x :  print(f"postional argument {x} and {y}")
x,y=2,20
z(x,y)
z=lambda x,y :  print(f"keyword argument {x+y}")
z(x=1,y=7)
z=lambda *x :  print(f"arbitary argument {x}")
x=[1,2,3]
z(x)