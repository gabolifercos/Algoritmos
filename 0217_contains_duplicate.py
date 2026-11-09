"""
LeetCode #217 - Contains Duplicate
Dificuldade : Easy
Link        : https://leetcode.com/problems/contains-duplicate/
Tópicos     : Arrays, Hash Table, Ordenação
Linguagem   : Python 3
Status      : [x] Resolvi sozinho   [ ] Resolvi com ajuda   [ ] Não consegui

================================================================================
ENUNCIADO (traduzido)
================================================================================
Dado um array de inteiros nums, retorne True se algum valor aparecer pelo menos
duas vezes no array, e False se todos os elementos forem distintos.

Exemplo 1:
    Entrada: nums = [1, 2, 3, 1]
    Saída  : True
    Explicação: o valor 1 aparece nos índices 0 e 3.

Exemplo 2:
    Entrada: nums = [1, 2, 3, 4]
    Saída  : False
    Explicação: todos os elementos são distintos.

Exemplo 3:
    Entrada: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    Saída  : True

Restrições:
    1 <= len(nums) <= 10^5
    -10^9 <= nums[i] <= 10^9

================================================================================
COMO USAR ESTE ARQUIVO
================================================================================
- O LeetCode entrega a função dentro de `class Solution`. Você só precisa
  escrever o corpo do método. O `self` é obrigatório como primeiro parâmetro,
  mas pode ignorá-lo por enquanto.
- `List[int]` é só uma anotação de tipo: significa "lista de inteiros".
- Para copiar para o LeetCode, leve só a `class Solution` da seção 1.
- Rode `python 0217_contains_duplicate.py` para testar com os exemplos.

================================================================================
DICA INICIAL (leia só se travar)
================================================================================
O jeito ingênuo é comparar cada elemento com todos os outros. Funciona, mas
pense: com 100.000 elementos, quantas comparações isso dá? Depois pergunte-se:
"existe um jeito de eu lembrar quais números eu JÁ VI enquanto percorro a
lista uma única vez?"
"""

from typing import List


# ==============================================================================
# 1) MINHA SOLUÇÃO
# ==============================================================================
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) > len(set(nums)):
            return True
        return False


# ==============================================================================
# 2) SOLUÇÃO COMPARADA DA IA
# ==============================================================================
# (Preenchido SOMENTE depois da minha tentativa. Objetivo: comparar abordagens,
#  não substituir a minha.)
#
# Complexidade da minha solução : Tempo O(n)   |  Espaço O(n)
# Complexidade da solução da IA : Tempo O(n)*  |  Espaço O(n)
#
# * Mesma ordem de grandeza, mas a IA para no PRIMEIRO repetido. Na minha,
#   set(nums) sempre percorre a lista inteira e guarda todos os valores, mesmo
#   que a duplicata esteja logo no começo. No pior caso (sem repetidos) as duas
#   fazem exatamente o mesmo trabalho.
#
# Solução da IA (percorre uma vez e lembra o que já viu). É código de verdade:
# o bloco de testes no fim roda a minha e esta, lado a lado.
class SolucaoIA:
    def containsDuplicate(self, nums: List[int]) -> bool:
        vistos = set()
        for valor in nums:
            if valor in vistos:       # já passei por ele antes?
                return True
            vistos.add(valor)
        return False


# Terceiro caminho (quando memória extra é problema): ordenar e comparar vizinhos.
#     nums.sort()                            # Tempo O(n log n) | Espaço O(1)
#     for i in range(1, len(nums)):
#         if nums[i] == nums[i - 1]:
#             return True
#     return False
#   Mais lento que o set, mas não cria estrutura nova. Em entrevista é a resposta
#   para "e se você não puder usar memória extra?".
#
# O que está certo na minha solução:
# - É a versão mais curta e mais "pythônica" do problema: o set descarta as
#   repetições sozinho, e comparar os tamanhos resolve em uma linha de lógica.
# - Reaproveitou a ideia do set vinda do Two Sum, agora no uso certo: aqui só
#   interessa "quais valores existem", não "onde estão".
#
# Diferenças que percebi:
# - A IA sai cedo; eu sempre processo a lista inteira. Para 100.000 elementos
#   com um repetido na posição 2, a IA dá 2 passos e eu dou 100.000.
# - `if cond: return True / return False` cabe em uma linha:
#   `return len(nums) > len(set(nums))`. A comparação já é um booleano.


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
# Usar o conceito do set que retira as duplicatas automaticamente logo se o tamanho
# da lista normal for maior que a do set significa que a lista tem duplicatas


# ==============================================================================
# TESTES LOCAIS - rode: python 0217_contains_duplicate.py
# ==============================================================================
if __name__ == "__main__":
    casos = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([7], False),
        ([-1, 0, -1], True),
    ]
    for nome, s in (("MINHA SOLUÇÃO", Solution()), ("SOLUÇÃO DA IA", SolucaoIA())):
        print(f"--- {nome} ---")
        for entrada, esperado in casos:
            resultado = s.containsDuplicate(entrada)
            if resultado is None:
                status = "VAZIO"
            elif resultado == esperado:
                status = " OK  "
            else:
                status = "ERRO "
            print(f"[{status}] containsDuplicate({entrada}) = {resultado}  (esperado: {esperado})")
