from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import numpy
from .models import Pred
from sklearn.preprocessing import StandardScaler
# Create your views here.
def predict(request):
    return render(request,'predict.html')

def submit_prediction(request):
    if request.POST.get('action')=='post':
        PassengerId = float(request.POST['PassengerId'])
        Pclass = float(request.POST['Pclass'])
        Age = float(request.POST['Age'])
        SibSp = float(request.POST['SibSp'])
        Parch = float(request.POST['Parch'])
        Fare = float(request.POST['Fare'])
        C = float(request.POST['C'])
        S = float(request.POST['S'])
        Q = float(request.POST['Q'])
        male = float(request.POST['male'])
        female = float(request.POST['female'])
        scaler = StandardScaler()
        model = pd.read_pickle(r"C:\Users\MSI\Desktop\proj\proj21\new_model.pickle")
        data = pd.read_csv('DB.csv')
        data.loc[len(data)+1] = [PassengerId,Pclass,Age,SibSp,Parch,Fare,C,S,Q,female,male] 
        a = scaler.fit_transform(data)
        result = model.predict(a)
        siuu = result[len(result)-1]
        classification = ''
        if siuu==0:
            classification = 'Dead'
        else:
            classification = 'Survived'
        Pred.objects.create(PassengerId=PassengerId,Pclass=Pclass,Age=Age,SibSp=SibSp,Parch=Parch,Fare=Fare,C=C,S=S,Q=Q,male=male,female=female,classification=classification)
        return JsonResponse({'result':classification,'PassengerId':PassengerId,'Pclass':Pclass,'Age':Age,'SibSp':SibSp,'Parch':Parch,'Fare':Fare,'C':C,'S':S,'Q':Q,'male':male,'female':female},safe=False)

def view_results(request): 
    return render(request,"result.html",{"dataset":Pred.objects.all()})  