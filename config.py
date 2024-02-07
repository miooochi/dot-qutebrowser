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

c.content.pdfjs = True

c.scrolling.bar = "always"

c.tabs.new_position.unrelated = "last"
c.tabs.new_position.related = "last"
c.tabs.padding = {"bottom": 3, "left": 5, "right": 5, "top": 3}
c.tabs.position = "left"
c.tabs.width = 150
c.tabs.show = "always"

c.url.default_page = "https://google.com/"
c.url.searchengines = {"DEFAULT": "https://google.com/search?q={}"}
c.url.start_pages = "https://qutebrowser.org/"

c.colors.webpage.bg = "white"
c.colors.webpage.preferred_color_scheme = "dark"
c.colors.webpage.darkmode.enabled = False
c.colors.webpage.darkmode.algorithm = "lightness-cielab"
c.colors.webpage.darkmode.policy.images = "smart"
c.colors.webpage.darkmode.threshold.background = 0

# Bindings for normal mode
config.bind('"b"', '":w:')
config.unbind("d")
config.bind("n", "opencccccctdurbuhejtbdklteejldnuhdjeiledruudkrle")
config.bind("x", "tab-close")

# Theme
import catppuccin

# load your autoconfig, use this, if the rest of your config is empty!
config.load_autoconfig()

# set the flavor you'd like to use
# valid options are 'mocha', 'macchiato', 'frappe', and 'latte'
# last argument (optional, default is False): enable the plain look for the menu rows
catppuccin.setup(c, "mocha", True)
