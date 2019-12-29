def test_args(*kakka):
    print(kakka)

    kakka = kakka[1:]
    print(kakka)
    for kak in kakka:
        print(kak)

    if not kakka:
        print("empty1")
    else:
        print(kakka[0])

    l = len(kakka)
    print(l)

    kakka = kakka[1:]
    print(kakka)
    for kak in kakka:
        print("moi")
        print(kak)

    l = len(kakka)
    print(l)

    if not kakka:
        print("empty2")
    else:
        print(kakka[0])


def test_split_list(lista):
    print(lista)
    lista = lista[1:]
    print(lista)
    lista = lista[1:]
    print(lista)
    lista = lista[1:]
    print(lista)
    lista = lista[1:]
    print(lista)
    lista = lista[1:]
    print(lista)
    lista = lista[1:]


def test_while_if():
    a = False

    while not a:
        if not a:
            print("moi")
        a = True
        if not a:
            print("moimoi")


# test_args("kakka", "kakka")

# test_args()

# test_args("a", "b", "c")

lista = [1, 2, 3]
test_split_list(lista)

test_while_if()