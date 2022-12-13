def ImageManager():
'''public ImageManager(final ImageContext context)
public ImageManager(final ImageImplRegistry registry, final ImageContext context)
'''
pass
def getRegistry():
'''public ImageImplRegistry getRegistry()
'''
pass
def getImageContext():
'''public ImageContext getImageContext()
'''
pass
def getCache():
'''public ImageCache getCache()
'''
pass
def getPipelineFactory():
'''public PipelineFactory getPipelineFactory()
'''
pass
def getImageInfo():
'''public ImageInfo getImageInfo(final String uri, final ImageSessionContext session)
'''
pass
def preloadImage():
'''public ImageInfo preloadImage(final String uri, final ImageSessionContext session)
public ImageInfo preloadImage(final String uri, final Source src)
'''
pass
def getImage():
'''public Image getImage(final ImageInfo info, final ImageFlavor flavor, Map hints, final ImageSessionContext session)
public Image getImage(final ImageInfo info, final ImageFlavor[] flavors, Map hints, final ImageSessionContext session)
public Image getImage(final ImageInfo info, final ImageFlavor flavor, final ImageSessionContext session)
public Image getImage(final ImageInfo info, final ImageFlavor[] flavors, final ImageSessionContext session)
'''
pass
def closeImage():
'''public void closeImage(final String uri, final ImageSessionContext session)
'''
pass
def convertImage():
'''public Image convertImage(final Image image, final ImageFlavor[] flavors, Map hints)
public Image convertImage(final Image image, final ImageFlavor[] flavors)
'''
pass
def choosePipeline():
'''public ImageProviderPipeline choosePipeline(final ImageProviderPipeline[] candidates)
'''
pass
