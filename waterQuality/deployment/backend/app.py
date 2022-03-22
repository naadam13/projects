from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
with open("rf_best_random.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route("/")
def get_prediction():
    aluminium = eval(request.args.get('aluminium'))
    ammonia = eval(request.args.get('ammonia'))
    arsenic = eval(request.args.get('arsenic'))
    barium = eval(request.args.get('barium'))
    cadmium = eval(request.args.get('cadmium'))
    chloramine = eval(request.args.get('chloramine'))
    chromium = eval(request.args.get('chromium'))
    copper = eval(request.args.get('copper'))
    flouride = eval(request.args.get('flouride'))
    bacteria = eval(request.args.get('bacteria'))
    viruses = eval(request.args.get('viruses'))
    lead = eval(request.args.get('lead'))
    nitrates = eval(request.args.get('nitrates'))
    nitrites = eval(request.args.get('nitrites'))
    mercury = eval(request.args.get('mercury'))
    perchlorate = eval(request.args.get('perchlorate'))
    radium = eval(request.args.get('radium'))
    selenium = eval(request.args.get('selenium'))
    silver = eval(request.args.get('silver'))
    uranium = eval(request.args.get('uranium'))
    features = [aluminium, ammonia, arsenic, barium, cadmium, chloramine, 
                chromium, copper, flouride, bacteria, viruses, lead,
                nitrates, nitrites, mercury, perchlorate, radium,
                selenium, silver, uranium]
    pred = model.predict([features])
    labels = ['not safe', 'safe']
    response = {'status':'success', 'code':200, 'data':{'Prediction':labels[int(pred[0])]}}
    return jsonify(response)

@app.route("/post", methods=['POST'])
def post_prediction():
    konten = request.json
    data = [konten['aluminium'],
            konten['ammonia'],
            konten['arsenic'],
            konten['barium'],
            konten['cadmium'],
            konten['chloramine'],
            konten['chromium'],
            konten['copper'],
            konten['flouride'],
            konten['bacteria'],
            konten['viruses'],
            konten['lead'],
            konten['nitrates'],
            konten['nitrites'],
            konten['mercury'],
            konten['perchlorate'],
            konten['radium'],
            konten['selenium'],
            konten['silver'],
            konten['uranium']]
    pred = model.predict([data])
    labels = ['not safe', 'safe']
    response = {'status':'success', 'code':200, 'data':{'Prediction':labels[int(pred[0])]}}
    return jsonify(response)