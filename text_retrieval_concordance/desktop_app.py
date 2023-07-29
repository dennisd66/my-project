import tkinter as Tk
from TextFileParser import TextFileParser, initialize_database
import text_processing

def search_callback():
    search_string = entry.get()
    results = text_processing.search_words_in_db(search_string, db_path)
    listbox.delete(0, Tk.END)
    for result in results:
        listbox.insert(Tk.END, f"{result.word} - Position: {result.idx} - Metadata: {result.metadata}")

db_path = initialize_database()
file_parser = TextFileParser(db_path)

root = Tk.Tk()
root.title("Text Analysis and Search")

frame = Tk.Frame(root)
frame.pack(pady=10)

entry = Tk.Entry(frame)
entry.pack(side=Tk.LEFT, padx=(0, 10))

search_button = Tk.Button(frame, text="Search", command=search_callback)
search_button.pack(side=Tk.RIGHT)

scrollbar = Tk.Scrollbar(root)
scrollbar.pack(side=Tk.RIGHT, fill=Tk.Y)

listbox = Tk.Listbox(root, yscrollcommand=scrollbar.set)
listbox.pack(side=Tk.LEFT, fill=Tk.BOTH)

scrollbar.config(command=listbox.yview)

root.mainloop()