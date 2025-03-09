if __name__ == '__main__':
    n1=input("Ingres el primer nombre: ")
    n2=input("Ingres un segundo nombre: ")

    t1=len(n1)
    t2=len(n2)

    if t1==t2:
        print(f"los nombres {n1} y {n2} tienen el mismo tamaño")
    elif t1>t2:
        print("El nombre mas largo es ", n1)
    else:
        print("El nombre mas largo es "+ n2)

