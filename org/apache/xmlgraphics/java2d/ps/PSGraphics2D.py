def ():
    '''returns PSGraphics2D\n\n
    (final boolean textAsShapes)\n
    (final boolean textAsShapes, final PSGenerator gen)\n
    (final PSGraphics2D g)\n
    '''
def setPSGenerator():
    '''returns None\n\n
    setPSGenerator(final PSGenerator gen)\n
    '''
def getPSGenerator():
    '''returns PSGenerator\n\n
    getPSGenerator()\n
    '''
def setGraphicContext():
    '''returns None\n\n
    setGraphicContext(final GraphicContext c)\n
    '''
def getFallbackTextHandler():
    '''returns TextHandler\n\n
    getFallbackTextHandler()\n
    '''
def getCustomTextHandler():
    '''returns TextHandler\n\n
    getCustomTextHandler()\n
    '''
def setCustomTextHandler():
    '''returns None\n\n
    setCustomTextHandler(final TextHandler handler)\n
    '''
def disableClipping():
    '''returns None\n\n
    disableClipping(final boolean b)\n
    '''
def create():
    '''returns Graphics\n\n
    create()\n
    '''
def handleIOException():
    '''returns None\n\n
    handleIOException(final IOException ioe)\n
    '''
def preparePainting():
    '''returns None\n\n
    preparePainting()\n
    '''
def drawImage():
    '''returns boolean\n\n
    drawImage(final Image img, final int x, final int y, final ImageObserver observer)\n
    drawImage(final Image img, final int x, final int y, final int width, final int height, final ImageObserver observer)\n
    '''
def buildBufferedImage():
    '''returns BufferedImage\n\n
    buildBufferedImage(final Dimension size)\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def processShape():
    '''returns int\n\n
    processShape(final Shape s, final boolean cached)\n
    '''
def processPathIterator():
    '''returns None\n\n
    processPathIterator(final PathIterator iter)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Shape s)\n
    '''
def shouldBeClipped():
    '''returns boolean\n\n
    shouldBeClipped(final Shape clip, final Shape s)\n
    '''
def writeClip():
    '''returns None\n\n
    writeClip(final Shape s)\n
    '''
def drawRenderedImage():
    '''returns None\n\n
    drawRenderedImage(final RenderedImage img, final AffineTransform xform)\n
    '''
def drawRenderableImage():
    '''returns None\n\n
    drawRenderableImage(final RenderableImage img, final AffineTransform xform)\n
    '''
def establishColor():
    '''returns None\n\n
    establishColor(final Color c)\n
    '''
def drawString():
    '''returns None\n\n
    drawString(final String s, final float x, final float y)\n
    '''
def fill():
    '''returns None\n\n
    fill(final Shape s)\n
    '''
def getDeviceConfiguration():
    '''returns GraphicsConfiguration\n\n
    getDeviceConfiguration()\n
    '''
def getFontMetrics():
    '''returns FontMetrics\n\n
    getFontMetrics(final Font f)\n
    '''
def setXORMode():
    '''returns None\n\n
    setXORMode(final Color c1)\n
    '''
def copyArea():
    '''returns None\n\n
    copyArea(final int x, final int y, final int width, final int height, final int dx, final int dy)\n
    '''
