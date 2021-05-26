while True:
    number = int(input("Enter a number that you want to check "))
    result = 0
    num = number
    while num > 0:
        d = (num % 10) ** 3
        num = num // 10
        result+=d
    if result==number:
        print("It's a armstrong number")
    else:
        print("It's not a armstrong number")
    wannaop=input("If you want to check another number write y ")
    if wannaop=="y":
        continue
    else:
        break
