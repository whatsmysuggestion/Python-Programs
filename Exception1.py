try:
    a = 10
    b=int(input("enter a value"))
    c=a/b
    print(c)


except ZeroDivisionError:
    print("Exception Occured Because Zero Denominator")

except TypeError:
    print("Exception Occured Because Invalid Input")

except Exception:
    print("Some Error Occured")

finally:
    print("End Of Program")



