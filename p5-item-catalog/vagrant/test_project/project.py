from flask import Flask
# Create Flask instance
app = Flask(__name__)

# Assign decortators
@app.route('/hello')
def helloWorld():
	return "<h2>Hello, World</h2>"

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)