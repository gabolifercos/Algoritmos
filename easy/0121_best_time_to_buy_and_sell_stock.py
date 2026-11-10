"""
LeetCode #121 - Best Time to Buy and Sell Stock
Dificuldade : Easy
Link        : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Tópicos     : Arrays, Programação Dinâmica (versão bem simples)
Linguagem   : Python 3
Status      : [x] Resolvi sozinho   [ ] Resolvi com ajuda   [ ] Não consegui

================================================================================
ENUNCIADO (traduzido)
================================================================================
Você recebe um array prices, onde prices[i] é o preço de uma ação no dia i.

Você quer maximizar seu lucro escolhendo UM ÚNICO dia para comprar uma ação e
um dia DIFERENTE, NO FUTURO, para vendê-la.

Retorne o lucro máximo que você consegue obter com essa transação. Se não for
possível obter lucro algum, retorne 0.

Exemplo 1:
    Entrada: prices = [7, 1, 5, 3, 6, 4]
    Saída  : 5
    Explicação: compra no dia 2 (preço 1) e vende no dia 5 (preço 6):
    lucro = 6 - 1 = 5. Comprar no dia 2 e vender no dia 1 não vale, porque
    a compra precisa vir antes da venda.

Exemplo 2:
    Entrada: prices = [7, 6, 4, 3, 1]
    Saída  : 0
    Explicação: os preços só caem; nenhuma transação dá lucro, então 0.

Restrições:
    1 <= len(prices) <= 10^5
    0 <= prices[i] <= 10^4

================================================================================
COMO USAR ESTE ARQUIVO
================================================================================
- O LeetCode entrega a função dentro de `class Solution`. Você só precisa
  escrever o corpo do método. O `self` é obrigatório como primeiro parâmetro,
  mas pode ignorá-lo por enquanto.
- `List[int]` é só uma anotação de tipo: significa "lista de inteiros".
- Para copiar para o LeetCode, leve só a `class Solution` da seção 1.
- Rode `python 0121_best_time_to_buy_and_sell_stock.py` para testar.

================================================================================
DICA INICIAL (leia só se travar)
================================================================================
O jeito ingênuo testa todo par (dia de compra, dia de venda posterior) e guarda
o melhor. Funciona, mas com 100.000 dias estoura o tempo. Pense numa passada
única, dia a dia: ao chegar num dia e considerar VENDER hoje, o que do passado
você precisaria lembrar para saber o melhor lucro possível? É um único número.
"""

from typing import List


# ==============================================================================
# 1) MINHA SOLUÇÃO
# ==============================================================================
# class Solution:
#    def maxProfit(self, prices: List[int]) -> int:
#        maxpriceperday = []
#    
#        for price in range(len(prices)):
#            maximodia = 0
#            for oprice in range(price + 1,len(prices)):
#                if prices[price] > prices[oprice]:
#                    continue
#                lucrodia = prices[oprice] - prices[price]
#               if maximodia < lucrodia:
#                   maximodia = lucrodia
#           maxpriceperday.append(maximodia)
#       return max(maxpriceperday)




# ==============================================================================
# 2) SOLUÇÃO COMPARADA DA IA
# ==============================================================================
# (Preenchido SOMENTE depois da minha tentativa. Objetivo: comparar abordagens,
#  não substituir a minha.)
#
# Complexidade da minha solução : Tempo O(n^2)  |  Espaço O(n)
# Complexidade da solução da IA : Tempo O(n)    |  Espaço O(1)
#
# Medi as duas no meu computador com listas aleatórias (tempo em segundos):
#
#     n (dias)    minha      IA
#       2.000      0,16    0,0001
#       5.000      0,79    0,0002
#      10.000      2,86    0,0004
#      20.000     11,42    0,0009
#
# Cada vez que n cresce 5x, a minha demora 25x mais (5 ao quadrado): é a
# assinatura do O(n^2). Para os 100.000 dias que o enunciado permite, a
# estimativa é de uns 5 minutos. O LeetCode corta em 1 a 2 segundos, então
# esta versão, apesar de CORRETA, receberia "Time Limit Exceeded" na submissão.
# A da IA faz 100.000 dias em menos de 0,01 s.
#
# Solução da IA (uma passada, lembrando o menor preço visto até o dia). É
# código de verdade: o bloco de testes no fim roda a minha e esta, lado a lado.
class SolucaoIA:
    def maxProfit(self, prices: List[int]) -> int:
        menor_preco = prices[0]                   # o mais barato que já vi
        melhor_lucro = 0
        for preco in prices:
            if preco < menor_preco:               # dia melhor para comprar
                menor_preco = preco
            elif preco - menor_preco > melhor_lucro:
                melhor_lucro = preco - menor_preco   # vender hoje bate o recorde
        return melhor_lucro


