import csv
from flask import Flask
from flask import abort
from flask import render_template
app = Flask(__name__)

def get_csv():
    csv_path = './static/no2_marker.csv'
    csv_file = open(csv_path, 'r', encoding='utf-8')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

@app.route("/")
def index():
    template = 'index.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)
    
@app.route('/<row_id>/')
def detail(row_id):
    object_list = get_csv()
    template = 'detail.html'
    for row in object_list:
        if row['id'] == row_id:
            return render_template(template, object=row)
    abort(404)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
