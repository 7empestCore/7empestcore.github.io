from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Artifact Data (same as your original)
artifact_data = {
    "Steroid Implant": {"AP": 5},
    # Add the rest of your artifact data here...
}

@app.route('/')
def home():
    return render_template('index.html', artifacts=artifact_data.keys())

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    selected_artifacts = data['selected_artifacts']
    roll_type = data['roll_type']
    hp_boost = data['hp_boost']

    totals = {"AP": 0, "ARM": 0, "HP": 0, "MP": 0, "HSP": 0, "SP": 0, "MR": 0, "CC": 0, "MCC": 0}
    
    # Perform the same calculation logic as your script
    for artifact in selected_artifacts:
        if artifact in artifact_data:
            for stat, value in artifact_data[artifact].items():
                # Apply roll type logic...
                totals[stat] += value

    if hp_boost == "20% Boost":
        totals["HP"] = int(totals["HP"] * 1.2)

    return jsonify(totals)

if __name__ == '__main__':
    app.run(debug=True)
