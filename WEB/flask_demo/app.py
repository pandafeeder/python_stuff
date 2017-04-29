from flask import Flask, request, jsonify, make_response, abort
import sqlite3
import json

app = Flask(__name__)

@app.route('/api/chars', methods=['GET', 'POST'])
def collection():
    if request.method == 'GET':
        data = get_all()
        if not isinstance(data, Exception):
            result = [ {'id': i[0], 'pron': i[1], 'hiragana': i[2], 'katagana': i[3]} for i in data ]
            res = make_response(json.dumps(result, ensure_ascii=False))
            res.headers['Content-Type'] = 'application/json'
            return res
        else:
            abort(500)

    if request.method == 'POST':
        data = request.form
        result = add_new(data['pron'], data['hira'], data['kata'])
        return jsonify(result)


@app.route('/api/char/<pron>', methods=['GET', 'PUT', 'DELETE'])
def resource(pron):
    if request.method == 'GET':
        data = get_single(pron)
        if not isinstance(data, Exception):
            result = dict(zip(['id', 'pron', 'hiragana', 'katagana'], data[0]))
            res = make_response(json.dumps(result, ensure_ascii=False))
            res.headers['Content-Type'] = 'application/json'
            return res
        else:
            abort(500)

    if request.method == 'PUT':
        post_data = dict(request.form)
        result = edit_single(pron, **post_data)
        if not isinstance(result, Exception):
            return jsonify(result)
        else:
            abort(500)

    if request.method == 'DELETE':
        result = del_single(pron)
        if not isinstance(result, Exception):
            return jsonify(result)
        else:
            abort(500)


def get_all():
    with sqlite3.connect('fifty_sound.db') as con:
        c = con.cursor()
        try: 
            c.execute("""
                SELECT * FROM FIFTY_SOUND;
                """)
            return c.fetchall()
        except Exception as ex:
            print(ex)
            return ex 

def add_new(pron, hira, kata):
    with sqlite3.connect('fifty_sound.db') as con:
        c = con.cursor()
        try: 
            c.execute("""
                INSERT INTO FIFTY_SOUND (pron, hiragana, katagana) VALUES (?, ?, ?);
                """, (pron, hira, kata,))
            return {'status':1, 'message': 'added'}
        except Exception as ex:
            print(ex)
            return {'status':0, 'message': 'error'}
        

def get_single(pron):
    with sqlite3.connect('fifty_sound.db') as con:
        c = con.cursor()
        try:
            c.execute("""
                SELECT * FROM FIFTY_SOUND WHERE pron = ?;
                """, (pron,))
            return c.fetchall()
        except Exception as ex:
            print(ex)
            return ex

def edit_single(pron, **kwargs):
    with sqlite3.connect('fifty_sound.db') as con:
        c = con.cursor()
        try:
            SQL = """UPDATE FIFTY_SOUND SET """
            values = []
            for k, v in kwargs.items():
                SQL += "%s = ?," % k
                values.append(v[0])
            SQL = SQL.rstrip(',')
            SQL += " WHERE pron = ?;"
            values.append(pron)
            t = tuple(values)
            c.execute(SQL,t)
            return {'status':0, 'message': 'updated'}
        except Exception as ex:
            print(ex)
            return ex


def del_single(pron):
    with sqlite3.connect('fifty_sound.db') as con:
        c = con.cursor()
        try:
            c.execute("""
                DELETE FROM FIFTY_SOUND WHERE pron = ?;
                """, (pron,))
            return {'status':0, 'message': 'deleted'}
        except Exception as ex:
            print(ex)
            return ex


if __name__ == '__main__':
    app.debug = True
    app.run()
