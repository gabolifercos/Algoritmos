"""
LeetCode #1 - Two Sum
Dificuldade : Easy
Link        : https://leetcode.com/problems/two-sum/
Tópicos     : Arrays, Hash Table
Linguagem   : Python 3
Status      : [ ] Resolvi sozinho   [x] Resolvi com ajuda   [ ] Não consegui

================================================================================
ENUNCIADO (traduzido)
================================================================================
Dado um array de inteiros nums e um inteiro target, retorne os ÍNDICES dos dois
números cuja soma seja igual a target.

Você pode assumir que cada entrada tem EXATAMENTE uma solução, e você não pode
usar o mesmo elemento duas vezes.

A resposta pode ser retornada em qualquer ordem.

Exemplo 1:
    Entrada: nums = [2, 7, 11, 15], target = 9
    Saída  : [0, 1]
    Explicação: nums[0] + nums[1] == 9, então retornamos [0, 1].

Exemplo 2:
    Entrada: nums = [3, 2, 4], target = 6
    Saída  : [1, 2]

Exemplo 3:
    Entrada: nums = [3, 3], target = 6
    Saída  : [0, 1]

Restrições:
    2 <= len(nums) <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Existe apenas uma resposta válida.

Desafio extra (follow-up): consegue um algoritmo com complexidade de tempo
menor que O(n^2)?

================================================================================
COMO USAR ESTE ARQUIVO
================================================================================
- O LeetCode entrega a função dentro de `class Solution`. Você só precisa
  escrever o corpo do método. O `self` é obrigatório como primeiro parâmetro,
  mas pode ignorá-lo por enquanto.
- `List[int]` é só uma anotação de tipo: significa "lista de inteiros".
- Para copiar para o LeetCode, leve só a `class Solution` da seção 1.
- Rode `python 0001_two_sum.py` para testar com os exemplos.

================================================================================
DICA INICIAL (leia só se travar)
================================================================================
Atenção: a resposta são os ÍNDICES, não os números. Comece pelo jeito mais
óbvio: testar cada par possível. Depois, para o desafio extra, pense assim:
"se estou olhando o número 7 e o target é 9, qual é o PARCEIRO que falta?
Eu já passei por ele antes?"
"""

from typing import List


# ==============================================================================
# 1) MINHA SOLUÇÃO
# ==============================================================================
class Solution:
    def twoSum(self, List, target):
        listinset = set(List)
        listinenumarate = enumerate(List)
        
        for indice,valor in listinenumarate :
            
            parceiro = target - valor        
            if parceiro in listinset and indice != List.index(parceiro):
                return [indice,List.index(parceiro)]
           

# ==============================================================================
# 2) SOLUÇÃO COMPARADA DA IA
# ==============================================================================
# (Preenchido SOMENTE depois da minha tentativa. Objetivo: comparar abordagens,
#  não substituir a minha.)
#
# Complexidade da minha solução : Tempo O(n) na prática*  |  Espaço O(n)
# Complexidade da solução da IA : Tempo O(n)              |  Espaço O(n)
#
# * O `in` no set é O(1), mas cada `List.index(parceiro)` é uma varredura
#   escondida de até n passos. Ela só roda quando o parceiro existe e, como o
#   enunciado garante UMA única solução, isso acontece pouquíssimas vezes. Sem
#   essa garantia (ex.: lista cheia de pares válidos), o pior caso seria O(n^2).
#
# Solução da IA (uma passada, dicionário valor -> índice). É código de verdade:
# o bloco de testes no fim roda a minha e esta, lado a lado.
class SolucaoIA:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vistos = {}                      # valor -> índice onde eu o vi
        for i, valor in enumerate(nums):
            parceiro = target - valor
            if parceiro in vistos:
                return [vistos[parceiro], i]
            vistos[valor] = i            # só guardo DEPOIS de checar


