import tkinter as tk
from tkinter import ttk
import requests
import json
from playsound import playsound

def search_word():
    """Search for a word definition in the API and update the display"""
    global word_entry, result_text  # Declare global variables
    word = word_entry.get()
    if not word.strip():
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Please enter a word to search.")
        return

    url = f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}"
    try:
        response = requests.get(url, timeout=10)  # Set a timeout for the request
        if response.status_code == 200:
            try:
                data = json.loads(response.content)
                if data:
                    result_text.delete("1.0", tk.END)
                    definition = data[0]["meanings"][0]["definitions"][0]["definition"]
                    result_text.insert(tk.END, f"Definition of '{word}':\n{definition}")
                    # Play the audio if available
                    audio_url = data[0]["phonetics"][0].get("audio", "")
                    if audio_url:
                        playsound(audio_url)
                    else:
                        result_text.insert(tk.END, "\n\nAudio not available.")
                else:
                    result_text.delete("1.0", tk.END)
                    result_text.insert(tk.END, "Word not found.")
            except (KeyError, IndexError):
                result_text.delete("1.0", tk.END)
                result_text.insert(tk.END, "Unexpected data format from API.")
        else:
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, f"Error: Unable to find the word. HTTP Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Error: Could not connect to API. ({str(e)})")

def main():
    global word_entry, result_text  # Declare global variables
    root = tk.Tk()
    root.title("Audio Dictionary")
    root.geometry("400x300")

    # Add a branding title with blue color
    title = tk.Label(root, text="Audio Dictionary", fg="white", bg="#3E6BEC", font=("Helvetica", 16))
    title.pack(fill="x")

    # Define the input field and search button
    word_label = ttk.Label(root, text="Enter word:")
    word_label.pack(pady=5)
    word_entry = ttk.Entry(root)
    word_entry.pack(pady=5)

    search_button = ttk.Button(root, text="Search", command=search_word)
    search_button.pack(pady=5)

    # Define the output field
    result_label = ttk.Label(root, text="Definition:")
    result_label.pack(pady=5)
    result_text = tk.Text(root, height=8, wrap="word")
    result_text.pack(pady=5)

    root.mainloop()

if __name__ == '__main__':
    main()
