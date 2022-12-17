OFFSET_CFTAG = "int  4"
OFFSET_CF = "int  8"
OFFSET_WMFDATA = "int  20"
CFTAG_WINDOWS = "int  -1"
CFTAG_MACINTOSH = "int  -2"
CFTAG_FMTID = "int  -3"
CFTAG_NODATA = "int  0"
CF_METAFILEPICT = "int  3"
CF_DIB = "int  8"
CF_ENHMETAFILE = "int  14"
CF_BITMAP = "int  2"
def ():
    '''returns Thumbnail\n\n
    ()\n
    (final byte[] thumbnailData)\n
    '''
def getThumbnail():
    '''returns byte[]\n\n
    getThumbnail()\n
    '''
def setThumbnail():
    '''returns None\n\n
    setThumbnail(final byte[] thumbnail)\n
    '''
def getClipboardFormatTag():
    '''returns long\n\n
    getClipboardFormatTag()\n
    '''
def getClipboardFormat():
    '''returns long\n\n
    getClipboardFormat()\n
    '''
def getThumbnailAsWMF():
    '''returns byte[]\n\n
    getThumbnailAsWMF()\n
    '''
