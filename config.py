# ---------------------------------------------------
# file:     $XDG_CONFIG_HOME/qutebrowser/config.py
# author:   jason ryan - http://jasonwryan.com/
# vim:fenc=utf-8:nu:ai:si:et:ts=4:sw=4:ft=python:
# ---------------------------------------------------

# load autoconfig.yml
config.load_autoconfig()

# general settings
c.content.headers.accept_language = 'en-US,en;q=0.5'
c.content.headers.user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
c.url.default_page = 'https://www.google.com/search?q={}'
c.editor.command = ["st", "-title", "scratchpad", "-geometry", "86x24+40+60", "-e", "vim", "-f", "{}"]
c.new_instance_open_target = "tab-bg"
c.prompt.filebrowser = False
c.completion.height = "30%"
c.completion.web_history_max_items = 1000
c.input.partial_timeout = 2000
c.tabs.show = 'never'
c.tabs.background = True
c.tabs.favicons.show = False
c.content.default_encoding = "utf-8"
c.tabs.title.format = "{title}"
c.downloads.location.directory = '/home/luksy/downloads'
c.content.cache.size = 52428800
c.content.webgl = False
c.content.host_blocking.enabled = False
c.hints.border = "1px solid #CCCCCC"
c.hints.mode = "number"
c.hints.chars = "123456789"
c.hints.min_chars = 1

# searches
c.url.searchengines['vw'] = 'https://wiki.voidlinux.eu/?search={}'
c.url.searchengines['gw'] = 'https://wiki.gentoo.org/?search={}'
c.url.searchengines['aw'] = 'https://wiki.archlinux.org/?search={}'
c.url.searchengines['g'] = 'http://www.google.com/search?hl=en&source=hp&ie=ISO-8859-l&q={}'
c.url.searchengines['yt'] = 'https://www.youtube.com/results?search_query={}'
c.url.searchengines['w'] = 'https://secure.wikimedia.org/wikipedia/en/w/index.php?title=Special%%3ASearch&search={}'
c.url.searchengines['gh'] = 'https://github.com/search?q={}&type=Code'

# aliases
c.aliases['tcl'] = 'tab-clone'
c.aliases['go'] = 'open -t https://stackoverflow.com'
c.aliases['gs'] = 'open -t https://unix.stackexchange.com'

# colors
c.colors.completion.fg = "#899CA1"
c.colors.completion.category.fg = "#F2F2F2"
c.colors.completion.category.bg = "#555555"
c.colors.completion.item.selected.fg = "white"
c.colors.completion.item.selected.bg = "#333333"
c.colors.completion.item.selected.border.top = "#333333"
c.colors.completion.item.selected.border.bottom = "#333333"
c.colors.completion.match.fg = "#F2F2F2"
c.colors.statusbar.normal.fg = "#899CA1"
c.colors.statusbar.normal.bg = "#222222"
c.colors.statusbar.insert.fg = "#899CA1"
c.colors.statusbar.insert.bg = "#222222"
c.colors.statusbar.command.bg = "#555555"
c.colors.statusbar.command.fg = "#F0F0F0"
c.colors.statusbar.caret.bg = "#5E468C"
c.colors.statusbar.caret.selection.fg = "white"
c.colors.statusbar.progress.bg = "#333333"
c.colors.statusbar.passthrough.bg = "#4779B3"
c.colors.statusbar.url.fg = c.colors.statusbar.normal.fg
c.colors.statusbar.url.success.http.fg = "#899CA1"
c.colors.statusbar.url.success.https.fg = "#53A6A6"
c.colors.statusbar.url.error.fg = "#8A2F58"
c.colors.statusbar.url.warn.fg = "#914E89"
c.colors.statusbar.url.hover.fg = "#2B7694"
c.colors.tabs.bar.bg = "#222222"
c.colors.tabs.even.fg = "#899CA1"
c.colors.tabs.even.bg = "#222222"
c.colors.tabs.odd.fg = "#899CA1"
c.colors.tabs.odd.bg = "#222222"
c.colors.tabs.selected.even.fg = "white"
c.colors.tabs.selected.even.bg = "#222222"
c.colors.tabs.selected.odd.fg = "white"
c.colors.tabs.selected.odd.bg = "#222222"
c.colors.tabs.indicator.start = "#222222"
c.colors.tabs.indicator.stop = "#222222"
c.colors.tabs.indicator.error = "#8A2F58"
c.colors.hints.bg = "#CCCCCC"
c.colors.hints.match.fg = "#000"
c.colors.downloads.start.fg = "black"
c.colors.downloads.start.bg = "#BFBFBF"
c.colors.downloads.stop.fg = "black"
c.colors.downloads.stop.bg = "#F0F0F0"
c.colors.keyhint.fg = "#FFFFFF"
c.colors.keyhint.suffix.fg = "#FFFF00"
c.colors.keyhint.bg = "rgba(0, 0, 0, 80%)"
c.colors.messages.error.bg = "#8A2F58"
c.colors.messages.error.border = "#8A2F58"
c.colors.messages.warning.bg = "#BF85CC"
c.colors.messages.warning.border = c.colors.messages.warning.bg
c.colors.messages.info.bg = "#333333"
c.colors.prompts.fg = "#333333"
c.colors.prompts.bg = "#DDDDDD"
c.colors.prompts.selected.bg = "#4779B3"

