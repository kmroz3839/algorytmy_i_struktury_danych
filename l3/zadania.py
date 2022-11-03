#zadanie 1
def numbers(n: int):
    print(n)
    if n != 0:
        if n > 0:
            numbers(n-1)
        else:
            numbers(n+1)

numbers(10)


#zadanie 2
def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(7))


#zadanie 3
def power(number: int, n: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return number
    else:
        return number * power(number,n-1)

print(power(2,6))


#zadanie 4
def reverse(txt: str) -> str:
    return txt[::-1]

print(reverse("SUGOMA"))


#zadanie 5
def factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n

print(factorial(10))


#zadanie 6
def prime(n: int) -> bool:
    return False
    #nie wiem jak to zrobić rekurencyjnie


#zadanie 7
def n_sums(n: int) -> list[int]:
    return None
    #nie wiem
