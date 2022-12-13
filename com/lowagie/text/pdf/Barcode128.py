CODE_AB_TO_C = "char  'c'"
CODE_AC_TO_B = "char  'd'"
CODE_BC_TO_A = "char  'e'"
FNC1_INDEX = "char  'f'"
START_A = "char  'g'"
START_B = "char  'h'"
START_C = "char  'i'"
FNC1 = "char  '\u00ca'"
DEL = "char  '\u00c3'"
FNC3 = "char  '\u00c4'"
FNC2 = "char  '\u00c5'"
SHIFT = "char  '\u00c6'"
CODE_C = "char  '\u00c7'"
CODE_A = "char  '\u00c8'"
FNC4 = "char  '\u00c8'"
STARTA = "char  '\u00cb'"
STARTB = "char  '\u00cc'"
STARTC = "char  '\u00cd'"
def Barcode128():
    '''public Barcode128()
    '''
def removeFNC1():
    '''public static String removeFNC1(final String code)
    '''
def getHumanReadableUCCEAN():
    '''public static String getHumanReadableUCCEAN(String code)
    '''
def getRawText():
    '''public static String getRawText(final String text, final boolean ucc)
    '''
def getBarsCode128Raw():
    '''public static byte[] getBarsCode128Raw(String text)
    '''
def getBarcodeSize():
    '''public Rectangle getBarcodeSize()
    '''
def placeBarcode():
    '''public Rectangle placeBarcode(final PdfContentByte cb, final Color barColor, final Color textColor)
    '''
def createAwtImage():
    '''public Image createAwtImage(final Color foreground, final Color background)
    '''
def setCode():
    '''public void setCode(final String code)
    '''
