"""
LeetCode #125 - Valid Palindrome
Dificuldade : Easy
Link        : https://leetcode.com/problems/valid-palindrome/
Tópicos     : Strings, Dois Ponteiros (Two Pointers)
Linguagem   : Python 3
Status      : [ ] Resolvi sozinho   [x] Resolvi com ajuda   [ ] Não consegui

================================================================================
ENUNCIADO (traduzido)
================================================================================
Uma frase é um palíndromo se, depois de converter todas as letras maiúsculas
em minúsculas e remover todos os caracteres que não são alfanuméricos, ela se
lê da mesma forma de frente para trás e de trás para frente. Caracteres
alfanuméricos são letras e números.

Dada uma string s, retorne True se ela for um palíndromo, ou False caso
contrário.

Exemplo 1:
    Entrada: s = "A man, a plan, a canal: Panama"
    Saída  : True
    Explicação: "amanaplanacanalpanama" é um palíndromo.

Exemplo 2:
    Entrada: s = "race a car"
    Saída  : False
    Explicação: "raceacar" não é um palíndromo.

Exemplo 3:
    Entrada: s = " "
    Saída  : True
    Explicação: depois de remover os caracteres não alfanuméricos, s vira a
    string vazia "". Uma string vazia se lê igual nos dois sentidos, então é
    um palíndromo.

Restrições:
    1 <= len(s) <= 2 * 10^5
    s contém apenas caracteres ASCII imprimíveis.

================================================================================
COMO USAR ESTE ARQUIVO
================================================================================
- O LeetCode entrega a função dentro de `class Solution`. Você só precisa
  escrever o corpo do método. O `self` é obrigatório como primeiro parâmetro,
  mas pode ignorá-lo por enquanto.
- `s: str` e `-> bool` são só anotações de tipo: entra um texto, sai True
  ou False.
- Para copiar para o LeetCode, leve só a `class Solution` da seção 1.
- Rode `python 0125_valid_palindrome.py` para testar com os exemplos.

================================================================================
DICA INICIAL (leia só se travar)
================================================================================
São dois problemas separados. (1) Limpar o texto: quais caracteres contam e
como igualar maiúsculas e minúsculas. Strings do Python têm métodos prontos
para as duas coisas; procure na documentação de str algo que responda "este
caractere é letra ou número?". (2) Conferir se o texto limpo lê igual nos dois
sentidos: lembre como você comparou um número com ele mesmo invertido no #9,
ou imagine dois dedos, um no começo e um no fim, caminhando um na direção do
outro e comparando a cada passo. Cuidado com "0P": dígito e letra contam.
"""


# ==============================================================================
# 1) MINHA SOLUÇÃO
# ==============================================================================
class Solution:
    def isPalindrome(self, s: str) -> bool:
        frase = "".join(caracter for caracter in s.lower() if caracter.isalnum())
        frase_invertido = frase[::-1]
        return frase_invertido == frase                    




# ==============================================================================
# 2) SOLUÇÃO COMPARADA DA IA
# ==============================================================================
# (Preenchido SOMENTE depois da minha tentativa. Objetivo: comparar abordagens,
#  não substituir a minha.)
#
# Complexidade da minha solução : Tempo O(n)   |  Espaço O(n)*
# Complexidade da solução da IA : Tempo O(n)   |  Espaço O(1)
#
# * A minha cria duas strings novas do tamanho do texto limpo: `frase` (o join)
#   e `frase_invertido` (o [::-1]). A da IA não cria string nenhuma: compara os
#   caracteres no lugar, com dois índices.
#
# Solução da IA (dois ponteiros: um dedo em cada ponta, pulando o que não é
# alfanumérico). É código de verdade: o bloco de testes no fim roda a minha e
# esta, lado a lado.
class SolucaoIA:
    def isPalindrome(self, s: str) -> bool:
        esq, dir = 0, len(s) - 1                 # um dedo em cada ponta
        while esq < dir:
            if not s[esq].isalnum():             # não conta: pula, à esquerda
                esq += 1
            elif not s[dir].isalnum():           # não conta: pula, à direita
                dir -= 1
            elif s[esq].lower() != s[dir].lower():
                return False                     # par diferente: já era
            else:
                esq += 1                         # par igual: avança os dois
                dir -= 1
        return True                              # os dedos se cruzaram sem desacordo


