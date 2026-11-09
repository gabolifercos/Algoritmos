-- ============================================================================
-- LeetCode #584 - Find Customer Referee
-- Dificuldade : Easy
-- Link        : https://leetcode.com/problems/find-customer-referee/
-- Tópicos     : SELECT, WHERE, NULL
-- Banco       : MySQL (padrão do LeetCode)
-- Status      : [x] Resolvi sozinho   [ ] Resolvi com ajuda   [ ] Não consegui
-- ============================================================================

/* ----------------------------------------------------------------------------
ENUNCIADO (traduzido)
-------------------------------------------------------------------------------
Tabela: Customer

    +-------------+---------+
    | Coluna      | Tipo    |
    +-------------+---------+
    | id          | int     |
    | name        | varchar |
    | referee_id  | int     |
    +-------------+---------+

    Na linguagem do SQL, id é a chave primária desta tabela.
    Cada linha indica o id de um cliente, seu nome e o id do cliente que o
    indicou (referee_id).

Encontre os nomes dos clientes que NÃO foram indicados pelo cliente de id = 2.

Retorne a tabela de resultado em qualquer ordem.

Exemplo 1:

    Entrada:
    Customer
    +----+------+------------+
    | id | name | referee_id |
    +----+------+------------+
    | 1  | Will | null       |
    | 2  | Jane | null       |
    | 3  | Alex | 2          |
    | 4  | Bill | null       |
    | 5  | Zack | 1          |
    | 6  | Mark | 2          |
    +----+------+------------+

    Saída:
    +------+
    | name |
    +------+
    | Will |
    | Jane |
    | Bill |
    | Zack |
    +------+
---------------------------------------------------------------------------- */

/* ----------------------------------------------------------------------------
PARA TESTAR LOCALMENTE (opcional)
-------------------------------------------------------------------------------
Funciona em MySQL e em SQLite (ex.: módulo sqlite3 do Python ou
https://sqliteonline.com).

    CREATE TABLE Customer (
        id         INT,
        name       VARCHAR(25),
        referee_id INT
    );

    INSERT INTO Customer (id, name, referee_id) VALUES
        (1, 'Will', NULL),
        (2, 'Jane', NULL),
        (3, 'Alex', 2),
        (4, 'Bill', NULL),
        (5, 'Zack', 1),
        (6, 'Mark', 2);
---------------------------------------------------------------------------- */

/* ----------------------------------------------------------------------------
DICA INICIAL (leia só se travar)
-------------------------------------------------------------------------------
Escreva a condição mais direta que vier à cabeça e rode. Compare a saída com a
esperada: sobrou ou faltou alguém? Se faltou, repare QUEM faltou e o que essas
linhas têm em comum na coluna referee_id. Esse detalhe é a lição inteira deste
exercício.
---------------------------------------------------------------------------- */


-- ============================================================================
-- 1) MINHA SOLUÇÃO
-- ============================================================================
Select name from Customer where referee_id is NULL or referee_id <> 2



-- ============================================================================
-- 2) SOLUÇÃO COMPARADA DA IA
-- ============================================================================
-- (Preenchido SOMENTE depois da minha tentativa. Objetivo: comparar abordagens,
--  não substituir a minha.)
--
-- Custo: todas as versões abaixo fazem uma varredura simples da tabela (índice
-- não ajuda num "diferente de"). A diferença é só de escrita.

SELECT name
FROM Customer
WHERE referee_id <> 2
   OR referee_id IS NULL;

-- Outras formas de escrever a mesma coisa:
--     WHERE COALESCE(referee_id, 0) <> 2     -- troca NULL por 0 antes de comparar
--     WHERE NOT referee_id <=> 2             -- <=> é o "igual seguro a NULL" do MySQL
--   (a segunda só existe em MySQL/MariaDB; não roda em SQLite nem em Postgres)
--
-- A armadilha deste exercício (e por que minha query passou):
--   `WHERE referee_id <> 2` sozinho devolve só Zack. Em SQL, NULL não é "igual"
--   nem "diferente" de nada: NULL <> 2 vale UNKNOWN, e o WHERE só deixa passar
--   linha cuja condição seja TRUE. Will, Jane e Bill sumiam. `IS NULL` é o
--   único jeito de perguntar "está vazio?".
--
-- O que está certo na minha solução:
-- - Já veio com `IS NULL OR <> 2`, ou seja, enxerguei a armadilha antes de
--   rodar. É exatamente a lição do exercício.
-- - Devolve só a coluna pedida (name), sem colunas extras.
--
-- Diferenças que percebi:
-- - Mesma lógica. A IA só inverte a ordem (<> 2 primeiro) e quebra em linhas.
--   Para o MySQL a ordem das duas condições não muda nada.
-- - `<>` e `!=` são sinônimos em MySQL. `<>` é o padrão SQL; `!=` é mais comum
--   em código do dia a dia.
-- - A IA termina com ponto e vírgula; a minha não. Num arquivo com mais de uma
--   query, como este, o `;` separa os comandos.



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
-- A usar <> para diferente e o filtro where para verificação de condições especificas em linhas 
