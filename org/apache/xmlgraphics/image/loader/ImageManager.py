def ():
    '''returns ImageManager\n\n
    (final ImageContext context)\n
    (final ImageImplRegistry registry, final ImageContext context)\n
    '''
def getRegistry():
    '''returns ImageImplRegistry\n\n
    getRegistry()\n
    '''
def getImageContext():
    '''returns ImageContext\n\n
    getImageContext()\n
    '''
def getCache():
    '''returns ImageCache\n\n
    getCache()\n
    '''
def getPipelineFactory():
    '''returns PipelineFactory\n\n
    getPipelineFactory()\n
    '''
def getImageInfo():
    '''returns ImageInfo\n\n
    getImageInfo(final String uri, final ImageSessionContext session)\n
    '''
def preloadImage():
    '''returns ImageInfo\n\n
    preloadImage(final String uri, final ImageSessionContext session)\n
    preloadImage(final String uri, final Source src)\n
    '''
def getImage():
    '''returns Image\n\n
    getImage(final ImageInfo info, final ImageFlavor flavor, Map hints, final ImageSessionContext session)\n
    getImage(final ImageInfo info, final ImageFlavor[] flavors, Map hints, final ImageSessionContext session)\n
    getImage(final ImageInfo info, final ImageFlavor flavor, final ImageSessionContext session)\n
    getImage(final ImageInfo info, final ImageFlavor[] flavors, final ImageSessionContext session)\n
    '''
def closeImage():
    '''returns None\n\n
    closeImage(final String uri, final ImageSessionContext session)\n
    '''
def convertImage():
    '''returns Image\n\n
    convertImage(final Image image, final ImageFlavor[] flavors, Map hints)\n
    convertImage(final Image image, final ImageFlavor[] flavors)\n
    '''
def choosePipeline():
    '''returns ImageProviderPipeline\n\n
    choosePipeline(final ImageProviderPipeline[] candidates)\n
    '''
