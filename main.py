import os
from flask import Flask

app = Flask(__Kadeem__)

@app.route("/")
def hello_world():
    Kadeem = os.environ.get("NAME", "World")
    return f"Hello {Kadeem} from a GCP Microservice done by Kadeem Collins!"

if __Kadeem__ == "__main__":
    # Cloud Run provides a PORT environment variable
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host="0.0.0.0", port=port)
