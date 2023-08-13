from flask import Flask,request
import pandas as pd
import numpy as np
import sys 
from sklearn import model_selection,preprocessing
from flask_cors import CORS

#x=preprocessing.scale(x)







app = Flask(__name__)
cors = CORS(app)
@app.route('/airCon', methods=['POST'])
def airCon():
    df=pd.read_csv(r'C:\Users\USER\Downloads\archive (1)\energy_efficiency_data.csv')
    x=np.array(df.drop(['Heating_Load','Cooling_Load'],axis=1))
    class Linear_Regression:
        def __init__(self,learning_rate=0.001,n_iter=1000):
            self.lr=learning_rate
            self.n_iter=n_iter
            self.w=None
            self.b=None
        def regressW(self,prediction,x,y):
            return np.dot(x,(prediction-y))
        def regressB(self,prediction,y):
            return np.sum(prediction-y)
        def fit(self,x,y):
            n_samples,n_features=x.shape
            self.w=np.zeros(n_features)
            self.b=0
            for _ in range(self.n_iter):
                for index,data in enumerate(x):
                    prediction=np.dot(self.w,data)+self.b
                    dw=self.regressW(prediction,data,y[index])
                    db=self.regressB(prediction,y[index])
                    self.w=self.w-self.lr*dw
                    self.b=self.b-self.lr*db
        def predict(self,x):
            #results=[]
            #for i in X:
             #   results.append(np.dot(i,self.w)+self.b)
            #if(len(x)==1):
             #   return results[0]
            return np.dot(x,self.w)+self.b
        def score(self,x,y):
            predictions=self.predict(x)
            results=[]
            for index,data in enumerate(predictions):
                results.append((data-y[index])**2)
            results=np.array(results)
            return 1-np.mean(results)/len(x)
    compactness=float(request.json['compactness'])
    surface_area=float(request.json['surface_area'])
    wall_area=float(request.json['wall_area'])
    roof_area=float(request.json['roof_area'])
    overall_height=float(request.json['overall_height'])
    orientation=float(request.json['orientation'])
    glazing_area=float(request.json['glazing_area'])
    glazing_area_distribution=float(request.json['glazing_area_distribution'])
    predictor=[compactness,surface_area,wall_area,roof_area,overall_height,orientation,glazing_area,glazing_area_distribution]
    newX=np.array(predictor).reshape(1,-1)
    newNewX=np.concatenate((x,newX))
    x=preprocessing.scale(newNewX)
    newX=x[-1]
    x=x[:-1]
    y1=np.array(df['Heating_Load'])
    y2=np.array(df['Cooling_Load'])
    heating_train_x,heating_test_x,heating_train_y,heating_test_y=model_selection.train_test_split(x, y1,test_size=0.2)
    cooling_train_x,cooling_test_x,cooling_train_y,cooling_test_y=model_selection.train_test_split(x,y2,test_size=0.2)
    Heating=Linear_Regression()
    Cooling=Linear_Regression()
    Heating.fit(heating_train_x,heating_train_y)
    Cooling.fit(cooling_train_x,cooling_train_y)
    accuracyHeat=Heating.score(heating_test_x,heating_test_y)
    accuracyCool=Cooling.score(cooling_test_x,cooling_test_y)
    predictionHeat=Heating.predict(newX)
    predictionCool=Cooling.predict(newX)
    
    return {"Heating":predictionHeat,"Cooling":predictionCool,"AccuracyHeat":accuracyHeat,"AccuracyCool":accuracyCool}
if __name__=="__main__":
    app.run(debug=True)