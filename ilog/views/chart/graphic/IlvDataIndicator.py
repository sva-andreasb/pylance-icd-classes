X_VALUE = "int  0"
Y_VALUE = "int  1"
X_RANGE = "int  2"
Y_RANGE = "int  3"
WINDOW = "int  4"
def ():
    '''returns IlvDataIndicator\n\n
    (final int n, final double n2, final String f)\n
    (final int n, final IlvDataInterval ilvDataInterval, final String f)\n
    (final int n, final IlvDataWindow ilvDataWindow, final String f)\n
    '''
def has3DSupport():
    '''returns boolean\n\n
    has3DSupport()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final double b)\n
    '''
def setRange():
    '''returns None\n\n
    setRange(final IlvDataInterval ilvDataInterval)\n
    '''
def setDataWindow():
    '''returns None\n\n
    setDataWindow(final IlvDataWindow ilvDataWindow)\n
    setDataWindow(final double n, final double n2, final double n3, final double n4)\n
    '''
def getText():
    '''returns String\n\n
    getText()\n
    '''
def setText():
    '''returns None\n\n
    setText(final String s)\n
    '''
def setLabelRenderer():
    '''returns None\n\n
    setLabelRenderer(final IlvLabelRenderer g)\n
    '''
def setStyle():
    '''returns None\n\n
    setStyle(final IlvStyle d)\n
    '''
def getDrawStyle():
    '''returns IlvStyle\n\n
    getDrawStyle()\n
    '''
def beforeDraw():
    '''returns None\n\n
    beforeDraw(final Graphics graphics)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics)\n
    '''
def afterDraw():
    '''returns None\n\n
    afterDraw(final Graphics graphics)\n
    '''
def getBounds():
    '''returns Rectangle2D\n\n
    getBounds(final Rectangle2D rectangle2D)\n
    '''
def getShape():
    '''returns Shape\n\n
    getShape()\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final int n, final int n2)\n
    '''
def setVisible():
    '''returns None\n\n
    setVisible(final boolean visible)\n
    '''
def chartAreaChanged():
    '''returns None\n\n
    chartAreaChanged(final ChartAreaEvent chartAreaEvent)\n
    '''
def propertyChange():
    '''returns None\n\n
    propertyChange(final PropertyChangeEvent propertyChangeEvent)\n
    '''
