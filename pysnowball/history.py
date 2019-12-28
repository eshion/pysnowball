from pysnowball import api_ref
from pysnowball import utls

def trade(symbol, count=10):
    
    url = "{}?symbol={}&count={}".format(api_ref.history_trade, symbol, count)

    return utls.fetch(url)


def quote(symbol):
    
    url = "{}?symbol={}&extend=detail".format(api_ref.history_quote, symbol)

    return utls.fetch(url)