
---

## 🖥️ Source Code: `qr_gui.py`
```python
import qrcode
from tkinter import Tk, Label, Entry, Button, messagebox, filedialog
from PIL import Image, ImageTk
import os

# Function to generate QR and display + save

def generate_qr():
    data = entry.get().strip()
    if not data:
        messagebox.showerror("Error", "Please enter a valid URL or text")
        return

    # Generate QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Preview
    img_preview = img.copy()
    img_preview.thumbnail((250, 250))
    img_tk = ImageTk.PhotoImage(img_preview)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

    # Save to Downloads
    downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    if not os.path.exists(downloads):
        os.makedirs(downloads)
    save_path = filedialog.asksaveasfilename(
        initialdir=downloads,
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")],
        title="Save QR Code"
    )
    if save_path:
        img.save(save_path)
        messagebox.showinfo("Saved", f"QR code saved as:\n{save_path}")

# Setup GUI
root = Tk()
root.title("Quick QR")
root.iconbitmap('icon.ico')

Label(root, text="Enter text or URL:").pack(pady=5)
entry = Entry(root, width=40)
entry.pack(pady=5)

Button(root, text="Generate QR", command=generate_qr).pack(pady=10)
qr_label = Label(root)
qr_label.pack(pady=10)

root.mainloop()
