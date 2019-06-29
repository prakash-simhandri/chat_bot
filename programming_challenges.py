from flask import Flask,jsonify,request,abort,json
import os,random
import pprint
program = Flask(__name__)

with open("challenges2.json","r")as All_questions:
	Questions_list=json.load(All_questions)
	# pprint.pprint(Questions_list)
	print("Your aap is run :)")

@program.route('/daily_program',methods=["GET"])
def create():
	return jsonify(Questions_list)

@program.route("/daily_program/<int:diet_id>",methods=["GET"])
def data_id(diet_id):
	task=[task for task in Questions_list if task["id"]==diet_id]
	if len(task)==0:
		abort(404)
	return jsonify(task)



@program.route("/daily_program/random",methods=["GET"])
def random_coues():
	calet=random.choice(Questions_list)
	return jsonify(calet["challenge"])




@program.route('/daily_program/<level>',methods=['GET'])
def get_by_level(level):
    by_level = [data for data in Questions_list if data["level"]==level]
    string = random.choice(by_level)
    level_id=jsonify(string["id"]) 
    return jsonify({"challenge":string["challenge"]})





# @program.route('/daily_program/upload', methods=['POST'])
# def post_by_challenge():
# 	with open("challenges2.json","r")as All_questions:
# 		Questions_post=json.load(All_questions)
# 		ID_get = len(Questions_list)+1
# 		# print(ID_get)
# 		Level_get = request.json.get('level')
# 		Challenge_get = request.json.get('challenge')
# 		HINT_get = request.json.get('hint')

# 		new_challenge={
# 			"id": ID_get,
# 			"level": Level_get,
# 			"challenge": Challenge_get,
# 			"hint": HINT_get
# 		}
# 		Questions_post.append(new_challenge)
# 		file_object = open("challenges2.json","w")
# 		json.dump(Questions_post, file_object)

# 		return jsonify(new_challenge)


if (__name__)==("__main__"):
	program.run(debug=True,port=50000)