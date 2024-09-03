# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
def fibonnaci_sequence(n):
    numOne, numTwo = 0, 1
    if n == numOne or n == numTwo:
        return f"O número {n} pertence a sequência de Fibonnaci"
    while numTwo < n:
        n3 = numOne + numTwo
        numOne, numTwo = numTwo, n3
    if numTwo == n:
        return f"O número {n} pertence a sequência de Fibonnaci"
    return f"O número {n} não pertence a sequência de Fibonnaci"

# Test case:
for i in range(0,40):
    print(fibonnaci_sequence(i))
print()



# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

# IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
def verify_string(s):
    return s.lower().count('a')

print(verify_string("apple"))
print(verify_string("bubble"))
print(verify_string("management"))
print(verify_string("ebcaaafdea"))
print(verify_string("AAAuAa"))
print()



# 3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

# Ao final do processamento, qual será o valor da variável SOMA?
def result_soma():
    index, soma, k = 12, 0, 1
    while k < index:
        k += 1
        soma += k
    return soma
print(result_soma()) # OUTPUT: 77



# 4) Descubra a lógica e complete o próximo elemento:
# a) 1, 3, 5, 7, 9
# b) 2, 4, 8, 16, 32, 64, 128
# c) 0, 1, 4, 9, 16, 25, 36, 49
# d) 4, 16, 36, 64, 100
# e) 1, 1, 2, 3, 5, 8, 13
# f) 2, 10, 12, 16, 17, 18, 19, 20



# 5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

# Passo 1 (sala dos interruptores):
# - Ligar o primeiro interruptor e deixar ligado
# - Ligar o segundo interruptor, deixar ligado por 15 minutos, depois desse tempo, desligar ela.
# - Não faça nada com o terceito interruptor

# Passo 2 (1 ida):
# - Entrar em uma das salas com lâmpada
# - Veja a lâmpada e toque para sentir a temperatura

# Passo 3:
# - Volte na sala dos interruptores mas não faça nada

# Passo 4 (2 ida):
# - Entrar em outra sala diferente
# - Veja a lâmpada e toque para sentir a temperatura

# Conclusão: 
# - Se a lâmpada estiver acesa então ela pertence ao primeiro interruptor
# - Se a lâmpada estiver apagada, mas quente ao toque, então ela corresponde ao segundo interruptor.
# - Se a lâmda estiver apagada e fria ao toque, então ela corresponde ao terceito interruptor
