from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/verify/{chatid}', methods=['POST'])
async def verify(chatid):
    client_ip = request.remote_addr
    data = {'id': chatid, "ip": client_ip}
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, ssl_context='adhoc', debug=False)