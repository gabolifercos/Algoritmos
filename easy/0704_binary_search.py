"""
LeetCode #704 - Binary Search
Dificuldade : Easy
Link        : https://leetcode.com/problems/binary-search/
Tópicos     : Arrays, Busca Binária
Linguagem   : Python 3
Status      : [ ] Resolvi sozinho   [x] Resolvi com ajuda   [ ] Não consegui

================================================================================
ENUNCIADO (traduzido)
================================================================================
Dado um array de inteiros nums ORDENADO em ordem crescente e um inteiro
target, escreva uma função que procure target em nums. Se target existir,
retorne o seu índice. Caso contrário, retorne -1.

Você DEVE escrever um algoritmo com complexidade de tempo O(log n).

Exemplo 1:
    Entrada: nums = [-1, 0, 3, 5, 9, 12], target = 9
    Saída  : 4
    Explicação: 9 existe em nums e seu índice é 4.

Exemplo 2:
    Entrada: nums = [-1, 0, 3, 5, 9, 12], target = 2
    Saída  : -1
    Explicação: 2 não existe em nums, então retornamos -1.

Restrições:
    1 <= len(nums) <= 10^4
    -10^4 < nums[i], target < 10^4
    Todos os inteiros em nums são únicos.
    nums está ordenado em ordem crescente.

================================================================================
COMO USAR ESTE ARQUIVO
================================================================================
- O LeetCode entrega a função dentro de `class Solution`. Você só precisa
  escrever o corpo do método. O `self` é obrigatório como primeiro parâmetro,
  mas pode ignorá-lo por enquanto.
- `List[int]` é só uma anotação de tipo: significa "lista de inteiros".
- Atenção: o bloco de testes só confere a RESPOSTA, não a velocidade.
  `nums.index(target)` ou `target in nums` passariam nos testes, mas percorrem
  a lista inteira (O(n)) e não cumprem o O(log n) exigido. O LeetCode também
  não barra, mas o exercício perde o sentido: a graça aqui é o algoritmo.
- Para copiar para o LeetCode, leve só a `class Solution` da seção 1.
- Rode `python 0704_binary_search.py` para testar com os exemplos.

================================================================================
DICA INICIAL (leia só se travar)
================================================================================
A lista está ORDENADA, e é isso que permite não olhar elemento por elemento.
Pense no jogo de adivinhar um número de 1 a 100 em que a resposta é "é maior"
ou "é menor": qual é o melhor primeiro palpite, e o que acontece com o
intervalo possível depois de cada resposta? Guarde dois índices, o início e o
fim do trecho onde o alvo AINDA pode estar, e a cada passo olhe o meio desse
trecho. Quando o trecho fica vazio, o alvo não está lá. Casos que costumam
quebrar: lista de um elemento, alvo na primeira ou na última posição.
"""

from typing import List


# ==============================================================================
# 1) MINHA SOLUÇÃO
# ==============================================================================
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        esq = 0
        dir = len(nums) - 1
        if nums[0] == target:
            return 0
        while dir >= esq:
            meio = (esq + dir)// 2

            if nums[meio] == target:
                return meio
            elif nums[meio] > target:
                dir = meio - 1
            else:
                esq = meio  + 1


        return - 1


# ==============================================================================
# 2) SOLUÇÃO COMPARADA DA IA
# ==============================================================================
# (Preenchido SOMENTE depois da minha tentativa. Objetivo: comparar abordagens,
#  não substituir a minha.)
#
# Complexidade da minha solução : Tempo O(log n)   |  Espaço O(1)
# Complexidade da solução da IA : Tempo O(log n)   |  Espaço O(1)
#
# Solução da IA (o mesmo algoritmo, sem o if extra do começo e lendo nums[meio]
# uma vez por volta). É código de verdade: o bloco de testes no fim roda a
# minha e esta, lado a lado.
class SolucaoIA:
    def search(self, nums: List[int], target: int) -> int:
        esquerda, direita = 0, len(nums) - 1     # trecho onde o alvo AINDA pode estar
        while esquerda <= direita:               # enquanto o trecho não esvaziou
            meio = (esquerda + direita) // 2
            valor = nums[meio]
            if valor == target:
                return meio
            if valor < target:
                esquerda = meio + 1              # alvo só pode estar à direita do meio
            else:
                direita = meio - 1               # alvo só pode estar à esquerda do meio
        return -1                                # trecho esvaziou: não está na lista


