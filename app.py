from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('search.html', msg = 'Inserisci qui le iniziali del prodotto')

@app.route('/search', methods = ['GET'])
def search():
    import pymssql
    import pandas as pd
    nomeProd = request.args['nomeProd']
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='zhao.filippo', password='xxx123##', database='zhao.filippo')  
    query = "select * from production.products where product_name like '" + nomeProd + "%'" 
    prodotti = pd.read_sql_query(query, conn)
    if len(prodotti) == 0:
        return render_template('search.html', msg='Prodotto non trovato')
    else:
        # https://stackoverflow.com/questions/52644035/how-to-show-a-pandas-dataframe-into-a-existing-flask-html-table'
        return render_template('table.html', nomiColonne = prodotti.columns.values, dati = list(prodotti.values.tolist()))
    

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)