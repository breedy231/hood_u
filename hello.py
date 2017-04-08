from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/zips.geojson')
def zips():
	return app.send_static_file('zips.geojson')

@app.route('/data/universities.geojson')
def universities():
	return app.send_static_file('data/universities.geojson')

if __name__ == '__main__':
	app.run(debug=True)
