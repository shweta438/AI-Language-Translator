from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyperclip
import pyttsx3

# ---------------- Initialize Voice Engine ----------------
engine = pyttsx3.init()
engine.setProperty("rate", 150)

# ---------------- Functions ----------------

def translate():
    try:
        text = input_text.get("1.0", END).strip()

        if text == "":
            messagebox.showwarning("Warning", "Please enter some text!")
            return

        source = source_lang.get()
        target = target_lang.get()

        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))


def clear():
    input_text.delete("1.0", END)
    output_text.delete("1.0", END)


def copy_text():
    text = output_text.get("1.0", END).strip()

    if text:
        pyperclip.copy(text)
        messagebox.showinfo("Copied", "Text copied successfully!")
    else:
        messagebox.showwarning("Warning", "Nothing to copy!")


def speak():
    text = output_text.get("1.0", END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Nothing to speak!")
        return

    engine.say(text)
    engine.runAndWait()


def swap_languages():
    source = source_lang.get()
    target = target_lang.get()

    source_lang.set(target)
    target_lang.set(source)


# ---------------- Window ----------------

root = Tk()
root.title("🌍 AI Language Translator")
root.geometry("850x700")
root.configure(bg="#EAF7F6")
root.resizable(False, False)

# ---------------- Heading ----------------

Label(
    root,
    text="🌍 AI Language Translator",
    font=("Arial", 26, "bold"),
    bg="#EAF7F6",
    fg="#007ACC"
).pack(pady=15)

# ---------------- Input ----------------

Label(
    root,
    text="Enter Text",
    font=("Arial", 15, "bold"),
    bg="#EAF7F6"
).pack()

input_text = Text(
    root,
    height=7,
    width=75,
    font=("Arial", 12)
)
input_text.pack(pady=10)
# ---------------- Language Selection ----------------

frame = Frame(root, bg="#EAF7F6")
frame.pack(pady=10)

Label(
    frame,
    text="From Language",
    font=("Arial",12,"bold"),
    bg="#EAF7F6"
).grid(row=0,column=0,padx=30)

Label(
    frame,
    text="To Language",
    font=("Arial",12,"bold"),
    bg="#EAF7F6"
).grid(row=0,column=1,padx=30)

# 100+ Supported Languages
languages = sorted(GoogleTranslator().get_supported_languages())

source_lang = ttk.Combobox(
    frame,
    values=languages,
    state="readonly",
    width=30,
    font=("Arial",11)
)
source_lang.set("english")
source_lang.grid(row=1,column=0,padx=20,pady=10)

target_lang = ttk.Combobox(
    frame,
    values=languages,
    state="readonly",
    width=30,
    font=("Arial",11)
)
target_lang.set("hindi")
target_lang.grid(row=1,column=1,padx=20,pady=10)

# ---------------- Buttons ----------------

button_frame = Frame(root, bg="#EAF7F6")
button_frame.pack(pady=20)

Button(
    button_frame,
    text="🌍 Translate",
    command=translate,
    bg="#007ACC",
    fg="white",
    font=("Arial",12,"bold"),
    width=14
).grid(row=0,column=0,padx=8)

Button(
    button_frame,
    text="📋 Copy",
    command=copy_text,
    bg="#28A745",
    fg="white",
    font=("Arial",12,"bold"),
    width=12
).grid(row=0,column=1,padx=8)

Button(
    button_frame,
    text="🗑 Clear",
    command=clear,
    bg="#DC3545",
    fg="white",
    font=("Arial",12,"bold"),
    width=12
).grid(row=0,column=2,padx=8)

Button(
    button_frame,
    text="🔄 Swap",
    command=swap_languages,
    bg="#F39C12",
    fg="white",
    font=("Arial",12,"bold"),
    width=12
).grid(row=0,column=3,padx=8)

Button(
    button_frame,
    text="🔊 Speak",
    command=speak,
    bg="#8E44AD",
    fg="white",
    font=("Arial",12,"bold"),
    width=12
).grid(row=0,column=4,padx=8)
# ---------------- Output ----------------

Label(
    root,
    text="Translated Text",
    font=("Arial", 15, "bold"),
    bg="#EAF7F6"
).pack()

output_text = Text(
    root,
    height=8,
    width=75,
    font=("Arial", 12)
)
output_text.pack(pady=10)

# ---------------- Footer ----------------

Label(
    root,
    text="Developed by Shweta Ray | CodeAlpha AI Internship Project",
    font=("Arial", 10, "italic"),
    bg="#EAF7F6",
    fg="gray"
).pack(side=BOTTOM, pady=15)

# ---------------- Run Application ----------------

root.mainloop()