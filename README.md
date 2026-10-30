Python Voice Recorder
A simple desktop voice recorder built with Python and Tkinter. It lets you record audio from your microphone, save it as a WAV file, and play back your latest recording all from a small, easy-to-use interface.
Features
- Start Recording capture audio from your microphone.
- Stop and Save stop recording and automatically save the audio.
- Play Recording listen to your most recent recording.
- Status updates  see when the app is ready, recording, saving, or playing audio.
- Automatic filenames recordings are timestamped to avoid overwriting earlier files.
Built With
- Python — application logic
- Tkinter — desktop interface
- sounddevice — audio recording and playback
- soundfile — reading and writing WAV files
- NumPy — combining recorded audio chunks
Installation
You'll need Python installed and a working microphone.
1. Clone the repository:
   git clone https://github.com/Orfeo03/VoiceRecorder.git
   cd VoiceRecorder
2. Create and activate a virtual environment (Windows CMD):
   python -m venv .venv
   .venv\Scripts\activate
3. Install the dependencies:
   pip install numpy sounddevice soundfile
4. Start the app:
   python VoiceRecorder.py
How to Use
1. Click Start Recording and speak into your microphone.
2. Click Stop & Save when you're finished.
3. Click Play Recording to listen to the recording you just made.
Audio files are saved automatically in the recordings/ folder with names like recording_20261030_143015.wav.

 The Play Recording button plays the latest recording made during the current session. Older recordings remain saved in the folder, but the app doesn't currently include a file browser for choosing them.
Project Structure
VoiceRecorder/
   VoiceRecorder.py      Main application
  .gitignore            Files excluded from Git
   README.md             Project documentation
  recordings/           Created automatically: audio files saved here

 Audio is recorded in mono at 44,100 Hz.
 The recordings folder and audio files are ignored by Git, so your personal recordings won't be included when you push code to GitHub.
 Make sure your operating system allows Python to access your microphone.
