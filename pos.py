# Fibonacci series up to n

import json

# Load menu data from two files
def load_menu(file_path):
    with open(file_path, 'r', encoding= 'utf-8') as file:
        return json.load(file)

# Compare two menus and return issues
def compare_menus(expected, live):
    issues = []
    live_dict = {item['item']: item['price'] for item in live}

    for item in expected:
        name = item['item']
        expected_price = item['price']
        live_price = live_dict.get(name)

        if live_price is None:
            issues.append(f"❌ Missing item in live POS: {name}")
        elif live_price == 0:
            issues.append(f"❌ {name} is priced at $0.00 in live POS")
        elif expected_price != live_price:
            issues.append(f"⚠️ {name} expected ${expected_price}, but live POS has ${live_price}")
        else:
            print(f"✅ {name} is correctly priced at ${live_price}")

    return issues

# Main function
import smtplib
from email.mime.text import MIMEText

def send_email_report(subject, body, to_email):
    from_email = "ernestwaitams@gmail.com"
    app_password = "gzyr vnkv vdgq ulcz"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(from_email, app_password)
            server.send_message(msg)
        print("✅ Email sent successfully.")
    except Exception as e:
        print(f"❌ Email failed: {e}")
        
from datetime import datetime
import os

def save_log(issues):
    today = datetime.now().strftime("%Y-%m-%d")
    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)
    filename = os.path.join(log_folder, f"report_{today}.txt")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("POS Update Check Report\n")
        f.write(f"Date: {today}\n\n")
        if issues:
            for issue in issues:
                f.write(issue + "\n")
        else:
            f.write("✅ All menu items validated successfully.\n")

    print(f"📁 Log saved to {filename}")
def main():
    expected_menu = load_menu('expected_menu.json')
    live_menu = load_menu('live_menu.json')
    
    print("\n🔍 Checking POS Menu...")
    issues = compare_menus(expected_menu, live_menu)
    save_log(issues)
   

    print("\n📋 Report:")
    if issues:
        for issue in issues:
            print(issue)
    else:
        print("✅ All items are correct!")
    if issues:
        report = "\n".join(issues)
        send_email_report("⚠️ POS Error Report", report, "ochrisernest@gmail.com")

if __name__ == '__main__':
    main()
