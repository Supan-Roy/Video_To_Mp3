import moviepy

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def convert_video_to_mp3():
    vid_path = filedialog.askopenfilename(
        title="Select a Video File",
        filetypes=[("Video files", "*.mp4 *.mkv *.avi *.mov *.flv")]
    )

    if not vid_path:
        return  # User cancelled

    try:
        video = moviepy.VideoFileClip(vid_path)
        audio = video.audio

        output_path = vid_path.rsplit('.', 1)[0] + "_audio.mp3"
        audio.write_audiofile(output_path)

        messagebox.showinfo("Success", f"Audio saved as:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")

# GUI setup
app = tk.Tk()
app.title("Video to MP3 Converter")
app.geometry("450x220")
app.configure(bg="#1e1e2f")  # Dark background for modern feel
app.resizable(False, False)

# Fonts and colors
font_title = ("Segoe UI", 14, "bold")
font_button = ("Segoe UI", 12, "bold")
font_label = ("Segoe UI", 11)

# Title Label
label = tk.Label(
    app,
    text="Select a video file to convert into MP3",
    font=font_title,
    bg="#1e1e2f",
    fg="#f0f0f5"
)
label.pack(pady=(30, 20))

# Convert Button with hover effect
def on_enter(e):
    convert_button['background'] = '#005f99'

def on_leave(e):
    convert_button['background'] = '#007acc'

convert_button = tk.Button(
    app,
    text="Choose Video To Convert",
    command=convert_video_to_mp3,
    font=font_button,
    bg="#007acc",
    fg="white",
    activebackground="#005f99",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2"
)
convert_button.pack()

convert_button.bind("<Enter>", on_enter)
convert_button.bind("<Leave>", on_leave)

# Footer Label
footer = tk.Label(
    app,
    text="Made by Supan Roy",
    font=("Segoe UI", 9, "italic"),
    bg="#1e1e2f",
    fg="#a0a0b0"
)
footer.pack(side="bottom", pady=15)

app.mainloop()