# Versão pronta da biblioteca padrão, só para conhecer (mesma complexidade):
#     from bisect import bisect_left
#     i = bisect_left(nums, target)             # onde target está, ou onde entraria
#     return i if i < len(nums) and nums[i] == target else -1
#   bisect_left faz exatamente a busca binária acima, em C. O "onde entraria"
#   é a resposta do #35, o exercício que confundiu na Dica 1.
#
# O que está certo na minha solução:
# - É a busca binária de verdade, e é a mesma da IA: dois índices delimitando o
#   trecho onde o alvo ainda pode estar, o meio comparado, e o trecho encolhe
#   SEMPRE (meio - 1 / meio + 1), que foi a correção da Dica 1.
# - `while dir >= esq` confere também o trecho de um elemento só, e `return -1`
#   quando o trecho esvazia. Os dois pontos da Dica 1 fechados.
# - A IA conferiu contra uma busca linear em 1.500 listas aleatórias de até
#   10.000 elementos, com alvos presentes, ausentes, menores que o primeiro e
#   maiores que o último, mais todos os alvos possíveis em listas de 1 a 40
#   elementos: zero erros. Passou nos 9 casos do arquivo e nos 3 acrescentados.
# - É O(log n) de verdade, e dá para VER isso. Leituras da lista no pior caso
#   com n = 10.000 (a IA contou cada nums[...] executado):
#       minha busca binária        29 leituras   (1 do if + 14 voltas x 2)
#       busca binária da IA        14 leituras   (14 voltas x 1)
#       nums.index(target)         até 10.000 leituras
#   14 voltas porque cada volta corta o trecho pela metade e 2^14 = 16.384 já
#   passa de 10.000. Com um bilhão de elementos seriam 30 voltas.
#
# Diferenças que percebi:
# - `if nums[0] == target: return 0` sobrou da versão com `while dir > esq`,
#   que não conferia o trecho de um elemento. Com o `>=` o laço já resolve o
#   índice 0 (siga [5] e 5: esq = 0, dir = 0, meio = 0, achou). O if não erra,
#   só gasta uma comparação e confunde quem lê: pode sair.
# - `dir` é o nome de uma função embutida do Python (dir(x) lista o que x
#   tem dentro). Dentro da função não dá problema, mas esconde a embutida ali.
#   `direita`, ou `lo`/`hi` como na biblioteca, evitam a colisão.
# - `nums[meio]` é lido duas vezes por volta (no == e no >). Guardar numa
#   variável (`valor = nums[meio]`) lê uma vez só. Detalhe, não erro.
# - Espaçamento: `(esq + dir)// 2`, `meio  + 1` e `return - 1` funcionam, mas
#   a grafia usual é `(esq + dir) // 2`, `meio + 1` e `return -1`. As linhas
#   em branco dentro do laço também podem sair.
# - Na seção 5 você descreveu a saída "até achar o alvo". Existe a outra saída,
#   que você implementou certo: o trecho esvazia (esq passa de dir) e a
#   resposta é -1.


# ==============================================================================
# 3) AJUDA QUE PEDI (preencher só se precisei)
# ==============================================================================
# Registro de cada dica que pedi à IA, na ordem em que pedi. A IA anota aqui:
# o código que eu tinha na hora, o prompt que mandei e a resposta que recebi.
#
# --- Dica 1 (2026-11-11) ------------------------------------------------------
# Código que eu tinha quando perguntei (o segundo caso do arquivo travava em
# loop infinito; a IA rodou cada caso separado, com limite de tempo: 5 casos
# travavam, [5]/-5 e [2, 5]/0 devolviam 0 em vez de -1, os outros passavam):
#
#     class Solution:
#         def search(self, nums: List[int], target: int) -> int:
#             esq = 0
#             dir = len(nums) - 1
#
#             while dir > esq:
#                 meio = (esq + dir)// 2
#
#                 if nums[meio] == target:
#                     return meio
#                 elif nums[meio] > target:
#                     dir = meio
#                 else:
#                     esq = meio
#             return esq
#
# Prompt (o que perguntei):
#
#     "verifique para mim os casos do exercício 704 do binary search. O segundo
#      caso está dando loop, eu queria ajuda. Mas pelo que eu entendi aqui,
#      está dizendo que a resposta deveria ser -1. Mas acredito que a resposta
#      deveria ser 2, não é?"
#
# Resposta da IA (dica, sem a solução pronta):
#
#     O -1 está certo. O 2 não existe em [-1, 0, 3, 5, 9, 12], e o enunciado
#     diz: se target existir, devolva o índice dele; se não existir, devolva
#     -1. O índice 2 é onde o 2 ENTRARIA para manter a ordem, mas isso é outro
#     exercício (#35, Search Insert Position). Aqui, não achou é -1. Isso vale
#     também para o `return esq` do fim: quando o laço termina sem encontrar,
#     o que deve voltar?
#
#     O loop: siga à mão com target = 2, anotando esq, dir e meio a cada volta.
#         esq=0, dir=5 -> meio=2, nums[2]=3 > 2  -> dir = 2
#         esq=0, dir=2 -> meio=1, nums[1]=0 < 2  -> esq = 1
#         esq=1, dir=2 -> meio=1, nums[1]=0 < 2  -> esq = 1
#     A terceira volta deixa tudo igual à segunda, então repete para sempre.
#     Por quê: quando nums[meio] não é o target, aquela posição JÁ foi
#     examinada e não serve mais, mas `esq = meio` (e `dir = meio`) deixa ela
#     dentro do intervalo. Cada volta precisa jogar fora pelo menos um
#     elemento. Pergunta: sabendo que nums[meio] < target, qual é a PRIMEIRA
#     posição que ainda pode conter o target? E, sabendo que nums[meio] >
#     target, qual é a ÚLTIMA?
#
#     Quando o loop sumir, os testes vão mostrar mais uma coisa: `while dir >
#     esq` para quando o intervalo tem exatamente UM elemento, sem comparar
#     esse elemento. Teste com nums = [5] e target = -5: a função devolve 0,
#     mas 5 não é -5. Pense no que a condição do while precisa dizer para o
#     último elemento também ser conferido.
#


