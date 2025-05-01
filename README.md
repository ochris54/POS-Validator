
# POS Validator

Its a Local PC Installation tool that validates POS updates after menu or price changes to ensure data accuracy and identify errors.

## Features
- Automatically checks POS data for discrepancies.
- Reports any errors or unchanged data after updates.
- Generates user-friendly reports that are store in the computer
- Automatically sends incident reports to IT teams by email.
- Easy to integrate with existing POS systems.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/POS-Validator.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt  # If Python
   ```

3. Run the tool:
   ```bash
   python pos.py  # Example for Python project
   ```

## Usage
1.	The tool is installed as a local application or script (e.g., Python script with a simple UI or batch/PowerShell automation).
2.	It runs manually by staff or automatically using Windows Task Scheduler (e.g., every day at 6 AM, post-deployment, or during store open hours).
3.	It reads POS data from local files or terminals and performs validation checks.

## Manually 
Step 1:

📁 POS_Menu_Validator/
├── pos.py       ← The main Python script
├── expected_menu.json          ← Pulled from backend or created manually.
├── live_menu.json              ← Exported or scraped from POS.
└── logs/
    └── report_YYYY-MM-DD.txt   ← Auto-generated after each run.


 Step 2: Install Python (if not installed)
If the PC doesn’t already have Python:
1. Download from https://www.python.org/downloads/
2. During installation: ✔ check “Add Python to PATH”


Step 3: Run the Software
1.	Open Command Prompt
2.	Navigate to your folder:
```bash
cd Desktop\POS
```

3.	Run the script:
```Bash
python pos.py
```
 
________________________________________


