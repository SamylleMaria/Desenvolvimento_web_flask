from flask import Flask, render_template #render template busca a pasta com nome "templates" para importar os arquivos.

app = Flask(__name__) #nome do app

@app.route('/') #caminho do link do site (no caso é local)
#Para cada link que criar, é necessário definir uma função
def homepage():
    return render_template('homepage.html')


@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

if __name__ == '__main__':
    app.run(debug=True) #Todas as alterações feitas serão automaticamente implementadas no site
    