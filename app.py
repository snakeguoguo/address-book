from flask import Flask, render_template, request, jsonify
import pandas as pd
from contacts import Contact

app = Flask(__name__)

# 初始化联系人列表
contacts = []

@app.route('/')
def index():
    return render_template('index.html', contacts=contacts)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')
    student_id = data.get('id')
    email = data.get('email')
    address = data.get('address')
    notes = data.get('notes')

    if not name:
        return jsonify({"status": "error", "message": "Name is required"}), 400

    new_contact = Contact(name=name, phone=phone, id=student_id, email=email, address=address, notes=notes)
    contacts.append(new_contact)
    return jsonify({"status": "success", "contact": new_contact.__dict__})
