import os,sys
import logging 
from datetime import datetime
# set the log folder 
log_file=f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"

log_path=os.path.join(os.getcwd(),"logs",log_file)
os.makedirs(log_path,exist_ok=True)

final_path=os.path.join(log_path,log_file)

logging.basicConfig(
                level=logging.INFO,
                format="[ %(asctime)s] %(lineno)s -%(levelname)s - %(message)s" ,
                filename=final_path
            )