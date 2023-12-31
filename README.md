# ABC Notion Music

## Project Overview

This Python-based music project allows users to manipulate and customize music using various features. Users can select waveforms, adjust loudness, specify an ABC file path, change speed (BPM), shift pitch, add background noise, mix with an external WAV file, play the configured music, save it as a WAV file, and exit the program.

## Features

1. **Selecting a waveform**
   - Users can choose between sine, square, sawtooth, and triangle waveforms for the music.
2. **Setting the loudness**
   - Adjust the loudness or volume of the music to the desired level.
3. **Indicating the ABC file path**
   - Specify the path of the ABC file containing music notation.
4. **Changing speed (BPM)**
   - Modify the speed of the music in beats per minute (BPM) to control the tempo.
5. **Shifting pitch**
   - Shift all notes to a higher or lower pitch. Users can choose between Hertz or semitone-based pitch shifting.
6. **Adding background noise**
   - Introduce background noise (white, pink, or brown) to enhance the audio experience.
7. **Mixing within an external WAV file**
   - Select an external WAV file to mix with the ABC file during playback.
8. **Playing the file**
   - Play the configured music according to the specified settings.
9. **Saving the music as a WAV file**
   - Save the customized music as a WAV file in the "OutputFiles" directory.
10. **Exit**
    - Close the program and exit the system.

## Environment Setup

- **Operating System:** Windows 10
- **IDE:** PyCharm Community Edition 2022
- **Python Version:** 3.10.8
- **FFmpeg Version:** N-108711-g3141dbb7ad-20221018 ([FFmpeg GitHub](https://github.com/kkroening/ffmpeg-python))

## Getting Started

1. Navigate to the project entry point: `MainMenu.py`.
2. Run the program in your chosen Python environment.

## Usage

1. Follow menus 1-7 to configure the music settings.
2. Play the configured music using menu option 8.
3. Save the customized music as a WAV file with menu option 9. The saved file is in the "OutputFiles" directory.
4. Choose menu option 10 to exit the system.

## Default Configurations

The system comes with default configurations. Upon entering the program, selecting menu option 8 will play the audio under these default settings.

## Notes on ABC Notations

- **Header Options:** X, T, K, C, M, Q
- **Body Features:** Lowercase letter, Uppercase letter, comma, apostrophe, number, slash (/), rest, and bar lines
- **ADSR:** Consider Attack, Decay, Sustain, and Release when generating (playing) notes.



Feel free to explore and customize the music using the provided options!