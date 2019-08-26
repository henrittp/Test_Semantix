# Project_Semantix

## Questões
Qual o objetivo do comando cache em Spark?
- O comando cache ajuda a melhorar a eficiência do código,pois permite que resultados intermediários de operações lazy possam ser armazenados e reutilizados repetidamente.

O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em MapReduce. Por quê?
- Sim, pois spark é capaz de executar tarefas de processamento em lote entre 10 a 100 vezes mais rápido que MapReduce. MapReduce é estritamente baseado em disco, enquanto Spark usa memória e pode usar um disco para processamento.

Qual é a função do SparkContext ?
- O SparkContext é um cliente do ambiente de execução do Spark e atua como o "mestre" da aplicação Spark. O SparkContext configura serviços internos e estabelece uma conexão com um ambiente de execução do Spark. Você pode criar RDDs, acumuladores e variáveis de transmissão, acessar serviços Spark e executar tarefas (até o SparkContext parar) após a criação do SparkContext. Apenas um SparkContext pode estar ativo por JVM. Se estiver ativo, você deve parar antes de criar um novo SparkContext.

Explique com suas palavras o que é Resilient Distributed Datasets (RDD)
- RDD (conjuntos de dados distribuídos resilientes) é uma coleção distribuída imutável de objetos. Cada conjunto de dados no RDD é dividido em partições lógicas, que podem ser calculadas em diferentes nós do cluster. Spark utiliza o conceito de RDD para obter operações MapReduce mais rápidas e eficientes.

GroupByKey é menos eficiente que reduceByKey em grandes dataset. Por quê?
- Sim, pois reducebykey funciona muito melhor em um grande conjunto de dados. Isso porque o Spark sabe que pode combinar a saída com uma chave comum em cada partição antes de embaralhar os dados.
 GroupByKey é apenas para agrupar seu conjunto de dados com base em uma chave o que resultará em embaralhamento de dados quando o RDD não estiver particionado.

Explique o que o código Scala abaixo faz
```
1. val textFile = sc . textFile ( "hdfs://..." )
2. val counts = textFile . flatMap ( line => line . split ( " " ))
3.           . map ( word => ( word , 1 ))
4.           . reduceByKey ( _ + _ )
5. counts . saveAsTextFile ( "hdfs://..." )
```

- (linha 1) o arquivo é lido.
- (linha 2) Cada linha é "quebrada" em uma sequência de palavras de acordo com o delimitador passado como parâmetro para a função split.
- (linha 3) Cada palavra é transformada em um mapeamente de chave-valor, com chave igual à própria palavra e valor 1
- (linha 4) Esses valores são agregados por chave, através da operação de soma.
- (linha 5) O RDD com a contagem de cada palavra é salvo em um arquivo texto.

## Desafio (dataAnalysis.py)
O principal objetivo da aplicação é ler um conjunto de dados e gerar um log com os resultados das seguintes analises:

1. Número de hosts únicos.
2. O total de erros 404.
3. Os 5 URLs que mais causaram erro 404.
4. Quantidade de erros 404 por dia.
5. O total de bytes retornados.

#### Dataset
- NASA_access_log_Jul95
- NASA_access_log_Aug95

#### Como executar
O arquivo que contém o conjunto de dados deve ser passado como parâmetro para o script:
 ```
 python dataAnalysis.py NASA_access_log_Jul95
 ```
Após a execução será gerado o log (relatorio.log) no diretório corrente.

Obs: A cada execução do script o relatorio.log é sobrescrito.
