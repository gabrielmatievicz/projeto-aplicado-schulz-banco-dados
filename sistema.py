import sqlite3
from pathlib import Path

DB = Path(__file__).with_name("calibracao.db")


def calcular_media(valor1, valor2):
    valores = [v for v in (valor1, valor2) if v is not None]

    if not valores:
        return None

    return sum(valores) / len(valores)


def calcular_status(valor_obtido, valor_nominal, tol_inferior, tol_superior):
    limite_inferior = valor_nominal + tol_inferior
    limite_superior = valor_nominal + tol_superior

    if limite_inferior <= valor_obtido <= limite_superior:
        return "APROVADO"

    return "REPROVADO"


def criar_banco(conexao):
    conexao.execute("PRAGMA foreign_keys = ON")

    conexao.executescript(
        """
        DROP TABLE IF EXISTS medicao;
        DROP TABLE IF EXISTS equipamento;
        DROP TABLE IF EXISTS tecnico_solicitante;

        CREATE TABLE tecnico_solicitante (
            id_tecnico INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            codigo TEXT NOT NULL UNIQUE,
            setor TEXT
        );

        CREATE TABLE equipamento (
            id_equipamento INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT NOT NULL UNIQUE,
            nome TEXT NOT NULL,
            fabricante TEXT,
            modelo TEXT,
            numero_serie TEXT UNIQUE
        );

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
        """
    )

    conexao.commit()


def inserir_dados_teste(conexao):
    cursor = conexao.cursor()

    # ============================================================
    # 1. TÉCNICOS / SOLICITANTES
    # ============================================================

    cursor.execute(
        """
        INSERT INTO tecnico_solicitante
        (nome, codigo, setor)
        VALUES (?, ?, ?)
        """,
        ("João da Silva", "TEC001", "Metrologia")
    )

    id_joao = cursor.lastrowid

    cursor.execute(
        """
        INSERT INTO tecnico_solicitante
        (nome, codigo, setor)
        VALUES (?, ?, ?)
        """,
        ("Carlos Souza", "TEC002", "Qualidade")
    )

    id_carlos = cursor.lastrowid

    # ============================================================
    # 2. EQUIPAMENTOS
    # ============================================================

    cursor.execute(
        """
        INSERT INTO equipamento
        (codigo, nome, fabricante, modelo, numero_serie)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            "MMC001",
            "Máquina de Medição por Coordenadas",
            "Schulz",
            "MMC-01",
            "SN000001"
        )
    )

    id_mmc001 = cursor.lastrowid

    cursor.execute(
        """
        INSERT INTO equipamento
        (codigo, nome, fabricante, modelo, numero_serie)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            "MMC002",
            "Máquina de Medição Dimensional",
            "Schulz",
            "MMC-02",
            "SN000002"
        )
    )

    id_mmc002 = cursor.lastrowid

    # ============================================================
    # 3. PRIMEIRA MEDIÇÃO
    # ============================================================

    valor_nominal = 50.00
    tol_superior = 0.05
    tol_inferior = -0.05
    medida_1 = 50.02
    medida_2 = 50.01

    media = calcular_media(medida_1, medida_2)
    valor_obtido = media
    desvio = valor_obtido - valor_nominal

    status = calcular_status(
        valor_obtido,
        valor_nominal,
        tol_inferior,
        tol_superior
    )

    cursor.execute(
        """
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
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            id_joao,
            id_mmc001,
            "OS2026001",
            "PM001",
            "2026-10-04",
            "14:30:00",
            "DES001",
            "PCA001",
            "Diâmetro",
            valor_nominal,
            tol_superior,
            tol_inferior,
            medida_1,
            medida_2,
            media,
            valor_obtido,
            desvio,
            "mm",
            status,
            "CERT2026001",
            "João da Silva",
            "2026-10-04"
        )
    )

    # ============================================================
    # 4. SEGUNDA MEDIÇÃO
    # ============================================================

    valor_nominal = 100.00
    tol_superior = 0.10
    tol_inferior = -0.10
    medida_1 = 100.05
    medida_2 = 100.03

    media = calcular_media(medida_1, medida_2)
    valor_obtido = media
    desvio = valor_obtido - valor_nominal

    status = calcular_status(
        valor_obtido,
        valor_nominal,
        tol_inferior,
        tol_superior
    )

    cursor.execute(
        """
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
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            id_carlos,
            id_mmc002,
            "OS2026002",
            "PM002",
            "2026-10-04",
            "15:00:00",
            "DES002",
            "PCA002",
            "Comprimento",
            valor_nominal,
            tol_superior,
            tol_inferior,
            medida_1,
            medida_2,
            media,
            valor_obtido,
            desvio,
            "mm",
            status
        )
    )

    conexao.commit()


def consultar_medicoes(conexao):
    cursor = conexao.execute(
        """
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
        ORDER BY m.id_medicao
        """
    )

    return cursor.fetchall()


def validar_estrutura(conexao):
    tabelas = {
        row[0]
        for row in conexao.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )
    }

    esperadas = {
        "tecnico_solicitante",
        "equipamento",
        "medicao"
    }

    if not esperadas.issubset(tabelas):
        raise RuntimeError(
            f"Estrutura inválida. Encontrado: {sorted(tabelas)}"
        )

    chaves_estrangeiras = list(
        conexao.execute(
            "PRAGMA foreign_key_list(medicao)"
        )
    )

    if len(chaves_estrangeiras) != 2:
        raise RuntimeError(
            "As duas chaves estrangeiras esperadas não foram encontradas."
        )


def main():
    # Recria o banco para executar o projeto do zero
    if DB.exists():
        DB.unlink()

    conexao = sqlite3.connect(DB)

    try:
        conexao.execute("PRAGMA foreign_keys = ON")

        criar_banco(conexao)
        validar_estrutura(conexao)
        inserir_dados_teste(conexao)

        registros = consultar_medicoes(conexao)

        print("=" * 65)
        print("PROJETO APLICADO I - SCHULZ S.A.")
        print("BANCO DE DADOS CRIADO E VALIDADO COM SUCESSO!")
        print("=" * 65)

        for registro in registros:
            (
                id_medicao,
                tecnico,
                equipamento,
                ordem_servico,
                caracteristica,
                valor_nominal,
                valor_obtido,
                desvio,
                unidade,
                status
            ) = registro

            print(f"ID da medição: {id_medicao}")
            print(f"Técnico: {tecnico}")
            print(f"Equipamento: {equipamento}")
            print(f"Ordem de serviço: {ordem_servico}")
            print(f"Característica: {caracteristica}")
            print(f"Valor nominal: {valor_nominal:.3f}")
            print(f"Valor obtido: {valor_obtido:.3f}")
            print(f"Desvio: {desvio:.3f}")
            print(f"Unidade: {unidade}")
            print(f"Status: {status}")
            print("-" * 65)

        print(f"Banco SQLite: {DB}")

    finally:
        conexao.close()


if __name__ == "__main__":''
main();