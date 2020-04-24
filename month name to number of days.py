while True:
    a = ['january', 'march',  'may', 'july', 'august', 'october',  'december']
    b = ['april', 'june', 'september', 'november']
    c = ['february']
    d = input("Please enter a Month> ").lower()

    if d in a:
        print(f'31 days in {d.capitalize()}')
        break
    elif d in b:
        print(f'30 days in {d.capitalize()}')
        break
    elif d in c:
        print(f'29 or 28 days in {d.capitalize()}')
        break
    else:
        print("Invalid Value")