# robotframework-simply-json
a simply (beginner level) python library that help Robot Framework works with Json file.

I created this tiny library because i need to simply read - store some data in Robot Framework.
Maybe there are powerful ways to obtain the same result. Take this script for learning purpose.

## how to import
* download Robotframework-Json.py and put somewhere (maybe in the same folder of the test)
* import   .py as a library (e.g. Library  Robotframework-Json.py)

## Keyword provided
### read_json_file
It needs only a parameter : the path of the json file.
This will return the content of a json.
e.g. ${jsonString}=         read_json_file          myJson.json

### get_json_key_value
It needs two parameters : the path of the json file and the key to be read
This will return the content of a json key.
e.g. if myJson.json contains {"foo":"bar"}
${jsonKeyValue}=         get_json_key_value          myJson.json         foo
so {jsonKeyValue} value is "bar"

### set_json_key_value
It needs three parameters : the path of the json file, the key to be updated and the value.
When updated, it "close" the file.
e.g. set_json_file          myJson.json         myKey       myValue
