# pyGiftSender 🎁

A simple Python automation script to send personalized WhatsApp messages with e-gift card codes and images — directly from an Excel file.

Perfect for festive giveaways, client appreciation messages, or any personalized WhatsApp outreach.

---

## ✨ Features
- Reads client data from all sheets in an Excel workbook (`clients.xlsx`)
- Sends personalized WhatsApp messages with:
  - Recipient name
  - Gift card code
  - Validity date
  - Custom image (e.g., a Diwali greeting)
- Automatically delays between messages to prevent spam detection
- Error handling for invalid phone numbers or send failures

---

## 📂 Example Excel Format (`clients.xlsx`)
| Customer Name | Phone       | Gift Card Code | Validity   |
|----------------|-------------|----------------|-------------|
| Rohan Mehta    | 919812345678 | ABCD-1234-EFGH | 31-Dec-2025 |
| Priya Sharma   | 918765432109 | XYZA-5678-LMNQ | 30-Nov-2025 |

Each sheet can represent a different group (e.g., ₹750 / ₹1000 / ₹1500 cards).

---

## ⚙️ Requirements
Install the dependencies:
```bash
pip install pandas pywhatkit
```

## 🚀 Usage
- Make sure WhatsApp Web is logged in on your default browser.
- Place your Excel file (clients.xlsx) and image (Chem.png) in the same directory.
- Run the script:
```bash
python pyGiftSender.py
```
- The script will automatically send messages sheet by sheet.

## 🧠 How It Works
- Uses pandas to read all sheets in Excel.
- Iterates over each client and generates a personalized message.
- Uses pywhatkit to send a WhatsApp message + image to each number.
- Adds a short delay to prevent WhatsApp rate limits.

