
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
from datetime import date

DBNAME = "news"


def run_query(query):
    """Connects to the database, runs the query passed to it,
    and returns the results"""
    db = psycopg2.connect('dbname=' + DBNAME)
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows


def get_top_articles():
    """Returns top 3 most read articles"""

    # Build Query String
    query = """
        SELECT articles.title, COUNT(*) AS num
        FROM articles
        JOIN log
        ON log.path LIKE concat('/article/%', articles.slug)
        GROUP BY articles.title
        ORDER BY num DESC
        LIMIT 3;
    """

    # Run Query
    results = run_query(query)

    # Print Results
    print('\nTOP THREE ARTICLES BY PAGE VIEWS:')
    count = 1
    for i in results:
        number = '(' + str(count) + ') "'
        title = i[0]
        views = '" with ' + str(i[1]) + " views"
        print(number + title + views)
        count += 1


def get_top_authors():
    """Returns most popular article authors of all time?"""

    # Build Query String
    query = """
        SELECT authors.name, COUNT(*) AS num
        FROM authors
        JOIN articles
        ON authors.id = articles.author
        JOIN log
        ON log.path LIKE concat('/article/%', articles.slug)
        GROUP BY authors.name
        ORDER BY num DESC
        LIMIT 3;
    """

    # Run Query
    results = run_query(query)

    # Print Results
    print('\nTOP THREE AUTHOR OF ALL TIME:')
    count = 1
    for i in results:
        number = '(' + str(count) + ') "'
        title = i[0]
        views = '" with ' + str(i[1]) + " views"
        print(number + title + views)
        count += 1


def get_error():
    """On which days did more than 1% of requests lead to errors?"""

    # Build Query String
    query = """
        SELECT to_char(date, 'FMMonth FMDD, YYYY'),
        (err/total) * 100 AS ratio
        FROM (SELECT time::date AS date,
        COUNT(*) AS total,
        SUM((status != '200 OK')::int)::float AS err
        FROM log GROUP BY date) AS errors
        WHERE err/total > 0.01;
    """

    # Run Query
    results = run_query(query)

    # Print Results
    print('\nDAY WITH MORE THAN 1% OF REQUESTS:')
    i = 1
    for result in results:
        print "\n", result[0], " --", result[1], "%"
        i += 1


print('Calculating Result...\n')
get_top_articles()
get_top_authors()
get_error()
