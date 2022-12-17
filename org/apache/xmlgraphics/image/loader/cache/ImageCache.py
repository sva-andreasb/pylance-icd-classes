def ():
    '''returns ImageCache\n\n
    ()\n
    (final TimeStampProvider timeStampProvider, final ExpirationPolicy invalidURIExpirationPolicy)\n
    '''
def setCacheListener():
    '''returns None\n\n
    setCacheListener(final ImageCacheListener listener)\n
    '''
def needImageInfo():
    '''returns ImageInfo\n\n
    needImageInfo(final String uri, final ImageSessionContext session, final ImageManager manager)\n
    '''
def isInvalidURI():
    '''returns boolean\n\n
    isInvalidURI(final String uri)\n
    '''
def getImage():
    '''returns Image\n\n
    getImage(final ImageInfo info, final ImageFlavor flavor)\n
    getImage(final String uri, final ImageFlavor flavor)\n
    '''
def putImage():
    '''returns None\n\n
    putImage(final Image img)\n
    '''
def clearCache():
    '''returns None\n\n
    clearCache()\n
    '''
def doHouseKeeping():
    '''returns None\n\n
    doHouseKeeping()\n
    '''
