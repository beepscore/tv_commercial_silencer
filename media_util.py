import json
import os
import pathlib
import subprocess
import logging_util

# instantiate at module level, not class level
# https://stackoverflow.com/questions/22807972/python-best-practice-in-terms-of-logging
logger = logging_util.get_logger(__name__)


def write_media_info(infilename, outfilename):
    """
    read media info using ffprobe, write to outfilename
    Calls a shell script to execute command similar to:
    ffprobe -i boost.mp3 -v quiet -print_format json -show_format -show_streams -hide_banner
    https://stackoverflow.com/questions/6239350/how-to-extract-duration-time-from-ffmpeg-output
    http://www.ffmpeg.org/ffprobe.html
    :param infilename: filename of a media file e.g. './data/commercial_mp3/chantix.mp3'
    :param outfilename: filename of output file e.g. './data/info.txt'
    """

    if infilename is None or outfilename is None:
        return

    # subprocess.run requires Python >= 3.5, so don't use it yet.
    # I couldn't get subprocess.call(ffprobe...) to work, I think due to redirect to file.
    # So instead use subprocess.call to call a shell script.

    # redirect_to_file = '> ./data/junk7.txt'
    # args = ['ffprobe', '-i', filename, '-v', 'quiet', '-print_format', 'json',
    #         '-show_format', '-show_streams', '-hide_banner', redirect_to_file]
    # info_json = subprocess.call(args)

    args = ['./media_info.sh', infilename, outfilename]
    subprocess.call(args)


def info_dict_from_media_info(filename):

    with open(filename) as f:
        text = f.read()
        info_dict = json.loads(text)

    return info_dict


def duration_seconds_from_info_dict(info_dict):
    format_dict = info_dict.get('format')
    if format_dict is None:
        return None

    duration_string = format_dict.get('duration')
    if duration_string is None:
        return None
    else:
        return float(duration_string)


def duration_seconds_from_media_file(media_filename):
    temp_info_filename = './data/temp_info.txt'
    write_media_info(media_filename, temp_info_filename)
    info_dict = info_dict_from_media_info(temp_info_filename)
    duration = duration_seconds_from_info_dict(info_dict)
    os.remove(temp_info_filename)
    return duration


def write_media_file_durations(indirname, outfilename):
    """
    gets duration of every .mp3 file in indirname and writes json dictionary to outfilename
    key is media filename, value is duration in seconds e.g. 15.1
    assumes every file in indirname is a media file such as an mp3
    :param indirname: e.g. './data/commercial_mp3'
    :param outfilename: e.g. './data/media_durations_second.json'
    :return:
    """
    filenames = [filename for filename in os.listdir(indirname)]

    duration_dict = {}

    for filename in filenames:
        if filename == '.DS_Store':
            continue

        # https://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
        extension = pathlib.Path(filename).suffix
        if extension != '.mp3':
            continue

        duration_seconds = duration_seconds_from_media_file(indirname + '/' + filename)
        duration_dict[filename] = duration_seconds

    duration_dict_string = json.dumps(duration_dict)

    with open(outfilename, mode='w') as outfile:
        outfile.write(duration_dict_string)


def media_durations_second_dict(media_durations_json_filename):
    """
    :param media_durations_json_filename: json file containing a dictionary
    e.g. './data/media_durations_second.json'
    :return: dictionary from json
    key is media filename, value is duration in seconds e.g. 15.1
    """
    try:
        with open(media_durations_json_filename) as file:
            media_duration_seconds = json.load(file)
    except FileNotFoundError as error:
        logger.debug(error)
        return None

    return media_duration_seconds


if __name__ == '__main__':

    print(duration_seconds_from_media_file('./data/commercial_mp3/boost.mp3'))
    print(duration_seconds_from_media_file('./data/commercial_mp3/chantix.mp3'))
    write_media_file_durations('./data/commercial_mp3', './data/media_durations_second.json')
