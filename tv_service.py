from enum import Enum
import json
import logging_util
import requests

# reference beepscore Remy / TVService.swift
# https://github.com/beepscore/Remy/blob/master/Remy/TVService.swift

# instantiate at module level, not class level
# https://stackoverflow.com/questions/22807972/python-best-practice-in-terms-of-logging
logger = logging_util.get_logger(__name__)


class TVCommand(Enum):
    mute = 'mute'
    power = 'power'
    bassDecrease = 'bass-decrease'
    bassIncrease = 'bass-increase'
    voiceDecrease = 'voice-decrease'
    voiceIncrease = 'voice-increase'
    volumeDecrease = 'volume-decrease'
    volumeIncrease = 'volume-increase'


def get_base_url(filename) -> str:
    """
    Reads configuration file
    https://stackoverflow.com/questions/5627425/what-is-a-good-way-to-handle-exceptions-when-trying-to-read-a-file-in-python
    :param filename: a json file that may contain a dictionary with key "base_url". e.g. data/config.json
    :return: base_url from file, else return base_url_default
    """
    base_url_default = 'http://10.0.0.4'

    try:
        with open(filename) as f:
            config_dict = json.load(f)
            base_url_from_file = config_dict.get('base_url')
            if base_url_from_file is not None:
                return base_url_from_file
            else:
                return base_url_default

    except IOError:
        # e.g. file doesn't exist
        logger.debug("Could not read file: " + filename)
        return base_url_default


def base_url_port_api_version_string() -> str:
    base_url = get_base_url('data/config.json')
    port = 5000
    api = 'api'
    api_version = 'v1'

    return base_url + ':' + str(port) + '/' + api + '/' + api_version


def command_url(tv_command: TVCommand) -> str:
    url_string = base_url_port_api_version_string() + '/tv/' + tv_command.value + '/'
    return url_string


def request_command(tv_command: TVCommand):
    """
    make a web request to a service
    :param tv_command: a TVCommand
    :return:
    """

    if tv_command is None:
        return

    url = command_url(tv_command)
    logger.debug('url: ' + url)

    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers)

    if response.status_code != 200:
        # http error
        logger.debug('status_code should be 200, but is {}'.format(str(response.status_code)))
        return

    try:
        response_json = response.json()
    except ValueError:
        logger.debug('Could not convert response json')
        return

    response_json_string = json.dumps(response_json)


def mute():
    """
    make a web request to a service to mute sound
    """
    request_command(tv_command=TVCommand.mute)


def power():
    """
    make a web request to a service to turn power off or on
    """
    request_command(tv_command=TVCommand.power)


def bass_decrease():
    """
    make a web request to a service to decrease bass
    """
    request_command(tv_command=TVCommand.bassDecrease)


def bass_increase():
    """
    make a web request to a service to increase bass
    """
    request_command(tv_command=TVCommand.bassIncrease)


def voice_decrease():
    """
    make a web request to a service to decrease voice
    """
    request_command(tv_command=TVCommand.voiceDecrease)


def voice_increase():
    """
    make a web request to a service to increase voice
    """
    request_command(tv_command=TVCommand.voiceIncrease)


def volume_decrease():
    """
    make a web request to a service to decrease volume
    """
    request_command(tv_command=TVCommand.volumeDecrease)


def volume_increase():
    """
    make a web request to a service to increase volume
    """
    request_command(tv_command=TVCommand.volumeIncrease)

