def getDrawable():
    '''returns DrawBackground\n\n
    getDrawable(final Shape<?, ?> shape)\n
    getDrawable(final Slide<?, ?> sheet)\n
    getDrawable(final Sheet<?, ?> sheet)\n
    getDrawable(final MasterSheet<?, ?> sheet)\n
    getDrawable(final TextBox<?, ?> shape)\n
    getDrawable(final FreeformShape<?, ?> shape)\n
    getDrawable(final ConnectorShape<?, ?> shape)\n
    getDrawable(final TableShape<?, ?> shape)\n
    getDrawable(final TextShape<?, ?> shape)\n
    getDrawable(final GroupShape<?, ?> shape)\n
    getDrawable(final PictureShape<?, ?> shape)\n
    getDrawable(final GraphicalFrame<?, ?> shape)\n
    getDrawable(final TextParagraph<?, ?, ?> paragraph)\n
    getDrawable(final Background<?, ?> shape)\n
    '''
def getTextFragment():
    '''returns DrawTextFragment\n\n
    getTextFragment(final TextLayout layout, final AttributedString str)\n
    '''
def getPaint():
    '''returns DrawPaint\n\n
    getPaint(final PlaceableShape<?, ?> shape)\n
    '''
def drawShape():
    '''returns None\n\n
    drawShape(final Graphics2D graphics, final Shape<?, ?> shape, final Rectangle2D bounds)\n
    '''
def fixFonts():
    '''returns None\n\n
    fixFonts(final Graphics2D graphics)\n
    '''
def getFontManager():
    '''returns DrawFontManager\n\n
    getFontManager(final Graphics2D graphics)\n
    '''
