a=42
b=0
print
try:
    print(a/b)
except ZeroDivisionError as e:
    print('not allowed')
else:
    print('Something else went wrong')
finally:
    print('this is clean up code')
print