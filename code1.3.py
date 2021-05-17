x = 20
y = 40

z = x
x = y
y = z

# without using third var.
x,y = y,x
print(y)
print(x)