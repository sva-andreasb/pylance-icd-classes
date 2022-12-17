XYZ = "int  0"
FIT = "int  1"
FITH = "int  2"
FITV = "int  3"
FITR = "int  4"
FITB = "int  5"
FITBH = "int  6"
FITBV = "int  7"
def ():
    '''returns PdfDestination\n\n
    (final int type)\n
    (final int type, final float parameter)\n
    (final int type, final float left, final float top, final float zoom)\n
    (final int type, final float left, final float bottom, final float right, final float top)\n
    '''
def hasPage():
    '''returns boolean\n\n
    hasPage()\n
    '''
def addPage():
    '''returns boolean\n\n
    addPage(final PdfIndirectReference page)\n
    '''
