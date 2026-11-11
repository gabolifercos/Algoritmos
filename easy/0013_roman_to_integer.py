"""
LeetCode #13 - Roman to Integer
Dificuldade : Easy
Link        : https://leetcode.com/problems/roman-to-integer/
Tópicos     : Hash Table, Strings, Matemática
Linguagem   : Python 3
Status      : [ ] Resolvi sozinho   [ ] Resolvi com ajuda   [ ] Não consegui

================================================================================
ENUNCIADO (traduzido)
================================================================================
Os numerais romanos são representados por sete símbolos: I, V, X, L, C, D e M.

    Símbolo   Valor
    I         1
    V         5
    X         10
    L         50
    C         100
    D         500
    M         1000

Por exemplo, 2 se escreve II em romano: dois "uns" somados. 12 se escreve
XII, que é X + II. O número 27 se escreve XXVII, que é XX + V + II.

Os numerais romanos costumam ser escritos do maior para o menor, da esquerda
para a direita. Porém, o numeral de quatro não é IIII; o quatro se escreve IV.
Como o um vem ANTES do cinco, nós o subtraímos, resultando em quatro. O mesmo
princípio vale para o nove, que se escreve IX. Há seis casos em que a
subtração é usada:

    - I antes de V (5) ou X (10) forma 4 e 9.
    - X antes de L (50) ou C (100) forma 40 e 90.
    - C antes de D (500) ou M (1000) forma 400 e 900.

Dado um numeral romano, converta-o para um inteiro.

Exemplo 1:
    Entrada: s = "III"
    Saída  : 3
    Explicação: III = 3.

Exemplo 2:
    Entrada: s = "LVIII"
    Saída  : 58
    Explicação: L = 50, V = 5, III = 3.

Exemplo 3:
    Entrada: s = "MCMXCIV"
    Saída  : 1994
    Explicação: M = 1000, CM = 900, XC = 90 e IV = 4.

Restrições:
    1 <= len(s) <= 15
    s contém apenas os caracteres ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    É garantido que s é um numeral romano válido no intervalo [1, 3999].

================================================================================
COMO USAR ESTE ARQUIVO
================================================================================
- O LeetCode entrega a função dentro de `class Solution`. Você só precisa
  escrever o corpo do método. O `self` é obrigatório como primeiro parâmetro,
  mas pode ignorá-lo por enquanto.
- `s: str` e `-> int` são só anotações de tipo: entra um texto, sai um
  número inteiro.
- Para copiar para o LeetCode, leve só a `class Solution` da seção 1.
- Rode `python 0013_roman_to_integer.py` para testar com os exemplos.

================================================================================
DICA INICIAL (leia só se travar)
================================================================================
Comece pelo caso SEM subtração: um dicionário símbolo -> valor e uma soma
símbolo a símbolo já resolvem "III" e "LVIII". Depois olhe o que diferencia IV
de VI: as mesmas duas letras, em ordem trocada. Percorrendo um símbolo de cada
vez, que comparação com o VIZINHO da direita diz se este símbolo soma ou
subtrai? Cuidado com o último símbolo, que não tem vizinho.
"""


# ==============================================================================
# 1) MINHA SOLUÇÃO
# ==============================================================================
class Solution:
    def romanToInt(self, s: str) -> int:
        dicionarioromanos = {  
            "I"    :     1,
            "V"    :     5,
            "X"    :     10,
            "L"    :     50,
            "C"    :     100,
            "D"    :     500,
            "M"    :     1000
            }
        soma = 0
        letra = 0
        numerodafrente = 0
        while letra < len(s):
            numero = dicionarioromanos[s[letra]]
            if letra != len(s) - 1:
                numerodafrente = dicionarioromanos[s[letra + 1]]
            if numerodafrente > numero:
                soma += numerodafrente - numero
                letra += 2
                continue
            soma += numero
            letra += 1
        return soma

            


