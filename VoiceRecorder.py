
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
from datetime import datetime

import numpy as np
import sounddevice as sd
import soundfile as sf

# Settings
SAMPLE_RATE = 44100
RECORDINGS_FOLDER = Path("recordings")
RECORDINGS_FOLDER.mkdir(exist_ok=True)

audio_chunks = []
recording = False
stream = None
last_file = None


def audio_callback(indata, frames, time, status):
    if status:
        print(status)
    audio_chunks.append(indata.copy())


def start_recording():
    global recording, stream, audio_chunks

    if recording:
        return

    sd.stop()
    audio_chunks = []

    try:
        stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=1,
            callback=audio_callback
        )
        stream.start()
        recording = True
        status_label.config(text="Recording...", fg="red")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def stop_recording():
    global recording, stream, last_file

    if not recording:
        return

    stream.stop()
    stream.close()
    stream = None
    recording = False

    if not audio_chunks:
        status_label.config(text="No audio recorded")
        return

    audio = np.concatenate(audio_chunks, axis=0)

    filename = datetime.now().strftime("recording_%Y%m%d_%H%M%S.wav")
    last_file = RECORDINGS_FOLDER / filename

    sf.write(last_file, audio, SAMPLE_RATE)

    status_label.config(text=f"Saved: {filename}", fg="green")


def play_recording():
    if recording:
        messagebox.showinfo("Info", "Stop recording first.")
        return

    if last_file is None:
        messagebox.showinfo("Info", "Record something first.")
        return

    try:
        audio, sample_rate = sf.read(last_file)
        sd.stop()
        sd.play(audio, sample_rate)
        status_label.config(text="Playing recording...", fg="blue")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def close_app():
    global stream

    if stream is not None:
        stream.stop()
        stream.close()

    sd.stop()
    window.destroy()


# Create the application
window = tk.Tk()
window.title("Python Voice Recorder")
window.geometry("400x300")
window.resizable(False, False)

title_label = tk.Label(
    window,
    text="Voice Recorder",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=20)

status_label = tk.Label(
    window,
    text="Ready to record",
    font=("Arial", 12)
)
status_label.pack(pady=10)

record_button = tk.Button(
    window,
    text="Start Recording",
    command=start_recording,
    width=20,
    bg="lightgreen"
)
record_button.pack(pady=5)

stop_button = tk.Button(
    window,
    text="Stop & Save",
    command=stop_recording,
    width=20,
    bg="tomato"
)
stop_button.pack(pady=5)

play_button = tk.Button(
    window,
    text="Play Recording",
    command=play_recording,
    width=20,
    bg="lightblue"
)
play_button.pack(pady=5)

window.protocol("WM_DELETE_WINDOW", close_app)
window.mainloop()
