from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
import redis
import json 
import os

app = FastAPI()

# configuration & connexion au conteneur redis
REDIS_HOST = os.getenv("REDIS_HOST", "redis") 
r = redis.Redis(host=REDIS_HOST, port=6379, db=0)

# chargement du modele, des colonnes et du preprocesseur : 
model = joblib.load('src/models/model_ml.joblib')
preprocessor = joblib.load('src/models/preprocessor.joblib')
features_list = joblib.load('src/models/features_list.joblib')

# défini le Json attendu en entree
class TransmissionRequest(BaseModel):
    step: int
    type: str
    amount: float
    nameOrig: str
    oldbalanceOrg: float
    newbalanceOrig: float
    nameDest: str
    oldbalanceDest: float
    newbalanceDest: float
    isFlaggedFraud: int
    
    
    
    

# réception et traitement des donnees
@app.post("/predict")
async def recevoir_transaction(transaction: TransmissionRequest):
    df = pd.DataFrame([transaction.model_dump()])             
    df['hour'] = df['step'] % 24
    df['nameOrig'] = df['nameOrig'].str[0]
    df['nameDest'] = df['nameDest'].str[0]
    df = df[features_list]
    X_transformed = preprocessor.transform(df)
    prediction = model.predict(X_transformed)
        
    verdict = "FRAUDE" if prediction[0] == 1 else "SAIN"
    
    # modèle de stockage dans redis au format dictionnaire
    res_to_store = {
        "step": int(transaction.step),
        "type": str(transaction.type),
        "amount": float(transaction.amount),
        "nameOrig": str(transaction.nameOrig),
        "nameDest": str(transaction.nameDest), 
        "verdict": "ALERTE FRAUDE" if prediction[0] == 1 else "SAIN"
    }
    # convertir en texte pour Redis
    json_data = json.dumps(res_to_store)

    # double liste dans Redis (flux_global et liste_fraudes)
    r.lpush("flux_global", json_data)   

    if prediction[0] == 1:
        r.lpush("liste_fraudes", json_data)
        # r.expire("liste_fraudes", 172800) => Facultatif on garde 2j la liste
        print(f"ALERTE : Fraude détectée ! Montant: {transaction.amount}€")
    else:
        print(f"Transaction saine : {transaction.amount}€")
    return {"prediction": verdict, "status": "success"}





@app.get("/report")
async def report():
    total_traitees = r.llen("flux_global")
    fraudes_brutes = r.lrange("liste_fraudes", 0, -1) 
    
    # dictionnaire des fraudes détectées
    fraudes_decodees = [json.loads(f) for f in fraudes_brutes]
    
    # réponse pour Streamlit
    return {
        "infos":  {"nb_transactions" : total_traitees},
        "details": fraudes_decodees,
        "nb_fraudes_detectees": len(fraudes_decodees)
    }

# Pour lancer le serveur : uv run uvicorn src.API.streamrecepteur:app --reload
# Pour acceder au rapport : http://127.0.0.1:8000/report