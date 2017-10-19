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
		:""")

	if mode  == '1':	
		while True:
			txt = input("请输入文本：")
			if txt == '!back':
				break
			if check_contain_chinese(txt):
				url = 'http://fanyi.baidu.com/v2transapi'       
				data = {
				'from':'zh',
				'to':'en',
				'query':txt,
				'transtype':'translang',
				'simple_means_flag':'3'
				}
			else:
				url = 'http://fanyi.baidu.com/v2transapi'       
				data = {
				'from':'en',
				'to':'zh',
				'query':txt,
				'transtype':'translang',
				'simple_means_flag':'3'
				}
			data = urllib.parse.urlencode(data).encode('utf-8')
			response = urllib.request.urlopen(url,data)
			html = response.read().decode('utf-8')
			html = json.loads(html)
			trans = html['trans_result']['data'][0]['dst']
			print("翻译结果：",trans)
	if mode == '2':
		while True:
			txt = input("请输入文本：")
			if txt == '!back':
				break
			if check_contain_japanese(txt):
				#url = 'https://dict.hjenglish.com/services/Translate.ashx'       
				#txt = urllib.parse.quote(txt)
				#data = {'from':'ja','to':'zh-CN','txt':txt,}
				url = 'http://fanyi.baidu.com/v2transapi'       
				data = {
				'from':'jp',
				'to':'zh',
				'query':txt,
				'transtype':'translang',
				'simple_means_flag':'3'
				}
			else:
				#url = 'https://dict.hjenglish.com/services/Translate.ashx'       
				#txt = urllib.parse.quote(txt)
				#data = {'from':'zh-CN','to':'ja','txt':txt,}
				url = 'http://fanyi.baidu.com/v2transapi'       
				data = {
				'from':'zh',
				'to':'jp',
				'query':txt,
				'transtype':'translang',
				'simple_means_flag':'3'
				}
			data = urllib.parse.urlencode(data).encode('utf-8')
			#主要是由于该网站禁止爬虫导致的，可以在请求加上头信息，伪装成浏览器访问User-Agent
			#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
			#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
			#req = urllib.request.Request(url, headers=headers)  
			response = urllib.request.urlopen(url,data)
			#response = urllib.request.urlopen(req)
			html = response.read().decode('utf-8')
			html = json.loads(html)
			#print(html)
			trans = html['trans_result']['data'][0]['dst']
			print("翻译结果：",trans)