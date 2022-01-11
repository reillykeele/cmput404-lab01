import requests as req

r = req.get('https://raw.githubusercontent.com/reillykeele/cmput404-lab01/master/lab01.py')
print(r.text)