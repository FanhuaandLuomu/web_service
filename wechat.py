#coding:utf-8
# pip install flask
# 实现问答 websevice
# http://ip:port/
# http://ip:port/chat/user=xxx&question=xxx
# status: -1:页面问题  0:参数丢失  1:成功
from flask import Flask,jsonify,abort
from flask import request
from flask import make_response
import time
# import cchardet

app=Flask(__name__)

# 首页
@app.route('/')
def index():
	return 'welcome to suda nlp wechat.'

# 将404信息改成json格式返回  404 Not Found
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'Error':'Page Not Found','status':-1}),404)

# 接收user和question,处理后返回结果
@app.route('/chat',methods=['GET'])
def get_reply():
	time_0=time.time()

	# user
	user=request.args.get('user','')

	# 用户名不为空
	if user==None or len(user)==0:
		return jsonify({'Error':'User None','status':0})

	# question
	question=request.args.get('question','')

	# if question==None:
	# 	return jsonify({'Error':'Question None','status':0})

	# TODO:
	# 输入：user  question
	# 输出：reply
	reply=process_question(user,question)

	return jsonify({'user':user,'question':question,'reply':reply,'ctime':time.ctime(),\
					'status':1})

# core 
def process_question(user,question):
	if u'qukuan' in question:
		print question
		reply=u'user:%s, hello. how much?' %(user)
	else:
		reply=u'user:%s, hello. i can not known.' %(user)

	return reply

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=4000,debug=True)