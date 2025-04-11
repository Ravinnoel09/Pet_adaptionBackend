from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_connection

app = Flask(__name__)
CORS(app)

@app.route('/pets', methods=['GET'])
def get_pets():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Pet WHERE status='Available'")
    pets = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(pets)

@app.route('/owners', methods=['POST'])
def add_owner():
    data = request.json
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO Owner (name, email, phone, address) VALUES (%s, %s, %s, %s) RETURNING owner_id",
                (data['name'], data['email'], data['phone'], data['address']))
    owner_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"owner_id": owner_id})

@app.route('/request', methods=['POST'])
def request_adoption():
    data = request.json
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO Adoption_Request (pet_id, owner_id, status) VALUES (%s, %s, 'Pending')",
                (data['pet_id'], data['owner_id']))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Request submitted"})

@app.route('/my_requests/<int:owner_id>', methods=['GET'])
def view_requests(owner_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT p.name, r.status, r.request_date
        FROM Adoption_Request r
        JOIN Pet p ON r.pet_id = p.pet_id
        WHERE r.owner_id = %s
    """, (owner_id,))
    requests = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(requests)

if __name__ == '__main__':
    # Bind to 0.0.0.0 to make it accessible externally
    app.run(host='0.0.0.0', port=5000, debug=True)