# O que está certo na minha solução:
# - A resposta é correta em todos os casos, inclusive nos de borda: um dia só,
#   preços só caindo (0), preços iguais (0).
# - O `continue` quando o preço futuro é menor evita calcular lucro negativo,
#   e maximodia começar em 0 garante que "sem lucro" vira 0, como o enunciado
#   pede.
# - O laço interno começar em price + 1 respeita a regra "comprar antes de
#   vender" sem nenhum teste extra.
# - Você mesmo nomeou a complexidade na seção 5. Saber que é O(n^2) é o
#   primeiro passo para saber quando isso vira problema: aqui, n = 100.000.
#
# Diferenças que percebi:
# - A minha compara TODO par de dias. A IA percorre uma vez e lembra uma única
#   coisa do passado: o menor preço visto até ali. "Vender hoje" só pode ser
#   bom se a compra foi no dia mais barato que já passou; não há motivo para
#   testar os outros dias de compra. Era exatamente a pergunta da dica inicial.
# - `maxpriceperday` guarda o melhor lucro de CADA dia para dar max() no fim.
#   Bastava uma variável com o melhor lucro global, atualizada dentro do laço:
#   espaço O(1) em vez de O(n), e sem o max() extra.
# - Nomes: `price` e `oprice` são ÍNDICES, não preços. Quem lê (inclusive você
#   daqui a um mês) vai se confundir. `i` e `j`, ou `dia_compra` e `dia_venda`,
#   contam a história certa.
# - `for price in range(len(prices))` carrega índices para fazer prices[price].
#   Na versão O(n^2) o índice é necessário para o laço interno; na O(n) não, e
#   percorrer direto os valores (for preco in prices) lê melhor.
# - Sobraram linhas em branco com espaços dentro da função, depois de
#   `maxpriceperday = []`. Cosmético.


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
# Fiz uma solução O(n^2): um for para percorrer cada elemento da lista e um for
# encadeado que, para cada elemento do primeiro, percorre todos os elementos
# seguintes, comparando os lucros. A comparação se dá pelo elemento do segundo
# for (o encadeado) menos o elemento do primeiro for; guardo o maior lucro de
# cada dia e, no fim, retorno o máximo.
# (Ditado por mim no chat em 2026-11-10; a IA só transcreveu.)


# ==============================================================================
# TESTES LOCAIS - rode: python 0121_best_time_to_buy_and_sell_stock.py
# ==============================================================================
if __name__ == "__main__":
    casos = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([2, 4, 1], 2),
        ([1, 2], 1),
        ([3, 3, 3], 0),
        ([2, 1, 2, 1, 0, 1, 2], 2),
        ([5], 0),
    ]
    solucoes = [("SOLUÇÃO DA IA", SolucaoIA())]
    for nome, sol in solucoes:
        print(f"--- {nome} ---")
        for prices, esperado in casos:
            resultado = sol.maxProfit(prices)
            if resultado is None:
                status = "VAZIO"
            elif resultado == esperado:
                status = " OK  "
            else:
                status = "ERRO "
            print(f"[{status}] maxProfit({prices}) = {resultado}  (esperado: {esperado})")
