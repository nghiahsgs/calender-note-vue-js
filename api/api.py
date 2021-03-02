from flask import Flask, request, render_template
from flask_cors import CORS
from utils import *

app = Flask(__name__)
CORS(app)



@app.route('/<int:month>/<int:year>', methods=['GET'])
def index(month,year):
    L = gen_date_in_month(month,year)
    return {'res':L}


    

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=3000)