from django.shortcuts import render, render_to_response

import psycopg2 # PostgreSQL
# Create your views here.

def db_keyboard(request):
    db = psycopg2.connect(user='kai', dbname='kai_db', password='zxcvbnm', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT name FROM keyboard ORDER BY name')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('keyboards/db_list.html', {'names': names})
