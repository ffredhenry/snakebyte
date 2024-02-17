#!/usr/bin/python3

import requests, sys

sub_list = open("wordlists.txt").read()
directories = sub_list.splitlines()

for dir in directories:
	dir_enum = f"http://{sys.argv[1]}/{dir}.html"
	r = requests.get(dir_enum)
	if r.status_code == 404:
		pass
	else:
		print("Valid directory:" ,dir_enum)
