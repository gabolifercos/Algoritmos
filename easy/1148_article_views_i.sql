-- ============================================================================
-- LeetCode #1148 - Article Views I
-- Dificuldade : Easy
-- Link        : https://leetcode.com/problems/article-views-i/
-- Tópicos     : SELECT, WHERE comparando colunas, DISTINCT, ORDER BY, alias
-- Banco       : MySQL (padrão do LeetCode)
-- Status      : [ ] Resolvi sozinho   [ ] Resolvi com ajuda   [ ] Não consegui
-- ============================================================================

/* ----------------------------------------------------------------------------
ENUNCIADO (traduzido)
-------------------------------------------------------------------------------
Tabela: Views

    +---------------+---------+
    | Coluna        | Tipo    |
    +---------------+---------+
    | article_id    | int     |
    | author_id     | int     |
    | viewer_id     | int     |
    | view_date     | date    |
    +---------------+---------+

    Esta tabela NÃO tem chave primária e pode conter linhas duplicadas.
    Cada linha indica que algum leitor (viewer) visualizou um artigo (escrito
    por algum autor) em alguma data.
    Note que author_id e viewer_id iguais indicam a MESMA pessoa.

Escreva uma query que encontre todos os autores que visualizaram pelo menos um
dos seus próprios artigos.

Retorne a tabela de resultado ordenada por id em ordem crescente.

Exemplo 1:

    Entrada:
    Views
    +------------+-----------+-----------+------------+
    | article_id | author_id | viewer_id | view_date  |
    +------------+-----------+-----------+------------+
    | 1          | 3         | 5         | 2019-08-01 |
    | 1          | 3         | 6         | 2019-08-02 |
    | 2          | 7         | 7         | 2019-08-01 |
    | 2          | 7         | 6         | 2019-08-02 |
    | 4          | 7         | 1         | 2019-07-22 |
    | 3          | 4         | 4         | 2019-07-21 |
    | 3          | 4         | 4         | 2019-07-21 |
    +------------+-----------+-----------+------------+

    Saída:
    +------+
    | id   |
    +------+
    | 4    |
    | 7    |
    +------+

    Explicação: o autor 7 viu o próprio artigo 2 e o autor 4 viu o próprio
    artigo 3 (duas vezes, mas ele aparece uma vez só na saída). O autor 3
    nunca viu os próprios artigos.
---------------------------------------------------------------------------- */

/* ----------------------------------------------------------------------------
PARA TESTAR LOCALMENTE (opcional)
-------------------------------------------------------------------------------
Funciona em MySQL e em SQLite (ex.: módulo sqlite3 do Python ou
https://sqliteonline.com).

    CREATE TABLE Views (
        article_id INT,
        author_id  INT,
        viewer_id  INT,
        view_date  DATE
    );

    INSERT INTO Views (article_id, author_id, viewer_id, view_date) VALUES
        (1, 3, 5, '2019-08-01'),
        (1, 3, 6, '2019-08-02'),
        (2, 7, 7, '2019-08-01'),
        (2, 7, 6, '2019-08-02'),
        (4, 7, 1, '2019-07-22'),
        (3, 4, 4, '2019-07-21'),
        (3, 4, 4, '2019-07-21');
---------------------------------------------------------------------------- */

/* ----------------------------------------------------------------------------
DICA INICIAL (leia só se travar)
-------------------------------------------------------------------------------
Até agora o WHERE comparou uma coluna com um VALOR fixo ('Y', NULL, um número).
Aqui a condição compara duas COLUNAS da mesma linha. Depois, releia a saída
esperada com atenção: a coluna se chama id, não author_id; o autor 4 aparece
uma vez só, mesmo tendo duas linhas; e a lista vem ordenada. Cada um desses
três detalhes tem uma palavra-chave própria do SQL.
---------------------------------------------------------------------------- */


-- ============================================================================
-- 1) MINHA SOLUÇÃO
-- ============================================================================
select author_id as id from Views where author_id = viewer_id group by id



-- ============================================================================
-- 2) SOLUÇÃO COMPARADA DA IA
-- ============================================================================
-- (Preenchido SOMENTE depois da minha tentativa. Objetivo: comparar abordagens,
--  não substituir a minha.)
--
-- Custo: varredura da tabela filtrando linha a linha, depois uma etapa para
-- remover repetidos e ordenar. DISTINCT e GROUP BY sem agregação viram o mesmo
-- plano no MySQL; a diferença real entre as duas versões é o ORDER BY.

SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;

-- O que está certo na minha solução:
-- - A condição compara duas colunas da mesma linha (author_id = viewer_id),
--   que era o conceito novo deste exercício.
-- - Renomeou a coluna com AS id, como a saída pede.
-- - Tirou os repetidos com GROUP BY id. Sem função de agregação (COUNT, SUM),
--   GROUP BY numa coluna só faz o mesmo que DISTINCT: uma linha por valor. É
--   um caminho válido, e o MySQL aceita o alias no GROUP BY.
-- - Testei com a tabela do exemplo e com três linhas extras (autores 2 e 10,
--   o 2 repetido duas vezes): vieram 2, 4, 7 e 10, sem repetição.
--
-- Diferenças que percebi (a primeira é um requisito do enunciado que ficou
-- de fora):
-- - Faltou o ORDER BY id. O enunciado diz "ordenada por id em ordem crescente",
--   e a dica inicial contava três palavras-chave: uma para renomear (AS), uma
--   para não repetir (DISTINCT ou GROUP BY) e uma para ordenar (ORDER BY).
--   GROUP BY NÃO garante ordem: até o MySQL 5.7 ele ordenava como efeito
--   colateral, e o MySQL 8.0, que o LeetCode usa, removeu isso de propósito.
--   Nos meus testes a saída veio ordenada por coincidência do motor; sem
--   ORDER BY, o SQL não promete nada. Query que passa por sorte é a que quebra
--   no dia da prova.
-- - DISTINCT diz O QUE você quer ("sem repetidos"); GROUP BY diz COMO fazer
--   ("agrupe"). Quando não há agregação, DISTINCT comunica melhor a intenção.
-- - Sem ponto e vírgula no fim.
-- - Maiúsculas nas palavras-chave: convenção de leitura, não regra.


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
-- Aprendi a comparação de colunas; na verdade, a usar o WHERE para comparar
-- colunas entre si e conseguir trazer os resultados necessários.
-- (Ditado por mim no chat em 2026-11-10; a IA só transcreveu.)
