class A:
    pass


a = 1


def fun():
    b = 2
    print locals()


print globals()
fun()
