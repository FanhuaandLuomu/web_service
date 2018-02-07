#coding:utf-8
# bottle simple http server
import jieba
import bottle
jieba.initialize()

# http://127.0.0.1:7777/token?text=我喜欢你
@bottle.route('/token',method='GET')
def token_home():
	text=bottle.request.GET.get('text')
	if not text:
		text=''
	return ' '.join(jieba.cut(text))

if __name__ == '__main__':
	bottle.run(host='0.0.0.0',port=7777)