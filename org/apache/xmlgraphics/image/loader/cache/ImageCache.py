def ImageCache():
    '''    public ImageCache()
    public ImageCache(final TimeStampProvider timeStampProvider, final ExpirationPolicy invalidURIExpirationPolicy)
    '''
def setCacheListener():
    '''    public void setCacheListener(final ImageCacheListener listener)
    '''
def needImageInfo():
    '''    public ImageInfo needImageInfo(final String uri, final ImageSessionContext session, final ImageManager manager)
    '''
def isInvalidURI():
    '''    public boolean isInvalidURI(final String uri)
    '''
def getImage():
    '''    public Image getImage(final ImageInfo info, final ImageFlavor flavor)
    public Image getImage(final String uri, final ImageFlavor flavor)
    '''
def putImage():
    '''    public void putImage(final Image img)
    '''
def clearCache():
    '''    public void clearCache()
    '''
def doHouseKeeping():
    '''    public void doHouseKeeping()
    '''
