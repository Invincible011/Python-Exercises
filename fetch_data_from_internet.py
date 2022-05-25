import requests 
#from django_main
# import json  # Load Json

url = 'http://www.google.com'
r = requests.get(url)

print(r.status_code)
data = r.read()
print(data.read())
# jsonData = json.load(data)
# print(jsonData)
#
#
# class Joke:
#
#     def __init__(self, setup, punchline) -> None:
#         self.setup = setup
#         self.punchline = punchline
#
#     #def __str__(self) -> str:
#      #   return 'setup {self.setup} punchline {self.punchline}'
#
#
# jokes = []
#
# for j in jsonData:
#     setup = j['setup']
#     punchline = j['punchline']
#     joke = Joke(setup, punchline)
#     jokes.append(joke)
#
# print(forgot {len(jokes)} jokes')
#
# for joke in jokes:
#  print(joke)
