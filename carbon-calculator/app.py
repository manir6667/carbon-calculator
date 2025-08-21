from flask import Flask, render_template, request

app = Flask(__name__)

# Simple emission factors (demo purposes only)
CAR_EMISSION = 0.12           # kg CO2 per km
BIKE_EMISSION = 0.05          # kg CO2 per km
ELECTRICITY_EMISSION = 0.4    # kg CO2 per kWh
FLIGHT_EMISSION = 90          # kg CO2 per short flight

def to_float(val):
    try:
        return float(val)
    except (TypeError, ValueError):
        return 0.0

@app.route("/", methods=["GET", "POST"])
def home():
    total = None
    if request.method == "POST":
        car_km = to_float(request.form.get("car"))
        bike_km = to_float(request.form.get("bike"))
        electricity = to_float(request.form.get("electricity"))
        flights = to_float(request.form.get("flights"))

        total = (car_km * CAR_EMISSION +
                 bike_km * BIKE_EMISSION +
                 electricity * ELECTRICITY_EMISSION +
                 flights * FLIGHT_EMISSION)

        # Round for nice display
        total = round(total, 2)

    return render_template("index.html", total=total)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
