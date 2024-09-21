from flask import Flask, request, jsonify

app = Flask(__name__)

store = []

@app.route("/api/store", methods = ['POST'])
def store_items():
      data = request.get_json()
      if not data:
            return jsonify({ 'error' : 'no data received'}), 400
      
      store.append(data)
      return jsonify({ 'message' : "data received" }), 200

@app.route("/api/store", methods = ['GET'])
def get_store():
      return jsonify(store), 200


app.run(port=7777, host="0.0.0.0")
      