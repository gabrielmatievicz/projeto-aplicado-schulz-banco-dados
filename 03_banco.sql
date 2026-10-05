-- ============================================================
-- PROJETO APLICADO I - SCHULZ S.A.
-- Entrega 02 - Modelagem e Implementação de Banco de Dados
-- Banco: SQLite
-- ============================================================

PRAGMA foreign_keys = ON;

-- ============================================================
-- REMOÇÃO DAS TABELAS EXISTENTES
-- ============================================================

DROP TABLE IF EXISTS medicao;
DROP TABLE IF EXISTS equipamento;
DROP TABLE IF EXISTS tecnico_solicitante;

-- ============================================================
-- 1. TÉCNICO / SOLICITANTE
-- ============================================================

CREATE TABLE tecnico_solicitante (
    id_tecnico INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    codigo TEXT NOT NULL UNIQUE,
    setor TEXT
);

-- ============================================================
-- 2. EQUIPAMENTO
-- ============================================================

CREATE TABLE equipamento (
    id_equipamento INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT NOT NULL UNIQUE,
    nome TEXT NOT NULL,
    fabricante TEXT,
    modelo TEXT,
    numero_serie TEXT UNIQUE
);

-- ============================================================
-- 3. MEDIÇÃO
-- ============================================================

CREATE TABLE medicao (
    id_medicao INTEGER PRIMARY KEY AUTOINCREMENT,

    id_tecnico INTEGER NOT NULL,
    id_equipamento INTEGER NOT NULL,

    ordem_servico TEXT,
    plano_medicao TEXT,

    data_medicao TEXT NOT NULL,
    hora_medicao TEXT,

    desenho TEXT,
    peca TEXT,
    caracteristica TEXT NOT NULL,

    valor_nominal REAL NOT NULL,
    tol_superior REAL NOT NULL,
    tol_inferior REAL NOT NULL,

    medida_1 REAL,
    medida_2 REAL,
    media REAL,
    valor_obtido REAL NOT NULL,
    desvio REAL,

    unidade TEXT NOT NULL,
    status_resultado TEXT NOT NULL,

    certificado_numero TEXT,
    usuario_aprovacao TEXT,
    data_aprovacao TEXT,

    FOREIGN KEY (id_tecnico)
        REFERENCES tecnico_solicitante(id_tecnico),

    FOREIGN KEY (id_equipamento)
        REFERENCES equipamento(id_equipamento)
);

-- ============================================================
-- DADOS DE EXEMPLO
-- ============================================================

-- Técnico 1
INSERT INTO tecnico_solicitante
(nome, codigo, setor)
VALUES
('João da Silva', 'TEC001', 'Metrologia');

-- Técnico 2
INSERT INTO tecnico_solicitante
(nome, codigo, setor)
VALUES
('Carlos Souza', 'TEC002', 'Metrologia');

-- Equipamento 1
INSERT INTO equipamento
(codigo, nome, fabricante, modelo, numero_serie)
VALUES
(
    'MMC001',
    'Máquina de Medição por Coordenadas',
    'Schulz',
    'MMC-01',
    'SN000001'
);

-- Equipamento 2
INSERT INTO equipamento
(codigo, nome, fabricante, modelo, numero_serie)
VALUES
(
    'MMC002',
    'Máquina de Medição por Coordenadas 2',
    'Schulz',
    'MMC-02',
    'SN000002'
);

-- ============================================================
-- MEDIÇÃO 1
-- ============================================================

INSERT INTO medicao (
    id_tecnico,
    id_equipamento,
    ordem_servico,
    plano_medicao,
    data_medicao,
    hora_medicao,
    desenho,
    peca,
    caracteristica,
    valor_nominal,
    tol_superior,
    tol_inferior,
    medida_1,
    medida_2,
    media,
    valor_obtido,
    desvio,
    unidade,
    status_resultado,
    certificado_numero,
    usuario_aprovacao,
    data_aprovacao
)
VALUES (
    1,
    1,
    'OS2026001',
    'PM001',
    '2026-10-04',
    '14:30:00',
    'DES001',
    'PCA001',
    'Diâmetro',
    50.00,
    0.05,
    -0.05,
    50.02,
    50.01,
    50.015,
    50.015,
    0.015,
    'mm',
    'APROVADO',
    'CERT2026001',
    'João da Silva',
    '2026-10-04'
);

-- ============================================================
-- MEDIÇÃO 2
-- ============================================================

INSERT INTO medicao (
    id_tecnico,
    id_equipamento,
    ordem_servico,
    plano_medicao,
    data_medicao,
    hora_medicao,
    desenho,
    peca,
    caracteristica,
    valor_nominal,
    tol_superior,
    tol_inferior,
    medida_1,
    medida_2,
    media,
    valor_obtido,
    desvio,
    unidade,
    status_resultado
)
VALUES (
    2,
    2,
    'OS2026002',
    'PM002',
    '2026-10-04',
    '15:30:00',
    'DES002',
    'PCA002',
    'Comprimento',
    100.00,
    0.10,
    -0.10,
    100.05,
    100.03,
    100.04,
    100.04,
    0.04,
    'mm',
    'APROVADO'
);