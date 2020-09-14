"""
Bruty is a library written in Python that 
utilizes multithreading to attain large 
amounts of requests per minute to bruteforce websites
"""
                                 
# ,-----.                   ,--.            
# |  |) /_ ,--.--.,--.,--.,-'  '-.,--. ,--. 
# |  .-.  \|  .--'|  ||  |'-.  .-' \  '  /  
# |  '--' /|  |   '  ''  '  |  |    \   '   
# `------' `--'    `----'   `--'  .-'  /    
#                                 `---'     


import requests

from .manager import BruteManager
from requests.sessions import Session

from .__version__ import __title__, __description__, __url__, __version__
from .__version__ import __author__, __author_email__, __license__, __copyright__

__title__ = 'Bruty'
__description__ = 'Bruteforcing library'
__version__ = '0.0.1'
__author__ = 'Prem Nair'
__author_email__ = 'premnair1112@gmail.com'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020 Prem Nair'
