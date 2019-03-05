#
# Udacity Back-End Fundamentals Nanodegree
# Database connection to access data news
#

import psycopg2

dbname = "dbname=news"


# Function to get top 3 articles
def get_articles():
    db = psycopg2.connect(dbname)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM top_articles")
    return cursor.fetchall()
    db.close()


# Function to get top authors
def get_authors():
    db = psycopg2.connect(dbname)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM top_authors")
    return cursor.fetchall()
    db.close()


# Function to get days with more than 1% error processing
def get_errors():
    db = psycopg2.connect(dbname)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM morethan_one")
    return cursor.fetchall()
    db.close()
