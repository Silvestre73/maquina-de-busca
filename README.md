# Máquina de busca

O projeto é composto por 3 módulos:

**MÓDULO 1:** Indexação

**MÓDULO 2**: Armazenamento

**MÓDULO 3:** Recuperação

A base de documentos a ser considerada a partir de cada área escolhida por grupo, no total de trinta documentos.
Os documentos serão considerados Artigos científicos da área escolhida, armazenar somente as seguintes informações:
* Título
* Autor
* Filiação Acadêmica
* Resumo
* Palavras-chave

## Módulo 1 - Indexação
1. Separação de palavras:
* extrair do início do documento o título, autor e todas as outras informações, deixando somente o resumo, e armazenar para posteriormente;
* varrer o texto e sempre que encontrar um espaço ou um símbolo especial considera uma palavra encerrada; (Obs. O hífen ‘-‘ é considerado uma letra);
* cada palavra encontrada é normalizada para todas letras minúsculas (mantendo-se a acentuação);
* A lista resultante é ordenada em ordem alfabética, ou outra técnica. É criado um arquivo com registros de dois campos, o primeiro contém o termo e o segundo o número de ocorrências. Exemplo: computação 3 – significa que no texto ocorreram 3 vezes a palavra computação.

2. Eliminação de stop-words:
* A lista obtida no passo anterior é confrontada com uma lista de stop words eliminando-se todas stopwords da lista.

3. Cria a lista (Term Frequency) final de pares <termo, frequência> das novas palavras e um registro
4. Passa a lista TF e o registro dos dados do novo documento para o módulo de armazenamento.

## Módulo 2 - Estrutura de dados
Este módulo mantém as seguintes estruturas de dados:

* Um dicionário de todos termos existentes na base de documentos (DT), em ordem, com a seguinte estrutura: [TERMO, QUANTIDADE]
* Uma tabela de registros de documentos contendo: <DocId, título, autor, total-de-termos-significativos>
* Um registro ,<DocId, TotPal> contendo o último identificador de documentos e o total de palavras existentes na base.
* Registro do documento original.

## Módulo 3 - Consultas
Este módulo irá permitir a colocação de uma consulta formada por uma lista de palavras chave. As palavras chaves deverão ser extraídas do dicionário de termo.

Este módulo realiza as seguintes tarefas:

1. Interface para que o usuário digite uma “frase” e clique em um botão de pesquisa 
2. Criar um vetor com os termos da consulta <v1,..,vn> (tratamento do mesmo processo da indexação deve ser feito aqui)
3. Para os termos vi da consulta, calcular a similaridade com todos os documentos da coleção. Calcular as similaridades entre v e cada di, segundo a fórmula vista em sala;
4. Apresentar os documentos ordenados de acordo com a similaridade calculada. Serão mostrados o título e autor, quando o usuário clicar abrir todas as informações do documento original.
