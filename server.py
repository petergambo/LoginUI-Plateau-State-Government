from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# print("App is running with the name: " + str(app))

@app.route('/login-data', methods=["GET", 'POST'])
def login():
    if(request.method == "POST"):
        user_email = request.form.get('userEmail')
        user_pass = request.form.get('pw')
        
        return jsonify(
            email= user_email,
            password = user_pass
        )
    else:
        return {
            'message': "no data"
        }
        

if __name__ == '__main__':
    app.run()
    
    
