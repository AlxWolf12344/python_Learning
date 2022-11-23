# count back from 50 -> user
import time

def count_back():
    print(f'{"*" * 75} \nThis program is made to count from 50 in back count to 0 or personal input\n{"*" * 75}')
    start, number = 50, int(input("Enter the end number from the count down: "))
    while start > number:
        start -= 1
        time.sleep(0.5)
        print(start)
    if number > start:
        print("You should enter a number less than 50")


count_back()
