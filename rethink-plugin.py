import sublime_plugin
import logging
import json
import os, sys
sys.path.append(os.path.join(os.getcwd(), 'libs'))

from rethinkdb import r

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit, selected):
		rdbHost = '127.0.0.1'
		rdbPort = '28015'
		try: 
			r.connect( rdbHost, rdbPort).repl()
		except Exception as e:
			self.view.insert(edit, 0, str(e))

		# Some insert queries will have these values in javascript format
		true = True
		false = False
		null = None
		code = compile(selected, '<string>','single')
		try:
			res = eval(selected)
		except Exception as e:
			self.view.insert(edit, 0, str(e))
		y = json.dumps(res, indent='    ')
		print(res)
		self.view.insert(edit, 0, y)

class QueryPanelCommand(sublime_plugin.WindowCommand):
	def run(self):
		currentView = self.window.active_view()
		sel = currentView.sel()[0]
		selected = currentView.substr(sel)
		# view = self.window.new_file(0, "JSON.sublime-syntax")
		view = self.window.create_output_panel('result', True)
		view.set_syntax_file("JSON.sublime-syntax")
		view.run_command("example", {"selected": selected})
		self.window.run_command('show_panel', {"panel" : "output.result"})

class QueryNewWindowCommand(sublime_plugin.WindowCommand):
	def run(self):
		currentView = self.window.active_view()
		sel = currentView.sel()[0]
		selected = currentView.substr(sel)
		view = self.window.new_file(0, "JSON.sublime-syntax")
		view.run_command("example", {"selected": selected})