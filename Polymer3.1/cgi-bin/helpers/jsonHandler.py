#!/usr/bin/env python
from cgi import parse_header
import logging, os, sys, json, datetime

logging.basicConfig(level=logging.INFO)


def validateDate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
        # raise TypeError("Unknown type")


def serializeJson(dict):
    data = json.dumps(dict, default=datetime_handler)
    output = "Content-Type: application/json;"
    output += "charset=utf-8" + "\n"
    output += "\n"
    output += str(data) + "\n"
    print(output)
    logging.info("data send: " + output)


def deserializeJson():
    logging.info("Start reading request")
    cl, _ = parse_header(os.environ['CONTENT_LENGTH'])
    data = json.loads(sys.stdin.read(int(cl)))
    logging.info("src data: " + str(data))
    return data
