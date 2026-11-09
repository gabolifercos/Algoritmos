-- ============================================================================
-- LeetCode #175 - Combine Two Tables
-- Dificuldade : Easy
-- Link        : https://leetcode.com/problems/combine-two-tables/
-- Tópicos     : JOIN, NULL
-- Banco       : MySQL (padrão do LeetCode)
-- Status      : [x] Resolvi sozinho   [ ] Resolvi com ajuda   [ ] Não consegui
-- ============================================================================

/* ----------------------------------------------------------------------------
ENUNCIADO (traduzido)
-------------------------------------------------------------------------------
Tabela: Person

    +-------------+---------+
    | Coluna      | Tipo    |
    +-------------+---------+
    | personId    | int     |
    | lastName    | varchar |
    | firstName   | varchar |
    +-------------+---------+

    personId é a chave primária (valores únicos) desta tabela.
    Cada linha contém informações sobre o id de uma pessoa, seu nome e
    sobrenome.

Tabela: Address

    +-------------+---------+
    | Coluna      | Tipo    |
    +-------------+---------+
    | addressId   | int     |
    | personId    | int     |
    | city        | varchar |
    | state       | varchar |
    +-------------+---------+

    addressId é a chave primária (valores únicos) desta tabela.
    Cada linha contém informações sobre a cidade e o estado de uma pessoa com
    id = personId.

Escreva uma query que mostre o primeiro nome, o sobrenome, a cidade e o estado
de CADA pessoa da tabela Person. Se o endereço de um personId não existir na
tabela Address, mostre null no lugar.

Retorne a tabela de resultado em qualquer ordem.

Exemplo 1:

    Entrada:
    Person
    +----------+----------+-----------+
    | personId | lastName | firstName |
    +----------+----------+-----------+
    | 1        | Wang     | Allen     |
    | 2        | Alice    | Bob       |
    +----------+----------+-----------+

    Address
    +-----------+----------+---------------+------------+
    | addressId | personId | city          | state      |
    +-----------+----------+---------------+------------+
    | 1         | 2        | New York City | New York   |
    | 2         | 3        | Leetcode      | California |
    +-----------+----------+---------------+------------+

    Saída:
    +-----------+----------+---------------+----------+
    | firstName | lastName | city          | state    |
    +-----------+----------+---------------+----------+
    | Allen     | Wang     | null          | null     |
    | Bob       | Alice    | New York City | New York |
    +-----------+----------+---------------+----------+

    Explicação: não há endereço na tabela Address para personId = 1, por isso
    mostramos null na cidade e no estado dessa pessoa. addressId = 2 pertence
    a personId = 3, que não existe em Person, então não aparece no resultado.
---------------------------------------------------------------------------- */

/* ----------------------------------------------------------------------------
PARA TESTAR LOCALMENTE (opcional)
-------------------------------------------------------------------------------
Funciona em MySQL e em SQLite (ex.: módulo sqlite3 do Python ou
https://sqliteonline.com).

    CREATE TABLE Person (
        personId  INT,
        lastName  VARCHAR(255),
        firstName VARCHAR(255)
    );

    CREATE TABLE Address (
        addressId INT,
        personId  INT,
        city      VARCHAR(255),
        state     VARCHAR(255)
    );

    INSERT INTO Person (personId, lastName, firstName) VALUES
        (1, 'Wang',  'Allen'),
        (2, 'Alice', 'Bob');

    INSERT INTO Address (addressId, personId, city, state) VALUES
        (1, 2, 'New York City', 'New York'),
        (2, 3, 'Leetcode',      'California');
---------------------------------------------------------------------------- */

/* ----------------------------------------------------------------------------
DICA INICIAL (leia só se travar)
-------------------------------------------------------------------------------
Existe mais de um tipo de JOIN, e eles diferem exatamente em quem "sobrevive"
quando não há correspondência do outro lado. Releia o enunciado: a frase
"CADA pessoa da tabela Person" diz qual tabela deve aparecer inteira.
---------------------------------------------------------------------------- */


-- ============================================================================
-- 1) MINHA SOLUÇÃO
-- ============================================================================
SELECT p.firstName,p.lastName,a.city,a.state from Person as p left join Address as a on p.personId = a.personId 



-- ============================================================================
-- 2) SOLUÇÃO COMPARADA DA IA
-- ============================================================================
-- (Preenchido SOMENTE depois da minha tentativa. Objetivo: comparar abordagens,
--  não substituir a minha.)
--
-- Custo: as duas versões geram o mesmo plano de execução (um LEFT JOIN por
-- personId). Não existe versão "mais rápida" aqui; a diferença é só de escrita.

SELECT p.firstName, p.lastName, a.city, a.state
FROM Person AS p
LEFT JOIN Address AS a
    ON a.personId = p.personId;

-- O que está certo na minha solução:
-- - LEFT JOIN com Person do lado esquerdo: é a tabela que não pode perder
--   linhas, exatamente o que "CADA pessoa da tabela Person" pedia.
-- - Ligação pela coluna certa (personId) e as quatro colunas na ordem pedida.
-- - Apelidos p e a deixam a query curta e legível.
--
-- Diferenças que percebi:
-- - Mesma lógica. A IA só quebra em linhas (uma cláusula por linha) e escreve
--   as palavras-chave em maiúsculas (SELECT, FROM, LEFT JOIN, ON). Para o
--   MySQL não muda nada; é convenção de leitura.
-- - A IA termina com ponto e vírgula. O LeetCode aceita sem, mas num script
--   com mais de uma query ele é obrigatório para separar os comandos.
-- - Armadilha que eu evitei: um INNER JOIN (ou só JOIN) teria derrubado o
--   Allen Wang, que não tem endereço. O LEFT JOIN preserva a linha com null.



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
-- Utilizar left join para mostras as informações de duas tabelas de forma conjunta
-- e preservando linhas que as vezes não contenham todas as informações na outra tabela

