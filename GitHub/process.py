import os
from time import sleep


branch = "localhost"
repo = "https://github.com/CircuitalMinds/FractalMetric.git"


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
