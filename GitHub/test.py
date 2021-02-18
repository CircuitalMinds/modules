import yaml
import requests

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
for j in modules_analysis:
    data = yaml.load(requests.get(url_analysis + j + ".yml").content, Loader=yaml.FullLoader)    
    for n in list(data.keys()): 
        nbs["data_analysis"]["module_" + j].append({"id": n, "url": data[n]})
for j in modules_basic:
    data = yaml.load(requests.get(url_basic + j + ".yml").content, Loader=yaml.FullLoader)    
    for n in list(data.keys()): 
        nbs["engineering-basic"]["module_" + j].append({"id": n, "url": data[n]})


with open("test.yml", "w") as outfile:
    yaml.dump(nbs, outfile, default_flow_style=False)
