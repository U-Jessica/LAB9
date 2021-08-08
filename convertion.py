

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

    l=jsonObj['l'].split(';')
    for i in range (len(l)):
        if (l[i]==''):
            l[i]=tuple()
            continue
        l[i]=tuple(map(int,l[i].split(",")))
    while(() in l):
        l.remove(())
    response=str(l)
    return response


def test(lst):
    result=map(sum,lst)
    return list(result)


@app.route("/submitJSON2", methods=["POST"])
def processJSON2(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    l=jsonObj['l'].split(';')
    for i in range (len(l)):
        if(l[i]==''):
            l[i]=tuple()
            continue
        l[i]=tuple(map(int,l[i].split(",")))
    response=str(test(l))    	    
    return response


@app.route("/submitJSON3", methods=["POST"])
def processJSON3(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    l1=jsonObj['l1'].split(';')
    l2=jsonObj['l2'].split(',')
    test_dict={}
    for i in l1:
        a=i.split(",")
        test_dict[a[0]]=a[1]
    keys=list(test_dict.keys())
    for i in keys:
        for j in l2:
            if test_dict[i].find(j) != -1:
                del test_dict[i]
                break
    response=str(test_dict)
    	    
    return response


@app.route("/submitJSON4", methods=["POST"])
def processJSON4(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    l=list(map(int,jsonObj['l'].split(',')))
    counts=dict()
    for i in range(1,(max(l)+1)):
        counts[i]=0
        for key in l:
            if key%i==0:
                counts[i]=counts[i]+1
    response=str(counts)    	    
    return response
@app.route("/submitJSON5", methods=["POST"])
def processJSON5(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    f={'music':{'x':5,'y':6,'z':3},'best':{'x':8,'y':3,'z':5}}
    dod={}
    ll=[]
    for v in f.values():
        for kk in v.keys():
            dod[kk]=[]
    for k,v in f.items():
        for kk,vv in v.items():
            dod[kk].append(tuple((k,vv)))

    response=str(dod)
    for k,v in dod.items():
        temp=[]
        temp.append(k)
        for vv in v:
            temp.append(vv)
        ll.append(tuple(temp))
    response=str(tuple(ll))     
    return response
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
