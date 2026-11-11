-- ============================================================================
-- LeetCode #1581 - Customer Who Visited but Did Not Make Any Transactions
-- Dificuldade : Easy
-- Link        : https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
-- Tópicos     : LEFT JOIN, IS NULL, GROUP BY, COUNT, apelido de coluna
-- Banco       : MySQL (padrão do LeetCode)
-- Status      : [ ] Resolvi sozinho   [ ] Resolvi com ajuda   [ ] Não consegui
-- ============================================================================

/* ----------------------------------------------------------------------------
ENUNCIADO (traduzido)
-------------------------------------------------------------------------------
Tabela: Visits

    +-------------+---------+
    | Coluna      | Tipo    |
    +-------------+---------+
    | visit_id    | int     |
    | customer_id | int     |
    +-------------+---------+

    visit_id é a chave primária desta tabela.
    Esta tabela contém informações sobre os clientes que visitaram o shopping.

Tabela: Transactions

    +----------------+---------+
    | Coluna         | Tipo    |
    +----------------+---------+
    | transaction_id | int     |
    | visit_id       | int     |
    | amount         | int     |
    +----------------+---------+

    transaction_id é a chave primária desta tabela.
    Esta tabela contém informações sobre as transações feitas durante a
    visita visit_id.

Escreva uma query que encontre os IDs dos clientes que visitaram o shopping
sem fazer nenhuma transação, e o número de vezes que fizeram esse tipo de
visita.

Retorne a tabela de resultado em qualquer ordem.

Exemplo 1:

    Entrada:
    Visits
    +----------+-------------+
    | visit_id | customer_id |
    +----------+-------------+
    | 1        | 23          |
    | 2        | 9           |
    | 4        | 30          |
    | 5        | 54          |
    | 6        | 96          |
    | 7        | 54          |
    | 8        | 54          |
    +----------+-------------+

    Transactions
    +----------------+----------+--------+
    | transaction_id | visit_id | amount |
    +----------------+----------+--------+
    | 2              | 5        | 310    |
    | 3              | 5        | 300    |
    | 9              | 5        | 200    |
    | 12             | 1        | 910    |
    | 13             | 2        | 970    |
    +----------------+----------+--------+

    Saída:
    +-------------+----------------+
    | customer_id | count_no_trans |
    +-------------+----------------+
    | 54          | 2              |
    | 30          | 1              |
    | 96          | 1              |
    +-------------+----------------+

    Explicação: o cliente 23 visitou uma vez e fez uma transação (id 12). O
    cliente 9 visitou uma vez e fez uma transação (id 13). O cliente 30
    visitou uma vez e não comprou nada. O cliente 54 visitou três vezes: em
    duas não comprou nada, e em uma fez 3 transações. O cliente 96 visitou uma
    vez e não comprou nada. Logo, 30 e 96 têm uma visita sem transação cada,
    e 54 tem duas.
---------------------------------------------------------------------------- */

/* ----------------------------------------------------------------------------
PARA TESTAR LOCALMENTE (opcional)
-------------------------------------------------------------------------------
Funciona em MySQL e em SQLite (ex.: módulo sqlite3 do Python ou
https://sqliteonline.com). Cole as duas tabelas e depois a sua query.

    CREATE TABLE Visits (
        visit_id    INT,
        customer_id INT
    );

    INSERT INTO Visits (visit_id, customer_id) VALUES
        (1, 23),
        (2, 9),
        (4, 30),
        (5, 54),
        (6, 96),
        (7, 54),
        (8, 54);

    CREATE TABLE Transactions (
        transaction_id INT,
        visit_id       INT,
        amount         INT
    );

    INSERT INTO Transactions (transaction_id, visit_id, amount) VALUES
        (2,  5, 310),
        (3,  5, 300),
        (9,  5, 200),
        (12, 1, 910),
        (13, 2, 970);
---------------------------------------------------------------------------- */

/* ----------------------------------------------------------------------------
DICA INICIAL (leia só se travar)
-------------------------------------------------------------------------------
Três etapas, uma de cada vez. (1) Juntar visitas e transações SEM perder as
visitas que não têm transação: qual JOIN faz isso, e o que aparece nas colunas
da transação quando não há par? (2) Ficar só com essas visitas sem par (mesma
pergunta sobre NULL do #577). (3) Contar quantas dessas visitas cada cliente
tem. Até aqui todas as queries devolviam linhas "cruas"; para "quantas por
cliente" o SQL tem um par de palavras-chave, uma que agrupa e outra que
conta. Procure por "agregação em SQL". A coluna da contagem precisa se chamar
count_no_trans (lembre do AS). Um caminho alternativo, sem JOIN: "visitas
cujo visit_id NÃO está entre os visit_id das transações".
---------------------------------------------------------------------------- */