# ==============================================================================
# 2) SOLUÇÃO COMPARADA DA IA
# ==============================================================================
# (Preenchido SOMENTE depois da minha tentativa. Objetivo: comparar abordagens,
#  não substituir a minha.)
#
# Complexidade da minha solução : Tempo O(n)   |  Espaço O(1)
# Complexidade da solução da IA : Tempo O(n)   |  Espaço O(1)
#
# (n <= 15 aqui, então tempo não é o assunto deste exercício; o assunto é
#  acertar o vizinho da direita em TODOS os casos.)
#
# Solução da IA (sem pular letra nenhuma: quem é menor que o vizinho da direita
# SUBTRAI, quem não é SOMA). É código de verdade: o bloco de testes no fim roda
# a minha e esta, lado a lado.
class SolucaoIA:
    def romanToInt(self, s: str) -> int:
        valores = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        soma = 0
        for i in range(len(s)):
            atual = valores[s[i]]
            proximo = valores[s[i + 1]] if i + 1 < len(s) else 0   # última letra: ninguém na frente
            if atual < proximo:
                soma -= atual                 # IV: o I entra como -1...
            else:
                soma += atual                 # ...e o V entra como +5. Dá 4 sem pular.
        return soma


# O que está certo na minha solução:
# - O dicionário símbolo -> valor e a ideia "olhe o vizinho da direita para
#   decidir se soma ou subtrai" são exatamente o cerne do problema.
# - O raciocínio sobre o laço está correto: num for sobre range, `letra += 1`
#   não pula a volta seguinte (o for reatribui a variável a cada volta), e o
#   while com `letra += 2` resolve isso de verdade. Boa troca.
# - O if que protege s[letra + 1] fechou o IndexError da Dica 1, e o
#   `numerodafrente = 0` antes do while fechou o UnboundLocalError do "I".
# - Passou nos 12 casos originais do arquivo.
#
# Diferenças que percebi (a primeira é um bug; veja os 4 casos novos no bloco
# de testes):
# - BUG: na última letra, numerodafrente fica com o valor VELHO da volta
#   anterior. O if só impede a atualização; não diz quanto a variável deve
#   valer quando não existe letra da frente. Siga "XCI" (91): letra = 0,
#   X = 10, frente = C = 100, 100 > 10, soma = 90, letra pula para 2. Na volta
#   de letra = 2 (a última), numero = I = 1, o if NÃO atualiza numerodafrente,
#   que continua 100. Aí "100 > 1" dispara e soma vira 90 + 99 = 189.
#   Acontece sempre que um par subtrativo é seguido de UMA letra final: XLI
#   (41), XLV (45), XCV (95), CDI (401), CMI (901), MCMI (1901)... A IA rodou
#   os 3999 numerais válidos: a minha erra 192 deles, o primeiro é o 41. Os 12
#   casos do arquivo não pegaram porque todos terminam em par (IV, IX) ou em
#   letra que acabou de atualizar a variável (III, LVIII). A pergunta: quando
#   a letra é a última, quanto numerodafrente deveria valer para a comparação
#   nunca disparar? Você já usou esse valor em outro lugar do código.
# - A IA não pula nada. Em "IV", em vez de somar 5 - 1 e saltar duas posições,
#   ela subtrai 1 na volta do I e soma 5 na volta do V: -1 + 5 = 4. Mesma
#   conta, sem continue, sem += 2, e por isso o for sobre range basta. A
#   dificuldade que você teve com "pular um loop" desaparece quando o laço não
#   precisa pular.
# - Nome: `letra` guarda um ÍNDICE (0, 1, 2...), não uma letra; s[letra] é que
#   é a letra. Mesma observação do #121 (`price` era índice). `i` ou `posicao`
#   contam a história certa. `dicionarioromanos` diz o tipo; `valores` diz o
#   papel.
# - Espaços sobrando depois de `dicionarioromanos = {` e numa linha em branco
#   depois do return. Não quebram nada; em portfólio vale limpar.


