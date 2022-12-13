def ImageManager():
    '''public ImageManager(final ImageContext context)
    public ImageManager(final ImageImplRegistry registry, final ImageContext context)
    '''
def getRegistry():
    '''public ImageImplRegistry getRegistry()
    '''
def getImageContext():
    '''public ImageContext getImageContext()
    '''
def getCache():
    '''public ImageCache getCache()
    '''
def getPipelineFactory():
    '''public PipelineFactory getPipelineFactory()
    '''
def getImageInfo():
    '''public ImageInfo getImageInfo(final String uri, final ImageSessionContext session)
    '''
def preloadImage():
    '''public ImageInfo preloadImage(final String uri, final ImageSessionContext session)
    public ImageInfo preloadImage(final String uri, final Source src)
    '''
def getImage():
    '''public Image getImage(final ImageInfo info, final ImageFlavor flavor, Map hints, final ImageSessionContext session)
    public Image getImage(final ImageInfo info, final ImageFlavor[] flavors, Map hints, final ImageSessionContext session)
    public Image getImage(final ImageInfo info, final ImageFlavor flavor, final ImageSessionContext session)
    public Image getImage(final ImageInfo info, final ImageFlavor[] flavors, final ImageSessionContext session)
    '''
def closeImage():
    '''public void closeImage(final String uri, final ImageSessionContext session)
    '''
def convertImage():
    '''public Image convertImage(final Image image, final ImageFlavor[] flavors, Map hints)
    public Image convertImage(final Image image, final ImageFlavor[] flavors)
    '''
def choosePipeline():
    '''public ImageProviderPipeline choosePipeline(final ImageProviderPipeline[] candidates)
    '''
