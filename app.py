from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    h_m = height_cm / 100.0
    return round(weight_kg / (h_m*h_m), 2)

def bmi_category(bmi: float) -> str:
    if bmi < 18.5: return "Underweight"
    if bmi < 25: return "Normal"
    if bmi < 30: return "Overweight"
    return "Obesity"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    weight = float(request.form["weight"])
    height = float(request.form["height"])
    bmi = calculate_bmi(weight, height)
    return render_template("index.html", result={"bmi": bmi, "category": bmi_category(bmi)})

if __name__ == "__main__":
    app.run(debug=True)
