-- ============================================================================
-- LeetCode #1683 - Invalid Tweets
-- Dificuldade : Easy
-- Link        : https://leetcode.com/problems/invalid-tweets/
-- Tópicos     : SELECT, WHERE, funções de texto (tamanho de string)
-- Banco       : MySQL (padrão do LeetCode)
-- Status      : [ ] Resolvi sozinho   [ ] Resolvi com ajuda   [ ] Não consegui
-- ============================================================================

/* ----------------------------------------------------------------------------
ENUNCIADO (traduzido)
-------------------------------------------------------------------------------
Tabela: Tweets

    +----------------+---------+
    | Coluna         | Tipo    |
    +----------------+---------+
    | tweet_id       | int     |
    | content        | varchar |
    +----------------+---------+

    tweet_id é a chave primária (valores únicos) desta tabela.
    content consiste em caracteres alfanuméricos, '!' ou ' ' (espaço), sem
    outros caracteres especiais.
    Cada linha contém o id de um tweet e o seu texto.

Escreva uma query que encontre os IDs dos tweets INVÁLIDOS. Um tweet é inválido
se o número de caracteres do seu content for ESTRITAMENTE maior que 15.

Retorne a tabela de resultado em qualquer ordem.

Exemplo 1:

    Entrada:
    Tweets
    +----------+-----------------------------------+
    | tweet_id | content                           |
    +----------+-----------------------------------+
    | 1        | Let us Code                       |
    | 2        | More than fifteen chars are here! |
    +----------+-----------------------------------+

    Saída:
    +----------+
    | tweet_id |
    +----------+
    | 2        |
    +----------+

    Explicação: o tweet 1 tem 11 caracteres (válido). O tweet 2 tem 33
    caracteres (inválido).
---------------------------------------------------------------------------- */

/* ----------------------------------------------------------------------------
PARA TESTAR LOCALMENTE (opcional)
-------------------------------------------------------------------------------
Funciona em MySQL e em SQLite (ex.: módulo sqlite3 do Python ou
https://sqliteonline.com). Atenção: no SQLite, LENGTH() conta caracteres; no
MySQL, LENGTH() conta bytes e CHAR_LENGTH() conta caracteres. Com texto só em
inglês dá no mesmo.

    CREATE TABLE Tweets (
        tweet_id INT,
        content  VARCHAR(50)
    );

    INSERT INTO Tweets (tweet_id, content) VALUES
        (1, 'Let us Code'),
        (2, 'More than fifteen chars are here!');
---------------------------------------------------------------------------- */

/* ----------------------------------------------------------------------------
DICA INICIAL (leia só se travar)
-------------------------------------------------------------------------------
Você precisa de uma função do SQL que responda "quantos caracteres tem este
texto?". No MySQL existem duas com nomes parecidos: uma conta BYTES e a outra
conta CARACTERES. Com texto em inglês dá no mesmo, mas com acentos não; vale
descobrir qual é qual. E atenção ao "estritamente maior": um tweet com exatos
15 caracteres ainda é válido.
---------------------------------------------------------------------------- */


-- ============================================================================
-- 1) MINHA SOLUÇÃO
-- ============================================================================
select tweet_id from Tweets where len(content) <= 15



-- ============================================================================
-- 2) SOLUÇÃO COMPARADA DA IA
-- ============================================================================
-- (Preenchido SOMENTE depois da minha tentativa. Objetivo: comparar abordagens,
--  não substituir a minha.)
--
-- Custo: varredura simples da tabela, calculando o tamanho de cada content e
-- filtrando linha a linha.

SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15;

-- No MySQL do LeetCode, CHAR_LENGTH conta CARACTERES e LENGTH conta BYTES.
-- Para este enunciado (só letras, números, '!' e espaço) as duas dão o mesmo
-- número; com acentos, 'ção' tem 3 caracteres e 5 bytes. No SQLite só existe
-- LENGTH, e lá ela conta caracteres.
--
-- O que está certo na minha solução (v1):
-- - Espinha dorsal no lugar: O QUE (tweet_id), DE ONDE (Tweets), QUAIS linhas
--   (uma condição sobre o tamanho do texto).
-- - Aplicar uma função ao content dentro do WHERE é exatamente a ferramenta
--   que o exercício pede.
--
-- Diferenças que percebi (as duas primeiras são erros; a v1 não passa):
-- - ERRO 1: len() não existe em SQL. É o nome da função do Python. O MySQL
--   responderia "FUNCTION Tweets.len does not exist" e o SQLite "no such
--   function: len". Os nomes certos estão no comentário "PARA TESTAR
--   LOCALMENTE" deste arquivo.
-- - ERRO 2: a comparação está invertida. O enunciado pede os tweets INVÁLIDOS,
--   com tamanho ESTRITAMENTE maior que 15. `<= 15` seleciona os válidos.
--   Testei trocando só len por LENGTH e mantendo o <= 15: a tabela do exemplo
--   devolve o tweet 1 (11 caracteres), e o esperado é o 2 (33). Com três
--   linhas a mais (15, 16 e 0 caracteres) a v1 devolve 1, 3 e 5; o esperado é
--   2 e 4. Exatamente o oposto.
-- - Sem ponto e vírgula no fim, quarto arquivo seguido.
-- - Como conferir sozinho antes de dizer "terminei": cole o bloco CREATE/INSERT
--   deste arquivo e a sua query em https://sqliteonline.com. Lá o len() já
--   teria dado erro na hora, e o resultado invertido ficaria na cara.


-- ============================================================================
-- 3) AJUDA QUE PEDI (preencher só se precisei)
-- ============================================================================
-- Não pedi ajuda neste exercício.


-- ============================================================================
-- 4) COMO REPRODUZI A PARTIR DA AJUDA
-- ============================================================================
-- Não se aplica: resolvi sem pedir ajuda.


-- ============================================================================
-- 5) O QUE APRENDI
-- ============================================================================
-- O uso do LENGTH, que serve para medir a quantidade de caracteres, neste
-- exemplo, de uma string. E, com isso, usar o filtro de comparação do WHERE
-- para determinar quais tweets seriam selecionados.
-- (Ditado por mim no chat em 2026-11-10; a IA só transcreveu.)
