from flask import Flask, render_template, request

app = Flask(__name__)

# Sample mock data (replace this later with real API or scraping)
mock_flights = [
    {"route": "SYD - MEL", "price": 150, "date": "2025-08-01"},
    {"route": "SYD - BNE", "price": 180, "date": "2025-08-02"},
    {"route": "SYD - PER", "price": 210, "date": "2025-08-03"},
    {"route": "MEL - BNE", "price": 170, "date": "2025-08-04"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    origin = request.form.get('origin')
    destination = request.form.get('destination')

    filtered = [
        flight for flight in mock_flights
        if origin.lower() in flight["route"].lower() and destination.lower() in flight["route"].lower()
    ]

    return render_template('results.html', flights=filtered, origin=origin, destination=destination)

if __name__ == '__main__':
    app.run(debug=True)
