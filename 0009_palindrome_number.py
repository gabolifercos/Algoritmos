"""
LeetCode #9 - Palindrome Number
Dificuldade : Easy
Link        : https://leetcode.com/problems/palindrome-number/
Tópicos     : Matemática, Strings
Linguagem   : Python 3
Status      : [x] Resolvi sozinho   [ ] Resolvi com ajuda   [ ] Não consegui

================================================================================
ENUNCIADO (traduzido)
================================================================================
Dado um inteiro x, retorne True se x for um palíndromo e False caso contrário.

Um inteiro é palíndromo quando ele se lê da mesma forma da esquerda para a
direita e da direita para a esquerda.

Exemplo 1:
    Entrada: x = 121
    Saída  : True
    Explicação: 121 lido ao contrário continua 121.

Exemplo 2:
    Entrada: x = -121
    Saída  : False
    Explicação: da esquerda para a direita é -121; da direita para a esquerda
                é 121-. Portanto não é palíndromo.

Exemplo 3:
    Entrada: x = 10
    Saída  : False
    Explicação: lido ao contrário vira 01. Portanto não é palíndromo.

Restrições:
    -2^31 <= x <= 2^31 - 1

Desafio extra (follow-up): consegue resolver SEM converter o número em string?

================================================================================
COMO USAR ESTE ARQUIVO
================================================================================
- O LeetCode entrega a função dentro de `class Solution`. Você só precisa
  escrever o corpo do método. O `self` é obrigatório como primeiro parâmetro,
  mas pode ignorá-lo por enquanto.
- Para copiar para o LeetCode, leve só a `class Solution` da seção 1.
- Rode `python 0009_palindrome_number.py` para testar com os exemplos.

================================================================================
DICA INICIAL (leia só se travar)
================================================================================
Pense em como você faria no papel. Um número negativo pode ser palíndromo?
Como você "vira" um número ao contrário? Primeiro resolva do jeito mais
simples que vier à cabeça. O desafio extra fica para depois.
"""


# ==============================================================================
# 1) MINHA SOLUÇÃO
# ==============================================================================
class Solution:
    def isPalindrome(self, x: int):
        if x < 0:
            return False
        elif x < 10:
            return True
        else: 
            num = x
            invertido = 0
            while num != 0:
                digito = num % 10
                invertido = (invertido * 10) + digito
                num = num // 10  
            if invertido == x:
                return True
            return False


        


# ==============================================================================
# 2) SOLUÇÃO COMPARADA DA IA
# ==============================================================================
# (Preenchido SOMENTE depois da minha tentativa. Objetivo: comparar abordagens,
#  não substituir a minha.)
#
# Complexidade da minha solução : Tempo O(d)*  |  Espaço O(1)
# Complexidade da solução da IA : Tempo O(d)   |  Espaço O(1)
#
# * d = quantidade de dígitos de x (cerca de log10 x). Para um int de 32 bits
#   são no máximo 10 voltas do while. Espaço O(1) porque uso só três variáveis,
#   sem criar string nem lista.
#
# Solução da IA (inverte só a METADE dos dígitos). É código de verdade: o bloco
# de testes no fim roda a minha e esta, lado a lado.
class SolucaoIA:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False          # negativos e terminados em 0 (menos o 0)
        invertido = 0
        while x > invertido:      # para quando passo da metade
            invertido = invertido * 10 + x % 10
            x //= 10
        # dígitos pares: x == invertido | ímpares: descarto o do meio
        return x == invertido or x == invertido // 10


# Caminho mais comum (que eu pulei direto): converter para string.
#     return str(x) == str(x)[::-1]     # Tempo O(d) | Espaço O(d)
#   Funciona, mas cria duas strings. O desafio extra pedia justamente evitar isso.
#
# O que está certo na minha solução:
# - Resolvi direto o desafio extra, usando % 10 e // 10 para desmontar o
#   número dígito a dígito.
# - Tratei os negativos antes de qualquer conta.
# - Guardei uma cópia (num) e deixei x intacto para a comparação final.
#
# Diferenças que percebi:
# - A IA para o laço na metade (while x > invertido); eu inverto o número
#   inteiro. Em Python o ganho é pequeno, mas em C ou Java inverter tudo pode
#   estourar o limite do int (2^31 - 1), e a versão pela metade evita isso.
# - Meu `elif x < 10: return True` não é errado, mas é redundante: o while já
#   devolve True para um dígito só (ex.: 7 -> invertido 7, e 7 == 7).
# - `if invertido == x: return True / return False` cabe em uma linha:
#   `return invertido == x`.
# - A IA elimina de cara os terminados em 0 (10, 100, ...), porque nenhum
#   deles pode ser palíndromo, exceto o próprio 0.


# ==============================================================================
# 3) AJUDA QUE PEDI (preencher só se precisei)
# ==============================================================================
# Não pedi ajuda neste exercício.


# ==============================================================================
# 4) COMO REPRODUZI A PARTIR DA AJUDA
# ==============================================================================
# Não se aplica: resolvi sem pedir ajuda.


# ==============================================================================
# 5) O QUE APRENDI
# ==============================================================================
# - Aprendi a utilizar modulo e logica para inverter um numero sendo o % 10
# para pegar o ultimo digito, o invertido para ir armazenando o valor e sua ordem
# de grandeza e por último ir dividindo ele por 10 (de forma inteira) para diminuir
# uma ordem de grandeza e assim conseguir realizar a inversão.


# ==============================================================================
# TESTES LOCAIS - rode: python 0009_palindrome_number.py
# ==============================================================================
if __name__ == "__main__":
    casos = [
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (12321, True),
        (1221, True),
        (123, False),
    ]
    for nome, s in (("MINHA SOLUÇÃO", Solution()), ("SOLUÇÃO DA IA", SolucaoIA())):
        print(f"--- {nome} ---")
        for entrada, esperado in casos:
            resultado = s.isPalindrome(entrada)
            if resultado is None:
                status = "VAZIO"
            elif resultado == esperado:
                status = " OK  "
            else:
                status = "ERRO "
            print(f"[{status}] isPalindrome({entrada}) = {resultado}  (esperado: {esperado})")
