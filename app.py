from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime
import os

app = Flask(__name__)

# In-memory storage for requests (for demo purposes)
requests_db = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        try:
            data = request.get_json()
            new_request = {
                'id': len(requests_db) + 1,
                'description': data.get('description'),
                'priority': data.get('priority'),
                'category': data.get('category'),
                'contact_email': data.get('contact_email'),
                'status': 'open',
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            requests_db.append(new_request)
            return jsonify({'success': True, 'request_id': new_request['id']})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
    return render_template('submit.html')

@app.route('/api/recent-requests')
def recent_requests():
    return jsonify(requests_db[-5:][::-1])  # Return last 5 requests, newest first

@app.route('/requests')
def list_requests():
    return render_template('requests.html', requests=requests_db[::-1])  # Show all requests, newest first

@app.route('/requests/<int:request_id>')
def view_request(request_id):
    request_data = next((req for req in requests_db if req['id'] == request_id), None)
    if request_data:
        return render_template('request.html', request=request_data)
    return "Request not found", 404

if __name__ == '__main__':
    app.run(debug=True, port=5000) 