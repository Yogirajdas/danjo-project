# danjo-project


import os
import sys
import requests
if sys.argv[2]:
    print("Adding {} to .gitignore".format(str(sys.argv[2])))
    os.chdir(sys.argv[1])
    name = requests.get("https://www.gitignore.io/api/{}".format(sys.argv[2]))
    with open(".gitignore", 'ab') as out:
        out.write(name.content + b"\n")
else:
    print(".gitignore not added")



#!/bin/bash
# $1 -> Contains project name.
# $2 -> Contains environment to put in .gitignore  

echo "Setting Up," $1
python3 create.py $1 $2 
echo "--------Repository Created ---------"

cd my-projects/
echo " "
echo "-------Setting up git locally------"

mkdir $1
cd $1 
git init .
git remote add origin https://github.com/Yogirajdas/$1.git
touch README.md
touch .gitignore
# Storing repository's path
VAR1=$(pwd)
echo " "

echo "-------Initializing .gitignore--------"
# Going back to the root directory,
# to fetch from https://www.gitignore.io/api/
# and write it to .gitignore
cd ~   
python3 create-gitignore.py $VAR1 $2
cd "$VAR1"  
git add .
git commit -m "Initial commit"
git push -u origin master
echo " "
# echo "--------Finished---------"

echo " "
echo "Launching Vs code"
code . 




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