-- ============================================================================
-- 1) MINHA SOLUÇÃO
-- ============================================================================
select v.customer_id, count(v.customer_id) as visitas_nao_pagas from Visits as v left join  Transactions as t on v.visit_id = t.visit_id 
where t.transaction_id is null
group by v.customer_id
order by COUNT(v.customer_id) desc



-- ============================================================================
-- 2) SOLUÇÃO COMPARADA DA IA
-- ============================================================================
-- (Preenchido SOMENTE depois da minha tentativa. Objetivo: comparar abordagens,
--  não substituir a minha.)
--
-- Solução da IA (a mesma estrutura da minha: LEFT JOIN, IS NULL, GROUP BY com
-- COUNT; a coluna da contagem com o nome que o enunciado exige):
--
--     SELECT v.customer_id, COUNT(*) AS count_no_trans
--     FROM Visits AS v
--     LEFT JOIN Transactions AS t ON t.visit_id = v.visit_id
--     WHERE t.transaction_id IS NULL
--     GROUP BY v.customer_id;
--
-- Resultado (conferido pela IA em SQLite com as tabelas do bloco de teste;
-- a minha query devolve exatamente as mesmas linhas):
--     54 | 2
--     30 | 1
--     96 | 1
--
-- Caminho alternativo, sem JOIN (o da dica inicial):
--     SELECT customer_id, COUNT(*) AS count_no_trans
--     FROM Visits
--     WHERE visit_id NOT IN (SELECT visit_id FROM Transactions)
--     GROUP BY customer_id;
--   "visitas cujo id não aparece em Transactions"; lê-se quase como
--   português. Cuidado: se a lista do NOT IN tiver um NULL, ele não devolve
--   nada (aqui visit_id nunca é NULL).
--
-- Teste extra da IA, com mais linhas: a visita 7 do cliente 54 ganhou uma
-- transação; o cliente 77 entrou com duas visitas, as duas com transação; o
-- cliente 88 entrou com uma visita sem transação. Minha query e a da IA
-- respondem igual: 54 | 1 (só a visita 8 ficou sem transação), 30 | 1,
-- 96 | 1, 88 | 1; o 77 não aparece.
--
-- O que está certo na minha solução:
-- - As três etapas da dica inicial, na ordem: LEFT JOIN (não perde visitas
--   sem transação), WHERE ... IS NULL (fica só com elas), GROUP BY + COUNT
--   (quantas por cliente). Primeira agregação do portfólio, sem pedir dica.
-- - A visita 5 vira 3 linhas no JOIN (3 transações) e some inteira no WHERE,
--   então não distorce a contagem.
-- - Apelidos v e t, cada coluna com o dono.
--
-- Diferenças que percebi (a primeira faz o LeetCode recusar):
-- - A coluna da contagem PRECISA se chamar count_no_trans, como mostra a
--   saída do enunciado (e a dica inicial avisou). Com `as visitas_nao_pagas`
--   o juiz do LeetCode responde Wrong Answer mesmo com os números certos:
--   ele compara o cabeçalho também. Correção de uma palavra, e é sua.
-- - `COUNT(v.customer_id)` e `COUNT(*)` dão o mesmo aqui, porque customer_id
--   nunca é NULL. COUNT(*) conta as linhas do grupo; COUNT(coluna) conta os
--   valores não nulos daquela coluna.
-- - `ORDER BY COUNT(v.customer_id) DESC` não é pedido ("qualquer ordem") e
--   repete a conta. Se quiser manter, dá para ordenar pelo apelido:
--   `ORDER BY count_no_trans DESC`.
-- - Faltou o `;` no fim, de novo. Dois espaços entre `left join` e
--   `Transactions`, e espaços sobrando no fim da primeira linha.


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
-- Aprendi a contar e a filtrar pela nulidade das linhas da tabela: contar as
-- linhas que são nulas (as visitas sem transação) em vez de contar as que
-- têm, para pegar os valores que são exigidos.
-- (Ditado por mim no chat em 2026-11-11; a IA só transcreveu.)
