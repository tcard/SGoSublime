from sgosubl import gs
import os
import sublime_plugin

def _stx(v):
	old = [
		'SGoSublime.tmLanguage',
		'SGoSublime-next.tmLanguage',
	]

	fn = 'Packages/SGoSublime/syntax/SGoSublime-Go.tmLanguage'
	if not os.path.exists(gs.dist_path('syntax/SGoSublime-Go.tmLanguage')):
		return

	stx = v.settings().get('syntax')
	if stx:
		name = stx.replace('\\', '/').split('/')[-1]
		if name in old:
			print('SGoSublime: changing syntax of `%s` from `%s` to `%s`' % (
				(v.file_name() or ('view://%s' % v.id())),
				stx,
				fn
			))
			v.set_syntax_file(fn)


class Ev(sublime_plugin.EventListener):
	def on_load(self, view):
		_stx(view)

	def on_activated(self, view):
		_stx(view)
