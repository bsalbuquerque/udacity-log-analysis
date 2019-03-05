# 🔎 Análise de Logs


Segundo projeto do programa de estudos <i>Nanodegree Fundamentos de Back-End da Udacity</i>. A aplicação retorna um relatório impresso em formato de arquivo de texto limpo, contendo respostas lastreadas nas informações do banco de dados fornecido pelo curso. Como adendo, foi criada a aplicação web com o framework `Flask` que retorna uma página contendo os mesmos resultados.

#### ❓Questões

* Quais são os três artigos mais populares de todos os tempos?
* Quem são os autores de artigos mais populares de todos os tempos?
* Em quais dias mais de 1% das requisições resultaram em erros?


[Exemplo do resultado em arquivo de texto limpo](https://raw.githubusercontent.com/bsalbuquerque/udacity-log-analysis/master/report.txt) (report.txt)

[Exemplo do resultado da aplicação web](https://raw.githubusercontent.com/bsalbuquerque/udacity-log-analysis/master/report.html) (report.html)

#### 🛠 Ferramentas necessárias
Como este repositório contem apenas códigos-fonte, algumas ferramentas serão necessárias para a execução das aplicações. São elas:

* [VirtualBox](https://www.virtualbox.org/wiki/Downloads) - Criação de ambiente para sistemas distintos
* [Vagrant](https://www.vagrantup.com/) - Configuração do sistena da máquina virtual
* PostgreSQL
* Flask - Caso deseje rodar a aplicação **web**

#### 📝 Instruções para instalação

Acesse [esta página](https://classroom.udacity.com/nanodegrees/nd051-br/parts/2c4de681-99d9-4e03-99f4-e15239804369/modules/6ca5a200-77ac-4aba-8936-4bae9f6a6d00/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0) caso ainda não tenha configurado uma VM e siga o passo-a-passo das instruções fornecidas. Cumprido este pré-requisito, você deverá:

* Caso esteja utilizando o Python3, instalar o pacote DB-API do PostgreSQL executando o comando `sudo pip3 install psycopg2` no terminal
* Como sugestão opcional, instalar o framework `Flask`para visualizar o relatório na aplicação web, executando o comando `sudo pip3 install flask` no terminal
* Baixar o banco de dados de onde foi extraída a análise dos dados - [acesse aqui](https://drive.google.com/uc?export=download&id=1lTXhG5Wnfc72r24FOcI3xYQxh4ztDwo_)
* Mover o arquivo baixado para o diretório `/vagrant` da máquina virtual
* Com o terminal aberto, executar o comando `psql -d news -f newsdata.sql` e aguardar a configuração das tabelas do banco de dados `news`
* Baixar este repositório e mover para sua pasta compartilhada `/vagrant` ❤️

#### 🕹 Executando as aplicações

* Para o relatório em formato de texto

`python3 report.py`

Aguardar a geração do arquivo 'report.txt'

* Para o relatório na aplicação web

`python3 report_html.py`

Acessar a página inputando *0.0.0.0:8000* no navegador

#### 👁 Table views

Para facilitar a verificação das consultas SQL foram criadas table views. 

1. top_articles -> `SELECT * FROM top_articles;`

```sql
CREATE VIEW top_articles AS
  SELECT title, count(path) AS views FROM articles, log
      WHERE CONCAT('/article/', slug) = log.path AND log.status = ‘200 OK’
          GROUP BY title ORDER BY views DESC LIMIT 3;
```

2. top_authors -> `SELECT * FROM top_authors;`

```sql
CREATE VIEW top_authors AS
  SELECT name, count(path) AS views FROM authors, articles, log
      WHERE authors.id = articles.author
      AND CONCAT('/article/', slug) = log.path and log.status = ‘200 OK’
          GROUP BY name ORDER BY views DESC;
```

3. morethan_one -> `SELECT * FROM morethan_one`

```sql
CREATE VIEW morethan_one AS
  SELECT * FROM
      (SELECT errors.date AS date, errors.num::decimal / oks.num * 100
        AS percent FROM
            (SELECT to_char(time, 'Mon DD,YYYY') AS date, count(status) AS num
            FROM log WHERE status != '200 OK'
                GROUP BY date ORDER BY num desc) AS errors,
            (SELECT to_char(time, 'Mon DD,YYYY') AS date, count(status) AS num
            FROM log WHERE status = '200 OK'
                GROUP BY date ORDER BY num desc) AS oks
          WHERE errors.date = oks.date ORDER BY percent DESC) AS requests
      WHERE percent > 1;
```


#### 📬 Dúvidas

Envie um e-mail com ☕️ para <contato@brunoalbuquerque.org> e será o maior prazer trocar conhecimento com você!
