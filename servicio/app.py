from flask import Flask
import json
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from pandas.io.json import json_normalize
import sklearn
import pickle
from flask import request
from flask import jsonify

#global model,opera_dic, mes_dic, tipovuelo_dic

def getCatalg():
   global model,opera_dic, mes_dic, tipovuelo_dic
   filename='model/modeloFinal2.pkl'
   # load the model from disk
   dat = pickle.load(open(filename, 'rb'))
   opera_dic=dat['opera']
   tipovuelo_dic=dat['tipovuelo']
   mes_dic=dat['mes']
   model=dat['model']


def fitTransformData(X):
    # Standardize the characteristics before training the model
    sc = StandardScaler()
    X_transfrom = sc.fit_transform(X)
    return X_transfrom

def getValueKey(object, value):
    for id, item in object.items():
        if str(item)==str(value):
           return id

def consultDict(df):
   #print(getValueKey(opera_dic,df.loc[0,'OPERA']))
   for index, row in df.iterrows():
        df.loc[index,'OPERA'] = getValueKey(opera_dic,row['OPERA'])
        df.loc[index,'MES'] = getValueKey(mes_dic,str(row['MES']))
        df.loc[index,'TIPOVUELO'] = getValueKey(tipovuelo_dic,row['TIPOVUELO'])
   return df

def predict(df):
    return model.predict(df)
app = Flask(__name__)

@app.route('/predict/', methods=['GET'])
def welcome():
    opera = request.args.get('opera')
    mes = request.args.get('mes')
    tipovuelo = request.args.get('tipovuelo')
    raw_data={'OPERA':opera,
             'MES':mes,
            'TIPOVUELO':tipovuelo}
    json_object = json.dumps(raw_data, indent = 4) 
    data = [raw_data]
    df = pd.DataFrame.from_dict(data)
    newDF=consultDict(df)
    #print(newDF)
    #print(type(newDF))
    transform= fitTransformData(newDF)
    result=predict(transform)
    return  jsonify({'atraso':str(result[0])})

if __name__ == '__main__':
    getCatalg()
    app.run(host='0.0.0.0', port=8000)
