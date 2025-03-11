
a = float(input("Informe A:  "))
b = float(input("Informe B: "))
menu = int(input("Digite menu 1-6"))
match menu:
    #Soma
    case 1:
        #print(a+b)
        c=(a+b)
    #Subtração
    case 2:
        #print(a-b)
        c=(a-b)
    #Multiplicação
    case 3:
        #print(a*b)
        c=(a*b)
    #Divisão
    case 4:
        #print(a/b)
        c=(a/b)
    #Potencia
    case 5:
        #print(a**b)
        c=(a**b)
    #Raiz
    case 6:
       #print(a**(1/b))
        c=(a**(1/b))