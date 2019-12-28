import json
import os
from pysnowball import cons
from pysnowball import api_ref
from pysnowball import utls

def list():
    url = api_ref.portfolio_list
    return utls.fetch(url)

def stock_list(pid):
    url = api_ref.portfolio_stock_list+pid
    return utls.fetch(url)
