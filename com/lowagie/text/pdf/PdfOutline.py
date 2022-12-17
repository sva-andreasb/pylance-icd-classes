def ():
    '''returns PdfOutline\n\n
    (final PdfOutline parent, final PdfAction action, final String title)\n
    (final PdfOutline parent, final PdfAction action, final String title, final boolean open)\n
    (final PdfOutline parent, final PdfDestination destination, final String title)\n
    (final PdfOutline parent, final PdfDestination destination, final String title, final boolean open)\n
    (final PdfOutline parent, final PdfAction action, final PdfString title)\n
    (final PdfOutline parent, final PdfAction action, final PdfString title, final boolean open)\n
    (final PdfOutline parent, final PdfDestination destination, final PdfString title)\n
    (final PdfOutline parent, final PdfDestination destination, final PdfString title, final boolean open)\n
    (final PdfOutline parent, final PdfAction action, final Paragraph title)\n
    (final PdfOutline parent, final PdfAction action, final Paragraph title, final boolean open)\n
    (final PdfOutline parent, final PdfDestination destination, final Paragraph title)\n
    (final PdfOutline parent, final PdfDestination destination, final Paragraph title, final boolean open)\n
    '''
def setIndirectReference():
    '''returns None\n\n
    setIndirectReference(final PdfIndirectReference reference)\n
    '''
def indirectReference():
    '''returns PdfIndirectReference\n\n
    indirectReference()\n
    '''
def parent():
    '''returns PdfOutline\n\n
    parent()\n
    '''
def setDestinationPage():
    '''returns boolean\n\n
    setDestinationPage(final PdfIndirectReference pageReference)\n
    '''
def getPdfDestination():
    '''returns PdfDestination\n\n
    getPdfDestination()\n
    '''
def level():
    '''returns int\n\n
    level()\n
    '''
def toPdf():
    '''returns None\n\n
    toPdf(final PdfWriter writer, final OutputStream os)\n
    '''
def addKid():
    '''returns None\n\n
    addKid(final PdfOutline outline)\n
    '''
def getKids():
    '''returns ArrayList\n\n
    getKids()\n
    '''
def setKids():
    '''returns None\n\n
    setKids(final ArrayList kids)\n
    '''
def getTag():
    '''returns String\n\n
    getTag()\n
    '''
def setTag():
    '''returns None\n\n
    setTag(final String tag)\n
    '''
def getTitle():
    '''returns String\n\n
    getTitle()\n
    '''
def setTitle():
    '''returns None\n\n
    setTitle(final String title)\n
    '''
def isOpen():
    '''returns boolean\n\n
    isOpen()\n
    '''
def setOpen():
    '''returns None\n\n
    setOpen(final boolean open)\n
    '''
def getColor():
    '''returns Color\n\n
    getColor()\n
    '''
def setColor():
    '''returns None\n\n
    setColor(final Color color)\n
    '''
def getStyle():
    '''returns int\n\n
    getStyle()\n
    '''
def setStyle():
    '''returns None\n\n
    setStyle(final int style)\n
    '''
