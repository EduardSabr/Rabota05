import tkinter as tk
from tkinter import messagebox

def a(text, shift):
    a_text = ""
    for c in text:
        if c.isalpha():
            if c.isupper():
                a_text += chr((ord(c) - ord('А') + shift) % 33 + ord('А'))
#учитывает 32 буквы вместо 33, Ё нет
            else:
                a_text += chr((ord(c) - ord('а') + shift) % 33 + ord('а'))
#учитывает 32 буквы вместо 33, Ё нет
        else:
            a_text += c
    return a_text

def b(text, shift):
    b_text = ""
    for c in text:
        if c.isalpha():
            if c.isupper():
                b_text += chr((ord(c) - ord('А') - shift) % 33 + ord('А'))
#учитывает 32 буквы вместо 33, Ё нет
            else:
                b_text += chr((ord(c) - ord('а') - shift) % 33 + ord('а'))
#учитывает 32 буквы вместо 33, Ё нет
        else:
            b_text += c
    return b_text

def click_a():
    text = entry.get("1.0", "end-1c")
    shift = int(shift_entry.get())
    a_text = a(text, shift)
    messagebox.showinfo("Шифрование", f"Зашифрованный текст:\n\n{a_text}")

def click_b():
    text = entry.get("1.0", "end-1c")
    shift = int(shift_entry.get())
    b_text = b(text, shift)
    messagebox.showinfo("Расшифровка", f"Расшифрованный текст:\n\n{b_text}")

root = tk.Tk()
root.title("Шифр Цезаря")
root.geometry("300x300")

label = tk.Label(root, text="Введите текст:")
label.pack()

entry = tk.Text(root, height=10, width=40)
entry.pack()

shift_label = tk.Label(root, text="Введите шаг сдвига:")
shift_label.pack()

shift_entry = tk.Entry(root)
shift_entry.pack()

encrypt_button = tk.Button(root, text="Зашифровать", command=click_a)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Расшифровать", command=click_b)
decrypt_button.pack()

root.mainloop()
