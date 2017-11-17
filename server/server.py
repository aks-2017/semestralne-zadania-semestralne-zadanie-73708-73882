#!flask/bin/python

from flask import Flask, jsonify, abort, request
from lib.create import create


app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/')
def root():

    return app.send_static_file('index.html')


@app.route('/create', methods=['POST'])
def create_topo():
    data = request.get_json()
    st = data['station']
    ap = data['ap']

    create(int(st), int(ap))
    sprava= "Uspesne vytvorena topologia s "+st+" stanicami a "+ap+" apckami!"

    return jsonify({'sprava': sprava})



if __name__ == '__main__':

    app.run(debug=True)