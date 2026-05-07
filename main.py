from flask import Flask, jsonify
from supabase import create_client
import os

app = Flask(__name__)

# Environment variables from Cloud Run
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")

# Create Supabase client
supabase = create_client(url, key)


@app.route("/")
def home():
    return "Cloud Run is working!"


# New endpoint
@app.route("/count/<table_name>")
def get_table_count(table_name):
    try:
        # Query table with exact count
        response = supabase.table(table_name).select(
            "*",
            count="exact"
        ).execute()

        count = response.count

        return jsonify({
            "table": table_name,
            "count": count
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