# fonts
#c.fonts.monospace = "Noto Sans Mono", "DejaVu Sans Mono", "Liberation Mono", monospace
c.fonts.tabs = "11pt Noto Sans Mono"
c.fonts.statusbar = "10pt Noto Sans Mono"
c.fonts.downloads = c.fonts.statusbar 
c.fonts.prompts = c.fonts.statusbar
c.fonts.hints = "13px Noto Sans Mono"
c.fonts.messages.info = "10pt Noto Sans Mono"
c.fonts.keyhint = c.fonts.messages.info
c.fonts.messages.warning = c.fonts.messages.info
c.fonts.messages.error = c.fonts.messages.info
c.fonts.completion.entry = c.fonts.statusbar
c.fonts.completion.category = c.fonts.statusbar

# keybinds
# config.unbind("<Shift-Ins>", mode="insert")
# config.unbind('gb', mode='normal')
# config.unbind('B', mode='normal')
# config.unbind('b', mode='normal')
# config.unbind('m', mode='normal')
# config.unbind('<Ctrl-B>', mode='normal')
config.bind('m', None)
config.bind('M', 'hint links spawn mpv {hint-url}')
# config.bind('<Ctrl-Right>', 'tab-next', mode='normal')
# config.bind('<Ctrl-Left>', 'tab-prev', mode='normal')
# config.bind('<Ctrl-Shift-Right>', 'tab-move +', mode='normal')
# config.bind('<Ctrl-Shift-Left>', 'tab-move -', mode='normal')
# config.bind('b', 'back', mode='normal')
# config.bind('m', 'forward', mode='normal')
# config.bind('B', 'set-cmd-text -s :bookmark-add', mode='normal')
# config.bind('t', 'set-cmd-text -s :open -t', mode='normal')
# config.bind('<Escape>', 'leave-mode', mode='passthrough')
# config.bind('gi', 'enter-mode insert ;; jseval --quiet var inputs = document.getElementsByTagName("input"); for(var i = 0; i < inputs.length; i++) { var hidden = false; for(var j = 0; j < inputs[i].attributes.length; j++) { hidden = hidden || inputs[i].attributes[j].value.includes("hidden"); }; if(!hidden) { inputs[i].focus(); break; } }')
# config.bind('<Ctrl-p>', 'jseval document.location=\'https://pinboard.in/add?next=same&url=\'+encodeURIComponent(location.href)+\'&title=\'+encodeURIComponent(document.title)', mode="normal")

