import pickle
from types import resolve_bases 

with open('model/Titanic.pkl', 'rb') as fid: 
    titanic = pickle.load(fid)
pred = titanic.predict([[0,60,40,3]])
pred = pred.tolist()[0]
# pred= 0
resposta =  True if pred== 1 else False
print(pred)
print(resposta)
