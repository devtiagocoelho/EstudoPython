# gerador_senhas.py
# Este projeto gera senhas aleatórias seguras com letras, números e símbolos.
# O usuário pode escolher o tamanho da senha.

import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def menu():
    while True:
        print("\n=== GERADOR DE SENHAS ===")
        try:
            tamanho = int(input("Digite o tamanho da senha (mínimo 4): "))
            if tamanho < 4:
                print(" O tamanho mínimo é 4.")
                continue
            senha = gerar_senha(tamanho)
            print(f" Sua senha é: {senha}")
        except ValueError:
            print(" Digite um número válido.")
            continue
        
        if input("Gerar outra senha? (s/n): ").lower() != "s":
            print("Até mais!")
            break

if __name__ == "__main__":
    menu()
