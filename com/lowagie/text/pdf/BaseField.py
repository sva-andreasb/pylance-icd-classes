BORDER_WIDTH_THIN = "float  1.0f"
BORDER_WIDTH_MEDIUM = "float  2.0f"
BORDER_WIDTH_THICK = "float  3.0f"
VISIBLE = "int  0"
HIDDEN = "int  1"
VISIBLE_BUT_DOES_NOT_PRINT = "int  2"
HIDDEN_BUT_PRINTABLE = "int  3"
READ_ONLY = "int  1"
REQUIRED = "int  2"
MULTILINE = "int  4"
DO_NOT_SCROLL = "int  8"
PASSWORD = "int  16"
FILE_SELECTION = "int  32"
DO_NOT_SPELL_CHECK = "int  64"
EDIT = "int  128"
COMB = "int  256"
def ():
    '''returns BaseField\n\n
    (final PdfWriter writer, final Rectangle box, final String fieldName)\n
    '''
def getBorderWidth():
    '''returns float\n\n
    getBorderWidth()\n
    '''
def setBorderWidth():
    '''returns None\n\n
    setBorderWidth(final float borderWidth)\n
    '''
def getBorderStyle():
    '''returns int\n\n
    getBorderStyle()\n
    '''
def setBorderStyle():
    '''returns None\n\n
    setBorderStyle(final int borderStyle)\n
    '''
def getBorderColor():
    '''returns Color\n\n
    getBorderColor()\n
    '''
def setBorderColor():
    '''returns None\n\n
    setBorderColor(final Color borderColor)\n
    '''
def getBackgroundColor():
    '''returns Color\n\n
    getBackgroundColor()\n
    '''
def setBackgroundColor():
    '''returns None\n\n
    setBackgroundColor(final Color backgroundColor)\n
    '''
def getTextColor():
    '''returns Color\n\n
    getTextColor()\n
    '''
def setTextColor():
    '''returns None\n\n
    setTextColor(final Color textColor)\n
    '''
def getFont():
    '''returns BaseFont\n\n
    getFont()\n
    '''
def setFont():
    '''returns None\n\n
    setFont(final BaseFont font)\n
    '''
def getFontSize():
    '''returns float\n\n
    getFontSize()\n
    '''
def setFontSize():
    '''returns None\n\n
    setFontSize(final float fontSize)\n
    '''
def getAlignment():
    '''returns int\n\n
    getAlignment()\n
    '''
def setAlignment():
    '''returns None\n\n
    setAlignment(final int alignment)\n
    '''
def getText():
    '''returns String\n\n
    getText()\n
    '''
def setText():
    '''returns None\n\n
    setText(final String text)\n
    '''
def getBox():
    '''returns Rectangle\n\n
    getBox()\n
    '''
def setBox():
    '''returns None\n\n
    setBox(final Rectangle box)\n
    '''
def getRotation():
    '''returns int\n\n
    getRotation()\n
    '''
def setRotation():
    '''returns None\n\n
    setRotation(int rotation)\n
    '''
def setRotationFromPage():
    '''returns None\n\n
    setRotationFromPage(final Rectangle page)\n
    '''
def getVisibility():
    '''returns int\n\n
    getVisibility()\n
    '''
def setVisibility():
    '''returns None\n\n
    setVisibility(final int visibility)\n
    '''
def getFieldName():
    '''returns String\n\n
    getFieldName()\n
    '''
def setFieldName():
    '''returns None\n\n
    setFieldName(final String fieldName)\n
    '''
def getOptions():
    '''returns int\n\n
    getOptions()\n
    '''
def setOptions():
    '''returns None\n\n
    setOptions(final int options)\n
    '''
def getMaxCharacterLength():
    '''returns int\n\n
    getMaxCharacterLength()\n
    '''
def setMaxCharacterLength():
    '''returns None\n\n
    setMaxCharacterLength(final int maxCharacterLength)\n
    '''
def getWriter():
    '''returns PdfWriter\n\n
    getWriter()\n
    '''
def setWriter():
    '''returns None\n\n
    setWriter(final PdfWriter writer)\n
    '''
