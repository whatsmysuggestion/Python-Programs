def display(n):

    if(n==10):
      return 10
    else:
     print(n)
     return display(n=n+1)

x=eval(input("enter a value"))
print(display(x))
