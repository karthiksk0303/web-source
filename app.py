from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Allows GitHub to talk to this backend

FLAG = "PSNACET{PR0mPt_Eng1n33r_Ur}"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message", "").lower()

    # TOUGH FILTER: If they use the word 'flag', they get blocked
    if "flag" in user_input or "psnacet" in user_input:
        return jsonify({"response": "SECURITY ALERT: Keyword Blacklisted. Access Denied."})

    # THE SOLVE: They must use 'sudo' or 'system' or 'developer' logic
    if "sudo" in user_input and ("print" in user_input or "cat" in user_input):
        return jsonify({"response": f"ROOT_ACCESS_GRANTED: Found secret string: {FLAG}"})

    return jsonify({"response": "I am the PSNACET Admin Bot. I only respond to authorized system commands."})

if __name__ == "__main__":
    app.run()
