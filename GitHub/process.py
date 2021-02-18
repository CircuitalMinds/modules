import yaml
import requests
import os
from time import sleep


branch = "localhost"
repo = "https://github.com/CircuitalMinds/FractalMetric.git"


url = "https://raw.githubusercontent.com/CircuitalMinds/FractalMetric/localhost/circuitalminds/databases/notebooks/"

# manager
# libraries
# repo versions
# organization
# ready
url_analysis = url + "data_analysis_module_"
url_basic = url + "engineering-basic_module_"

modules_analysis = [str(j) for j in range(1, 8)]
modules_basic = [str(j) for j in range(0, 8)]

nbs = {"data_analysis": {"module_" + j: [] for j in modules_analysis} , "engineering-basic": {"module_" + j: [] for j in modules_basic}}

with open("test.yml", "w") as outfile:
    yaml.dump(nbs, outfile, default_flow_style=False)


for j in modules_analysis:
    data = yaml.load(requests.get(url_analysis + j + ".yml").content, Loader=yaml.FullLoader)
    for n in list(data.keys()):
        nbs["data_analysis"]["module_" + j].append({"id": n, "url": data[n]})
for j in modules_basic:
    data = yaml.load(requests.get(url_basic + j + ".yml").content, Loader=yaml.FullLoader)
    for n in list(data.keys()):
        nbs["engineering-basic"]["module_" + j].append({"id": n, "url": data[n]})

def gitpush():
    sentence_1 = "git init"
    sentence_2 = " && git add ."
    sentence_3 = " && git commit -m 'auto'"
    sentence_4 = " && git push origin " 
    sentence = sentence_1 + sentence_2 + sentence_3 + sentence_4
    
    f = open("./" + branch + "/gitpush.py", "w")
    f.write('import os\nos.system("' + sentence + branch + '")')
    f.close()
    print("cd ./" + branch + " && python3 gitpush.py")
    os.system("cd ./" + branch + " && python3 gitpush.py")
        
def gitclone():
    sentence = "git clone -b "
    print(sentence + branch + " " + repo + " " + branch)
    os.system(sentence + branch + " " + repo + " " + branch)
        

while True:
    gitpush()
    sleep(600)
