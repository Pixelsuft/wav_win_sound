from setuptools import setup as setuptools_setup
from setuptools import find_packages as setuptools_find_packages


long_description = '''# WAV Windows Sound
Play WAV Sounds (Windows ONLY!)<br />
![Lol](https://github.com/Pixelsuft/Loxa-bot/raw/main/bot_small.png?raw=true)
# Changelog
Fixed playing after closing<br />
Now async_play() function using threading<br />
Old async_play function is old_aync_play()
# Installation
```
python -m pip install wav-win-sound
```
# Example
```
from wav_win_sound import Mixer as wav_mixer

mixer = wav_mixer()

mixer.load("track1.wav")
mixer.sync_play()

mixer.load(["track1.wav", "track2.wav"])
mixer.async_play()

mixer.stop()
```
# Bugs
You must has internet before start first playing after installation<br />
(I can't pack wav player to a package, before first playing it will be downloaded!)
'''

setuptools_setup(
    name="wav_win_sound",
    version = "1.0.7",
    author = "Pixelsuft",
    description = "Play WAV Sounds (Windows ONLY!)",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Pixelsuft/wav_win_sound/",
    packages = setuptools_find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    python_requires='>=3.5',
    license='MIT', 
    keywords='wav_win_sound',
    install_requires=['parse_args', 'urllib3'],
    py_modules=['wav_win_sound']
)