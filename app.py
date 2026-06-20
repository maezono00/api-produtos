#IMPORTAÇÕES DE FRAMEWORKS
from flask import Flask, jsonify, request
from flask_cors import CORS

#CRIAR APP
app = Flask(__name__)

#HABILIAR CORS
CORS(app)

#CRIANDO BANCO DE DADOS LOCAL
produtos = [
    {"id":1,
     "nome":"Notebook Gamer",
     "preco":4000
     },
    {"id":2,
     "nome":"Cadeira Gamer",
     "preco":300
     },
    {"id":3,
     "nome":"Monitor",
     "preco":500
     }
]

#MÉTODOS HTTP
#CRIAR UMA ROTA E MÉTODO GET(VISUALIZAR OS DADOS)
@app.route("/", methods = ['GET'])

def exibirProdutos():
    return jsonify(produtos)

#CRIAR UMA ROTA E O MÉTODO POST(CRIAR)
@app.route("/criar", methods = ['POST'])
def criarProdutos():
    produtoNovo = request.get_json()
    produtos.append(produtoNovo)
    
    return jsonify(produtoNovo), 201

#CRIAR UMA ROTA E O MÉTODO PUT(ATUALIZAR)
@app.route("/atualizar/<int:id>", methods = ['PUT'])
def atualizarProdutos(id):
    dados = request.get_json()
    for produto in produtos:
        if produto['id'] == id:
            produto['preco'] = dados['preco']
            
            return jsonify(dados)
    return jsonify({"mensagem":"ID não encontrado!"}),404

#CRIAR UMA ROTDA E O MÉTODO DELETE(APAGAR)
@app.route("/apagar/<int:id>", methods = ['DELETE'])
def apagarProduto(id):
    for produto in produtos:
        if produto['id'] == id:
            produtos.remove(produto)
            return jsonify({"mensagem":"Produto removido!"})
    return jsonify({"mensagem":"ID não encontrado!"}), 404

#RODAR O PROGRAMA
if __name__ == '__main__' :
    app.run(port = 8000, host = "0.0.0.0")