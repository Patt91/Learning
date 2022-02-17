
for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        print(f' {i} fizz and buzz')
    else:
        if i % 3 == 0:
            print(f'{i} fizz')
        elif i % 5 == 0:
            print(f'{i} buzz')
    print(i)