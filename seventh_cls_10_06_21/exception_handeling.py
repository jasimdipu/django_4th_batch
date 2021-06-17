try:
    a = 10
    b = 0

    if a < 0 or b < 0:
        raise ValueError
    print(a + b)
    print(a / b)
except Exception as e:
    print("Negetive Value is not exceptable")
# prin("")
print("Django")

age = int(input())


# custom error class
class AgeException(Exception):
    pass


try:
    if age < 18:
        raise AgeException
    if age > 60:
        raise AgeException
except AgeException as e:
    print("Age is not perfect")


class AlphabeticException(Exception):
    pass


try:
    # alp = input()
    alp = int(input())
    if type(alp) == int or type(alp) == float:
        raise AlphabeticException
except Exception:
    print("Please enter an elphabet")
