from flask import Flask,jsonify,request,abort,json
import os,random
import pprint
program = Flask(__name__)

with open("challenges2.json","r")as All_questions:
	Questions_list=json.load(All_questions)
	# pprint.pprint(Questions_list)
	print("Your aap is run :)")
	
# Getting all the challenges from here

@program.route('/daily_program',methods=["GET"])
def create():
	return jsonify(Questions_list)

# Getting challenges through Id

@program.route("/daily_program/<int:diet_id>",methods=["GET"])
def data_id(diet_id):
	task=[task for task in Questions_list if task["id"]==diet_id]
	if len(task)==0:
		abort(404)
	return jsonify(task)

# Getting challenges through Randomly

@program.route("/daily_program/random",methods=["GET"])
def random_coues():
	calet=random.choice(Questions_list)
	return jsonify(calet["challenge"])


# Getting the challenges according to the level

@program.route('/daily_program/<level>',methods=['GET'])
def get_by_level(level):
    by_level = [data for data in Questions_list if data["level"]==level]
    string = random.choice(by_level)
    level_id=jsonify(string["id"]) 
    return jsonify({"challenge":string["challenge"]})

# server run this localhost port.

if (__name__)==("__main__"):
	program.run(debug=True,port=50000)
