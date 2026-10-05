-- ============================================================
-- PROJETO APLICADO I - SCHULZ S.A.
-- Entrega 02 - Testes do Banco de Dados
-- Banco: SQLite
-- ============================================================


-- ============================================================
-- 1. CONSULTAR TÉCNICOS
-- ============================================================

SELECT *
FROM tecnico_solicitante;


-- ============================================================
-- 2. CONSULTAR EQUIPAMENTOS
-- ============================================================

SELECT *
FROM equipamento;


-- ============================================================
-- 3. CONSULTAR MEDIÇÕES
-- ============================================================

SELECT *
FROM medicao;


-- ============================================================
-- 4. CONSULTAR AS MEDIÇÕES COM TÉCNICO E EQUIPAMENTO
-- ============================================================

SELECT
    m.id_medicao,
    t.nome AS tecnico,
    e.codigo AS equipamento,
    m.ordem_servico,
    m.caracteristica,
    m.valor_nominal,
    m.valor_obtido,
    m.desvio,
    m.unidade,
    m.status_resultado
FROM medicao AS m
INNER JOIN tecnico_solicitante AS t
    ON m.id_tecnico = t.id_tecnico
INNER JOIN equipamento AS e
    ON m.id_equipamento = e.id_equipamento
ORDER BY m.id_medicao;


-- ============================================================
-- 5. CONSULTAR SOMENTE OS RESULTADOS APROVADOS
-- ============================================================

SELECT
    m.id_medicao,
    t.nome AS tecnico,
    e.codigo AS equipamento,
    m.caracteristica,
    m.valor_obtido,
    m.desvio,
    m.status_resultado
FROM medicao AS m
INNER JOIN tecnico_solicitante AS t
    ON m.id_tecnico = t.id_tecnico
INNER JOIN equipamento AS e
    ON m.id_equipamento = e.id_equipamento
WHERE m.status_resultado = 'APROVADO';


-- ============================================================
-- 6. CONSULTAR MEDIÇÕES POR TÉCNICO
-- ============================================================

SELECT
    t.nome AS tecnico,
    COUNT(m.id_medicao) AS quantidade_medicoes
FROM tecnico_solicitante AS t
LEFT JOIN medicao AS m
    ON t.id_tecnico = m.id_tecnico
GROUP BY t.id_tecnico, t.nome;


-- ============================================================
-- 7. TESTE DE INTEGRIDADE - FK
-- ============================================================

-- O comando abaixo foi utilizado durante os testes para
-- confirmar que o banco impede uma medição relacionada
-- a um técnico inexistente.
--
-- Não executar no teste normal.

-- INSERT INTO medicao (
--     id_tecnico,
--     id_equipamento,
--     data_medicao,
--     caracteristica,
--     valor_nominal,
--     tol_superior,
--     tol_inferior,
--     valor_obtido,
--     unidade,
--     status_resultado
-- )
-- VALUES (
--     999,
--     1,
--     '2026-10-04',
--     'Teste FK',
--     50.00,
--     0.05,
--     -0.05,
--     50.01,
--     'mm',
--     'APROVADO'
-- );


-- ============================================================
-- 8. TESTE DE INTEGRIDADE - UNIQUE
-- ============================================================

-- O comando abaixo foi utilizado durante os testes para
-- confirmar que o banco impede códigos de equipamento
-- duplicados.
--
-- Não executar no teste normal.

-- INSERT INTO equipamento
-- (codigo, nome, fabricante, modelo, numero_serie)
-- VALUES
-- (
--     'MMC001',
--     'Equipamento Duplicado',
--     'Teste',
--     'TESTE',
--     'SN999999'
-- );