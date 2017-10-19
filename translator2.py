import urllib.request
import urllib.parse 
import json


#中文检测
def check_contain_chinese(check_str):
	rt = False
	if check_str>= u"\u4e00" and check_str<= u"\u9fa6":
		rt = True
	return rt
#日文检测
def check_contain_japanese(check_str):
	rt = False
	if check_str>= u"\u3040" and check_str<= u"\u30ff":
		rt = True
	return rt

print("""----------肉丸翻译机----------
	支持中译英和英译中""")
while True:
	mode = input("""请选择模式：
		1.中英
		2.中日
	模式:""")
	if mode  == '1':	
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
			if check_contain_chinese(txt):     
				data['from'] = 'zh'
				data['to'] = 'en'
			else:
				data['from'] = 'en'
				data['to'] = 'zh'
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
	if mode == '2':
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
			if check_contain_japanese(txt):
				data['from'] = 'jp'
				data['to'] = 'zh'
			else:
				data['from'] = 'zh'
				data['to'] = 'jp'
			data = urllib.parse.urlencode(data).encode('utf-8')
			response = urllib.request.urlopen(url,data)
			html = response.read().decode('utf-8')
			html = json.loads(html)
			result = html['trans_result']['data'][0]['dst']
			print("翻译结果：",result)