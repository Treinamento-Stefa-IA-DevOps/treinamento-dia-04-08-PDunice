import pickle
from fastapi import FastAPI


app = FastAPI()
@app.post('/model')
def titanic(Sex:int, Age:float,Lifeboat:int,Pclass:int  ):
    with open('model/Titanic.pkl', 'rb') as fid: 
        titanic = pickle.load(fid)
    pred = titanic.predict([[Sex,Age,Lifeboat,Pclass]])
    pred = pred.tolist()[0]
    resposta =  True if pred== 1 else False
    return {
        'survived': resposta,
        'status': 200,
        'message': 'Sucesso requisicao',
    }

@app.get('/model')
def get():
    return {'hello':'test'}

@app.get('/')
def get():
    return {'API em /doc'}
