# Purpose
Listen to television audio, detect commercials, request decrease volume.

# Results

## install Dejavu

    conda activate remy_python
    pip install -e git+https://github.com/bcollazo/dejavu@v1.2#egg=PyDejavu

This installed directory src/pydejavu.
Then delete src/pip-delete-this-directory.txt to prevent src from being deleted.

# References

## Dejavu project
Audio fingerprinting and recognition in Python.
It has recognizers for recorded files and for live microphone input.
Originally by worldveil/dejavu, forked by DataWookie/dejavu and <a href="https://github.com/bcollazo/dejavu">bcollazo/dejavu.</a>
In 2019-03 bcollazo/dejavu appeared to be the most active fork.

### beepscore/Dejavu
I forked bcollazo/dejavu as beepscore/dejavu and added branch "beepscore".
<a href="https://github.com/beepscore/dejavu/tree/beepscore">https://github.com/beepscore/dejavu/tree/dejavu</a>

## remy_python
A Raspberry Pi infrared remote control. The Python app has three parts: Functions to send commands to the infrared transmitter. A Flask web service to accept television command requests (e.g. volume decrease, volume increase). A scheduler that automatically sends remote control commands at programmed times (e.g. mute during TV commercials).
<a href="https://github.com/beepscore/remy_python">https://github.com/beepscore/remy_python</a>

## Network enabled Raspberry Pi tv remote control
http://beepscore.com/website/2019/02/05/network-enabled-raspberry-pi-tv-remote-control.html

## Remy
Remote control television by sending commands from iOS device to a server.
https://github.com/beepscore/Remy

