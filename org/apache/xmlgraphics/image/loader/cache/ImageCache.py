def ImageCache():
'''public ImageCache()
public ImageCache(final TimeStampProvider timeStampProvider, final ExpirationPolicy invalidURIExpirationPolicy)
'''
pass
def setCacheListener():
'''public void setCacheListener(final ImageCacheListener listener)
'''
pass
def needImageInfo():
'''public ImageInfo needImageInfo(final String uri, final ImageSessionContext session, final ImageManager manager)
'''
pass
def isInvalidURI():
'''public boolean isInvalidURI(final String uri)
'''
pass
def getImage():
'''public Image getImage(final ImageInfo info, final ImageFlavor flavor)
public Image getImage(final String uri, final ImageFlavor flavor)
'''
pass
def putImage():
'''public void putImage(final Image img)
'''
pass
def clearCache():
'''public void clearCache()
'''
pass
def doHouseKeeping():
'''public void doHouseKeeping()
'''
pass
