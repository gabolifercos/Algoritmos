-- ============================================================================
-- LeetCode #1757 - Recyclable and Low Fat Products
-- Dificuldade : Easy
-- Link        : https://leetcode.com/problems/recyclable-and-low-fat-products/
-- Tópicos     : SELECT, WHERE, operadores lógicos
-- Banco       : MySQL (padrão do LeetCode)
-- Status      : [x] Resolvi sozinho   [ ] Resolvi com ajuda   [ ] Não consegui
-- ============================================================================

/* ----------------------------------------------------------------------------
ENUNCIADO (traduzido)
-------------------------------------------------------------------------------
Tabela: Products

    +-------------+---------+
    | Coluna      | Tipo    |
    +-------------+---------+
    | product_id  | int     |
    | low_fats    | enum    |
    | recyclable  | enum    |
    +-------------+---------+

    product_id é a chave primária (valores únicos) desta tabela.
    low_fats é um ENUM do tipo ('Y', 'N'): 'Y' significa que o produto é
    light (baixa gordura) e 'N' que não é.
    recyclable é um ENUM do tipo ('Y', 'N'): 'Y' significa que o produto é
    reciclável e 'N' que não é.

Escreva uma query que encontre os ids dos produtos que são, AO MESMO TEMPO,
light e recicláveis.

Retorne a tabela de resultado em qualquer ordem.

Exemplo 1:

    Entrada:
    Products
    +-------------+----------+------------+
    | product_id  | low_fats | recyclable |
    +-------------+----------+------------+
    | 0           | Y        | N          |
    | 1           | Y        | Y          |
    | 2           | N        | Y          |
    | 3           | Y        | Y          |
    | 4           | N        | N          |
    +-------------+----------+------------+

    Saída:
    +-------------+
    | product_id  |
    +-------------+
    | 1           |
    | 3           |
    +-------------+

    Explicação: apenas os produtos 1 e 3 são light E recicláveis.
---------------------------------------------------------------------------- */

/* ----------------------------------------------------------------------------
PARA TESTAR LOCALMENTE (opcional)
-------------------------------------------------------------------------------
Funciona em MySQL e em SQLite (ex.: módulo sqlite3 do Python ou
https://sqliteonline.com). Troquei ENUM por VARCHAR só para rodar nos dois.

    CREATE TABLE Products (
        product_id INT,
        low_fats   VARCHAR(1),
        recyclable VARCHAR(1)
    );

    INSERT INTO Products (product_id, low_fats, recyclable) VALUES
        (0, 'Y', 'N'),
        (1, 'Y', 'Y'),
        (2, 'N', 'Y'),
        (3, 'Y', 'Y'),
        (4, 'N', 'N');
---------------------------------------------------------------------------- */

/* ----------------------------------------------------------------------------
DICA INICIAL (leia só se travar)
-------------------------------------------------------------------------------
Toda query de filtro tem a mesma espinha dorsal: O QUE eu quero ver, DE ONDE
vem, e QUAIS linhas me interessam. Aqui são duas condições que precisam ser
verdadeiras juntas. Qual palavra do SQL junta duas condições assim?
---------------------------------------------------------------------------- */


-- ============================================================================
-- 1) MINHA SOLUÇÃO
-- ============================================================================
SELECT product_id from Products where low_fats = 'Y' and recyclable = 'Y'


-- ============================================================================
-- 2) SOLUÇÃO COMPARADA DA IA
-- ============================================================================
-- (Preenchido SOMENTE depois da minha tentativa. Objetivo: comparar abordagens,
--  não substituir a minha.)
--
-- Custo: varredura simples da tabela, filtrando linha a linha. As duas versões
-- abaixo são idênticas para o otimizador do MySQL.

SELECT product_id
FROM Products
WHERE low_fats = 'Y'
  AND recyclable = 'Y';

-- O que está certo na minha solução:
-- - Espinha dorsal completa: O QUE (product_id), DE ONDE (Products) e QUAIS
--   linhas (as duas condições unidas por AND).
-- - Comparou com 'Y' entre aspas simples, que é como o MySQL trata o ENUM desta
--   tabela. Sem aspas, Y viraria nome de coluna e daria erro.
--
-- Diferenças que percebi:
-- - Mesma query. A IA só quebra em linhas e usa maiúsculas nas palavras-chave
--   (FROM, WHERE, AND). Convenção de leitura; o MySQL não diferencia.
-- - A IA termina com ponto e vírgula; a minha não. Num arquivo com mais de uma
--   query, como este, o `;` separa os comandos.
-- - Armadilha que NÃO existe aqui, mas existe no vizinho (#584): as duas colunas
--   são ENUM 'Y'/'N' e nunca ficam NULL, então o AND simples basta.



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
-- A utiizar and para verificação de duas condições na hora de filtrar a query
