#!/usr/bin/env python3

import click
import json
import os

TODO_LOC = os.path.expanduser("~") + "/.todo/todo.json"

cli = click.Group()

@cli.command(name="init")
def initialize():
	home = os.path.expanduser("~")
	try:
		os.makedirs(home+"/.todo/")
	except:
		pass
	if not os.path.isfile(TODO_LOC):
		f = open(TODO_LOC,'w')
		f.write("{}")
		f.close()

@cli.command(name="list")
def print_list():
	try:
		f = open(TODO_LOC, 'r')
		d = json.load(f)
		f.close()
		l = [(k, d[k]) for k in d]
		sorted(l, key = lambda x: x[0])
		for t in l:
			print("{}: {}".format(int(t[0])+1, t[1]))
		print()
	except:
		print("todo is not initialized. run `todo init`.")

@cli.command(name="add")
@click.argument("text")
def add_to_list(text):
	try:
		f = open(TODO_LOC, 'r')
		d = json.load(f)
		f.close()
		new_key = len(d)
		d[new_key] = text
		f = open(TODO_LOC, 'w')
		f.write(json.dumps(d))
		f.close()
	except:
		print("todo is not initialized. run `todo init`.")

@cli.command(name="remove")
@click.argument("num_to_remove", type=int)
def remove_from_list(num_to_remove):
	try:
		num_to_remove -=1
		f = open(TODO_LOC, 'r')
		d = json.load(f)
		f.close()
		for i in range(num_to_remove, len(d)-1):
			d[str(i)] = d[str(i+1)]
		d.pop(str(len(d)-1), None)
		f = open(TODO_LOC, 'w')
		f.write(json.dumps(d))
		f.close()
	except:
		print("todo is not initialized. run `todo init`.")

@cli.command(name="edit")
@click.argument("num_to_edit", type=int)
@click.argument("new_text", type=str)
def edit_item(num_to_edit, new_text):
	try:
		num_to_edit = str(num_to_edit-1)
		f = open(TODO_LOC, 'r')
		d = json.load(f)
		f.close()
		d[num_to_edit] = new_text
		f = open(TODO_LOC, 'w')
		f.write(json.dumps(d))
		f.close()
	except:
		print("todo is not initialized. run `todo init`.")

@cli.command(name="move")
@click.argument("num_item", type=int)
@click.argument("direction")
def reorder(num_item, direction):
	try:
		num_item -=1
		f = open(TODO_LOC, 'r')
		d = json.load(f)
		f.close()
		if direction in ['up','u']:
			if num_item==0:
				print("invalid operation")
				return
			swap_id = str(num_item-1)
			num_item = str(num_item)
			temp = d[swap_id]
			d[swap_id] = d[num_item]
			d[num_item] = temp
		elif direction in ['down','d']:
			if num_item==len(d)-1:
				print("invalid operation")
				return
			swap_id = str(num_item+1)
			num_item = str(num_item)
			temp = d[swap_id]
			d[swap_id] = d[num_item]
			d[num_item] = temp
		f = open(TODO_LOC, 'w')
		f.write(json.dumps(d))
		f.close()
	except:
		print("todo is not initialized. run `todo init`.")

def main():
	cli()

if __name__ == '__main__':
	main()
