import json

lista = [1, 2, 3, 4, 5, 6]

dt_json = json.dumps(lista, indent=2, ensure_ascii=False, sort_keys=True)  # Serialize obj to a JSON formatted str.

nw_dt_python = json.loads('db.json')  # Deserialize s (a str, bytes or bytearray instance containing
                                      # a JSON document) to a Python object.

with open('db.jason', 'w') as js:
    json.dump(dt_json, js)  # Serialize obj as a JSON formatted stream to fp (a .write()-supporting file-like object).

with open('db.jason', 'r') as js:
    data = json.load(js)  #  Deserialize fp (a .read()-supporting file-like object containing a JSON document)
                          # to a Python object.