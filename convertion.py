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
   
@app.route("/submitJSON1", methods=["POST"])
def processJSON1(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    l=jsonObj['l'].split(',')
    k=int(jsonObj['k'])
    list1=[]
    list3=[]
##unique
    for i in l:
        if i not in list1:
            list1.append(i)
    list2=[0]*len(list1)
    for i in range (len(list1)):
        for j in range (len(l)):
            if list1[i]==l[j]:
                list2[i]=list2[i]+1
    for i in range (len(list2)):
        if (k<list2[i]):
             list3.append(list1[i])         
    response+="<b> "+str(list3)+"</b><br>"
        
    
    	    
    return response

@app.route("/submitJSON2", methods=["POST"])
def processJSON2(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    l1=jsonObj['l1'].split(',')
    l2=jsonObj['l2'].split(',')
    k=l2.reverse()
    m=min(len(l1),len(l2))
    p=max(len(l1),len(l2))
    for i in range (m):
        response+="<b> "+str(l1[i])+" " +str(l2[i])+"</b><br>"
    if (len(l1)==p):
        for i in range (-(p-m),0):
            response+="<b> "+str(l1[i])+"</b><br>"
    elif (len(l2)==p):
        for i in range (-(p-m),0):
            response+="<b> "+str(l2[i])+"</b><br>"
    	    
    return response

@app.route("/submitJSON3", methods=["POST"])
def processJSON3(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    l1=jsonObj['l1'].split(',')
    list1=[]
    for i in l1:
        if i not in list1:
            list1.append(i)
    response+="<b> "+str(list1)+"</b><br>"
    	    
    return response

@app.route("/submitJSON4", methods=["POST"])
#two lists and for loops

def processJSON4(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    l1=jsonObj['l1'].split(',')
    l2=jsonObj['l2'].split(',')
    ans=[]
    for i in range (len(l1)):
        l1[i]=l1[i].lower()
    for i in range (len(l2)):
        l2[i]=l2[i].lower()
    for i in l2:
        if i in l1 and i not in ans:
            ans.append(i)

    response+="<b> "+str(ans)+"</b><br>"
    	    
    return response
    


if __name__ == "__main__":
    app.run(debug=True)
    
    
