
from .Readers.readVideoffmpeg import readVideoffmpeg
from .Readers.readVideoHDF5 import readVideoHDF5
from .Readers.readDatFiles import readDatFiles
from .Readers.readTifFiles import readTifFiles
from .Readers.readVideoCapture import readVideoCapture

def selectVideoReader(video_file):
    # open video to read
    isHDF5video = video_file.endswith('.hdf5')
    isMJPGvideo = video_file.endswith('.mjpg')
    isDATfiles = video_file.endswith('spool.dat')
    isTIFfiles = video_file.endswith('.tif')

    if isHDF5video:
        # use tables to read hdf5 with lz4 compression generated by the Gecko
        # plugin
        vid = readVideoHDF5(video_file)
    elif isMJPGvideo:
        # use previous ffmpeg that is more compatible with the Gecko MJPG
        # format
        vid = readVideoffmpeg(video_file)
    elif isDATfiles:
        video_dir = os.path.split(video_file)[0]
        vid = readDatFile(video_dir)
    elif isTIFfiles:
        # TODO: this currently requires just the first image file. make it so
        # that one can supply a path to multiple folders, and run compression
        # on the files inside in parallel
        video_dir = os.path.split(video_file)[0]
        vid = readTifFiles(video_dir)
    else:
        # use opencv VideoCapture
        vid = readVideoCapture(video_file)
    return vid
