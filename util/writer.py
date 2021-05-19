from uuid import uuid1
import json

def writeReport(data):
    with open('C:\\Users\\jyurk\\Documents\\sims\\{0}.json'.format(str(uuid1())), 'w') as f:
        f.write(json.dumps(data))