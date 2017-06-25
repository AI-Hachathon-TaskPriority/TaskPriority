from bottle import run, get, post, Bottle, request, response
import inference
mydata = [
    	{"Importance":"3.Low","Assignor":"Me","Assignee":"Boss","Category":"Job","Title":"Request to check the presentation for Project A","Time":"15","Deadline":"06/26 Mon. 17:00"},
    	{"Importance":"2.Mid","Assignor":"HR","Assignee":"Me","Category":"Job","Title":"Check the resume of the engineer candidate A and answer","Time":"20","Deadline":"06/26 Mon. 20:00"},
    	{"Importance":"3.Low","Assignor":"Takahashi-san","Assignee":"Subordinate A","Category":"Job","Title":"Instruct to change the date of the meeting about Client C","Time":"5","Deadline":"06/26 Mon. 20:00"},
    	{"Importance":"1.High","Assignor":"Client A","Assignee":"Me","Category":"Job","Title":"Make the report about spec. out about product B","Time":"180","Deadline":"06/27 Tue. 09:00"},
    	{"Importance":"1.High","Assignor":"Client A","Assignee":"Subordinate A","Category":"Job","Title":"Instruct to print the deck for the appointment with Client A","Time":"5","Deadline":"06/27 Tue. 15:00"},
    	{"Importance":"2.Mid","Assignor":"Client B","Assignee":"Me","Category":"Job","Title":"Confirm the drawing of product AA","Time":"120","Deadline":"06/27 Tue. 18:00"},
    	{"Importance":"1.High","Assignor":"All subordinates","Assignee":"Me","Category":"Job","Title":"Feedback about the meeting with Client C","Time":"30","Deadline":"06/27 Tue. 20:00"},
    	{"Importance":"2.Mid","Assignor":"Me","Assignee":"Takashi-san","Category":"Job","Title":"Fix the problem of the VPN connection","Time":"15","Deadline":"06/27 Tue. 20:00"},
    	{"Importance":"2.Mid","Assignor":"All subordinates","Assignee":"Yoko-san","Category":"Job","Title":"Instruct to arrange the term-end drinking of the division","Time":"10","Deadline":"06/27 Tue. 20:00"},
    	{"Importance":"2.Mid","Assignor":"Client B","Assignee":"Me","Category":"Job","Title":"Set the meeting about Client B with Subordinate A","Time":"5","Deadline":"06/27 Tue. 20:00"},
    	{"Importance":"2.Mid","Assignor":"Client B","Assignee":"Me","Category":"Job","Title":"Confirm the drawing of product YY","Time":"120","Deadline":"06/28 Wed. 12:00"},
    	{"Importance":"2.Mid","Assignor":"Me","Assignee":"Subordinate B","Category":"Job","Title":"Make the agenda for the next meeting with client B","Time":"60","Deadline":"06/28 Wed. 12:00"},
    	{"Importance":"2.Mid","Assignor":"Me","Assignee":"Me","Category":"Job","Title":"Prepare a GPU instance for the image recognition","Time":"60","Deadline":"06/28 Wed. 12:00"},
    	{"Importance":"2.Mid","Assignor":"Boss","Assignee":"Me","Category":"Job","Title":"Refer the specification of component C","Time":"30","Deadline":"06/28 Wed. 12:00"},
    	{"Importance":"1.High","Assignor":"Boss","Assignee":"Me","Category":"Job","Title":"Create the deck for the monthly meeting","Time":"30","Deadline":"06/28 Wed. 15:00"},
    	{"Importance":"3.Low","Assignor":"Subordinate C","Assignee":"Me","Category":"Job","Title":"Confirm the drawing of product DD","Time":"90","Deadline":"06/28 Wed. 18:00"},
    	{"Importance":"2.Mid","Assignor":"Me","Assignee":"Subordinate B","Category":"Job","Title":"Have a design review about Product BB","Time":"90","Deadline":"06/29 Fri. 12:00"}
    	]
    	
@get('/tasks')
def getAll():
    response.headers['Access-Control-Allow-Origin'] = '*'
    return {'tasks' : mydata}

@post('/task/add')
def addTask():
    response.headers['Access-Control-Allow-Origin'] = '*'
    newTask = {}

    newTask['Assignor'] = request.forms.get('Assignor')
    newTask['Assignee'] = request.forms.get('Assignee')
    newTask['Category'] = request.forms.get('Category')
    newTask['Title'] = request.forms.get('Title')
    newTask['Time'] = request.forms.get('Time')
    newTask['Deadline'] = request.forms.get('Deadline')

    newTask['Importance'] = inference.inference(newTask)
        
    print newTask
    mydata.append(newTask)
    return {'tasks' : mydata}

run(host='localhost', port=8888, reloader=True, debug=True)