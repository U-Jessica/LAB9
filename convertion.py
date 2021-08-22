

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
    sub_set=jsonObj['sub_set'].split(',')
    n=int(jsonObj['n'])
    total=[]
    def ans (n,values,till):
        if (len(till)==n):
            total.append(set(till))
        elif (len(values)==0):
            return
        for i in range (len(values)):
            ans(n,values[i+1:],till+[values[i]])
    ans(n,sub_set,[])
    response=str(total)
    return response

def count(name):
    f = open(name, "r")
    T = 0
    for x in f:
        if x[0] != "T" and x[0] != "t":
            T=T+1
    f.close()
    return T
def vowels(name):
    check=['a','e','i','o','u']
    f = open(name, "r")
    T = 0
    for x in f:
        all_words=x.split(" ")
        for k in all_words:
            temp=k
            temp= temp.lower()
            temp=set(list(temp))
            if (len(temp & set(check))==0):
                T=T+1
    f.close()
    return T
@app.route("/submitJSON2", methods=["POST"])
def processJSON2(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    l=jsonObj['l']
    response = ""
    T=count(l)
    a=vowels(l)
    response=response+"Number of lines without T "+str(T) 
    response=response+"          ;Number of words without vowels "+str(a)  
    return response


@app.route("/submitJSON3", methods=["POST"])
def processJSON3(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    l1=jsonObj['l1']   
    l2=int(jsonObj['l2'])  
    l3=int(jsonObj['l3'])  
    response = ""
    f = open(l1, "r")
    T = 1
    for x in f:
        if (T>=l2 and T<l2+l3):
            response=response+x+"<br>"
        T=T+1
    f.close()	    
    return response

import os
@app.route("/submitJSON4", methods=["POST"])
def processJSON4(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    response = ""
    f = open("a.txt", "w")
    f.close()
    f = open("a.txt", "a")
    f.write("First line")  
    f.write("\nsecond line")
    f.write("\nthird line")  
    f.close()
    os.rename('a.txt', 'myfile.txt')
    f = open("myfile.txt")
    string_list = f.readlines()
    string_list[1]="\nsorry!The content of this line has been changed!"
    f.close()
    f=open("myfile.txt","w")
    f.writelines(string_list)
    f.close()	
    response="".join(string_list)	    
    return response

import pickle
def find_frequency(name):
    f = open(name, "r")
    dict1={}
    dict2={}
    for x in f:
        all_words=x.split(" ")
        for k in all_words:
            if (k in dict1):
                dict1[k]=dict1[k]+1
            else:
                dict1[k]=1
            temp=list(k)
            for i in temp:
                if (i in dict2):
                    dict2[i]=dict2[i]+1
                else:
                    dict2[i]=1
    f.close()
    return (dict1,dict2)
@app.route("/submitJSON5", methods=["POST"])
def processJSON5(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    response=""
    filename=jsonObj['filename']
    dict1,dict2=find_frequency(filename) 
    with open('pickle_word', 'wb') as f:
        pickle.dump(dict1, f)
    with open('pickle_char', 'wb') as f:
        pickle.dump(dict2, f)
    read = open ("pickle_word", "rb")
    words = pickle.load(read)
    read.close()
    new_text=""
    for i in words:
        new_text=new_text+(i+" ")*words[i]
    f=open("new_file.txt","w")
    f.write(new_text)
    f.close()
    dict3,dict4=find_frequency("new_file.txt")
    if (dict2==dict4):
        response=response+"Both have same character frequency"
    else:
        response=response+"Both don't have same character frequency"    
    return response
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
