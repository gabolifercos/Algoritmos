-- ============================================================================
-- LeetCode #577 - Employee Bonus
-- Dificuldade : Easy
-- Link        : https://leetcode.com/problems/employee-bonus/
-- Tópicos     : LEFT JOIN, NULL (IS NULL), OR
-- Banco       : MySQL (padrão do LeetCode)
-- Status      : [ ] Resolvi sozinho   [x] Resolvi com ajuda   [ ] Não consegui
-- ============================================================================

/* ----------------------------------------------------------------------------
ENUNCIADO (traduzido)
-------------------------------------------------------------------------------
Tabela: Employee

    +-------------+---------+
    | Coluna      | Tipo    |
    +-------------+---------+
    | empId       | int     |
    | name        | varchar |
    | supervisor  | int     |
    | salary      | int     |
    +-------------+---------+

    empId é a chave primária desta tabela.
    Cada linha indica o nome e o id de um funcionário, além do salário e do
    id do seu gerente (supervisor).

Tabela: Bonus

    +-------------+------+
    | Coluna      | Tipo |
    +-------------+------+
    | empId       | int  |
    | bonus       | int  |
    +-------------+------+

    empId é a chave primária desta tabela e chave estrangeira para Employee.
    Cada linha contém o id de um funcionário e o seu bônus.

Escreva uma query que reporte o nome (name) e o valor do bônus (bonus) de
cada funcionário com bônus MENOR que 1000.

Retorne a tabela de resultado em qualquer ordem.

Exemplo 1:

    Entrada:
    Employee
    +-------+--------+------------+--------+
    | empId | name   | supervisor | salary |
    +-------+--------+------------+--------+
    | 3     | Brad   | null       | 4000   |
    | 1     | John   | 3          | 1000   |
    | 2     | Dan    | 3          | 2000   |
    | 4     | Thomas | 3          | 4000   |
    +-------+--------+------------+--------+

    Bonus
    +-------+-------+
    | empId | bonus |
    +-------+-------+
    | 2     | 500   |
    | 4     | 2000  |
    +-------+-------+

    Saída:
    +------+-------+
    | name | bonus |
    +------+-------+
    | Brad | null  |
    | John | null  |
    | Dan  | 500   |
    +------+-------+

    Explicação: Brad e John não têm bônus cadastrado (null) e entram; Dan tem
    500, que é menor que 1000, e entra; Thomas tem 2000 e fica de fora.
---------------------------------------------------------------------------- */

/* ----------------------------------------------------------------------------
PARA TESTAR LOCALMENTE (opcional)
-------------------------------------------------------------------------------
Funciona em MySQL e em SQLite (ex.: módulo sqlite3 do Python ou
https://sqliteonline.com). Cole as duas tabelas e depois a sua query.

    CREATE TABLE Employee (
        empId      INT,
        name       VARCHAR(20),
        supervisor INT,
        salary     INT
    );

    INSERT INTO Employee (empId, name, supervisor, salary) VALUES
        (3, 'Brad',   NULL, 4000),
        (1, 'John',   3,    1000),
        (2, 'Dan',    3,    2000),
        (4, 'Thomas', 3,    4000);

    CREATE TABLE Bonus (
        empId INT,
        bonus INT
    );

    INSERT INTO Bonus (empId, bonus) VALUES
        (2, 500),
        (4, 2000);
---------------------------------------------------------------------------- */

/* ----------------------------------------------------------------------------
DICA INICIAL (leia só se travar)
-------------------------------------------------------------------------------
Brad e John não têm linha na tabela Bonus e MESMO ASSIM aparecem na saída, com
bonus nulo. Isso decide qual JOIN usar (releia o #175). Depois, lembre do #584:
um bônus que não existe (NULL) passa no teste `bonus < 1000`? O que o NULL
responde a QUALQUER comparação, e qual é a forma certa de perguntar "está
vazio?" em SQL? São duas condições, e basta uma delas valer.
---------------------------------------------------------------------------- */


-- ============================================================================
-- 1) MINHA SOLUÇÃO
-- ============================================================================
-- v1 (minha, 2026-11-11): certa na estrutura, mas `<= 1000` deixa passar um
-- bônus de exatamente 1000, e o enunciado pede MENOR que 1000. Sem `;`.
--   select e.name, b.bonus
--   from Employee as e left join Bonus as b on e.empId = b.empId
--   where b.bonus <= 1000 or b.bonus is null
-- v2 (corrigida pela IA a meu pedido, 2026-11-11; ver seção 3):
select e.name, b.bonus
from Employee as e left join Bonus as b on e.empId = b.empId
where b.bonus < 1000 or b.bonus is null;



