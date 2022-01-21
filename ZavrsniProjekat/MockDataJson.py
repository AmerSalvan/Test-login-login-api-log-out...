import json


def getTestData():
    TEST_DATA = []

    with open("MOCK_DATA.json","r") as f:
        TEST_DATA = json.load(f)
    return TEST_DATA

