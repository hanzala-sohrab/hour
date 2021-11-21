import pytz

from datetime import datetime
from flask import request, Flask

app = Flask(__name__)

IST = pytz.timezone('Asia/Kolkata')

@app.route("/get-hour")
def get_hour():
    return {"hour": datetime.now(IST).hour}

if __name__ == '__main__':
    app.run()
