## 01 - Organização dos Dados

## Modelo Conceitual Simplificado

O banco de dados proposto tem como objetivo organizar as informações relacionadas ao processo de calibração da Schulz S.A.

Na situação analisada na Entrega 01, os dados utilizados no processo de medição e na emissão dos certificados estão distribuídos entre arquivos de medição, planilhas de controle e cadastros auxiliares.

Para a Entrega 02, essas informações serão organizadas em três entidades principais: **Técnico/Solicitante, Equipamento e Medição**.

A entidade **Técnico/Solicitante** armazena as informações da pessoa responsável pela realização da medição ou relacionada à solicitação do processo.

Entre os dados dessa entidade estão o identificador, nome, código e setor do técnico ou solicitante.

A entidade **Equipamento** armazena as informações dos equipamentos utilizados durante o processo de medição.

Entre os dados do equipamento estão seu identificador, código, nome, fabricante, modelo e número de série.

A entidade **Medição** concentra as informações específicas de cada medição realizada.

Cada registro de medição possui uma identificação própria por meio de uma chave primária.

A tabela de Medição também possui chaves estrangeiras para relacionar cada registro ao Técnico/Solicitante e ao Equipamento utilizado.

Dessa forma, um mesmo técnico ou solicitante pode estar relacionado a várias medições.

Da mesma maneira, um mesmo equipamento pode ser utilizado em diversas medições ao longo do tempo.

Essa estrutura permite manter um histórico das medições realizadas, relacionando cada resultado ao responsável e ao equipamento utilizado.

Os dados da medição incluem informações como ordem de serviço, plano de medição, data, horário, desenho, peça e característica avaliada.

Também são armazenados o valor nominal, as tolerâncias superior e inferior e os valores obtidos durante a medição.

Quando aplicável, podem ser armazenados os valores das medidas individuais, a média, o valor obtido, o desvio, a unidade de medida e o status do resultado.

Também podem ser registrados o número do certificado, o usuário responsável pela aprovação e a data de aprovação.

A utilização de chaves primárias garante que cada registro seja identificado de forma única dentro de sua respectiva tabela.

As chaves estrangeiras garantem que uma medição esteja relacionada a registros existentes de Técnico/Solicitante e Equipamento.

A separação das informações em diferentes entidades ajuda a evitar a duplicação de dados.

Por exemplo, os dados de um técnico não precisam ser repetidos em todos os registros de medição realizados por ele.

O mesmo ocorre com os dados de um equipamento, pois fabricante, modelo e número de série ficam cadastrados uma única vez e podem ser utilizados em várias medições.

Essa organização reduz a possibilidade de inconsistências e facilita a manutenção e atualização dos dados.

A estrutura também facilita consultas e a recuperação do histórico das medições realizadas.

O modelo proposto atende ao objetivo da Entrega 02 de organizar as informações do processo de calibração em uma estrutura relacional utilizando SQLite.

Assim, o banco de dados proporciona uma estrutura mais organizada para armazenamento, relacionamento e consulta das informações utilizadas no processo de calibração.