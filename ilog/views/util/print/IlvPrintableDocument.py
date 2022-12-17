ORDERED_BY_COLUMNS = "int  0"
ORDERED_BY_ROWS = "int  1"
def ():
    '''returns IlvPrintableDocument\n\n
    (final String e, final PageFormat pageFormat)\n
    (final String e, final int b, final Paper paper)\n
    (final String e, final int b)\n
    (final String e)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String e)\n
    '''
def getDate():
    '''returns Date\n\n
    getDate()\n
    '''
def setDate():
    '''returns None\n\n
    setDate(final Date h)\n
    '''
def getAuthor():
    '''returns String\n\n
    getAuthor()\n
    '''
def setAuthor():
    '''returns None\n\n
    setAuthor(final String f)\n
    '''
def getSides():
    '''returns Sides\n\n
    getSides()\n
    '''
def setSides():
    '''returns None\n\n
    setSides(final Sides g)\n
    '''
def getTemplatePage():
    '''returns IlvPage\n\n
    getTemplatePage()\n
    '''
def setTemplatePage():
    '''returns None\n\n
    setTemplatePage(final IlvPage d)\n
    '''
def getHeader():
    '''returns IlvHeader\n\n
    getHeader()\n
    '''
def setHeader():
    '''returns None\n\n
    setHeader(final IlvHeader j)\n
    '''
def getFooter():
    '''returns IlvFooter\n\n
    getFooter()\n
    '''
def setFooter():
    '''returns None\n\n
    setFooter(final IlvFooter i)\n
    '''
def getOrientation():
    '''returns int\n\n
    getOrientation()\n
    '''
def setOrientation():
    '''returns None\n\n
    setOrientation(final int b)\n
    '''
def getPaperFormat():
    '''returns Paper\n\n
    getPaperFormat()\n
    '''
def setPaperFormat():
    '''returns None\n\n
    setPaperFormat(final Paper paper)\n
    '''
def getPageFormat():
    '''returns PageFormat\n\n
    getPageFormat()\n
    getPageFormat(final int n)\n
    '''
def setPageFormat():
    '''returns None\n\n
    setPageFormat(final PageFormat pageFormat)\n
    '''
def getFlow():
    '''returns IlvFlow\n\n
    getFlow()\n
    '''
def isFlowLayoutValid():
    '''returns boolean\n\n
    isFlowLayoutValid()\n
    '''
def invalidateFlowLayout():
    '''returns None\n\n
    invalidateFlowLayout()\n
    '''
def getColumnCount():
    '''returns int\n\n
    getColumnCount()\n
    '''
def setColumnCount():
    '''returns None\n\n
    setColumnCount(final int m)\n
    '''
def getPageOrder():
    '''returns int\n\n
    getPageOrder()\n
    '''
def setPageOrder():
    '''returns None\n\n
    setPageOrder(final int l)\n
    '''
def getPage():
    '''returns IlvPage\n\n
    getPage(final int index)\n
    '''
def getPageIndex():
    '''returns int\n\n
    getPageIndex(final IlvPage o)\n
    '''
def getPrintable():
    '''returns Printable\n\n
    getPrintable(final int n)\n
    '''
def print():
    '''returns int\n\n
    print(final Graphics graphics, final PageFormat pageFormat, final int n)\n
    '''
def enablePrintStyle():
    '''returns None\n\n
    enablePrintStyle(final boolean b)\n
    '''
def addPropertyChangeListener():
    '''returns None\n\n
    addPropertyChangeListener(final String propertyName, final PropertyChangeListener listener)\n
    addPropertyChangeListener(final PropertyChangeListener listener)\n
    '''
def removePropertyChangeListener():
    '''returns None\n\n
    removePropertyChangeListener(final String propertyName, final PropertyChangeListener listener)\n
    removePropertyChangeListener(final PropertyChangeListener listener)\n
    '''
