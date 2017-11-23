#!flask/bin/python

from flask import Flask, jsonify, abort, request, json
from lib.functions import Functions


app = Flask(__name__)


mini=None

tasks = [
    {
        'name': 'ap1',
        'loc': '75 74.1',
        'category': 'ap'
    },
    {
        'name': 'st1',
        'loc': '125 125',
        'category': 'st'
    },
    {
        'name': 'st2',
        'loc': '0 -5',
        'category': 'st'
    },
]

@app.route('/shutdown', methods=['GET'])
def shutdown():
    if(mini!=None): mini.stop()
    shutdown_server()
    return 'Server shutting down...'

@app.route('/reset', methods=['GET'])
def reset():
    if(mini!=None): mini.stop()


    return 'Topology RESET'


@app.route('/graph/positions', methods=['GET'])
def get_positions():
    pole = mini.ret_info()
    json_string = json.dumps([z.__dict__ for z in pole])
    return json_string



@app.route('/')
def root():

    return app.send_static_file('index.html')


@app.route('/create', methods=['POST'])
def create_topo():
    data = request.get_json()
    st = data['station']
    ap = data['ap']
    global mini
    mini = Functions()
    mini.create(int(st), int(ap))
    sprava= "Uspesne vytvorena topologia s "+st+" stanicami a "+ap+" apckami!"

    return jsonify({'sprava': sprava})


'''SERVER START a SHUTDOWN'''


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


if __name__ == '__main__':

    app.run(debug=True)
