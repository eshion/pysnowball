from pysnowball import api_ref
from pysnowball import utls


def performances(gid):
    url = api_ref.moni_performances+gid
    return utls.fetch(url)


def trans_groups():
    url = api_ref.moni_trans_groups
    return utls.fetch(url)
