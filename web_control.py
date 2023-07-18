import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

os.popen('start chrome --remote-debugging-port=9527 --user-data-dir="C:\chromedriver_win32"')
opt = Options()
opt.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
driver = webdriver.Chrome(options=opt)

'''
1. chromedriver放在"C:\chromedriver_win32"，並且設置全域變數
2. 使用開發者模式開啟Chrome才不會被Google擋登入
3. 定期更新chromedriver，因為Chrome自動更新很頻繁
'''