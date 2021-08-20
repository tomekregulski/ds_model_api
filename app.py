from flas import Flask

app = Flask(__name__)

def greeting():
  return 'Flask is awesome!'