# ==============================================================================
# 3) AJUDA QUE PEDI (preencher só se precisei)
# ==============================================================================
# Registro de cada dica que pedi à IA, na ordem em que pedi. A IA anota aqui:
# o código que eu tinha na hora, o prompt que mandei e a resposta que recebi.
#
# --- Dica 1 (2026-11-11) ------------------------------------------------------
# Código que eu tinha quando perguntei (todos os 12 testes davam
# "EXCEÇÃO IndexError"):
#
#     class Solution:
#         def romanToInt(self, s: str) -> int:
#             dicionarioromanos = {
#                 "I"    :     1,
#                 "V"    :     5,
#                 "X"    :     10,
#                 "L"    :     50,
#                 "C"    :     100,
#                 "D"    :     500,
#                 "M"    :     1000
#                 }
#             soma = 0
#             for letra in range(len(s)):
#                 numero = dicionarioromanos[s[letra]]
#                 numerodafrente = dicionarioromanos[s[letra + 1]]
#                 if numerodafrente > numero:
#                     soma += numerodafrente - numero
#                     letra += 1
#                     continue
#                 soma += numero
#             return soma
#
# Prompt (o que perguntei):
#
#     "pq esta dando inex error"
#
# Resposta da IA (dica, sem a solução pronta):
#
#     IndexError quer dizer "pedi uma posição que não existe". Siga o laço
#     com "III", que tem 3 letras: range(3) dá letra = 0, 1, 2. Na volta em
#     que letra vale 2, a linha do numerodafrente pede s[3]. Mas o maior
#     índice válido de "III" é 2: a última letra nunca tem vizinha à direita.
#     Com "I" (1 letra) quebra já na primeira volta, porque pede s[1].
#
#     A regra é a mesma da pilha vazia no #20: antes de olhar s[letra + 1],
#     garanta que a posição letra + 1 existe. Pergunta para você responder:
#     qual é o maior índice válido de uma string de tamanho n, e o que deve
#     acontecer com a última letra, que não tem ninguém na frente?
#
#     Depois que o IndexError sumir, rode os testes e olhe "IV" e "IX" com
#     atenção. Se o resultado sair maior que o esperado, teste isto: num
#     `for letra in range(len(s))`, o `letra += 1` que você faz dentro do
#     laço muda qual letra vem na PRÓXIMA volta? Ponha um print(letra) na
#     primeira linha do laço e veja a sequência.
#


# ==============================================================================
# 4) COMO REPRODUZI A PARTIR DA AJUDA
# ==============================================================================
# Após entender o IndexError, fiz uma correção com um if antes de definir o
# número da frente: eu vejo se aquele elemento é realmente o último, porque se
# for o último não vai ter número da frente. Também estava difícil pular um
# loop quando era o caso de um número romano menor estar atrás de um maior: eu
# tentava pular o próximo loop para não somar duas vezes, mas percebi que com o
# for não seria possível, então fiz a alteração para o while. E estava dando
# UnboundLocalError quando era só um elemento, porque o número da frente não
# era definido (como só tinha um elemento, não tinha número da frente), então
# na comparação "número da frente maior que número" ele dava o erro. Corrigi
# isso colocando a definição da variável numerodafrente igual a zero no começo,
# antes do while.
# (Ditado por mim no chat em 2026-11-11; a IA só transcreveu.)


# ==============================================================================
# 5) O QUE APRENDI
# ==============================================================================
# Treinei a lógica de programação no geral. Aprendi sobre definição de
# variáveis e a evitar IndexError e UnboundLocalError nos loops, e uma situação
# em que o while era melhor que o for.
# (Ditado por mim no chat em 2026-11-11; a IA só transcreveu.)


# ==============================================================================
# TESTES LOCAIS - rode: python 0013_roman_to_integer.py
# ==============================================================================
if __name__ == "__main__":
    casos = [
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("IV", 4),
        ("IX", 9),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
        ("XLIV", 44),
        ("MMMCMXCIX", 3999),
        ("I", 1),
        # Casos acrescentados na comparação (seção 2): par subtrativo seguido
        # de UMA letra final.
        ("XLI", 41),
        ("XCV", 95),
        ("CDI", 401),
        ("MCMI", 1901),
    ]
    solucoes = [("MINHA SOLUÇÃO", Solution()), ("SOLUÇÃO DA IA", SolucaoIA())]
    for nome, sol in solucoes:
        print(f"--- {nome} ---")
        for s, esperado in casos:
            try:
                resultado = sol.romanToInt(s)
            except Exception as erro:          # um crash também é erro
                resultado = f"EXCEÇÃO {type(erro).__name__}"
            if resultado is None:
                status = "VAZIO"
            elif resultado == esperado:
                status = " OK  "
            else:
                status = "ERRO "
            print(f'[{status}] romanToInt("{s}") = {resultado}  (esperado: {esperado})')
