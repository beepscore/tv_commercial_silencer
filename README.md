# Purpose
Listen to television audio, detect commercials, request decrease volume.

# Results

## install Dejavu

    conda activate remy_python
    pip install -e git+https://github.com/bcollazo/dejavu@v1.2#egg=PyDejavu

This installed directory src/pydejavu.
I didn't delete file added by pip: src/pip-delete-this-directory.txt
See also Appendix- Install dejavu dependencies.

## Activate conda environment
If using Anaconda.

    conda activate <my_environment>
    conda activate remy_python

## Install audio files

### convert wav to mp3

    ffmpeg -i a.wav -f mp3 a.mp3

### put audio mp3 files in directory data/commercials_mp3

## Select live audio input source
Selecting live audio input from an audio interface instead of from microphone gives a cleaner signal without room noise.
If using macOS and an audio interface, go to System Preferences / Sound / Input.
Select the interface e.g. Scarlett 2i4 USB.
Note I haven't tried running Dejavu on Raspberry Pi Raspbian yet, and haven't selected an audio input source.

## ./test_dejavu.sh
Optional step. Running test_dejavu.sh makes a temporary sqlite file

    $ chmod u+x ./test_dejavu.sh
    $ ./test_dejavu.sh

## database
check sqlite schema

#### create database (how to set up schema?)

#### set environment variable for database

---
To run test

    ./test_dejavu.sh

This populates results directory including test.db
Ok to delete contents of results directory.

## data/config.json
may contain a json dictionary e.g.

    {"DATABASE_URL": "results/test.db"}

Ways to run:
Can run recognize_audio.py
If no database exists it will make a new one, I think in-memory sqlite.

    conda activate <environment>
    python3 recognize_audio.py

## example output

    2019-04-21 18:42:17 DEBUG    recognize_audio_from_a_file line:49
    filename_containing_audio_to_match: data/commercial_mp3/chantix.mp3,
    match_dict_json: {"song_id": 14, "song_name": "chantix", "confidence": 43335,
    "offset": 0, "offset_seconds": 0.0, "file_sha1": "a4fcabb2afb6518a65321c5807c5fc7c798a0aa2",
    "match_time": 11.153626918792725}

    2019-04-21 18:42:48 DEBUG    recognize_audio_from_microphone line:80
    From mic with 5 seconds we recognized: {"song_id": 19,
    "song_name": "tecovas-western-boots", "confidence": 179, "offset": 62,
    "offset_seconds": 2.87927, "file_sha1": "ca324b141675b59c05bdcbbdf05c038d68940376"}

### Appendix- Install dejavu dependencies
I installed many of these as conda packages in environment remy_python.
I don't know if installing dejavu from pip would handle this automatically.
https://github.com/worldveil/dejavu/blob/master/INSTALLATION.md

#### ffmpeg
for converting audio files to .wav format
on macOS

    brew install ffmpeg

#### matplotlib
used for spectrograms and plotting

#### MySQLdb
for interfacing with MySQL databases

#### numpy
for taking the FFT of audio signals

#### pydub
a Python ffmpeg wrapper

#### scipy
used in peak finding algorithms

#### pyaudio
for grabbing audio from microphone

#### sqlalchemy

#### sqlalchemy_utils
https://sqlalchemy-utils.readthedocs.io/en/latest/installation.html

##### package name contains dash
    sqlalchemy-utils

##### import name contains underscore
import sqlalchemy_utils

# References

## Dejavu project
Audio fingerprinting and recognition in Python.
It has recognizers for recorded files and for live microphone input.
Originally by worldveil/dejavu, forked by DataWookie/dejavu and <a href="https://github.com/bcollazo/dejavu">bcollazo/dejavu.</a>
In 2019-03 bcollazo/dejavu appeared to be the most active fork.

### beepscore/Dejavu (currently unused)
I forked bcollazo/dejavu as beepscore/dejavu and added branch "beepscore".
<a href="https://github.com/beepscore/dejavu/tree/beepscore">https://github.com/beepscore/dejavu/tree/dejavu</a>

## PyAudio with USB audio interface
### Recording multiple microphones in python
Scarlett audio interface and PyAudio
https://stackoverflow.com/questions/25620285/recording-multiple-microphones-in-python

### python2.7 on Raspberry Pi 3 - Pyaudio Input overflowed
Raspberry Pi 3 Model B and Focusrite Scarlett 2i2 USB Sound Card
https://stackoverflow.com/questions/38042875/python2-7-on-raspberry-pi-3-pyaudio-input-overflowed

## remy_python
A Raspberry Pi infrared remote control. The Python app has three parts: Functions to send commands to the infrared transmitter. A Flask web service to accept television command requests (e.g. volume decrease, volume increase). A scheduler that automatically sends remote control commands at programmed times (e.g. mute during TV commercials).
<a href="https://github.com/beepscore/remy_python">https://github.com/beepscore/remy_python</a>

## Network enabled Raspberry Pi tv remote control
http://beepscore.com/website/2019/02/05/network-enabled-raspberry-pi-tv-remote-control.html

## Remy
Remote control television by sending commands from iOS device to a server.
https://github.com/beepscore/Remy

