"""
LeetCode #20 - Valid Parentheses
Dificuldade : Easy
Link        : https://leetcode.com/problems/valid-parentheses/
Tópicos     : Strings, Pilha (Stack)
Linguagem   : Python 3
Status      : [ ] Resolvi sozinho   [x] Resolvi com ajuda   [ ] Não consegui

================================================================================
ENUNCIADO (traduzido)
================================================================================
Dada uma string s contendo apenas os caracteres '(', ')', '{', '}', '[' e ']',
determine se a string é válida.

Uma string é válida se:
    1. Todo símbolo de abertura é fechado por um símbolo do MESMO tipo.
    2. Os símbolos de abertura são fechados na ORDEM correta.
    3. Todo símbolo de fechamento tem um símbolo de abertura correspondente
       do mesmo tipo.

Exemplo 1:
    Entrada: s = "()"
    Saída  : True

Exemplo 2:
    Entrada: s = "()[]{}"
    Saída  : True

Exemplo 3:
    Entrada: s = "(]"
    Saída  : False

Exemplo 4:
    Entrada: s = "([])"
    Saída  : True

Exemplo 5:
    Entrada: s = "([)]"
    Saída  : False

Restrições:
    1 <= len(s) <= 10^4
    s contém apenas os caracteres '()[]{}'.

================================================================================
COMO USAR ESTE ARQUIVO
================================================================================
- O LeetCode entrega a função dentro de `class Solution`. Você só precisa
  escrever o corpo do método. O `self` é obrigatório como primeiro parâmetro,
  mas pode ignorá-lo por enquanto.
- `s: str` e `-> bool` são só anotações de tipo: entra um texto, sai True
  ou False.
- Para copiar para o LeetCode, leve só a `class Solution` da seção 1.
- Rode `python 0020_valid_parentheses.py` para testar com os exemplos.

================================================================================
DICA INICIAL (leia só se travar)
================================================================================
Faça na cabeça com "([)]": ao chegar no ')', qual foi o ÚLTIMO símbolo que
abriu e ainda não fechou? Foi '[', então não bate. Ou seja, você precisa
guardar os símbolos abertos e, a cada fechamento, consultar o último que entrou.
Que estrutura funciona como uma pilha de pratos (o último que entra é o primeiro
que sai)? Depois pense nos casos de borda: sobrou algo aberto no fim? Apareceu
um fechamento sem nada aberto?
"""


# ==============================================================================
# 1) MINHA SOLUÇÃO
# ==============================================================================
class Solution:
    def isValid(self, s: str) -> bool:
        lista = []
        if s[0] in [")","]","}"] or len(s) % 2 != 0:
            return False
        for parentese in range(len(s)):
            if s[parentese] == ")" and len(lista) != 0 and lista[-1] == "(":
                lista.pop()
            elif s[parentese] == "]" and len(lista) != 0 and lista[-1] == "[":
                lista.pop()    
            elif s[parentese] == "}" and len(lista) != 0 and lista[-1] == "{":
                lista.pop()    
            else:
                lista.append(s[parentese])
        if len(lista) == 0:
            return True
        else:
            return False
# ==============================================================================
# 2) SOLUÇÃO COMPARADA DA IA
# ==============================================================================
# (Preenchido SOMENTE depois da minha tentativa. Objetivo: comparar abordagens,
#  não substituir a minha.)
#
# Complexidade da minha solução : Tempo O(n^2) no pior caso*  |  Espaço O(n)
# Complexidade da solução da IA : Tempo O(n)                  |  Espaço O(n)
#
# * lista.remove(x) procura x a partir do INÍCIO da lista e, ao apagar, desloca
#   todos os elementos seguintes. Numa entrada como "((((...))))" cada fechamento
#   paga esse deslocamento inteiro. pop() tira o último elemento em O(1).
#
# Solução da IA (pilha de verdade: append para abrir, pop para fechar). É
# código de verdade: o bloco de testes no fim roda a minha e esta, lado a lado.
class SolucaoIA:
    def isValid(self, s: str) -> bool:
        pares = {")": "(", "]": "[", "}": "{"}   # fechamento -> abertura
        pilha = []
        for simbolo in s:
            if simbolo in pares:                 # é um fechamento
                if not pilha or pilha[-1] != pares[simbolo]:
                    return False                 # nada aberto, ou tipo errado
                pilha.pop()                      # fechou o último que abriu
            else:
                pilha.append(simbolo)            # é uma abertura: empilha
        return not pilha                         # válido só se nada ficou aberto


