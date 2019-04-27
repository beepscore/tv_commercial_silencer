#!/bin/sh

# for use by python subprocess, start bash file with shebang #!/bin/sh and chmod u+x

# https://stackoverflow.com/questions/6239350/how-to-extract-duration-time-from-ffmpeg-output
# http://www.ffmpeg.org/ffprobe.html

# usage
# ./media_info.sh <infilename> <outfilename>

ffprobe -i $1 -v quiet -print_format json -show_format -show_streams -hide_banner > $2
