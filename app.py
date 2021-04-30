import os
from flask import Flask


app = Flask(__name__)

@app.route ('/Teste', methods=['POST'])
def teste():
    
   
    return "<h1>Hello World2</hi>"

@app.route("/")
def index():
    return "<h1>Silas Eva e Adao</hi>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
