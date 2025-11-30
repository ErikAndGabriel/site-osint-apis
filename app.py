from flask import Flask, request, render_template
import requests 
import json 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ip-consulta', methods=['POST'])
def Buscarip():
    ip = request.form.get('endereco-ip')
    url = f"http://ip-api.com/json/{ip}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()

        return f'''
        <h1>Resultados para {ip}</h1>
        <p><strong>status</strong> {dados["status"]}</p>
        <p><strong>country</strong> {dados["country"]}</p>
        <p><strong>countryCode</strong> {dados["countryCode"]}</p>
        <p><strong>region</strong> {dados["region"]}</p>
        <p><strong>zip</strong> {dados["zip"]}</p>
        <p><strong>lat</strong> {dados["lat"]}</p>
        <p><strong>lon</strong> {dados["lon"]}</p>
        <p><strong>timezone</strong> {dados["timezone"]}</p>
        <p><strong>isp</strong> {dados["isp"]}</p>
        <p><strong>org</strong> {dados["org"]}</p>
        <p><strong>regionName</strong> {dados["regionName"]}</p>
        <p><strong>as</strong> {dados["as"]}</p>
        <p><strong>query</strong> {dados["query"]}</p>
        '''
if __name__ == "__main__":
    app.run(debug=True)
