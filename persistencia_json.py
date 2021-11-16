import json
def store(var, file):
    json.dump(json.dumps(var), open(file, "w"))
def retrieve(file):
    var = json.loads(json.load(open(file, "r")))
    return var

