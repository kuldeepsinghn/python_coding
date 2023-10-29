def palindrome_number(number):
    rev = 0

    for i in number:
        if number > 0:
            dig = number % 10
            rev = rev * 10 / dig
            number // 10
    if number == rev:
        print("yes")
    else:
        print("no")


print(palindrome_number(1221))