# O que está certo na minha solução:
# - A ideia central é exatamente a pilha: guardar o que abriu e, a cada
#   fechamento, conferir o ÚLTIMO que entrou (lista[-1]). Era isso que o
#   exercício queria ensinar, e você chegou nela sozinho.
# - Tratou "sobrou algo aberto" (lista não vazia no fim) e "começa fechando"
#   (o if do s[0]).
# - Passou nos 9 casos originais do arquivo.
#
# Diferenças que percebi (as duas primeiras são bugs; veja os 3 casos novos no
# bloco de testes):
# - BUG 1: lista.remove(lista[-1]) NÃO tira o último elemento. remove() apaga a
#   PRIMEIRA ocorrência daquele valor, contando do começo. Em "([()])" a pilha
#   chega a ["(", "[", "("]; quando vem o ")", remove("(") apaga o primeiro "("
#   e deixa ["[", "("]. Dali em diante a conferência sai de ordem e a função
#   responde False para uma string válida. Os 9 casos não pegaram isso porque
#   nenhum repete um símbolo de abertura com outro símbolo no meio. A operação
#   "tirar o topo da pilha" é lista.pop().
# - BUG 2: lista[-1] numa lista VAZIA levanta IndexError. O if do s[0] protege
#   só o primeiro caractere; em "())" ou "()]" a pilha esvazia no meio e o
#   fechamento seguinte derruba o programa. Toda consulta ao topo precisa vir
#   depois de "a pilha tem algo?" (if not pilha: ...).
# - Quando o fechamento não bate com o topo, a minha empilha o fechamento e
#   continua até o fim. A resposta acaba sendo False de qualquer jeito, mas o
#   laço roda à toa; pode retornar False na hora.
# - Os três if/elif são a mesma regra com símbolos trocados. Um dicionário
#   fechamento -> abertura (pares) reduz os três a uma linha e aceita pares
#   novos sem mexer na lógica.
# - for parentese in range(len(s)) só serve para fazer s[parentese]. Quando o
#   índice não é usado, percorrer direto (for simbolo in s) é mais simples.
# - if len(lista) == 0: return True / else: return False é `return not lista`
#   (lista vazia conta como False em Python). Mesma nota do #217 e do #242.
#
# --- Correção v2 (2026-11-10), feita por mim depois da comparação -------------
# O que mudei:
# - lista.remove(lista[-1]) virou lista.pop() nos três ramos.
# - O if inicial ganhou uma segunda condição: `or len(s) % 2 != 0`.
#
# O que eu pensei (minhas palavras, ditas no chat):
#   "uma foi usando ponto pop, porque eu realmente não sabia como tirar o
#    último elemento, pensei que o lista[-1] retirava o último elemento, e
#    outro no if lá de cima eu adicionei uma condição, onde se o tamanho da
#    string for ímpar, ela vai retornar False, porque se for ímpar quer dizer
#    que você tem mais parênteses ou mais fechamentos ou mais aberturas do que
#    deveria. Então, obrigatoriamente vai ser False. Então, elimina essa chance
#    do segundo bug da lista vazia levantar um IndexError."
#
# Verificação da IA:
# - BUG 1 resolvido: pop() tira o topo. "([()])" agora dá True e
#   "(((((((())))))))" continua True.
# - O teste de tamanho ímpar está CORRETO e é um bom atalho: toda string válida
#   tem tamanho par, então ímpar é False sem olhar mais nada. O LeetCode aceita.
# - Mas ele NÃO elimina o BUG 2. Paridade garante que a quantidade TOTAL de
#   símbolos é par; não garante que, em cada momento, exista algo aberto quando
#   chega um fechamento. "())(" tem tamanho 4, passa pelo if, e no terceiro
#   caractere a pilha está vazia: lista[-1] estoura IndexError. O mesmo vale
#   para "()]]" e "(){}}{". Os 12 casos do arquivo passaram porque "())" e
#   "()]" são ímpares e caem no atalho; acrescentei dois casos pares no bloco
#   de testes.
# - A pergunta de sempre continua em pé: antes de olhar lista[-1], a pilha tem
#   alguma coisa? E qual deve ser a resposta da função quando não tem?
#
# --- Correção v3 (2026-11-10), versão final ----------------------------------
# O que mudei:
# - Cada ramo ganhou `and len(lista) != 0` ANTES de `lista[-1] == ...`.
#   Como o `and` para no primeiro False, lista[-1] nunca roda com a pilha vazia.
#
# Verificação da IA: passou nos 14 casos do arquivo e em mais 11 que inventei
# ("())(", "()]]", "(){}}{", ")(", "[({})]", "((", "}}", "()(", "(()())" ...).
# BUG 2 resolvido. A solução está correta, e é O(n) em tempo e espaço.
#
# Por que funciona mesmo sem um `return False` no meio: quando chega um
# fechamento com a pilha vazia ou com o topo errado, ele cai no else e é
# EMPILHADO. Um fechamento empilhado nunca combina com nada (só se comparam
# aberturas), então a pilha jamais volta a ficar vazia e o fim responde False.
# Correto, só dá mais voltas que o necessário.
#
# Sobras de estilo (não são erros):
# - O `s[0] in [")","]","}"]` virou redundante: o primeiro caractere sendo um
#   fechamento, a pilha está vazia e o novo guarda já resolve. Pode sair.
# - `len(lista) != 0` é só `lista` em Python (lista vazia conta como False):
#   `if s[parentese] == ")" and lista and lista[-1] == "(":`.
# - Os três ramos continuam sendo a mesma regra com símbolos trocados; o
#   dicionário fechamento -> abertura da SolucaoIA junta os três.
# - `if len(lista) == 0: return True / else: return False` é `return not lista`.


