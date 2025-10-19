import pandas as pd
import pywhatkit as kit
import time

# Read all sheets from Excel file
file_path = "clients.xlsx"
sheets = pd.read_excel(file_path, sheet_name=None)

# Single image to send
image_path = r"Chem.png"

print("\n📱 Make sure WhatsApp Web is logged in before running this script.\n")

for sheet_name, data in sheets.items():
    print(f"\n🧾 Processing sheet: {sheet_name}")
    
    for i, row in data.iterrows():
        customer_name = row.get('Customer Name', 'Client')
        phone = str(row.get('Phone', ''))
        code = row.get('Gift Card Code', 'N/A')
        validity = row.get('Validity', 'N/A')

        if not phone or len(phone) < 10:
            print(f"⚠️ Skipping {customer_name} — invalid phone number")
            continue

        message = f"""
🎁 Hello Sir,

🔑 Here is your Amazon Gift Card Code: *{code}*
Valid till: {validity}

Wishing you happiness, success, and good fortune this Diwali! 🌟
"""

        print(f"📨 Sending to {customer_name} ({phone}) from sheet '{sheet_name}'...")

        try:
            # Send text + image together
            kit.sendwhats_image(f"+{phone}", image_path, caption=message, wait_time=15, tab_close=True)
            time.sleep(10)  # delay to avoid spam detection

            print(f"✅ Successfully sent to {customer_name}\n")
        except Exception as e:
            print(f"❌ Could not send to {customer_name}: {e}\n")

print("\n🎉 All vouchers from all sheets processed successfully!")
