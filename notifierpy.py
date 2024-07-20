import time
from tkinter import *
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
import threading

# Initialize the main window
t = Tk()
t.title('Notifier')
t.geometry("500x300")
t.resizable(0, 0)

# Load and display the image
try:
    img = Image.open("notify-label.png")
    tkimage = ImageTk.PhotoImage(img)
    img_label = Label(t, image=tkimage).grid(row=0, column=0, columnspan=2)
except Exception as e:
    messagebox.showerror("Error", f"Image loading error: {e}")

# Function to handle the notification setting and display
def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()
    
    if not get_title or not get_msg or not get_time:
        messagebox.showerror("Alert", "All fields are required!")
    else:
        try:
            int_time = int(float(get_time))
            min_to_sec = int_time * 60
            messagebox.showinfo("Notifier Set", "Notification has been set!")
            
            # Use threading to avoid blocking the main thread
            threading.Thread(target=notify, args=(get_title, get_msg, min_to_sec)).start()
        except ValueError:
            messagebox.showerror("Alert", "Please enter a valid time!")

# Function to handle the notification after the specified time
def notify(title, message, delay):
    time.sleep(delay)
    notification.notify(
        title=title,
        message=message,
        app_name="Notifier",
        app_icon="ico.ico",
        toast=True,
        timeout=10
    )

# Label - Title
t_label = Label(t, text="Title to Notify", font=("poppins", 10))
t_label.place(x=12, y=70)

# Entry - Title
title = Entry(t, width=25, font=("poppins", 13))
title.place(x=123, y=70)

# Label - Message
m_label = Label(t, text="Display Message", font=("poppins", 10))
m_label.place(x=12, y=120)

# Entry - Message
msg = Entry(t, width=40, font=("poppins", 13))
msg.place(x=123, height=30, y=120)

# Label - Time
time_label = Label(t, text="Set Time", font=("poppins", 10))
time_label.place(x=12, y=175)

# Entry - Time
time1 = Entry(t, width=5, font=("poppins", 13))
time1.place(x=123, y=175)

# Label - min
time_min_label = Label(t, text="min", font=("poppins", 10))
time_min_label.place(x=175, y=180)

# Button
but = Button(t, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20, relief="raised", command=get_details)
but.place(x=170, y=230)

t.mainloop()
