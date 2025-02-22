from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sales_by_category')
def sales_by_category():
    return render_template('sales_by_category.html')

@app.route('/sales_by_region')
def sales_by_region():
    return render_template('sales_by_region.html')

if __name__ == '__main__':
    app.run(debug=True)