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


if __name__ == '__main__':

    write_media_info('./data/commercial_mp3/boost.mp3', './data/info.txt')
