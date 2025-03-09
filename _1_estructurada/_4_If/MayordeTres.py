if __name__ == '__main__':
    a=int(input("Proporciona un numero: "))
    b=int(input("Proporciona otro numero: "))
    c=int(input("Proporciona un úlimo numero: "))

    if a>b:
        if a>c:
            print (f"El número mayor es {a}")
        else:
            print (f"El número mayor es {c}")
    else:
        if b>c:
            print (f"El número mayor es {b}")
        else:
            print (f"El número mayor es {c}")