# ==============================================================================
# 4) COMO REPRODUZI A PARTIR DA AJUDA
# ==============================================================================
# Precisei pedir ajuda para entender por que estava dando o loop infinito. Aí
# pensei que, se eu só igualasse a esquerda ou a direita ao meio, ia ocorrer
# loop para sempre. Então eu precisava que, quando o alvo estivesse mais para a
# esquerda, a direita fosse igual ao meio menos 1, e quando o alvo estivesse
# mais para a direita, a esquerda fosse igual ao meio mais 1, para eliminar o
# elemento que o meio já verificou. Senão ia ficar nesse loop infinito.
# (Ditado por mim no chat em 2026-11-11; a IA só transcreveu.)


# ==============================================================================
# 5) O QUE APRENDI
# ==============================================================================
# Aprendi a fazer a busca binária. Ela consiste em você definir a esquerda e a
# direita: a esquerda como o primeiro elemento da lista e a direita como o
# último. Aí usamos um while enquanto a direita for maior ou igual à esquerda,
# ou seja, a busca só para quando a esquerda ficar maior do que a direita.
# Depois você define que o meio é igual à esquerda mais a direita, com divisão
# inteira por 2. Você pega o elemento do meio e vê se ele é igual ao seu alvo.
# Se não é, você vê se o alvo está mais para a esquerda ou mais para a direita:
# mais para a esquerda quer dizer que o alvo é menor do que o elemento do meio;
# mais para a direita, que é maior. A partir disso você define a nova direita
# ou a nova esquerda, e vai fazendo repetidamente até achar o alvo.
# (Ditado por mim no chat em 2026-11-11; a IA só transcreveu.)


# ==============================================================================
# TESTES LOCAIS - rode: python 0704_binary_search.py
# ==============================================================================
if __name__ == "__main__":
    casos = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([5], -5, -1),
        ([1, 2, 3, 4, 5, 6], 1, 0),
        ([1, 2, 3, 4, 5, 6], 6, 5),
        ([1, 3], 3, 1),
        ([2, 5], 0, -1),
        ([-10, -3, 0, 7, 8, 20, 21], 7, 3),
        # Casos acrescentados na comparação (seção 2).
        ([1, 3], 1, 0),                 # alvo na primeira posição de um par
        ([1, 3, 5], 4, -1),             # alvo entre dois elementos
        ([1, 3, 5], 6, -1),             # alvo maior que o último
    ]
    solucoes = [("MINHA SOLUÇÃO", Solution()), ("SOLUÇÃO DA IA", SolucaoIA())]
    for nome, sol in solucoes:
        print(f"--- {nome} ---")
        for nums, target, esperado in casos:
            try:
                resultado = sol.search(nums, target)
            except Exception as erro:          # um crash também é erro
                resultado = f"EXCEÇÃO {type(erro).__name__}"
            if resultado is None:
                status = "VAZIO"
            elif resultado == esperado:
                status = " OK  "
            else:
                status = "ERRO "
            print(f"[{status}] search({nums}, {target}) = {resultado}  (esperado: {esperado})")
