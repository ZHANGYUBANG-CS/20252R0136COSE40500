def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("팩토리얼을 구할 숫자를 입력하세요: "))
print(f"{num}! = {factorial(num)}")