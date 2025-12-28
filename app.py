from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        
        rent = float(data.get('rent', 0))
        food = float(data.get('food', 0))
        electricity_units = float(data.get('electricity_units', 0))
        charge_per_unit = float(data.get('charge_per_unit', 0))
        persons = int(data.get('persons', 1))
        
        if persons <= 0:
            return jsonify({'error': 'Number of persons must be greater than 0'}), 400
        
        # Calculate electricity bill
        electricity_bill = electricity_units * charge_per_unit
        
        # Calculate total expense
        total_expense = rent + food + electricity_bill
        
        # Calculate per person amount
        amount_per_person = total_expense / persons
        
        return jsonify({
            'rent': rent,
            'food': food,
            'electricity_bill': electricity_bill,
            'total_expense': total_expense,
            'persons': persons,
            'amount_per_person': round(amount_per_person, 2)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
