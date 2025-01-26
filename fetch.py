from json import loads
from os import rename
import cdsapi


JSON_PATH = "configuration.json"

conf = None
with open(JSON_PATH) as f:
    conf = loads(f.read())


client = cdsapi.Client()
fetched = client.retrieve(conf['dataset'], conf['request']).download()
print("FETCHED: ", fetched)

if conf['datafolder'] != "":
    if conf['datafolder'].endswith('/'):
        rename(fetched, conf['datafolder']+fetched)
    else:
        rename(fetched, conf['datafolder']+'/'+fetched)
