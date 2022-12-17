def ():
    '''returns IIOMultiImageWriter\n\n
    (final String mime)\n
    (final OutputStream out)\n
    '''
def writeImage():
    '''returns None\n\n
    writeImage(final RenderedImage image, final OutputStream out)\n
    writeImage(final RenderedImage image, final OutputStream out, final ImageWriterParams params)\n
    writeImage(final RenderedImage image, final ImageWriterParams params)\n
    '''
def getMIMEType():
    '''returns String\n\n
    getMIMEType()\n
    '''
def isFunctional():
    '''returns boolean\n\n
    isFunctional()\n
    '''
def warningOccurred():
    '''returns None\n\n
    warningOccurred(final javax.imageio.ImageWriter source, final int imageIndex, final String warning)\n
    '''
def createMultiImageWriter():
    '''returns MultiImageWriter\n\n
    createMultiImageWriter(final OutputStream out)\n
    '''
def supportsMultiImageWriter():
    '''returns boolean\n\n
    supportsMultiImageWriter()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
