import os
import yaml                                                                    
from multiprocessing import Pool                                                
                                                                                

repos = yaml.load(open("repositories.yml"))                                                                            
processes = tuple(repos.values())                                    
                                                  
                                                                                
def run_process(process):

    os.system('git clone {}'.format(process))
                                                                                
                                                                                
pool = Pool(processes=len(processes))                                                        
pool.map(run_process, processes)
