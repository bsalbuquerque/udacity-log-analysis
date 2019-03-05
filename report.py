#!/usr/bin/env python3
#
# Udacity Back-End Fundamentals Nanodegree
# Log Analysis Report
#

import psycopg2

dbname = "dbname=news"

# Function to get top 3 articles
def get_articles():
    db = psycopg2.connect(dbname)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM top_articles")
    articles = cursor.fetchall()
    db.close()
    text = "What is the most three popular articles of the time?\n"
    for row in articles:
        text += "{0} -- {1} views\n".format(row[0], row[1])
    text += "\n\n"
    return text


# Function to get top authors
def get_authors():
    db = psycopg2.connect(dbname)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM top_authors")
    authors = cursor.fetchall()
    db.close()
    text = "Who is the most popular authors of the time?\n"
    for row in authors:
        text += "{0} -- {1} visualizações\n".format(row[0], row[1])
    text += "\n\n"
    return text


# Function to get days with more than 1% error processing
def get_errors():
    db = psycopg2.connect(dbname)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM morethan_one")
    errors = cursor.fetchall()
    db.close()
    text = "On what days more than 1% of requests resulted in errors?\n"
    for row in errors:
        text += "{0} -- {1} %\n".format(row[0], round(float(row[1]), 2))
    text += "\n\n"
    return text

# Function to write the Log Analysis Report
def main():
    print("Writing report, please wait...\n")
    report = open("report.txt", "w")
    report.write("Udacity Project - Log Analysis Report" + "\n\n")
    report.write(get_articles())
    report.write(get_authors())
    report.write(get_errors())
    report.close()
    print("Report file complete!\nNow access file 'report.txt'")


if __name__ == "__main__":
    main()
