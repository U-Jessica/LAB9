

import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")

@app.route('/sum1')
def sum1():    
    return render_template('sum1.html')

@app.route('/sum2')
def sum2():    
    return render_template('sum2.html')

@app.route('/sum3')
def sum3():    
    return render_template('sum3.html')

@app.route('/sum4')
def sum4():    
    return render_template('sum4.html')

def ans1(a,b):
    list2=[]
    ans=""
    for i in a:
        if i not in list2:
            list2.append(i)
    list3=[0]*len(list2)
    for i in range (len(list2)):
        for j in a:
            if j==list2[i]:
                list3[i]=list3[i]+1
    for k in range (len(list3)):
        if list3[k]>2:
            ans=ans+"<b>Item "+str(list2[k])+" with frequency "+str(list3[k])+"</b><br>"
    return ans

@app.route("/submitJSON1", methods=["POST"])
def processJSON1(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""

    l=jsonObj['l'].split(',')
    k=int(jsonObj['k'])
    response=ans1(l,k)	    
    return response


def ans2(a):
    list2=[]
    for i in a:
        if i not in list2:
            list2.append(i)
    list3=[0]*len(list2)
    for i in range (len(list2)):
        for j in a:
            if j==list2[i]:
                list3[i]=list3[i]+1
    for k in range (len(list3)):
        if list3[k]>1:
            temp=list2[k]
            for i in range(list3[k]-1):
                a.remove(temp)
@app.route("/submitJSON2", methods=["POST"])
def processJSON2(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    l=jsonObj['l'].split(',')
    ans2(l)
    response=str(l)    	    
    return response

def ans3(a,row,col):
    ans=""
    flag=True
    if (row!=col):
        flag=False
    for i in range (col):
        for j in range (row):
            if (col==row):
                if (a[j][i]!=a[i][j] and flag):
                    flag=False
            ans=ans+a[j][i]+" "
        ans=ans+"<br>"
    if (flag):
        ans=ans+"Symmetfr5rdric"
        return ans
    else:
        ans=ans+"Not Symmetric"
        return ans
@app.route("/submitJSON3", methods=["POST"])
def processJSON3(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    l1=jsonObj['l1'].split(',')
    l2=int(jsonObj['l2'])
    l3=int(jsonObj['l3'])
    array=[]
    k=0
    for i in range (l2):
        temp=[]
        for j in range (l3):
            temp.append(l1[k])
            k=k+1
        array.append(temp)
    response=ans3(array,l2,l3)
    	    
    return response

def ans4(a,ans):
    if (a==1):
        return "1"+ans
    if (a%2==0):
        return ans4(a//2,"0"+ans)
    else:
        return ans4(a//2,"1"+ans)
@app.route("/submitJSON4", methods=["POST"])
def processJSON4(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    i=int(jsonObj['i'])
    response=ans4(i,"")
    return response
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
