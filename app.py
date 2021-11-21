from datetime import datetime

from flask import request, Flask

app = Flask(__name__)

@app.route("/get-hour")
def get_hour():
    return {"hour": datetime.now().hour}

if __name__ == '__main__':
    app.run()
