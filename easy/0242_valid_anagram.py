"""
LeetCode #242 - Valid Anagram
Dificuldade : Easy
Link        : https://leetcode.com/problems/valid-anagram/
Tópicos     : Strings, Hash Table, Ordenação
Linguagem   : Python 3
Status      : [x] Resolvi sozinho   [ ] Resolvi com ajuda   [ ] Não consegui

================================================================================
ENUNCIADO (traduzido)
================================================================================
Dadas duas strings s e t, retorne True se t for um anagrama de s, e False caso
contrário.

Um anagrama é uma palavra formada reorganizando as letras de outra, usando
todas as letras originais exatamente uma vez.

Exemplo 1:
    Entrada: s = "anagram", t = "nagaram"
    Saída  : True

Exemplo 2:
    Entrada: s = "rat", t = "car"
    Saída  : False

Restrições:
    1 <= len(s), len(t) <= 5 * 10^4
    s e t contêm apenas letras minúsculas do alfabeto inglês.

Desafio extra (follow-up): e se as entradas tivessem caracteres Unicode
(acentos, outros alfabetos)? Como você adaptaria sua solução?

================================================================================
COMO USAR ESTE ARQUIVO
================================================================================
- O LeetCode entrega a função dentro de `class Solution`. Você só precisa
  escrever o corpo do método. O `self` é obrigatório como primeiro parâmetro,
  mas pode ignorá-lo por enquanto.
- `s: str` e `-> bool` são só anotações de tipo: entram dois textos, sai
  True ou False.
- Para copiar para o LeetCode, leve só a `class Solution` da seção 1.
- Rode `python 0242_valid_anagram.py` para testar com os exemplos.

================================================================================
DICA INICIAL (leia só se travar)
================================================================================
Duas palavras são anagramas quando têm as MESMAS letras nas MESMAS quantidades,
só que em outra ordem. Pense em dois caminhos: (a) existe um jeito de "contar"
quantas vezes cada letra aparece em cada palavra e comparar as contagens?
(b) existe um jeito de colocar as duas palavras numa forma padrão, que fique
idêntica se forem anagramas? E antes de tudo: tamanhos diferentes já decidem
alguma coisa?
"""


# ==============================================================================
# 1) MINHA SOLUÇÃO
# ==============================================================================
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictletters = {}
        dictletters2 = {}
        for letter in s:
            if letter not in dictletters:
                dictletters[letter] = 1
            else:
                dictletters[letter] += 1
        for letter2 in t:
            if letter2 not in dictletters2:
                dictletters2[letter2] = 1
            else:
                dictletters2[letter2] += 1
        if dictletters == dictletters2:
            return True
        return False        

        
            
        



# ==============================================================================
# 2) SOLUÇÃO COMPARADA DA IA
# ==============================================================================
# (Preenchido SOMENTE depois da minha tentativa. Objetivo: comparar abordagens,
#  não substituir a minha.)
#
# Complexidade da minha solução : Tempo O(n)   |  Espaço O(k)*
# Complexidade da solução da IA : Tempo O(n)   |  Espaço O(k)*
#
# * k = quantidade de letras DISTINTAS. Com o alfabeto inglês minúsculo, k <= 26,
#   então na prática é espaço constante. A minha usa dois dicionários, a IA usa
#   um só; mesma ordem de grandeza.
#
# Solução da IA (um dicionário só: soma em s, subtrai em t). É código de
# verdade: o bloco de testes no fim roda a minha e esta, lado a lado.
class SolucaoIA:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):              # tamanhos diferentes: já era
            return False
        contagem = {}
        for letra in s:                   # cada letra de s soma 1
            contagem[letra] = contagem.get(letra, 0) + 1
        for letra in t:                   # cada letra de t tira 1
            contagem[letra] = contagem.get(letra, 0) - 1
            if contagem[letra] < 0:       # t tem uma letra que s não tinha
                return False
        return True                       # mesmo tamanho e nada negativo: tudo zerou


# Outros dois caminhos que valem conhecer:
#     return sorted(s) == sorted(t)        # Tempo O(n log n) | uma linha
#   Ordenar coloca as duas palavras na "forma padrão" da dica (b). Mais lento
#   para entradas grandes, mas imbatível em legibilidade.
#
#     from collections import Counter
#     return Counter(s) == Counter(t)      # Tempo O(n) | a sua ideia, pronta
#   Counter é um dicionário que já nasce contando. É exatamente o que você
#   escreveu à mão, e é o que se usa no dia a dia.
#
# O que está certo na minha solução:
# - A ideia é a certa para o problema: contar letras e comparar contagens.
#   É O(n) e já resolve o desafio extra (Unicode): o dicionário conta qualquer
#   caractere, não só a-z.
# - Comparar os dois dicionários com == funciona porque o Python compara
#   chaves e valores, sem ligar para a ordem em que foram inseridos.
# - Passou em "aacc"/"ccac" (mesmas letras, quantidades diferentes), o caso
#   que derruba quem compara só set(s) == set(t).
#
# Diferenças que percebi:
# - A IA desiste cedo: tamanhos diferentes retornam False antes de contar
#   nada, e a primeira letra "sobrando" em t também encerra. A minha sempre
#   conta as duas palavras inteiras.
# - Os dois laços de contagem são idênticos, só muda a variável. Bloco que se
#   repete é sinal para virar função auxiliar (ou usar Counter).
# - `if letra not in d: d[letra] = 1 / else: d[letra] += 1` cabe em uma linha:
#   `d[letra] = d.get(letra, 0) + 1`. O .get devolve 0 quando a chave não existe.
# - `if a == b: return True / return False` é só `return a == b` (mesma nota
#   do #217).
# - Nomes: dictletters, dictletters2 e letter2 dizem o TIPO, não o papel. Algo
#   como contagem_s e contagem_t conta a história sozinho.
# - Sobraram linhas em branco com espaços depois do return. Não quebram nada,
#   mas o editor costuma marcar e o git mostra como mudança sem conteúdo.


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
# (Preencho eu ao terminar.)


# ==============================================================================
# TESTES LOCAIS - rode: python 0242_valid_anagram.py
# ==============================================================================
if __name__ == "__main__":
    casos = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "ab", False),
        ("aacc", "ccac", False),
        ("listen", "silent", True),
    ]
    solucoes = [("MINHA SOLUÇÃO", Solution()), ("SOLUÇÃO DA IA", SolucaoIA())]
    for nome, sol in solucoes:
        print(f"--- {nome} ---")
        for s, t, esperado in casos:
            resultado = sol.isAnagram(s, t)
            if resultado is None:
                status = "VAZIO"
            elif resultado == esperado:
                status = " OK  "
            else:
                status = "ERRO "
            print(f'[{status}] isAnagram("{s}", "{t}") = {resultado}  (esperado: {esperado})')
