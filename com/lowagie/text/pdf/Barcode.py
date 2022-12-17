EAN13 = "int  1"
EAN8 = "int  2"
UPCA = "int  3"
UPCE = "int  4"
SUPP2 = "int  5"
SUPP5 = "int  6"
POSTNET = "int  7"
PLANET = "int  8"
CODE128 = "int  9"
CODE128_UCC = "int  10"
CODE128_RAW = "int  11"
CODABAR = "int  12"
def ():
    '''returns Barcode\n\n
    ()\n
    '''
def getX():
    '''returns float\n\n
    getX()\n
    '''
def setX():
    '''returns None\n\n
    setX(final float x)\n
    '''
def getN():
    '''returns float\n\n
    getN()\n
    '''
def setN():
    '''returns None\n\n
    setN(final float n)\n
    '''
def getFont():
    '''returns BaseFont\n\n
    getFont()\n
    '''
def setFont():
    '''returns None\n\n
    setFont(final BaseFont font)\n
    '''
def getSize():
    '''returns float\n\n
    getSize()\n
    '''
def setSize():
    '''returns None\n\n
    setSize(final float size)\n
    '''
def getBaseline():
    '''returns float\n\n
    getBaseline()\n
    '''
def setBaseline():
    '''returns None\n\n
    setBaseline(final float baseline)\n
    '''
def getBarHeight():
    '''returns float\n\n
    getBarHeight()\n
    '''
def setBarHeight():
    '''returns None\n\n
    setBarHeight(final float barHeight)\n
    '''
def getTextAlignment():
    '''returns int\n\n
    getTextAlignment()\n
    '''
def setTextAlignment():
    '''returns None\n\n
    setTextAlignment(final int textAlignment)\n
    '''
def isGenerateChecksum():
    '''returns boolean\n\n
    isGenerateChecksum()\n
    '''
def setGenerateChecksum():
    '''returns None\n\n
    setGenerateChecksum(final boolean generateChecksum)\n
    '''
def isChecksumText():
    '''returns boolean\n\n
    isChecksumText()\n
    '''
def setChecksumText():
    '''returns None\n\n
    setChecksumText(final boolean checksumText)\n
    '''
def isStartStopText():
    '''returns boolean\n\n
    isStartStopText()\n
    '''
def setStartStopText():
    '''returns None\n\n
    setStartStopText(final boolean startStopText)\n
    '''
def isExtended():
    '''returns boolean\n\n
    isExtended()\n
    '''
def setExtended():
    '''returns None\n\n
    setExtended(final boolean extended)\n
    '''
def getCode():
    '''returns String\n\n
    getCode()\n
    '''
def setCode():
    '''returns None\n\n
    setCode(final String code)\n
    '''
def isGuardBars():
    '''returns boolean\n\n
    isGuardBars()\n
    '''
def setGuardBars():
    '''returns None\n\n
    setGuardBars(final boolean guardBars)\n
    '''
def getCodeType():
    '''returns int\n\n
    getCodeType()\n
    '''
def setCodeType():
    '''returns None\n\n
    setCodeType(final int codeType)\n
    '''
def createTemplateWithBarcode():
    '''returns PdfTemplate\n\n
    createTemplateWithBarcode(final PdfContentByte cb, final Color barColor, final Color textColor)\n
    '''
def createImageWithBarcode():
    '''returns Image\n\n
    createImageWithBarcode(final PdfContentByte cb, final Color barColor, final Color textColor)\n
    '''
def getInkSpreading():
    '''returns float\n\n
    getInkSpreading()\n
    '''
def setInkSpreading():
    '''returns None\n\n
    setInkSpreading(final float inkSpreading)\n
    '''
