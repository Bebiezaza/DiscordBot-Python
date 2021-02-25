#START dotenv
import os
from dotenv import load_dotenv
load_dotenv()
global TOKEN
TOKEN = os.getenv('TOKEN')

global prefix
prefix = os.getenv('PREFIX')
#END dotenv

global version
version = "Alpha 2.0.1"