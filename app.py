import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# 定义文件路径
UID_LIST_FILE_PATH = '/usr/app/whitelist.json'

def load_uid_list():
    with open(UID_LIST_FILE_PATH, 'r') as file:
        return json.load(file)

@app.route('/auth', methods=['POST'])
def validate_user():
    data = request.json
    uid = data.get('uid')
    
    if not uid:
        return jsonify({"error": "UID is required"}), 400

    uid_list = load_uid_list()
    permit = uid_list.get(uid)

    if permit is None:
        return jsonify({"error": "UID not found"}), 404

    return jsonify({"permit": permit}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
