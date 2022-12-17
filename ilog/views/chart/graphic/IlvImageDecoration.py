ANCHORED = "int  0"
TILED = "int  1"
SCALED = "int  2"
def ():
    '''returns IlvImageDecoration\n\n
    (final Image image)\n
    (final Image image, final int n, final int n2)\n
    (final URL c, final int n, final int n2)\n
    '''
def getMode():
    '''returns int\n\n
    getMode()\n
    '''
def setMode():
    '''returns None\n\n
    setMode(final int d)\n
    '''
def getAnchor():
    '''returns int\n\n
    getAnchor()\n
    '''
def setAnchor():
    '''returns None\n\n
    setAnchor(final int anchor)\n
    '''
def getOffset():
    '''returns Point\n\n
    getOffset()\n
    '''
def setOffset():
    '''returns None\n\n
    setOffset(final Point offset)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics)\n
    '''
def getBounds():
    '''returns Rectangle2D\n\n
    getBounds(Rectangle2D rectangle2D)\n
    '''
def validateObject():
    '''returns None\n\n
    validateObject()\n
    '''
def imageUpdate():
    '''returns boolean\n\n
    imageUpdate(final Image image, final int n, final int n2, final int n3, final int n4, final int n5)\n
    '''