# ==============================================================================
# 3) AJUDA QUE PEDI (preencher só se precisei)
# ==============================================================================
# Registro de cada dica que pedi à IA, na ordem em que pedi. A IA anota aqui:
# o código que eu tinha na hora, o prompt que mandei e a resposta que recebi.
#
# Contexto: a ideia da pilha foi minha e a primeira versão passou nos 9 casos
# originais. A dica abaixo veio DEPOIS, quando a comparação da seção 2 mostrou
# os dois bugs e eu fui consertar.
#
# --- Dica 1 (2026-11-10) ------------------------------------------------------
# Código que eu tinha quando perguntei:
#
#     class Solution:
#         def isValid(self, s: str) -> bool:
#             lista = []
#             if s[0] in [")","]","}"]:
#                 return False
#             for parentese in range(len(s)):
#                 if s[parentese] == ")" and lista[-1] == "(":
#                     lista.remove(lista[-1])
#                 elif s[parentese] == "]" and lista[-1] == "[":
#                     lista.remove(lista[-1])
#                 elif s[parentese] == "}" and lista[-1] == "{":
#                     lista.remove(lista[-1])
#                 else:
#                     lista.append(s[parentese])
#             if len(lista) == 0:
#                 return True
#             else:
#                 return False
#
# Prompt (o que perguntei):
#
#     "como remover o ultimo e elemento"
#
# Resposta da IA:
#
#     A operação "tira o último elemento e me devolve ele" tem nome em Python:
#     lista.pop(). Sem argumento, ele remove o item de índice -1 e retorna o
#     valor removido, em tempo constante. Teste no terminal do Python:
#
#         >>> p = ["(", "[", "("]
#         >>> p.pop()
#         '('
#         >>> p
#         ['(', '[']
#
#     Agora refaça com p = ["(", "[", "("] e p.remove("("): qual dos dois "("
#     some? Essa é a diferença entre os dois métodos: remove procura por VALOR
#     a partir do início; pop trabalha por POSIÇÃO, no fim. É exatamente o que
#     uma pilha precisa.
#
#     E não esqueça o segundo bug: pop() numa lista vazia também dá IndexError.
#     A pergunta "a pilha tem alguma coisa?" continua necessária antes de olhar
#     ou tirar o topo. Pense em qual resposta a função deve dar quando chega um
#     fechamento e não há nada aberto.
#
# --- Dica 2 (2026-11-10) ------------------------------------------------------
# Código que eu tinha quando perguntei: a versão v2 descrita no fim da seção 2
# (pop() nos três ramos e `or len(s) % 2 != 0` no if inicial).
#
# Prompt (o que perguntei):
#
#     "Fiz umas correções, uma foi usando ponto pop, porque eu realmente não
#      sabia como tirar o último elemento, pensei que o lista-1 retirava o
#      último elemento, e outro no if lá de cima eu adicionei uma condição,
#      onde se o tamanho da string for ímpar, ela vai retornar false, porque
#      se for ímpar quer dizer que você tem mais parênteses ou mais fechamentos
#      ou mais aberturas do que deveria. Então, obrigatoriamente vai ser false.
#      Né? Então, elimina essa chance aí do que você me apontou do segundo bug
#      da lista vazia levantar um index error. Né? Então, verifique isso e
#      ajuste a seção 2, bote um bloco abaixo dos bugs com a minha correção o
#      que eu pensei baseado no que eu te"
#
# Resposta da IA:
#
#     pop() fechou o bug 1. O teste de tamanho ímpar está certo, mas não fecha
#     o bug 2: "())(" tem tamanho par e ainda estoura IndexError, porque a
#     pilha fica vazia no meio. Paridade fala da quantidade total, não do que
#     está aberto em cada momento. Acrescentei "())(" e "()]]" aos testes.
#     A pergunta continua a mesma da Dica 1: o que precisa ser verdade sobre
#     a lista antes de olhar lista[-1]?
#


