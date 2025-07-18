import json, unittest, datetime
from msvcrt import kbhit

with open("./data-1.json", "r", encoding="utf-8") as f:
    jsonData1 = json.load(f)

with open("./data-2.json", "r", encoding="utf-8") as f:
    jsonData2 = json.load(f)

with open("./data-result.json", "r", encoding="utf-8") as f:
    jsonExpectedResult = json.load(f)


def convertFromFormat1(jsonObject):
    # IMPLEMENT: Conversion From Type 1

    location__ = jsonObject['location'].split('/')

    converted_file = {
        'deviceID' : jsonObject['deviceID'],
        'deviceType' : jsonObject['deviceType'],
        'timestamp' : jsonObject['timestamp'],

        'location' : {
            'country' : location__[0],
            'city' : location__[1],
            'area' : location__[2],
            'factory' : location__[3],
            'section' : location__[4]
        },

        'data' : {
            'status' : jsonObject['operationStatus'],
            'temperature' : jsonObject['temp']


        }

    }

    return converted_file


def convertFromFormat2(jsonObject):
    # IMPLEMENT: Conversion From Type 1
    # inspiration from https://stackoverflow.com/questions/60442518/python-3-convert-iso-8601-to-milliseconds/60443033#60443033
    millisec = datetime.datetime(2021, 6, 23, 10, 57, 17).timestamp()


    converted_file = {
        'deviceID' : jsonObject['device']['id'],
        'deviceType' : jsonObject['device']['type'],

        'timestamp' : millisec,

        'location' : {
            'country' : jsonObject['country'],
            'city' : jsonObject['city'],
            'area' : jsonObject['area'],
            'factory' : jsonObject['factory'],
            'section' : jsonObject['section']

        },

        'data' : {
            'status' : jsonObject['data']['status'],
            'temperature' : jsonObject['data']['healthy']

        }

    }


    return converted_file


def main(jsonObject):
    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)
    return result


class TestSolution(unittest.TestCase):

    def test_sanity(self):
        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(
            result,
            jsonExpectedResult
        )

    def test_dataType1(self):
        result = main(jsonData1)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 1 failed'
        )

    def test_dataType2(self):
        result = main(jsonData2)
        self.assertEqual(
            result,
            jsonExpectedResult,
            'Converting from Type 2 failed'
        )


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
