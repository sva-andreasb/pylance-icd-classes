COURIER = "String  \"Courier\""
COURIER_BOLD = "String  \"Courier-Bold\""
COURIER_OBLIQUE = "String  \"Courier-Oblique\""
COURIER_BOLDOBLIQUE = "String  \"Courier-BoldOblique\""
HELVETICA = "String  \"Helvetica\""
HELVETICA_BOLD = "String  \"Helvetica-Bold\""
HELVETICA_OBLIQUE = "String  \"Helvetica-Oblique\""
HELVETICA_BOLDOBLIQUE = "String  \"Helvetica-BoldOblique\""
SYMBOL = "String  \"Symbol\""
TIMES_ROMAN = "String  \"Times-Roman\""
TIMES_BOLD = "String  \"Times-Bold\""
TIMES_ITALIC = "String  \"Times-Italic\""
TIMES_BOLDITALIC = "String  \"Times-BoldItalic\""
ZAPFDINGBATS = "String  \"ZapfDingbats\""
ASCENT = "int  1"
CAPHEIGHT = "int  2"
DESCENT = "int  3"
ITALICANGLE = "int  4"
BBOXLLX = "int  5"
BBOXLLY = "int  6"
BBOXURX = "int  7"
BBOXURY = "int  8"
AWT_ASCENT = "int  9"
AWT_DESCENT = "int  10"
AWT_LEADING = "int  11"
AWT_MAXADVANCE = "int  12"
FONT_TYPE_T1 = "int  0"
FONT_TYPE_TT = "int  1"
FONT_TYPE_CJK = "int  2"
FONT_TYPE_TTUNI = "int  3"
FONT_TYPE_DOCUMENT = "int  4"
IDENTITY_H = "String  \"Identity-H\""
IDENTITY_V = "String  \"Identity-V\""
CP1250 = "String  \"Cp1250\""
CP1252 = "String  \"Cp1252\""
CP1257 = "String  \"Cp1257\""
WINANSI = "String  \"Cp1252\""
MACROMAN = "String  \"MacRoman\""
EMBEDDED = "boolean  true"
NOT_EMBEDDED = "boolean  false"
CACHED = "boolean  true"
NOT_CACHED = "boolean  false"
RESOURCE_PATH = "String  \"com/lowagie/text/pdf/fonts/\""
CID_NEWLINE = "char  '\u7fff'"
notdef = "String  \".notdef\""
def getWidth():
    '''returns int\n\n
    getWidth(final char char1)\n
    getWidth(final String text)\n
    '''
def getDescent():
    '''returns int\n\n
    getDescent(final String text)\n
    '''
def getAscent():
    '''returns int\n\n
    getAscent(final String text)\n
    '''
def getDescentPoint():
    '''returns float\n\n
    getDescentPoint(final String text, final float fontSize)\n
    '''
def getAscentPoint():
    '''returns float\n\n
    getAscentPoint(final String text, final float fontSize)\n
    '''
def getWidthPointKerned():
    '''returns float\n\n
    getWidthPointKerned(final String text, final float fontSize)\n
    '''
def getWidthPoint():
    '''returns float\n\n
    getWidthPoint(final String text, final float fontSize)\n
    getWidthPoint(final char char1, final float fontSize)\n
    '''
def getEncoding():
    '''returns String\n\n
    getEncoding()\n
    '''
def getFontType():
    '''returns int\n\n
    getFontType()\n
    '''
def isEmbedded():
    '''returns boolean\n\n
    isEmbedded()\n
    '''
def isFontSpecific():
    '''returns boolean\n\n
    isFontSpecific()\n
    '''
def getCodePagesSupported():
    '''returns String[]\n\n
    getCodePagesSupported()\n
    '''
def getWidths():
    '''returns int[]\n\n
    getWidths()\n
    '''
def getDifferences():
    '''returns String[]\n\n
    getDifferences()\n
    '''
def getUnicodeDifferences():
    '''returns char[]\n\n
    getUnicodeDifferences()\n
    '''
def isForceWidthsOutput():
    '''returns boolean\n\n
    isForceWidthsOutput()\n
    '''
def setForceWidthsOutput():
    '''returns None\n\n
    setForceWidthsOutput(final boolean forceWidthsOutput)\n
    '''
def isDirectTextToByte():
    '''returns boolean\n\n
    isDirectTextToByte()\n
    '''
def setDirectTextToByte():
    '''returns None\n\n
    setDirectTextToByte(final boolean directTextToByte)\n
    '''
def isSubset():
    '''returns boolean\n\n
    isSubset()\n
    '''
def setSubset():
    '''returns None\n\n
    setSubset(final boolean subset)\n
    '''
def getUnicodeEquivalent():
    '''returns char\n\n
    getUnicodeEquivalent(final char c)\n
    '''
def getCidCode():
    '''returns char\n\n
    getCidCode(final char c)\n
    '''
def charExists():
    '''returns boolean\n\n
    charExists(final char c)\n
    '''
def setCharAdvance():
    '''returns boolean\n\n
    setCharAdvance(final char c, final int advance)\n
    '''
def getCharBBox():
    '''returns int[]\n\n
    getCharBBox(final char c)\n
    '''
def ():
    '''returns StreamFont\n\n
    (final byte[] contents, final int[] lengths)\n
    (final byte[] contents, final String subType)\n
    '''
