from conversor import celsius_para_fahrenheit, fahrenheit_para_celsius

def main():
    print("Conversor de Temperatura")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    opcao = int(input("Escolha uma opção (1 ou 2): "))
    
    if opcao == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))
        resultado = celsius_para_fahrenheit(celsius)
        print(f"{celsius}°C = {resultado:.2f}°F")
    
    elif opcao == 2:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        resultado = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit}°F = {resultado:.2f}°C")
    
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
