from cgi import parse_header
import logging, os, sys, json

logging.basicConfig(level=logging.INFO)

def serializeJson(dict):
    data = json.dumps(dict)
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