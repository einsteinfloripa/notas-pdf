

# Notas-pdf

Geração de PDF automatizado de desempenho individual dos alunos

## Description

O projeto foi feito com o objetivo de gerar relatórios em pdf de simulados realizados pelos alunos do Einstein Floripa

## Primeiros Passos

### Dependencias

Para instalar as depedencias do projeto, utilize :
```shell
$ pip install -r ./requirements/requirements.txt
```

### Execução do programa

* O arquivo studentsObject.py é responsável por coletar as informações dos estudantes e tem a funcão principal para rodar e gerar todos os PDFS

* O arquivo layout.py fica responsável apenas por construir o layout do PDF.

* infos.py é o arquivo responsável por coletar dados da planilha e gerar um dicionário que utiliza o CPF do aluno como chave e o nome do aluno como valor

## Entrada
### Coloque todos os arquivos a seguir na pasta assets:
*  Uma planilha com nomeada "alunos_infos.csv" que segue o exemplo: [alunos_infos.csv](https://docs.google.com/spreadsheets/d/1qcMPtjl_alxNrsyyoLf03T3io6KqqQY9MMRQjJhQHF8/edit?usp=sharing)

*  Uma planilha com o gabarito oficial nomeada "gabarito_oficial.csv" da prova que segue o exemplo: [Gabarito.csv](https://docs.google.com/spreadsheets/d/1PWZcggZ8dgjvqNzvmkWFJPKI2ZCwQcLzl2xSJya_od4/edit?usp=sharing) 

*  Uma planilha com os dados brutos da prova nomeada "dados_brutos.csv" que segue o exemplo: [dados_brutos.csv](https://docs.google.com/spreadsheets/d/1u5oqa3SEUwNgMILGOFIaU61FFNi2gR5q/edit?usp=sharing&ouid=108849602823930974697&rtpof=true&sd=true) - Essa é a planilha gerada pela IA

*  Uma planilha com o ranking dos alunos nomeada "ranking.csv" que segue o exemplo: [ranking.csv](https://docs.google.com/spreadsheets/d/1lqL_7Mqi-RMFUh3u_6Xj93lIpVLdXDy-YPC7C-SwyVM/edit?usp=sharing) - Essa planilha pode ser gerada pelo [relatorio-provasPDF](https://github.com/einsteinfloripa/relatorio-provasPDF)  -> 




