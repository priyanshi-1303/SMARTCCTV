import tkinter as tk
import tkinter.font as font
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from PIL import Image, ImageTk
from find_motion import find_motion
from identify import maincall

import os

# Ensure that the 'record' and 'visitors' directories exist
if not os.path.exists('record'):
    os.makedirs('record')

if not os.path.exists('visitors'):
    os.makedirs('visitors')

try:
    window = tk.Tk()
    window.title("Smart CCTV")
    window.iconphoto(False, tk.PhotoImage(file=r"C:\Users\DELL\Desktop\SmartCCTV\smart-cctv-ver2.0-main\mn.png"))
    window.geometry('1080x700')

    frame1 = tk.Frame(window)

    label_title = tk.Label(frame1, text="Smart CCTV Camera")
    label_font = font.Font(size=35, weight='bold', family='Helvetica')
    label_title['font'] = label_font
    label_title.grid(pady=(10, 10), column=2)

    icon = Image.open(r"C:\Users\DELL\Desktop\SmartCCTV\smart-cctv-ver2.0-main\icons\spy.png")
    icon = icon.resize((150, 150), Image.Resampling.LANCZOS)
    icon = ImageTk.PhotoImage(icon)
    label_icon = tk.Label(frame1, image=icon)
    label_icon.grid(row=1, pady=(5, 10), column=2)

    btn1_image = Image.open(r"C:\Users\DELL\Desktop\SmartCCTV\smart-cctv-ver2.0-main\icons\lamp.png")
    btn1_image = btn1_image.resize((50, 50), Image.Resampling.LANCZOS)
    btn1_image = ImageTk.PhotoImage(btn1_image)

    btn2_image = Image.open(r"C:\Users\DELL\Desktop\SmartCCTV\smart-cctv-ver2.0-main\icons\rectangle-of-cutted-line-geometrical-shape.png")
    btn2_image = btn2_image.resize((50, 50), Image.Resampling.LANCZOS)
    btn2_image = ImageTk.PhotoImage(btn2_image)

    btn5_image = Image.open(r"C:\Users\DELL\Desktop\SmartCCTV\smart-cctv-ver2.0-main\icons\exit.png")
    btn5_image = btn5_image.resize((50, 50), Image.Resampling.LANCZOS)
    btn5_image = ImageTk.PhotoImage(btn5_image)

    btn3_image = Image.open(r"C:\Users\DELL\Desktop\SmartCCTV\smart-cctv-ver2.0-main\icons\security-camera.png")
    btn3_image = btn3_image.resize((50, 50), Image.Resampling.LANCZOS)
    btn3_image = ImageTk.PhotoImage(btn3_image)

    btn6_image = Image.open(r"C:\Users\DELL\Desktop\SmartCCTV\smart-cctv-ver2.0-main\icons\incognito.png")
    btn6_image = btn6_image.resize((50, 50), Image.Resampling.LANCZOS)
    btn6_image = ImageTk.PhotoImage(btn6_image)

    btn4_image = Image.open(r"C:\Users\DELL\Desktop\SmartCCTV\smart-cctv-ver2.0-main\icons\recording.png")
    btn4_image = btn4_image.resize((50, 50), Image.Resampling.LANCZOS)
    btn4_image = ImageTk.PhotoImage(btn4_image)

    btn7_image = Image.open(r"C:\Users\DELL\Desktop\SmartCCTV\smart-cctv-ver2.0-main\icons\rec.png")
    btn7_image = btn7_image.resize((50, 50), Image.Resampling.LANCZOS)
    btn7_image = ImageTk.PhotoImage(btn7_image)

    # --------------- Button -------------------#
    btn_font = font.Font(size=25)

    def safe_callback(callback):
        try:
            callback()
        except Exception as e:
            print(f"Error in callback: {e}")

    btn1 = tk.Button(frame1, text='Monitor', height=90, width=180, fg='green', command=lambda: safe_callback(find_motion), image=btn1_image, compound='left')
    btn1['font'] = btn_font
    btn1.grid(row=3, pady=(20, 10))

    btn2 = tk.Button(frame1, text='Rectangle', height=90, width=180, fg='orange', command=lambda: safe_callback(rect_noise), compound='left', image=btn2_image)
    btn2['font'] = btn_font
    btn2.grid(row=3, pady=(20, 10), column=3, padx=(20, 5))

    btn3 = tk.Button(frame1, text='Noise', height=90, width=180, fg='green', command=lambda: safe_callback(noise), image=btn3_image, compound='left')
    btn3['font'] = btn_font
    btn3.grid(row=5, pady=(20, 10))

    btn4 = tk.Button(frame1, text='Record', height=90, width=180, fg='orange', command=lambda: safe_callback(record), image=btn4_image, compound='left')
    btn4['font'] = btn_font
    btn4.grid(row=5, pady=(20, 10), column=3)

    btn6 = tk.Button(frame1, text='In Out', height=90, width=180, fg='green', command=lambda: safe_callback(in_out), image=btn6_image, compound='left')
    btn6['font'] = btn_font
    btn6.grid(row=5, pady=(20, 10), column=2)

    btn5 = tk.Button(frame1, height=90, width=180, fg='red', command=window.quit, image=btn5_image)
    btn5['font'] = btn_font
    btn5.grid(row=6, pady=(20, 10), column=2)

    btn7 = tk.Button(frame1, text="Identify", fg="orange", command=lambda: safe_callback(maincall), compound='left', image=btn7_image, height=90, width=180)
    btn7['font'] = btn_font
    btn7.grid(row=3, column=2, pady=(20, 10))

except Exception as e:
    print(f"Error occurred: {e}")

frame1.pack()
window.mainloop()