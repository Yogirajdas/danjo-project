import sys
import requests
import json
import os
user= 'Yogirajdas'
token = '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'

repo_name = str(sys.argv[1])


# Passing Repository name
payload = {'name': repo_name}

login = requests.post('https://api.github.com/' + 'user/repos', auth=(user,token), data=json.dumps(payload))
print(login.status_code)
