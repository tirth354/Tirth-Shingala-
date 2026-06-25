import pickle

model = pickle.load(open("model.pkl", "rb"))

def predict_fraud(transaction):

    data = [[
        transaction["amount"],
        transaction["hour"],
        transaction["new_device"],
        transaction["location_mismatch"]
    ]]

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    return prediction, probability