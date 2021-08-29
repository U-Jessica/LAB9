

import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

class Rectangle(object):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def Area(self):
        return self.length*self.breadth

class Time(object):
    def __init__(self,hours=0,minutes=0):
        self.minutes=minutes
        self.hours=hours
    def Addtime(self,add):
        self.hours+=add.hours
        self.minutes+=add.minutes
        self.hours+=self.minutes//60
        self.minutes=self.minutes%60
    def displayTime(self):
        return ("%d hours and %d minutes"%(self.hours,self.minutes))
    def displayMinutes(self):
        return str(self.hours*60+self.minutes)

class Students(object):
    count=0
    even_marks=0
    odd_marks=0
    even_count=0
    odd_count=0
    def __init__(self,name,roll_no,age):
        self.name=name
        self.roll_no=roll_no
        if (roll_no%2==0):
            Students.even_count+=1
        else:
            Students.odd_count+=1
        self.age=age
        self.marks=0
        Students.count+=1
    def display(self):
        return ("%s %d %d" %(self.name,self.roll_no,self.age))
    def setMarks(self,marks):
        self.marks=marks
        if (self.roll_no%2==0):
            Students.even_marks+=marks
        else:
            Students.odd_marks+=marks
    def printCount(self):
        return ("The total count of students is %d"%(Students.count))
    def printEavg(self):
        return ("The average of even roll no students is %d"%(Students.even_marks/Students.even_count))
    def printOavg(self):
        return ("The average of odd roll no students is %d"%(Students. odd_marks/Students.odd_count))

@app.route("/")
def home():
    return render_template("InputOutput.html")

@app.route('/sum2')
def sum2():    
    return render_template('sum2.html')

@app.route('/sum3')
def sum3():    
    return render_template('sum3.html')

@app.route('/sum4')
def sum4():    
    return render_template('sum4.html')

@app.route("/submitJSON2", methods=["POST"])
def processJSON2(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    l=int(jsonObj['l'])
    b=int(jsonObj['b'])
    response = "The area of the rectangle is "
    rectangle=Rectangle(l,b)
    response=response+str(rectangle.Area())+" units"
    return response


@app.route("/submitJSON3", methods=["POST"])
def processJSON3(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    if(jsonObj['l1']!=""):
        l1=list(map(int,jsonObj['l1'].split(",")))
    else:
         l1=[]
    if(jsonObj['l2']!=""):
        l2=list(map(int,jsonObj['l2'].split(",")))
    else:
         l2=[]  
    if(jsonObj['l3']!=""):
        l3=list(map(int,jsonObj['l3'].split(",")))
    else:
         l3=[]
    while(len(l1)<2):
        l1.append(0)  
    while(len(l2)<2):
        l2.append(0) 
    while(len(l3)<2):
        l3.append(0)
    obj1=Time(l1[0],l1[1])
    obj2=Time(l2[0],l2[1])
    obj3=Time(l3[0],l3[1])
    response = "Addition of hours and minutes 1 and hours and minutes 2 is "
    obj1.Addtime(obj2)
    response=response+obj1.displayTime()+"<br>"  
    response=response+"Time of 1 is "+obj1.displayTime()+"<br>" 
    response=response+"Time of 2 is "+obj2.displayTime()+"<br>" 
    response=response+"Time of 3 is "+obj3.displayTime()+"<br>"
    response=response+"Time of 1 in minutes is "+obj1.displayMinutes()+"<br>"
    response=response+"Time of 2 in minutes is "+obj2.displayMinutes()+"<br>"
    response=response+"Time of 3 in minutes is "+obj3.displayMinutes()+"<br>"   
    return response

@app.route("/submitJSON4", methods=["POST"])
def processJSON4(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    l1=list(jsonObj['l1'].split(","))
    l2=list(jsonObj['l2'].split(","))
    l3=list(jsonObj['l3'].split(","))
    l4=list(jsonObj['l4'].split(","))
    l5=list(jsonObj['l5'].split(","))
    l6=list(jsonObj['l6'].split(","))
    l1=Students(l1[0],int(l1[1]),int(l1[2]))
    l2=Students(l2[0],int(l2[1]),int(l2[2]))
    l3=Students(l3[0],int(l3[1]),int(l3[2]))
    l4=Students(l4[0],int(l4[1]),int(l4[2]))
    l5=Students(l5[0],int(l5[1]),int(l5[2]))
    l6=Students(l6[0],int(l6[1]),int(l6[2]))
    if(jsonObj['m1']!=""):
        l1.setMarks(int(jsonObj['m1']))
    if(jsonObj['m2']!=""):
        l2.setMarks(int(jsonObj['m2']))
    if(jsonObj['m3']!=""):
        l3.setMarks(int(jsonObj['m3']))
    if(jsonObj['m4']!=""):
        l4.setMarks(int(jsonObj['m4']))
    if(jsonObj['m5']!=""):
        l5.setMarks(int(jsonObj['m5']))
    if(jsonObj['m6']!=""):
        l6.setMarks(int(jsonObj['m6']))
    response=""
    response=response+l1.display()+"<br>"
    response=response+l2.display()+"<br>"
    response=response+l3.display()+"<br>"
    response=response+l4.display()+"<br>"
    response=response+l5.display()+"<br>"
    response=response+l6.display()+"<br>"
    response=response+l1.printCount()+"<br>"
    response=response+l1.printEavg()+"<br>"
    response=response+l1.printOavg()+"<br>"	    
    return response
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