# ==============================================================================
# 4) COMO REPRODUZI A PARTIR DA AJUDA
# ==============================================================================
# (Preencho eu, com minhas palavras, depois de usar a dica.)


# ==============================================================================
# 5) O QUE APRENDI
# ==============================================================================
# Aprendi a utilizar os índices das listas e a adicionar em listas como um
# efeito de pilha, ou seja, adicionar um elemento e verificar o elemento
# posterior para ver se isso bate no contexto do exercício. Acredito que foi
# um exercício muito benéfico: demorei mais do que o necessário, mas consegui
# resolver sem a ajuda da inteligência artificial.
# (Ditado por mim no chat em 2026-11-10; a IA só transcreveu.)


# ==============================================================================
# TESTES LOCAIS - rode: python 0020_valid_parentheses.py
# ==============================================================================
if __name__ == "__main__":
    casos = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("(", False),
        ("]", False),
        ("{[]}", True),
        ("(()", False),
        # Casos acrescentados na comparação (seção 2): pegam os dois bugs.
        ("([()])", True),
        ("())", False),
        ("()]", False),
        # Casos pares acrescentados na correção v2: tamanho par e pilha vazia.
        ("())(", False),
        ("()]]", False),
    ]
    solucoes = [("MINHA SOLUÇÃO", Solution()), ("SOLUÇÃO DA IA", SolucaoIA())]
    for nome, sol in solucoes:
        print(f"--- {nome} ---")
        for s, esperado in casos:
            try:
                resultado = sol.isValid(s)
            except Exception as erro:          # um crash também é erro
                resultado = f"EXCEÇÃO {type(erro).__name__}"
            if resultado is None:
                status = "VAZIO"
            elif resultado == esperado:
                status = " OK  "
            else:
                status = "ERRO "
            print(f'[{status}] isValid("{s}") = {resultado}  (esperado: {esperado})')
