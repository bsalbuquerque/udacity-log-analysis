CREATE VIEW top_articles AS
  SELECT title, count(path) AS views FROM articles, log
      WHERE CONCAT('/article/', slug) = log.path AND log.status = ‘200 OK’
          GROUP BY title ORDER BY views DESC LIMIT 3;

CREATE VIEW top_authors AS
  SELECT name, count(path) AS views FROM authors, articles, log
      WHERE authors.id = articles.author
      AND CONCAT('/article/', slug) = log.path and log.status = ‘200 OK’
          GROUP BY name ORDER BY views DESC;

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
