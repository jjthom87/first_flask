from flask import Flask, request, render_template

#pass in name to help Flask, help it determine the root path
app = Flask(__name__)

#@app.route('/')
#def index():
#	return 'this is the homepage'
	
@app.route('/profile/<name>')
def profile(name):
	return render_template("profile.html", name=name)
	
@app.route('/bacon', methods=['GET','POST'])
def bacon():
	if request.method == 'GET':
		return "You are probably using GET"
	else:
		return "You are using POST"

#check to make sure that we only start the web server when 
#this file is called directly
if __name__ == "__main__":
	app.run(debug=True)