# O que está certo na minha solução:
# - Separou os dois problemas da dica inicial: limpar (lower + isalnum + join)
#   e conferir (invertida == original). Cada linha faz uma coisa só.
# - A limpeza está completa: iguala maiúsculas e minúsculas E deixa passar só
#   letra ou dígito. "0P" dá False (dígito e letra contam), "ab_a" dá True.
# - Passou nos 8 casos do arquivo, nos 2 que a IA acrescentou abaixo e em mais
#   15 que a IA inventou (só pontuação, só dígitos, "Madam, I'm Adam",
#   "!!!a!!!b", ",a,,b,,a,"...).
# - É O(n) e rápida: join, lower e [::-1] rodam em C por dentro do Python.
#
# Tempo medido com 200.000 caracteres (o limite do enunciado), neste PC:
#     entrada                                  minha       IA
#     palíndromo (pior caso: compara tudo)     ~11 ms      ~16 ms
#     difere bem no meio                       ~11 ms      ~16 ms
#     difere logo nas pontas ("a...b")         ~11 ms      < 0,01 ms
#   A minha sempre faz o trabalho inteiro: limpa tudo, inverte tudo, compara
#   tudo. A da IA desiste no primeiro par diferente. Quando precisa ir até o
#   fim, a da IA é até mais lenta (laço em Python puro contra join e [::-1] em
#   C), mas gasta memória constante. No limite do LeetCode as duas passam
#   folgado.
#
# Diferenças que percebi:
# - Memória: a minha guarda duas cópias do texto limpo; a IA guarda dois
#   inteiros. Para 2 * 10^5 caracteres não importa; para um arquivo de 2 GB
#   importaria.
# - Sobre a minha explicação na seção 4: o que está dentro do join é uma
#   EXPRESSÃO GERADORA, não uma list comprehension. A diferença é o colchete:
#   `[c for c in s]` monta a lista inteira na memória antes de entregar;
#   `(c for c in s)` entrega um caractere por vez, e o join vai pegando. Quando
#   a expressão é o único argumento de uma chamada, o Python dispensa o
#   parêntese dela, por isso a linha 70 não tem colchete nem parêntese próprio.
#   E o join é chamado UMA vez só: recebe todos os caracteres aprovados e cola
#   todos de uma vez, com o separador "" (vazio) entre eles. É por isso que a
#   string sai "toda juntinha".
# - Nome: `frase_invertido` combina mal com `frase` (feminino);
#   `frase_invertida` ou só `invertida` leem melhor. Detalhe, não erro.
# - A linha do return tem espaços sobrando no fim. Não quebra nada, mas em
#   portfólio vale limpar.
#
# Versão ainda mais curta da sua ideia, só para conhecer (mesma complexidade):
#     limpa = "".join(filter(str.isalnum, s.lower()))
#     return limpa == limpa[::-1]
#   filter(função, iterável) deixa passar só os itens em que a função dá True;
#   é a sua expressão geradora com outro nome.


# ==============================================================================
# 3) AJUDA QUE PEDI (preencher só se precisei)
# ==============================================================================
# Registro de cada dica que pedi à IA, na ordem em que pedi. A IA anota aqui:
# o código que eu tinha na hora, o prompt que mandei e a resposta que recebi.
#
# --- Dica 1 (2026-11-11) ------------------------------------------------------
# Código que eu tinha quando perguntei: a função ainda vazia (só a assinatura).
#
# Prompt (o que perguntei), com a frase "remover os caracteres não
# alfanuméricos" do enunciado selecionada no editor:
#
#     "para remover s caracteres nao alfanumericos"
#
# Resposta da IA (dica, sem a solução pronta):
#
#     Para perguntar a um caractere "você é letra ou número?", as strings do
#     Python têm um método pronto: isalnum(). Ele funciona em um caractere de
#     cada vez (um caractere também é uma string, de tamanho 1):
#
#         >>> "a".isalnum()
#         True
#         >>> "7".isalnum()
#         True
#         >>> ",".isalnum()
#         False
#         >>> " ".isalnum()
#         False
#
#     A parte que é sua: em Python você não "remove" caracteres de uma string,
#     porque strings não mudam. Você constrói uma string NOVA só com os
#     caracteres que passam no teste. Pense em um for sobre s e uma variável
#     que vai acumulando os aprovados. E lembre a outra metade da limpeza:
#     maiúsculas e minúsculas precisam ficar iguais; procure o método de
#     string que faz isso. Teste a limpeza sozinha antes de pensar no
#     palíndromo: imprima o texto limpo de "A man, a plan, a canal: Panama" e
#     confira se saiu "amanaplanacanalpanama".
#


# ==============================================================================
# 4) COMO REPRODUZI A PARTIR DA AJUDA
# ==============================================================================
# Na linha 70, o que acontece é que usamos um list comprehension para ele
# colocar um join em caracteres. Para cada caractere da string recebida,
# somente se o caractere for alfanumérico, ele vai retornar o caractere. E daí
# o caractere retornado vai receber um join na variável frase, e a cada join
# vai completando a string, que fica toda juntinha, porque o nosso join está
# sem nenhum espaço dentro das aspas.
# (Ditado por mim no chat em 2026-11-11; a IA só transcreveu. Ver na seção 2 a
#  nota dela sobre "list comprehension" x expressão geradora.)


# ==============================================================================
# 5) O QUE APRENDI
# ==============================================================================
# Aprendi o uso do join para a criação de strings, o [::-1] para inverter
# strings e a comparação entre elas, e o isalnum() para verificar se um
# caractere é alfanumérico.
# (Ditado por mim no chat em 2026-11-11; a IA só transcreveu.)


# ==============================================================================
# TESTES LOCAIS - rode: python 0125_valid_palindrome.py
# ==============================================================================
if __name__ == "__main__":
    casos = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
        ("Was it a car or a cat I saw?", True),
        ("ab_a", True),
        ("a", True),
        ("No 'x' in Nixon", True),
        # Casos acrescentados na comparação (seção 2).
        (".,", True),                  # só pontuação: vira "" e "" é palíndromo
        ("1a2", False),                # dígitos contam e "1a2" não é simétrico
    ]
    solucoes = [("MINHA SOLUÇÃO", Solution()), ("SOLUÇÃO DA IA", SolucaoIA())]
    for nome, sol in solucoes:
        print(f"--- {nome} ---")
        for s, esperado in casos:
            try:
                resultado = sol.isPalindrome(s)
            except Exception as erro:          # um crash também é erro
                resultado = f"EXCEÇÃO {type(erro).__name__}"
            if resultado is None:
                status = "VAZIO"
            elif resultado == esperado:
                status = " OK  "
            else:
                status = "ERRO "
            print(f"[{status}] isPalindrome({s!r}) = {resultado}  (esperado: {esperado})")
