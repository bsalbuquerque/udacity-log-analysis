#!/usr/bin/env python3
#
# Udacity Back-end fundamentals nanodegree
# Main page with answers to the questions
#

# Modules
from flask import Flask, request
from reportdb import get_articles, get_authors, get_errors

# Flask Application
app = Flask(__name__)

# HTML template for page content
HTML_WRAP = '''<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <title>Udacity - Reporting log analysis</title>
    <style>
      table{{border: 1px solid black; margin: 15px; border-collapse: collapse}}
      td, th{{border: 1px solid black; padding: 5px 4px; width: 220px}}
      thead{{background: #CFCFCF}}
    </style>
  </head>
  <body>
    <h2>Back-end fundamentals nanodegree</h2>
    <p>
      Project that consists to generate log analysis with SQL requests into a
      specific database <mark>(news)</mark> to answer some questions.
    </p>
    <h3>Questions of the project below:</h3>
    <ol>
      <li>What is the most three popular articles of the time?
        <table>
          <thead>
            <tr>
              <th><b>Article name</b></th>
              <th><b>Views</b></th>
            </tr>
          </thead>
          <tbody>
            {articles}
          </tbody>
        </table>
      <li>What is the most three popular authors of the time?
        <table>
          <thead>
            <tr>
              <th><b>Author name</b></th>
              <th><b>Views</b></th>
            </tr>
          </thead>
          <tbody>
            {authors}
          </tbody>
        </table>
      <li>On what days more than 1% of requests resulted in errors?
        <table>
          <thead>
            <tr>
              <th><b>Days</b></th>
              <th><b>Error (% percent)</b></th>
            </tr>
          </thead>
          <tbody>
            {errors}
          </tbody>
        </table>
    </ol>
  </body>
</html>'''

# HTML for articles title and number of views
QUESTION1 = '''<tr>
              <td>{0}</td>
              <td>{1}</td>
            </tr>'''

# HTML for authors title and number of views
QUESTION2 = '''<tr>
              <td>{0}</td>
              <td>{1}</td>
            </tr>'''

# HTML for dates with more than one percent of errors
QUESTION3 = '''<tr>
              <td>{0}</td>
              <td>{1}</td>
            </tr>'''

# Getting main page
@app.route('/', methods=['GET'])
def main():
    articles = "".join(QUESTION1.format(title, int(views))
    for title, views in get_articles())
    authors = "".join(QUESTION2.format(author, int(views))
    for author, views in get_authors())
    errors = "".join(QUESTION3.format(date, round(float(percent), 2))
    for date, percent in get_errors())
    html = HTML_WRAP.format(articles=articles, authors=authors, errors=errors)
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
