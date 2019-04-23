import json
import os
import logging_util

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

import tv_service

import warnings
warnings.filterwarnings("ignore")

# Reference example.py

# instantiate at module level, not class level
# https://stackoverflow.com/questions/22807972/python-best-practice-in-terms-of-logging
logger = logging_util.get_logger(__name__)


def config_environment_variable_database_url_from_file(filename):
    """
    Reads configuration file, may set environment variable DATABASE_URL.
    https://stackoverflow.com/questions/5627425/what-is-a-good-way-to-handle-exceptions-when-trying-to-read-a-file-in-python
    Alternatively could set a python variable.
    :param filename: a json file that may contain a dictionary with key "DATABASE_URL"
    """
    try:
        with open(filename) as f:
            config_dict = json.load(f)
            db_url_from_file = config_dict.get('DATABASE_URL')
            if db_url_from_file is not None:
                os.environ['DATABASE_URL'] = db_url_from_file

    except IOError:
        # e.g. file doesn't exist
        logger.debug("Could not read file: " + filename)
        print("Could not read file: " + filename)


def recognize_audio_from_a_file(djv, filename_containing_audio_to_match):
    """
    Shows example usage of djv.recognize, prints match_dict
    :param djv: a dejavu instance, preconfigured by having run fingerprint_directory
    :param filename_containing_audio_to_match:
    """
    match_dict = djv.recognize(FileRecognizer, filename_containing_audio_to_match)
    match_dict_json = json.dumps(match_dict)
    logger.debug('filename_containing_audio_to_match: {0}, match_dict_json: {1}\n'
                 .format(filename_containing_audio_to_match, match_dict_json))

    # example output
    # filename_containing_audio_to_match: mp3/chantix.mp3,
    # match_dict_json: {"song_id": 12, "song_name": "chantix", "confidence": 43335,
    # "offset": 0, "offset_seconds": 0.0,
    # "file_sha1": "7050797273712b325559706c4d6878594238583866486d4b4371493d0a",
    # "match_time": 11.098071813583374}


def recognize_audio_from_microphone(djv, seconds=5):
    """
    method will return shortly after 'seconds' number of seconds
    :param djv: a dejavu instance, preconfigured by having run fingerprint_directory
    :param seconds: number of seconds to recognize audio
    :return: match_dict if confidence is >= confidence_minimum, else None
    """
    match_dict = djv.recognize(MicrophoneRecognizer, seconds=seconds)

    if match_dict is None:
        # "Nothing recognized -- did you play the song out loud so your mic could hear it? :)"
        return None

    else:
        # use confidence_minimum to help avoid false positives,
        # e.g. avoid algorithm accidentally matching to background noise with confidence ~ 10
        confidence_minimum = 100
        confidence = match_dict.get('confidence')

        if confidence is not None and confidence >= confidence_minimum:
            logger.debug('match_dict: {}'.format(match_dict))
            # example output
            # 2019-04-22 17:47:34 DEBUG    recognize_audio_from_microphone line:79 match_dict:
            # {'song_id': 4, 'song_name': 'google-help-cooper', 'confidence': 146,
            # 'offset': 17, 'offset_seconds': 0.78948, 'file_sha1': '5b2709b5d22011c18f9a7b6ab7f04f0e89da4d41'}

            # FIXME: don't use mute, too easy for app to get toggle confused
            # instead in tv_service add methods like volume_duck(number_of_times, duration_seconds)
            tv_service.mute()
            # TODO: get duration of matching audio file
            # after duration volume_duck will increase volume
            # tv_service.volume_duck(number_of_times=3, duration_seconds=30)

            return match_dict

    return None


def recognize_audio_from_microphone_with_count(djv, seconds=5, count_max=4):
    """
    :param djv: a dejavu instance, preconfigured by having run fingerprint_directory
    :param seconds: number of seconds to recognize audio
    :param count_max: number of times to iterate
    :return:
    """
    for count in range(0, count_max):
        iteration = count + 1
        logger.debug(msg='{}/{}'.format(iteration, count_max))

        # waits for recognize_audio_from_microphone to return
        # recognize_audio_from_microphone returns shortly after 'seconds' number of seconds
        match_dict = recognize_audio_from_microphone(djv, seconds)


if __name__ == '__main__':

    config_environment_variable_database_url_from_file('data/config.json')

    dburl = os.getenv('DATABASE_URL', default='sqlite://')
    logger.debug('dburl: {}'.format(dburl))

    # instantiate a Dejavu object, configured to use database at dburl
    djv = Dejavu(dburl=dburl)

    # Prepare djv to be able to recognize audio.
    # Fingerprint all the mp3's in the directory we give it
    # this may take several seconds per file
    djv.fingerprint_directory("data/commercial_mp3", [".mp3"])

    # example, may be useful for debugging
    # recognize_audio_from_a_file(djv, filename_containing_audio_to_match='data/commercial_mp3/chantix.mp3')

    recognize_audio_from_microphone_with_count(djv, seconds=5, count_max=40)
