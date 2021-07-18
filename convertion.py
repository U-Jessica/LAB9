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

@app.route('/sum5')
def sum5():    
    return render_template('sum5.html')
   
@app.route("/submitJSON1", methods=["POST"])
def processJSON1(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    a=int(jsonObj['a'])
    s=0
    for i in range (1,a+1):
        if(i%2==1):
            if(i%5==0):
                s=s
            else:
                s=s+i
   
    response+="<b> The sum of all odds excludin the numbers divisible by 5 is : <b>"+str(s)+"</b><br>"
     	    
    return response

@app.route("/submitJSON2", methods=["POST"])
def processJSON2(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    a=int(jsonObj['a'])
    f=[]
    for i in range (a):
        if(i==0):
            f.append(0)
        elif (i==1):
            f.append(1)
        else:
            f.append(f[i-1]+f[i-2])
    k=str(f)[1:-1]
    response+="<b><b>"+k+"</b><br>"
     	    
    return response

@app.route("/submitJSON3", methods=["POST"])
def processJSON3(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    ans=""
    s=0
    for i in range(5):
        for j in range(i+1):
            s=s+1
            ans=ans+str(s)+" "
        ans=ans+"<br>"
    response+="<b><b>"+ans+"</b><br>" 	    
    return response 

@app.route("/submitJSON4", methods=["POST"])
#two lists and for loops

def processJSON4(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    a=jsonObj['a']
    k=a.lower()
    list1=[]
    for a in k:
        if a not in list1:
            list1.append(a)
    list2=[0]*len(list1)
    for i in range (len(list1)):
        for j in range(len(k)):
            if (list1[i]==k[j]):
                list2[i]=list2[i]+1
    index=list2.index(max(list2))
    response+="<b><b>"+list1[index]+"</b><br>" 	    
    return response 

@app.route("/submitJSON5", methods=["POST"])
def processJSON5(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    a=int(jsonObj['a'])
    s=1
    for i in range(1,a+2):
        s=s*i
    for i in range(a+1,1,-1):
        s=s//i
        response+="<b><b>"+str(i-1)+"! ="+str(s)+"</b><br>" 	    
    return response  
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
