import webbrowser
import selenium.webdriver as wd
import content as c

br = wd.Firefox()
br.get(c.url)
webbrowser.open(c.url, 1)
print(br.title)
print(c.url)
print(br.current_url == c.url)
