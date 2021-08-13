from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
  numero_1 = request.args.get('numero1', None)
  numero_2 = request.args.get('numero2', None)
  operacao = request.args.get('operacao', None)
  if not numero_1 or not numero_2 or not operacao:
    return jsonify({
      'mensagem': "Por favor envie dois numeros, e a operação que deseja realizar.",
      'ajuda': "?numero1=X&numero2=X&operacao=X",
      'operacoes': 'soma'
    })
  else:
    if operacao == 'soma':
      return jsonify({
        'resultado': int(numero_1) + int(numero_2)
      })
    else:
      return jsonify({
        'erro': 'operacao nao reconhecida',
      })
app.run(host='0.0.0.0', port=8080)