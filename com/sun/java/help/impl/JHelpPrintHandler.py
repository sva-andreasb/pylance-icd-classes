PRINT_BUTTON_NAME = "String  \"PrintButton\""
PAGE_SETUP_BUTTON_NAME = "String  \"PageSetupButton\""
PRINT_LATER_BUTTON_NAME = "String  \"PrintLaterButton\""
def ():
    '''returns JHEditorPane\n\n
    (final JHelp help)\n
    (final JEditorPane editor, final URL url, final PageFormat pf, final int firstPage, final boolean scaleToFit)\n
    (final JEditorPane editor, final URL[] urls, final PageFormat pf)\n
    ()\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled()\n
    '''
def setEnabled():
    '''returns None\n\n
    setEnabled(final boolean b)\n
    '''
def actionPerformed():
    '''returns None\n\n
    actionPerformed(final ActionEvent actionEvent)\n
    '''
def printSetup():
    '''returns None\n\n
    printSetup()\n
    '''
def print():
    '''returns int\n\n
    print(final URL url)\n
    print(final URL[] array)\n
    print(final Graphics graphics, final PageFormat pageFormat, int n)\n
    print(final Graphics graphics, final PageFormat pageFormat, final int n)\n
    '''
def getPageFormat():
    '''returns PageFormat\n\n
    getPageFormat()\n
    getPageFormat(final int n)\n
    '''
def getPF():
    '''returns PageFormat\n\n
    getPF()\n
    '''
def setPageFormat():
    '''returns None\n\n
    setPageFormat(final PageFormat pageFormat)\n
    '''
def setPF():
    '''returns None\n\n
    setPF(final PageFormat pageFormat)\n
    '''
def getPrinterJob():
    '''returns PrinterJob\n\n
    getPrinterJob()\n
    '''
def handlePageSetup():
    '''returns None\n\n
    handlePageSetup(final Component component)\n
    '''
def setHelpModel():
    '''returns None\n\n
    setHelpModel(final HelpModel helpModel)\n
    '''
def getHelpModel():
    '''returns HelpModel\n\n
    getHelpModel()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def getHeight():
    '''returns double\n\n
    getHeight()\n
    '''
def setHeight():
    '''returns None\n\n
    setHeight(final double height)\n
    '''
def getNumberOfPages():
    '''returns int\n\n
    getNumberOfPages()\n
    getNumberOfPages()\n
    '''
def createTransforms():
    '''returns Vector\n\n
    createTransforms()\n
    '''
def getPrintable():
    '''returns Printable\n\n
    getPrintable(final int i)\n
    '''
def addNotify():
    '''returns None\n\n
    addNotify()\n
    '''
def validate():
    '''returns None\n\n
    validate()\n
    '''
def getGraphics():
    '''returns Graphics\n\n
    getGraphics()\n
    '''
def getEditorKitForContentType():
    '''returns EditorKit\n\n
    getEditorKitForContentType(final String type)\n
    '''
def addMouseListener():
    '''returns None\n\n
    addMouseListener(final MouseListener mouseListener)\n
    '''
def removeMouseListener():
    '''returns None\n\n
    removeMouseListener(final MouseListener mouseListener)\n
    '''
def addMouseMotionListener():
    '''returns None\n\n
    addMouseMotionListener(final MouseMotionListener mouseMotionListener)\n
    '''
def removeMouseMotionListener():
    '''returns None\n\n
    removeMouseMotionListener(final MouseMotionListener mouseMotionListener)\n
    '''
def addFocusListener():
    '''returns None\n\n
    addFocusListener(final FocusListener focusListener)\n
    '''
def removeFocusListener():
    '''returns None\n\n
    removeFocusListener(final FocusListener focusListener)\n
    '''
def addKeyListener():
    '''returns None\n\n
    addKeyListener(final KeyListener keyListener)\n
    '''
def removeKeyListener():
    '''returns None\n\n
    removeKeyListener(final KeyListener keyListener)\n
    '''
