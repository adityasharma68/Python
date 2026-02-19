import pandas as pd
import requests #requests -> library internet se data lene ke liye use hoti hai
from io import StringIO #ek tool hai jo string ko file jaisa bana deta hai and this imp bcz pd.read_html() directly string ko accept nahi karta properly, Usko file-like object chahiye

url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"


headers = { 
    "User-Agent": "Mozilla/5.0"
} 
""" Website ko lagta hai:
Agar request browser se aayi → allow
Agar bot se aayi → block (403 error)
So hum bol rahe hain:
"Hi Wikipedia 👋 main Chrome browser hoon"
Isliye 403 error solve ho gaya. """



response = requests.get(url, headers=headers)

html_data = StringIO(response.text)

tables = pd.read_html(html_data)

print("Number of tables:", len(tables))
print(tables[0].head())


#PART 2 Lec13

# XML Files : XML (eXtensible Markup Language) is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable. It is commonly used for storing and transporting data.

