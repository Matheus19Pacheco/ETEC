def main():
    print("=== Verificador de Triângulo ===")
    
    
    lado_a = float(input("Digite o primeiro lado: "))
    lado_b = float(input("Digite o segundo lado: "))
    lado_c = float(input("Digite o terceiro lado: "))
    
   
    if (lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a):
        print("Os valores PODEM formar um triângulo!")
        
       
        if lado_a == lado_b == lado_c:
            print("O triângulo é EQUILÁTERO.")
        elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
            print("O triângulo é ISÓSCELES.")
        else:
            print("O triângulo é ESCALENO.")
    else:
        print("Os valores NÃO podem formar um triângulo.")

if __name__ == "__main__":
    main()
