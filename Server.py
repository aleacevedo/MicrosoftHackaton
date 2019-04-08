from flask import Flask, request
from Menus import Menu
from Tables import Table

app = Flask(__name__)
Tabless = {}
menu = Menu()
for i in range(1,10):
    Tabless[i] = Table()

@app.route('/')
def index():
    return 'Bienvenidos al Restaurant'

@app.route('/getMenu')
def get():
    return menu.getMenu();

@app.route('/checkTables', methods=['POST', 'GET'])
def checkTables():
    if request.method == 'POST':
        date = str(request.form['date'])
        time = str(request.form['time'])
        time = time.split('-')
        for i in range (1,10):
            if(Tabless[i].checkDateAvaiable(date,time)):
                return str("True")
    return str("False")

@app.route('/reserveTable', methods=['POST', 'GET'])
def reserveTable():
    if request.method == 'POST':
        date = str(request.form['date'])
        time = str(request.form['time'])
        for i in range (1,10):
            if(Tabless[i].checkDateAvaiable(date,time)):
                Tabless[i].reserveTable(date,time)
                return str("True")
    return False


if __name__ == '__main__':
    app.run(debug=True)