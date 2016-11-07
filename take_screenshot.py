from pyvirtualdisplay import Display
from selenium import webdriver

# Set screen resolution to 1366 x 768 like most 15" laptops
display = Display(visible=0, size=(1366, 768))
display.start()

# now Firefox will run in a virtual display.
browser = webdriver.Chrome()

# Sets the width and height of the current window
browser.set_window_size(1366, 768)

# Open the URL
browser.get('http://www.google.com/')

# set timeouts
browser.set_script_timeout(30)
browser.set_page_load_timeout(30) # seconds

# Take screenshot
browser.save_screenshot('/Users/divyasrikanth/Desktop/Screenshot.png')

# quit browser
browser.quit()

# quit Xvfb display
display.stop()
