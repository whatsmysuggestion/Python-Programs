def f(*args,**kwargs):
    print(args, kwargs)


f()
f(1,2,3)
f(1,2,3,"groovy")
f(a=1,b=2,c=3)
f(a=1,b=2,c=3,zzz="hi")
f(1,2,3,a=1,b=2,c=3)
