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
    bass_increase = 'bass-increase'
    voice_decrease = 'voice-decrease'
    voice_increase = 'voice-increase'
    volume_decrease = 'volume-decrease'
    volume_increase = 'volume-increase'
    volume_decrease_increase = 'volume-decrease-increase'


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


def request_command(tv_command: TVCommand, data_dict=None):
    """
    make a web request to a service
    :param tv_command: a TVCommand
    :param data_dict: a Python dictionary. may be used to pass data
    :return:
    """

    if tv_command is None:
        return

    url = command_url(tv_command)
    logger.debug('url: {}, data_dict: {}'.format(url, data_dict))

    # in call to requests.post, supplying json= automatically sets content type
    # headers = {'Content-Type': 'application/json'}

    # https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
    try:
        # https://stackoverflow.com/questions/20001229/how-to-get-posted-json-in-flask
        response = requests.post(url, json=data_dict)
        # https://2.python-requests.org//en/latest/api/#requests.Response.raise_for_status
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        logger.debug(error)
        return

    if response.status_code != 200:
        # http error
        logger.debug('status_code should be 200, but is {}'.format(str(response.status_code)))
        return

    try:
        # response_dict is a python dictionary
        response_dict = response.json()
        # logger.debug('response_dict: {}'.format(response_dict))
        # 2019-04-22 17:25:41 DEBUG    request_command line:94 response_dict:
        # {'api_name': 'tv', 'response': 'transmitted command mute', 'version': '1.0'}

    except ValueError:
        logger.debug('Could not convert response json')
        return

    # convert json dictionary to string
    response_json_string = json.dumps(response_dict)
    logger.debug('response_json_string: {}'.format(response_json_string))
    # 2019-04-22 17:25:41 DEBUG    request_command line:101 response_json_string:
    # {"api_name": "tv", "response": "transmitted command mute", "version": "1.0"}


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
    request_command(tv_command=TVCommand.bass_increase)


def voice_decrease():
    """
    make a web request to a service to decrease voice
    """
    request_command(tv_command=TVCommand.voice_decrease)


def voice_increase():
    """
    make a web request to a service to increase voice
    """
    request_command(tv_command=TVCommand.voice_increase)


def volume_decrease():
    """
    make a web request to a service to decrease volume
    """
    request_command(tv_command=TVCommand.volume_decrease)


def volume_increase():
    """
    make a web request to a service to increase volume
    """
    request_command(tv_command=TVCommand.volume_increase)


def volume_decrease_increase(duration_seconds):
    """
    make a web request to a service to decrease volume, then increase
    """
    # spell key duration-seconds with '-' similar to headers convention
    data_dict = {'duration-seconds': duration_seconds}

    request_command(tv_command=TVCommand.volume_decrease_increase, data_dict=data_dict)