# O que está certo na minha solução:
# - Resultado correto em todos os casos, inclusive com números repetidos.
# - Usar enumerate para carregar o índice junto com o valor resolveu o
#   problema de buscar a posição do número atual.
# - A ideia central (parceiro = target - valor, e "ele existe?") é a mesma
#   da solução clássica.
#
# Diferenças que percebi:
# - set guarda só "quais valores existem"; o dicionário guarda "valor E onde
#   está". Por isso a IA não precisa de .index() em lugar nenhum.
# - A IA preenche o dicionário DURANTE o laço, só com o que já passou. Assim
#   um elemento nunca se encontra consigo mesmo, e [3, 3] funciona sem
#   nenhuma checagem extra de índice.
# - Minha versão chama List.index(parceiro) duas vezes quando acha o par
#   (no if e no return). Dava para guardar o resultado numa variável.
# - Nomes: o parâmetro `List` esconde o `List` importado do typing (funciona,
#   mas confunde; o LeetCode usa `nums`). `listinenumarate` tem erro de
#   digitação e nem precisa existir: dá para escrever o enumerate direto no for.


# ==============================================================================
# 3) AJUDA QUE PEDI (preencher só se precisei)
# ==============================================================================
# Registro de cada dica que pedi à IA, na ordem em que pedi. A IA anota aqui:
# o código que eu tinha na hora, o prompt que mandei e a resposta que recebi.
#
# --- Dica 1 (2026-11-09) ------------------------------------------------------
# Código que eu tinha quando perguntei:
#
#     class Solution:
#         def twoSum(self, List, target):
#             listinset = set(List)
#
#             for num in range(len(List)):
#                 numAtual = List[num]
#                 parceiro = target - numAtual
#
#                 if parceiro in listinset and List.index(parceiro) != num :
#                     return [List.index(numAtual),List.index(parceiro)]
#
# Prompt (o que perguntei):
#
#     "estou com dificuldade em preveninir quando existem dois numeros iguais
#      na lista me direções de que caminho tomar, sem corrigir explicitamente"
#
# Resposta da IA (dica, sem a solução pronta):
#
#     O caso que você descreve é exatamente o Exemplo 3: [3, 3] com target 6.
#
#     Primeiro, um teste no papel (preveja antes de rodar). Percorra sua
#     função com List = [3, 3] e target = 6:
#       - Na primeira volta (num = 0), o que List.index(parceiro) devolve?
#         A condição do if passa?
#       - Na segunda volta (num = 1), a condição passa? Então, na linha do
#         return, o que List.index(numAtual) devolve e o que
#         List.index(parceiro) devolve?
#     Anote o resultado que você espera e só depois rode
#     python 0001_two_sum.py para conferir.
#
#     A direção: .index() sempre responde "a PRIMEIRA posição em que esse
#     valor aparece". Quando há dois valores iguais, ele não consegue
#     distinguir os gêmeos, e isso contamina as duas chamadas do return.
#     Repare também que a posição do número atual você já tem na mão (é a
#     variável do seu laço), então uma dessas buscas nem precisa existir.
#
#     O que realmente falta é a posição do PARCEIRO. Seu set lembra "quais
#     valores existem", mas não "onde cada um está". Pergunte-se: existe uma
#     estrutura em Python que guarda um valor E uma informação associada a
#     ele (por exemplo, a posição dele na lista)? Se você montasse essa
#     estrutura no lugar do set, o que aconteceria com o caso [3, 3]?
#


# ==============================================================================
# 4) COMO REPRODUZI A PARTIR DA AJUDA
# ==============================================================================
# Com a resposta da IA entendi que preceisaria utilizar o Enumerate para rodar
# as comparações pois minha dificuldade principal estava em entender por que 
# quando haviam dois elementos de valores então com o enumerate se retornavam os
# valores dos indices que são elementos em lugares diferentes da lista. 

# ==============================================================================
# 5) O QUE APRENDI
# ==============================================================================
# A utilizar o set para buscas rápidas e o enumerate para entender indice e comp
# arar da maneira correta!


# ==============================================================================
# TESTES LOCAIS - rode: python 0001_two_sum.py
# ==============================================================================
if __name__ == "__main__":
    # A ordem dos dois índices não importa, por isso comparamos ordenado.
    casos = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([3,1,3], 6, [0, 2]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ]
    for nome, s in (("MINHA SOLUÇÃO", Solution()), ("SOLUÇÃO DA IA", SolucaoIA())):
        print(f"--- {nome} ---")
        for nums, target, esperado in casos:
            resultado = s.twoSum(nums, target)
            if resultado is None:
                status = "VAZIO"
            elif sorted(resultado) == sorted(esperado):
                status = " OK  "
            else:
                status = "ERRO "
            print(f"[{status}] twoSum({nums}, {target}) = {resultado}  (esperado: {esperado})")
