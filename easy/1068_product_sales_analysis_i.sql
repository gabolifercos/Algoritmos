-- ============================================================================
-- LeetCode #1068 - Product Sales Analysis I
-- Dificuldade : Easy
-- Link        : https://leetcode.com/problems/product-sales-analysis-i/
-- Tópicos     : JOIN (INNER JOIN), duas tabelas, apelido de tabela
-- Banco       : MySQL (padrão do LeetCode)
-- Status      : [ ] Resolvi sozinho   [x] Resolvi com ajuda   [ ] Não consegui
-- ============================================================================

/* ----------------------------------------------------------------------------
ENUNCIADO (traduzido)
-------------------------------------------------------------------------------
Tabela: Sales

    +-------------+-------+
    | Coluna      | Tipo  |
    +-------------+-------+
    | sale_id     | int   |
    | product_id  | int   |
    | year        | int   |
    | quantity    | int   |
    | price       | int   |
    +-------------+-------+

    (sale_id, year) é a chave primária (combinação única) desta tabela.
    product_id é chave estrangeira para a tabela Product.
    Cada linha mostra uma venda do produto product_id em um certo ano.
    price é o preço por unidade.

Tabela: Product

    +--------------+---------+
    | Coluna       | Tipo    |
    +--------------+---------+
    | product_id   | int     |
    | product_name | varchar |
    +--------------+---------+

    product_id é a chave primária desta tabela.
    Cada linha indica o nome de um produto.

Escreva uma query que reporte product_name, year e price de cada sale_id da
tabela Sales.

Retorne a tabela de resultado em qualquer ordem.

Exemplo 1:

    Entrada:
    Sales
    +---------+------------+------+----------+-------+
    | sale_id | product_id | year | quantity | price |
    +---------+------------+------+----------+-------+
    | 1       | 100        | 2008 | 10       | 5000  |
    | 2       | 100        | 2009 | 12       | 5000  |
    | 7       | 200        | 2011 | 15       | 9000  |
    +---------+------------+------+----------+-------+

    Product
    +------------+--------------+
    | product_id | product_name |
    +------------+--------------+
    | 100        | Nokia        |
    | 200        | Apple        |
    | 300        | Samsung      |
    +------------+--------------+

    Saída:
    +--------------+------+-------+
    | product_name | year | price |
    +--------------+------+-------+
    | Nokia        | 2008 | 5000  |
    | Nokia        | 2009 | 5000  |
    | Apple        | 2011 | 9000  |
    +--------------+------+-------+

    Explicação: pela venda sale_id = 1, sabemos que a Nokia foi vendida por
    5000 em 2008. Pela sale_id = 2, Nokia por 5000 em 2009. Pela sale_id = 7,
    Apple por 9000 em 2011. Samsung não tem venda, então não aparece.
---------------------------------------------------------------------------- */

/* ----------------------------------------------------------------------------
PARA TESTAR LOCALMENTE (opcional)
-------------------------------------------------------------------------------
Funciona em MySQL e em SQLite (ex.: módulo sqlite3 do Python ou
https://sqliteonline.com). Cole as duas tabelas e depois a sua query.

    CREATE TABLE Sales (
        sale_id    INT,
        product_id INT,
        year       INT,
        quantity   INT,
        price      INT
    );

    INSERT INTO Sales (sale_id, product_id, year, quantity, price) VALUES
        (1, 100, 2008, 10, 5000),
        (2, 100, 2009, 12, 5000),
        (7, 200, 2011, 15, 9000);

    CREATE TABLE Product (
        product_id   INT,
        product_name VARCHAR(10)
    );

    INSERT INTO Product (product_id, product_name) VALUES
        (100, 'Nokia'),
        (200, 'Apple'),
        (300, 'Samsung');
---------------------------------------------------------------------------- */

/* ----------------------------------------------------------------------------
DICA INICIAL (leia só se travar)
-------------------------------------------------------------------------------
Os dados pedidos estão em duas tabelas, e o elo entre elas é product_id. No
#175 você usou LEFT JOIN para NÃO perder pessoas sem endereço. Aqui a saída é
"para cada venda": existe algum lado que precise ser mantido mesmo sem par?
Repare que a Samsung (sem venda) não aparece. Qual tipo de JOIN descreve isso?
Como as duas tabelas têm product_id, diga de qual tabela vem cada coluna
(Sales.year, ou um apelido como s.year).
---------------------------------------------------------------------------- */


