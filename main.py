import moviepy
import threading
import tkinter as tk
from tkinter import messagebox, filedialog, ttk

def convert_video_to_mp3():
    vid_path = filedialog.askopenfilename(
        title="Select a Video File",
        filetypes=[("Video files", "*.mp4 *.mkv *.avi *.mov *.flv")]
    )
    if not vid_path:
        return  # User cancelled

    progress_bar['value'] = 0
    progress_bar.pack(pady=15)
    convert_button.config(state='disabled')

    def conversion_thread():
        try:
            video = moviepy.VideoFileClip(vid_path)
            audio = video.audio

            output_path = vid_path.rsplit('.', 1)[0] + "_audio.mp3"

            audio.write_audiofile(output_path)

            progress_bar['value'] = 100

            messagebox.showinfo("Success", f"Audio saved as:\n{output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")
        finally:
            convert_button.config(state='normal')
            progress_bar.pack_forget()

    threading.Thread(target=conversion_thread).start()

app = tk.Tk()
app.title("Video to MP3 Converter")
app.geometry("450x250")
app.configure(bg="#1e1e2f")
app.resizable(False, False)

font_title = ("Segoe UI", 14, "bold")
font_button = ("Segoe UI", 12, "bold")

label = tk.Label(app, text="Select a video file to convert into MP3", font=font_title, bg="#1e1e2f", fg="#f0f0f5")
label.pack(pady=(30, 20))

convert_button = tk.Button(app, text="Choose Video & Convert", command=convert_video_to_mp3,
                           font=font_button, bg="#007acc", fg="white", activebackground="#005f99",
                           activeforeground="white", relief="flat", padx=20, pady=10, cursor="hand2")
convert_button.pack()

progress_bar = ttk.Progressbar(app, orient='horizontal', length=300, mode='determinate')

app.mainloop()
