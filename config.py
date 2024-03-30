config.load_autoconfig(False)

c.auto_save.session = True

config.set("content.cookies.accept", "all", "chrome-devtools://*")
config.set("content.cookies.accept", "all", "devtools://*")
config.set("content.headers.accept_language", "", "https://matchmaker.krunker.io/*")
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}",
    "https://web.whatsapp.com/",
)
config.set(
    "content.headers.user_agent",
    "Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0",
    "https://accounts.google.com/*",
)
config.set("content.images", True, "chrome-devtools://*")
config.set("content.images", True, "devtools://*")
config.set("content.javascript.enabled", True, "chrome-devtools://*")
config.set("content.javascript.enabled", True, "devtools://*")
config.set("content.javascript.enabled", True, "chrome://*/*")
config.set("content.javascript.enabled", True, "qute://*/*")
config.set(
    "content.local_content_can_access_remote_urls",
    True,
    "file:///home/kev/.local/share/qutebrowser/userscripts/*",
)
config.set(
    "content.local_content_can_access_file_urls",
    False,
    "file:///home/kev/.local/share/qutebrowser/userscripts/*",
)

# open_categories
c.completion.open_categories = ["searchengines", "quickmarks", "bookmarks", "history"]

# history
c.completion.web_history.max_items = 100
c.completion.cmd_history_max_items = 100

# enable clipboard
c.content.javascript.clipboard = "access"
c.content.pdfjs = True

# enable notification
c.content.notifications.enabled = True
c.content.notifications.presenter = "libnotify"

# enable brave browser adblocker
c.content.blocking.method = "both"

# always show scrollbar
c.scrolling.bar = "always"

# enable spellcheck
c.spellcheck.languages = ["en-US"]


c.tabs.new_position.unrelated = "last"
c.tabs.new_position.related = "last"
c.tabs.padding = {"bottom": 3, "left": 5, "right": 5, "top": 3}
c.tabs.position = "left"
c.tabs.width = 150
c.tabs.show = "always"

c.url.default_page = "https://google.com/"
c.url.searchengines = {
    "DEFAULT": "https://google.com/search?q={}",
    "aw": "https://wiki.archlinux.org/?search={}",
    "re": "https://www.reddit.com/r/{}",
    "yt": "https://www.youtube.com/results?search_query={}",
    "np": "https://search.nixos.org/packages?channel=unstable&from=0&size=50&sort=relevance&type=packages&query={}",
    "nc": "https://mynixos.com/search?q={}",
    "no": "https://search.nixos.org/options?channel=unstable&from=0&size=50&sort=relevance&type=packages&query={}",
}
c.url.start_pages = "https://qutebrowser.org/"

c.colors.webpage.bg = "white"
c.colors.webpage.preferred_color_scheme = "dark"
c.colors.webpage.darkmode.enabled = False
c.colors.webpage.darkmode.algorithm = "lightness-cielab"
c.colors.webpage.darkmode.policy.images = "smart"
c.colors.webpage.darkmode.threshold.background = 0

# Bindings for normal mode
config.unbind("O")
config.unbind("d")
config.unbind("D")
config.unbind("q")
config.unbind("m")
config.unbind("M")
config.unbind("h")
config.bind("<Ctrl-o>", "cmd-set-text -s :open -t ")
config.bind("x", "tab-close")
config.bind(
    "qv", "hint links spawn mpv {hint-url} --hwdec=auto --audio-device=auto"
)  # spawn mpv to play video from the selected url
config.bind(
    "qa", "hint links spawn mpv {hint-url} --hwdec=auto --audio-device=auto --no-video"
)  # spawn mpv to play audio only from the selected url
config.bind("tt", "config-cycle tabs.show always never")  # toggle tabs
config.bind("mm", "cmd-set-text -s :quickmark-add {url}")  # quickmark-add
config.bind("mM", "cmd-set-text -s :bookmark-add")  # bookmark-add
config.bind("ml", "cmd-set-text -s :quickmark-load -t")  # quickmark-load
config.bind("mL", "cmd-set-text -s :bookmark-load -t")  # bookmark-load
config.bind("mB", ":open -t qute://bookmarks/")  # open qute://bookmarks/
config.bind("h", ":open -t qute://history/")  # open qute://history/

# Theme
import catppuccin

# load your autoconfig, use this, if the rest of your config is empty!
config.load_autoconfig()

# set the flavor you'd like to use
# valid options are 'mocha', 'macchiato', 'frappe', and 'latte'
# last argument (optional, default is False): enable the plain look for the menu rows
catppuccin.setup(c, "mocha", True)