-- ============================================================================
-- 1) MINHA SOLUÇÃO
-- ============================================================================
-- v1 (minha, 2026-11-11), não rodava: `=` sobrando depois do ON, `products`
-- em vez de Product, `s.products_id` em vez de s.product_id, sem `;`:
--   SELECT p.product_name, s.year, s.price
--   from sales as s inner join products as p on = p.product_id = s.products_id
--   order by s.year asc
-- v2 (corrigida pela IA a meu pedido, 2026-11-11; ver seção 3):
SELECT p.product_name, s.year, s.price
from Sales as s inner join Product as p on p.product_id = s.product_id
order by s.year asc;



-- ============================================================================
-- 2) SOLUÇÃO COMPARADA DA IA
-- ============================================================================
-- (Preenchido SOMENTE depois da minha tentativa. Objetivo: comparar abordagens,
--  não substituir a minha.)
--
-- Solução da IA (INNER JOIN pelo product_id; em SQL, "JOIN" sozinho já quer
-- dizer INNER JOIN):
--
--     SELECT p.product_name, s.year, s.price
--     FROM Sales AS s
--     JOIN Product AS p ON p.product_id = s.product_id;
--
-- Resultado (conferido pela IA em SQLite com as tabelas do bloco de teste;
-- a v2 da seção 1 devolve as mesmas 3 linhas):
--     Nokia | 2008 | 5000
--     Nokia | 2009 | 5000
--     Apple | 2011 | 9000
--
-- Teste extra da IA: uma venda com product_id 999, que não existe em Product.
-- O INNER JOIN descarta essa venda (e continua sem mostrar a Samsung, que não
-- tem venda): só sai o que casa nos DOIS lados do ON. Com LEFT JOIN a partir
-- de Sales, a venda 999 apareceria com product_name NULL. É essa a diferença
-- entre este exercício e o #175.
--
-- O que está certo na minha solução (v1):
-- - O tipo de JOIN: INNER, porque a saída é "para cada venda" e a Samsung
--   (sem venda) não aparece. Era a pergunta da dica inicial.
-- - Apelidos s e p, e cada coluna com o dono: p.product_name, s.year, s.price.
-- - As três colunas, na ordem pedida.
--
-- O que estava errado na v1 (a query não rodava; a IA corrigiu a meu pedido,
-- ver seção 3):
-- - `on = p.product_id`: um `=` sobrando logo depois do ON. Erro de sintaxe.
-- - `products`: a tabela se chama Product, no singular. "Table doesn't exist".
-- - `s.products_id`: a coluna se chama product_id. "Unknown column".
-- - Faltou o `;` no fim, de novo.
-- - `order by s.year asc` não está errado, mas o enunciado aceita qualquer
--   ordem; é trabalho a mais para o banco. E ASC já é o padrão.
-- - Nome das tabelas: em MySQL no Linux, `sales` e `Sales` podem ser tratadas
--   como tabelas diferentes (depende da configuração do servidor). O LeetCode
--   costuma aceitar os dois; escrever como está no enunciado nunca falha.


-- ============================================================================
-- 3) AJUDA QUE PEDI (preencher só se precisei)
-- ============================================================================
-- Registro de cada dica que pedi à IA, na ordem em que pedi. A IA anota aqui:
-- a query que eu tinha na hora, o prompt que mandei e a resposta que recebi.
--
-- --- Dica 1 (2026-11-11): correção feita pela IA a meu pedido ---------------
-- Query que eu tinha quando pedi:
--
--     SELECT p.product_name, s.year, s.price
--     from sales as s inner join products as p on = p.product_id = s.products_id
--     order by s.year asc
--
-- Prompt (o que pedi):
--
--     "terminei o 1068 redija e corrija coloque que aprendi inner join para
--      nao mostrar linhas que contenham o on do join nas duas tabelas"
--
-- Resposta da IA: a query não rodava por três erros de digitação (um `=`
-- sobrando depois do ON, `products` em vez de Product, `s.products_id` em vez
-- de s.product_id) e faltava o `;`. A IA corrigiu isso na v2 da seção 1,
-- mantendo a v1 como comentário. A lógica (INNER JOIN com ON e apelidos) era
-- minha e estava certa.


-- ============================================================================
-- 4) COMO REPRODUZI A PARTIR DA AJUDA
-- ============================================================================
-- Não reproduzi: pedi que a IA corrigisse por mim (ver seção 3). A lógica da
-- query era minha; a correção foi nos nomes da tabela e da coluna e num `=`
-- sobrando.
-- (Anotado pela IA a partir do meu pedido no chat em 2026-11-11.)


-- ============================================================================
-- 5) O QUE APRENDI
-- ============================================================================
-- Aprendi o INNER JOIN, para não mostrar as linhas que não contenham o valor
-- do ON do join nas duas tabelas: só aparece o que existe nos dois lados.
-- (Ditado por mim no chat em 2026-11-11; a IA só transcreveu.)
