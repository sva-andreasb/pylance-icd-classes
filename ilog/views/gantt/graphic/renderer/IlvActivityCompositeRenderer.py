def ():
    '''returns IlvActivityCompositeRenderer\n\n
    ()\n
    '''
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def getRenderer():
    '''returns IlvActivityRenderer\n\n
    getRenderer(final int n)\n
    '''
def addRenderer():
    '''returns None\n\n
    addRenderer(final IlvActivityRenderer ilvActivityRenderer)\n
    '''
def insertRendererAt():
    '''returns None\n\n
    insertRendererAt(final IlvActivityRenderer ilvActivityRenderer, final int n)\n
    '''
def setRenderer():
    '''returns None\n\n
    setRenderer(final int n, final IlvActivityRenderer ilvActivityRenderer)\n
    '''
def getBounds():
    '''returns IlvRect\n\n
    getBounds(final IlvActivityGraphic ilvActivityGraphic, final IlvTransformer ilvTransformer)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvActivityGraphic ilvActivityGraphic, final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvActivityGraphic ilvActivityGraphic, final IlvTransformer ilvTransformer)\n
    '''
def isRelayoutNeeded():
    '''returns boolean\n\n
    isRelayoutNeeded(final IlvActivityGraphic ilvActivityGraphic, final ActivityEvent activityEvent)\n
    '''
def isRedrawNeeded():
    '''returns boolean\n\n
    isRedrawNeeded(final IlvActivityGraphic ilvActivityGraphic, final ActivityEvent activityEvent)\n
    isRedrawNeeded(final ActivityEvent activityEvent)\n
    '''
def makeSelection():
    '''returns IlvSelection\n\n
    makeSelection(final IlvActivityGraphic ilvActivityGraphic)\n
    '''
def createSelection():
    '''returns IlvSelection\n\n
    createSelection(final IlvActivityGraphic ilvActivityGraphic, final String[] array)\n
    '''
def getToolTipText():
    '''returns String\n\n
    getToolTipText(final IlvActivityGraphic ilvActivityGraphic, final IlvPoint ilvPoint, final IlvTransformer ilvTransformer)\n
    '''
def getPopupMenu():
    '''returns JPopupMenu\n\n
    getPopupMenu(final IlvActivityGraphic ilvActivityGraphic, final IlvPoint ilvPoint, final IlvTransformer ilvTransformer, final IlvManagerView ilvManagerView, final IlvPopupMenuManager ilvPopupMenuManager)\n
    '''
def setPopupMenuName():
    '''returns None\n\n
    setPopupMenuName(final String b)\n
    '''
def getPopupMenuName():
    '''returns String\n\n
    getPopupMenuName()\n
    '''