-- ============================================================================
-- 2) SOLUÇÃO COMPARADA DA IA
-- ============================================================================
-- (Preenchido SOMENTE depois da minha tentativa. Objetivo: comparar abordagens,
--  não substituir a minha.)
--
-- Solução da IA (a mesma estrutura da minha: LEFT JOIN a partir de Employee e
-- duas condições no WHERE, bastando uma valer):
--
--     SELECT e.name, b.bonus
--     FROM Employee AS e
--     LEFT JOIN Bonus AS b ON b.empId = e.empId
--     WHERE b.bonus < 1000 OR b.bonus IS NULL;
--
-- Resultado (conferido pela IA em SQLite com as tabelas do bloco de teste;
-- a v1 e a v2 da seção 1 devolvem as mesmas 3 linhas aqui):
--     Brad | NULL
--     John | NULL
--     Dan  | 500
--
-- Teste extra da IA, com dois funcionários a mais: Eva com bônus de
-- exatamente 1000 e Fay com 999.
--     v1 (<= 1000) : Brad, John, Dan, Eva, Fay   <- Eva não deveria entrar
--     v2 (< 1000)  : Brad, John, Dan, Fay        <- correto
--   O exemplo do enunciado não tem ninguém com bônus 1000, por isso a v1
--   passa nele; os testes escondidos do LeetCode costumam ter esse limite.
--   Dois erros clássicos, só para ver o estrago:
--     sem o `OR b.bonus IS NULL`  : Dan, Fay          (Brad e John somem:
--                                   NULL < 1000 não é verdadeiro nem falso)
--     com INNER JOIN em vez de LEFT: Dan, Fay          (Brad e John nem
--                                   chegam ao WHERE: não têm linha em Bonus)
--
-- Outro caminho, só para conhecer: tratar "sem bônus" como zero.
--     WHERE IFNULL(b.bonus, 0) < 1000
--   IFNULL(x, 0) devolve x, ou 0 quando x é NULL (em MySQL e SQLite; o
--   padrão SQL é COALESCE). Uma condição só, mesmo resultado.
--
-- O que está certo na minha solução:
-- - LEFT JOIN a partir de Employee: Brad e John não têm linha em Bonus e
--   mesmo assim precisam aparecer. Era a pergunta da dica inicial.
-- - `b.bonus IS NULL` como segunda condição, com OR: a lição do #584 aplicada
--   sem precisar de dica. NULL não passa em nenhuma comparação, então
--   "sem bônus" tem que ser perguntado de outro jeito.
-- - Apelidos e e b, cada coluna com o dono.
--
-- O que estava errado na v1 (a IA corrigiu a meu pedido, ver seção 3):
-- - `<= 1000` em vez de `< 1000`. O enunciado diz "MENOR que 1000": 1000 não
--   entra. É o tipo de erro que o exemplo não pega e o teste escondido pega.
--   Quando a regra tem um limite, teste o próprio limite (999, 1000, 1001).
-- - Faltou o `;` no fim, de novo.
-- - Espaços sobrando no fim de duas linhas. Não quebram nada; em portfólio
--   vale limpar.


-- ============================================================================
-- 3) AJUDA QUE PEDI (preencher só se precisei)
-- ============================================================================
-- Registro de cada dica que pedi à IA, na ordem em que pedi. A IA anota aqui:
-- a query que eu tinha na hora, o prompt que mandei e a resposta que recebi.
--
-- --- Dica 1 (2026-11-11): correção feita pela IA a meu pedido ---------------
-- Query que eu tinha quando pedi:
--
--     select e.name, b.bonus
--     from Employee as e left join Bonus as b on e.empId = b.empId
--     where b.bonus <= 1000 or b.bonus is null
--
-- Prompt (o que pedi):
--
--     "terminei o 577 redija e corrija e preencha os campos necessários no que
--      aprendi coloque so reforcei conhecimentos de filtro e left join"
--
-- Resposta da IA: a estrutura (LEFT JOIN + `IS NULL` com OR) estava certa e
-- a query passava no exemplo, mas `<= 1000` inclui um bônus de exatamente
-- 1000, e o enunciado pede MENOR que 1000. A IA trocou `<=` por `<` e pôs o
-- `;` na v2 da seção 1, mantendo a v1 como comentário.


-- ============================================================================
-- 4) COMO REPRODUZI A PARTIR DA AJUDA
-- ============================================================================
-- Não reproduzi: pedi que a IA corrigisse por mim (ver seção 3). A estrutura
-- da query era minha; a correção foi no sinal da comparação: `<=` virou `<`.
-- (Anotado pela IA a partir do meu pedido no chat em 2026-11-11.)


-- ============================================================================
-- 5) O QUE APRENDI
-- ============================================================================
-- Só reforcei conhecimentos de filtro (WHERE) e de LEFT JOIN.
-- (Ditado por mim no chat em 2026-11-11; a IA só transcreveu.)
