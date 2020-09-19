a = range(1,101)
for i in a:
     if i % 7 == 0:
        continue
    elif i % 10 ==7:
        continue
    elif i//10 ==7:
        continue
    else:
        print(i)
