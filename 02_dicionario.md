# 02 - Dicionário de Dados

Os campos abaixo foram definidos a partir das informações levantadas na Entrega 01 e dos campos utilizados pelo script Python desta Entrega 02.

| Tabela | Campo | Tipo | Chave | Descrição |
|---|---|---|---|---|
| tecnico_solicitante | id_tecnico | Inteiro | PK | Identificador único do técnico/solicitante |
| tecnico_solicitante | nome | Texto | - | Nome do técnico ou solicitante |
| tecnico_solicitante | codigo | Texto | UNIQUE | Código de identificação do técnico |
| tecnico_solicitante | setor | Texto | - | Setor do técnico/solicitante |
| equipamento | id_equipamento | Inteiro | PK | Identificador único do equipamento |
| equipamento | codigo | Texto | UNIQUE | Código de identificação do equipamento |
| equipamento | nome | Texto | - | Nome ou descrição do equipamento |
| equipamento | fabricante | Texto | - | Fabricante do equipamento |
| equipamento | modelo | Texto | - | Modelo do equipamento |
| equipamento | numero_serie | Texto | UNIQUE | Número de série do equipamento |
| medicao | id_medicao | Inteiro | PK | Identificador único da medição |
| medicao | id_tecnico | Inteiro | FK | Técnico/solicitante relacionado à medição |
| medicao | id_equipamento | Inteiro | FK | Equipamento utilizado na medição |
| medicao | ordem_servico | Texto | - | Identificação da ordem de serviço |
| medicao | plano_medicao | Texto | - | Plano utilizado para realizar a medição |
| medicao | data_medicao | Texto | - | Data da medição no formato AAAA-MM-DD |
| medicao | hora_medicao | Texto | - | Horário da medição |
| medicao | desenho | Texto | - | Identificação do desenho |
| medicao | peca | Texto | - | Identificação da peça avaliada |
| medicao | caracteristica | Texto | - | Parâmetro ou característica avaliada |
| medicao | valor_nominal | Real | - | Valor de referência da medição |
| medicao | tol_superior | Real | - | Limite superior de tolerância |
| medicao | tol_inferior | Real | - | Limite inferior de tolerância |
| medicao | medida_1 | Real | - | Primeiro valor obtido |
| medicao | medida_2 | Real | - | Segundo valor obtido |
| medicao | media | Real | - | Média dos valores medidos |
| medicao | valor_obtido | Real | - | Valor final considerado para avaliação |
| medicao | desvio | Real | - | Diferença entre o valor obtido e o valor nominal |
| medicao | unidade | Texto | - | Unidade de medida utilizada |
| medicao | status_resultado | Texto | - | Situação do resultado, como APROVADO ou REPROVADO |
| medicao | certificado_numero | Texto | - | Identificação do certificado |
| medicao | usuario_aprovacao | Texto | - | Usuário responsável pela aprovação |
| medicao | data_aprovacao | Texto | - | Data da aprovação |

## Tipos de dados

No banco de dados, os identificadores numéricos são representados como **INTEGER**, os valores de medição e cálculos são representados como **REAL** e os códigos, nomes, datas e demais informações descritivas são representados como **TEXT**.

Os códigos e números de série são tratados como texto porque são identificadores e podem possuir zeros à esquerda ou caracteres alfanuméricos.

As datas são armazenadas como texto utilizando o formato padronizado **AAAA-MM-DD**, facilitando a organização e a consulta dos registros no SQLite.