import webbrowser as wb
import os

def workauto():
    # Open Microsoft Word
    codepath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
    os.startfile(codepath)

    # URLs to open in the default web browser
    URLS = [
        "https://chatgpt.com/g/g-kZ0eYXlJe-scholar-gpt",
        "https://app.grammarly.com/ddocs/2679736083",
        "https://scholar.google.com/"
    ]

    # Open each URL
    for url in URLS:
        wb.open(url)

# Execute the function
workauto()
