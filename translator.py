import urllib.request
import urllib.parse 
import json


#中文检测
def check_contain_chinese(check_str):
	rt = False
	if check_str>= u"\u4e00" and check_str<= u"\u9fa6":
		rt = True
	return rt

print("""
******************************************************
 -----------------欢迎使用肉丸翻译机-----------------

 使用帮助：
	 支持中文⇦⇨外文翻译转换
	 
	 支持长文翻译

	 支持英、日、德、法、西、俄、韩六国语言

	 输入“!back”返回模式菜单
 	 *注意*“!”为英文字符

******************************************************
	""")
while True:
	try:
		mode = input("""请输入数字选择模式：

1.中英
2.中日
3.中德
4.中法
5.中西
6.中俄
7.中韩

模式:""")
		mode = int(mode)
		while True:	
			txt = input("请输入文本：")
			url = 'http://fanyi.baidu.com/v2transapi'
			data = {
				'from':'',
				'to':'',
				'query':txt,
				'transtype':'translang',
				'simple_means_flag':'3'
			}
			if txt == '!back':
				break
			elif mode == 1:
				if check_contain_chinese(txt):     
					data['from'] = 'zh'
					data['to'] = 'en'
				else:
					data['from'] = 'en'
					data['to'] = 'zh'
			elif mode == 2:
				if check_contain_chinese(txt):
					data['from'] = 'zh'
					data['to'] = 'jp'
				else:
					data['from'] = 'jp'
					data['to'] = 'zh'
			elif mode == 3:
				if check_contain_chinese(txt):
					data['from'] = 'zh'
					data['to'] = 'de'
				else:
					data['from'] = 'de'
					data['to'] = 'zh'
			elif mode == 4:
				if check_contain_chinese(txt):
					data['from'] = 'zh'
					data['to'] = 'fra'
				else:
					data['from'] = 'fra'
					data['to'] = 'zh'
			elif mode == 5:
				if check_contain_chinese(txt):
					data['from'] = 'zh'
					data['to'] = 'spa'
				else:
					data['from'] = 'spa'
					data['to'] = 'zh'
			elif mode == 6:
				if check_contain_chinese(txt):
					data['from'] = 'zh'
					data['to'] = 'ru'
				else:
					data['from'] = 'ru'
					data['to'] = 'zh'
			elif mode == 7:
				if check_contain_chinese(txt):
					data['from'] = 'zh'
					data['to'] = 'kor'
				else:
					data['from'] = 'jp'
					data['to'] = 'kor'
			data = urllib.parse.urlencode(data).encode('utf-8')
			#主要是由于该网站禁止爬虫导致的，可以在请求加上头信息，伪装成浏览器访问User-Agent
			#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
			#req = urllib.request.Request(url, headers=headers)
			#response = urllib.request.urlopen(req) 
			response = urllib.request.urlopen(url,data)
			html = response.read().decode('utf-8')
			html = json.loads(html)
			result = html['trans_result']['data'][0]['dst']
			print("翻译结果：",result)
	except:
		print("*输入有误，请重新输入！*")
		continue