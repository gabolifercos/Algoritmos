-- ============================================================================
-- LeetCode #595 - Big Countries
-- Dificuldade : Easy
-- Link        : https://leetcode.com/problems/big-countries/
-- Tópicos     : SELECT, WHERE, operadores lógicos (OR)
-- Banco       : MySQL (padrão do LeetCode)
-- Status      : [x] Resolvi sozinho   [ ] Resolvi com ajuda   [ ] Não consegui
-- ============================================================================

/* ----------------------------------------------------------------------------
ENUNCIADO (traduzido)
-------------------------------------------------------------------------------
Tabela: World

    +-------------+---------+
    | Coluna      | Tipo    |
    +-------------+---------+
    | name        | varchar |
    | continent   | varchar |
    | area        | int     |
    | population  | int     |
    | gdp         | bigint  |
    +-------------+---------+

    name é a chave primária (valores únicos) desta tabela.
    Cada linha contém o nome de um país, o continente ao qual pertence, sua
    área, sua população e seu PIB (gdp).

Um país é considerado GRANDE se:
    - tem área de pelo menos três milhões (3000000 km²), OU
    - tem população de pelo menos vinte e cinco milhões (25000000).

Escreva uma query que encontre o nome (name), a população (population) e a
área (area) dos países grandes.

Retorne a tabela de resultado em qualquer ordem.

Exemplo 1:

    Entrada:
    World
    +-------------+-----------+---------+------------+--------------+
    | name        | continent | area    | population | gdp          |
    +-------------+-----------+---------+------------+--------------+
    | Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
    | Albania     | Europe    | 28748   | 2831741    | 12960000000  |
    | Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
    | Andorra     | Europe    | 468     | 78115      | 3712000000   |
    | Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
    +-------------+-----------+---------+------------+--------------+

    Saída:
    +-------------+------------+---------+
    | name        | population | area    |
    +-------------+------------+---------+
    | Afghanistan | 25500100   | 652230  |
    | Algeria     | 37100000   | 2381741 |
    +-------------+------------+---------+

    Explicação: Afghanistan e Algeria entram pela população (>= 25.000.000).
    Nenhum dos cinco passa pela área, mas um país grande só precisa atender a
    UMA das duas condições.
---------------------------------------------------------------------------- */

/* ----------------------------------------------------------------------------
PARA TESTAR LOCALMENTE (opcional)
-------------------------------------------------------------------------------
Funciona em MySQL e em SQLite (ex.: módulo sqlite3 do Python ou
https://sqliteonline.com).

    CREATE TABLE World (
        name       VARCHAR(255),
        continent  VARCHAR(255),
        area       INT,
        population INT,
        gdp        BIGINT
    );

    INSERT INTO World (name, continent, area, population, gdp) VALUES
        ('Afghanistan', 'Asia',   652230,  25500100, 20343000000),
        ('Albania',     'Europe', 28748,   2831741,  12960000000),
        ('Algeria',     'Africa', 2381741, 37100000, 188681000000),
        ('Andorra',     'Europe', 468,     78115,    3712000000),
        ('Angola',      'Africa', 1246700, 20609294, 100990000000);
---------------------------------------------------------------------------- */

/* ----------------------------------------------------------------------------
DICA INICIAL (leia só se travar)
-------------------------------------------------------------------------------
Mesma espinha dorsal do #1757 (O QUE eu quero ver, DE ONDE vem, QUAIS linhas),
com uma diferença: lá as duas condições precisavam ser verdadeiras JUNTAS; aqui
basta UMA delas. Qual palavra do SQL expressa isso? Repare também que a saída
pede três colunas numa ordem específica, e que "pelo menos" inclui o valor
exato.
---------------------------------------------------------------------------- */


-- ============================================================================
-- 1) MINHA SOLUÇÃO
-- ============================================================================
Select name,population, area from World where area >= 3000000 or population >= 25000000



-- ============================================================================
-- 2) SOLUÇÃO COMPARADA DA IA
-- ============================================================================
-- (Preenchido SOMENTE depois da minha tentativa. Objetivo: comparar abordagens,
--  não substituir a minha.)
--
-- Custo: varredura simples da tabela, filtrando linha a linha. As duas versões
-- abaixo são idênticas para o otimizador do MySQL.

SELECT name, population, area
FROM World
WHERE area >= 3000000
   OR population >= 25000000;

-- O que está certo na minha solução:
-- - Espinha dorsal completa: O QUE (name, population, area), DE ONDE (World)
--   e QUAIS linhas (as duas condições unidas por OR).
-- - Colunas na ordem exata que a saída pede: name, population, area.
-- - Usou >= e não >: "pelo menos três milhões" inclui o próprio 3000000.
--   Testei com um país de área exatamente 3000000 e outro de população
--   exatamente 25000000: os dois entraram. Um com 2999999 e 24999999 ficou
--   de fora. Correto nos dois limites.
-- - OR é a escolha certa: Afghanistan e Algeria entram só pela população e
--   nenhum país do exemplo passa pela área. Com AND a saída viria vazia.
--
-- Diferenças que percebi:
-- - Mesma query. A IA só quebra em linhas e usa maiúsculas nas palavras-chave
--   (SELECT, FROM, WHERE, OR). Convenção de leitura; o MySQL não diferencia.
-- - Espaçamento: `name,population, area` mistura vírgula sem espaço e com
--   espaço. Funciona, mas um espaço após cada vírgula deixa a leitura uniforme.
-- - A IA termina com ponto e vírgula; a minha não. Terceiro arquivo com esse
--   detalhe: num arquivo com mais de uma query, como este, o `;` separa os
--   comandos.
-- - Armadilha que NÃO existe aqui: area e population nunca são NULL nesta
--   tabela, então o OR simples basta. Se pudessem ser NULL, uma linha com
--   area NULL e população grande ainda entraria (NULL OR verdadeiro =
--   verdadeiro), mas uma com os dois NULL ficaria de fora. Mesmo lembrete
--   do #584.
-- - Precedência: se um dia misturar AND com OR na mesma condição, use
--   parênteses. O AND é avaliado antes do OR, e sem parênteses a query pode
--   filtrar algo diferente do que você leu.


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
-- Uso do OR e wwhere para filtro duplo novamente
