#!/usr/bin/env python3
#coding=utf-8
import requests
import re
import os
import json
import sys
import pprint
# from urllib.parse import unquote

def get_true_url(url, headers):
	s = requests.session()
	status_code = 302
	while status_code == 302:
		r = s.head(url, headers=headers)#,allow_redirects=False,stream=True)
		print(r.status_code)
		status_code = r.status_code
		if status_code == 403:
			# return 0,0
			return 0
		elif r.headers.get('location'):
			url = r.headers.get('location')
			print(url)
			if 'nj02all01.baidupcs' in url:
				break
			else:
				pass
	return url


def getdlurl(txt, bdp_serv):
	# cookies = config['cookies']
	# headers = config['headers']
	task_pool = []
	# headers = {}
	# url = ''
	with open(txt) as f:
		for line in f.readlines():
			line = line.rstrip()
			if line.startswith('http'):
				task_pool.append({'url':line,
							 'headers':{},
							 'name':''})
				# if url:
			elif line.startswith(' header'):
				# headers += line.replace(' header=','') + ';'
				line = line.replace(' header=','')
				key, value = line.split(': ')
				task_pool[-1]['headers'][key] = value
			elif line.startswith(' out'):
				task_pool[-1]['name'] = line.split('=')[-1]
			else:
				pass

	for task in task_pool:
		dlurl = get_true_url(task['url'], task['headers'])
		if bdp_serv:
			p = re.compile('//.+?(baidupcs)')
			dlurl = p.sub(r'//{}.\1'.format(bdp_serv),dlurl)
			print(dlurl)
		else:
			pass
		yield (dlurl, task['name'])
		
	# if 'fin=' in url:
	# 	p = re.compile('fin=(.+?)&')
	# 	name = unquote( p.findall(url)[0] )
	# else:
	# 	name = ""

	# 	return dlurl, name
	# else:
	# 	return url, name

def main():
	txt = sys.argv[1]
	if os.name == 'nt':
		dldir = '\\'.join(txt.split('\\')[:-1])
		if os.path.exists('fuckbdp.json'):
			cfg = 'fuckbdp.json'
		else:
			cfg = '\\'.join( sys.argv[0].split('\\')[:-1] ) + '\\fuckbdp.json'
	else:
		dldir = '/'.join(txt.split('/')[:-1])
		cfg = os.path.expanduser('~/.fuckbdp')
	config = open(cfg).read()
	config = json.loads(config)

	for url_and_name in getdlurl(txt, config['head']):
		dlurl,name = url_and_name

		if name:
			os.system( 'aria2c -x{s} -s{s} -k1M -U "netdisk" -d "{dir}" -o "{name}" -c "{url}"'.format(s=config['thread'],dir=dldir,name=name,url=dlurl) )
		else:
			os.system( 'aria2c -x{s} -s{s} -k1M -U "netdisk" -d "{dir}" -c "{url}"'.format(s=config['thread'],dir=dldir,url=dlurl) )

	input("Done.")


# try:
main()
# except Exception as e:
# 	print(e)
# 	input(":")
