# Rent Calculator (Python)

A beautiful web-based application to calculate how much each person needs to pay when rent, food, and electricity bills are shared equally.

## Features
✅ Calculate individual shares of rent, food, and electricity expenses  
✅ Beautiful, responsive web interface  
✅ Real-time calculation  
✅ Works on any browser (localhost)  
✅ Perfect for roommates or flat-mates  

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/prakashorigin/rent-calculator.git
cd rent-calculator
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

## How to Run

### Web Application (Recommended)
```bash
python app.py
```

Then open your browser and go to:
```
http://localhost:5000
```

### Command-line Version (Original)
```bash
python rent_calculator.py
```

## How to Use the Web App

1. Enter the rent amount
2. Enter food expenses
3. Enter electricity units used
4. Enter charge per unit
5. Enter number of persons sharing
6. Click **Calculate**
7. View the results instantly!

## Project Structure
```
rent-calculator/
├── app.py                 # Flask web application
├── rent_calculator.py     # Original CLI version
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Web interface
└── static/
    ├── style.css         # Styling
    └── script.js         # Frontend logic
```

## Requirements
- Python 3.x
- Flask 2.3.3

## Author
Prakash

## License
MIT License

---
**🚀 Tip:** Share the localhost link with your roommates to calculate bills together!
