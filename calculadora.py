import sys
import os

def operacao(ope):
    for i in range(1000):
        try:
            print("\nDigite o primeiro número:", end=" ")
            n1 = float(input())
            print("Digite o segundo número:", end=" ")
            n2 = float(input())
            break
        except ValueError:
            print("Por favor, digite um número")
    if ope=='+':
        resultado = n1+n2
        print("Resultado: {0} + {1} = {2}\n".format(n1, n2, resultado))
    if ope=='-':
        resultado = n1-n2
        print("Resultado: {0} - {1} = {2}\n".format(n1, n2, resultado))
    if ope=='*':
        resultado = n1*n2
        print("Resultado: {0} * {1} = {2}\n".format(n1, n2, resultado))
    if ope=='/':
        if n2==0:
            print("Divisão por zero não é permitida\n")
            return 0
        else:
            resultado = n1/n2
            print("Resultado: {0} / {1} = {2}\n".format(n1, n2, resultado))
    for i in range(1000):
        print("Gostaria de salvar as operações em um arquivo txt? (s/n):", end="")
        es = input()
        if es == 's' or es == 'S':
            with open("histórico de operações.txt", "a") as arquivo:
                arquivo.write(f"{n1} {ope} {n2} = {resultado}")
                arquivo.write("\n")
            break
        if es == 'n' or es == 'N':
            break
        print("Resposta inválida. Por favor, digite 's' para sim, ou 'n' para não\n")

for i in range(1000):

    print("===============================")
    print("   Calculadora Simples")
    print("===============================")
    print("Selecione uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    print("6. Imprimir histórico de operações")
    print("7. Apagar o histórico de operações")
    print("Opção:", end=" ")

    for i in range(1000):
        try:
            esc = int(input())
            if esc < 1 or esc > 7:
                raise(ValueError)
            else:
                break
        except ValueError:
            print("Por favor, digite uma opcao valida")

    if esc==1:
        operacao('+')
    if esc==2:
        operacao('-')
    if esc==3:
        operacao('*')
    if esc==4:
        operacao('/')
    if esc==5:
        print("Adeus!")
        sys.exit()
    if esc==6:
        print("")
        with open("histórico de operações.txt", "r") as arquivo:
            for linha in arquivo:
                print(linha, end="")
        print("")
    if esc==7:
        os.remove("histórico de operações.txt")
    

    for i in range(1000):
        print("Deseja realizar outra operação? (s/n):", end="")
        res = input()
        if res == 's' or res == 'S':
            print("\n")
            break
        if res == 'n' or res == 'N':
            print("Obrigado por usar a calculadora, até a próxima!")
            sys.exit()
        print("Resposta inválida. Por favor, digite 's' para sim, ou 'n' para não\n")