import sublime_plugin
import logging
import json

from RethinkDB.libs.rethinkdb import r

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit, selected):
		rdbHost = '127.0.0.1'
		rdbPort = '28015'
		projectId = '98e5e32e-e37f-4432-96a8-8843fab0631a'
		r.connect( rdbHost, rdbPort).repl()
		# NOHA GET THE FUCKING BOAT NOW!!!
		true = True
		false = False
		null = None
		code = compile(selected, '<string>','single')
		res = eval(selected)
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