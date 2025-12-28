document.getElementById('calculatorForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const rent = parseFloat(document.getElementById('rent').value);
    const food = parseFloat(document.getElementById('food').value);
    const electricity_units = parseFloat(document.getElementById('electricity_units').value);
    const charge_per_unit = parseFloat(document.getElementById('charge_per_unit').value);
    const persons = parseInt(document.getElementById('persons').value);
    
    try {
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                rent,
                food,
                electricity_units,
                charge_per_unit,
                persons
            })
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            showError(data.error);
            return;
        }
        
        // Display results
        document.getElementById('resultRent').textContent = '₹ ' + data.rent.toFixed(2);
        document.getElementById('resultFood').textContent = '₹ ' + data.food.toFixed(2);
        document.getElementById('resultElectricity').textContent = '₹ ' + data.electricity_bill.toFixed(2);
        document.getElementById('resultTotal').textContent = '₹ ' + data.total_expense.toFixed(2);
        document.getElementById('resultPersons').textContent = data.persons;
        document.getElementById('resultPerPerson').textContent = '₹ ' + data.amount_per_person.toFixed(2);
        
        document.getElementById('resultContainer').style.display = 'block';
        document.getElementById('errorContainer').style.display = 'none';
        
    } catch (error) {
        showError('An error occurred. Please try again.');
    }
});

function showError(message) {
    document.getElementById('errorContainer').textContent = '⚠️ ' + message;
    document.getElementById('errorContainer').style.display = 'block';
    document.getElementById('resultContainer').style.display = 'none';
}
