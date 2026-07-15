from flask import Flask
import pymysql

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = pymysql.connect(
            host="newdatabase-1.cpu20giac4ke.ap-south-1.rds.amazonaws.com",
            user="admin",
            password="mydatabase15",
            database="mysql",
            port=3306
        )

        cursor = conn.cursor()
        cursor.execute("SELECT VERSION();")
        version = cursor.fetchone()

        conn.close()

        return f"""
        <h1>3-Tier AWS Architecture 🚀</h1>
        <h2>Connected to Amazon RDS Successfully!</h2>
        <p>Database Version: {version[0]}</p>
        """

    except Exception as e:
        return f"<h2>Database Connection Failed</h2><pre>{e}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
