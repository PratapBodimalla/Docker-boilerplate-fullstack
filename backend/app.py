from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get the DATABASE_URL environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

print(DATABASE_URL)


# Connect to PostgreSQL using DATABASE_URL
def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn


# # Database connection details (can be loaded from environment variables)
# DB_HOST = os.getenv("DB_HOST", "host.docker.internal")
# # DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
# DB_PORT = os.getenv("DB_PORT", "5432")
# DB_NAME = os.getenv("DB_NAME")
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")


# # Connect to PostgreSQL
# def get_db_connection():
#     conn = psycopg2.connect(
#         host=DB_HOST,
#         database=DB_NAME,
#         user=DB_USER,
#         password=DB_PASSWORD,
#         port=DB_PORT,
#         cursor_factory=RealDictCursor,
#     )
#     return conn


# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)


# POST a new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING *;",
            (name, email),
        )
        new_user = cur.fetchone()
        conn.commit()
    except psycopg2.Error as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cur.close()
        conn.close()

    return jsonify(new_user), 201


# PUT (update) a user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "UPDATE users SET name = %s, email = %s WHERE id = %s RETURNING *;",
            (name, email, user_id),
        )
        updated_user = cur.fetchone()
        if not updated_user:
            return jsonify({"error": "User not found"}), 404
        conn.commit()
    except psycopg2.Error as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cur.close()
        conn.close()

    return jsonify(updated_user)


# DELETE a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM users WHERE id = %s RETURNING *;", (user_id,))
        deleted_user = cur.fetchone()
        if not deleted_user:
            return jsonify({"error": "User not found"}), 404
        conn.commit()
    except psycopg2.Error as e:
        return jsonify({"error": str(e)}), 400
    finally:
        cur.close()
        conn.close()

    return jsonify(deleted_user)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
