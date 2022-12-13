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
def BaseField():
    '''public BaseField(final PdfWriter writer, final Rectangle box, final String fieldName)
    '''
def getBorderWidth():
    '''public float getBorderWidth()
    '''
def setBorderWidth():
    '''public void setBorderWidth(final float borderWidth)
    '''
def getBorderStyle():
    '''public int getBorderStyle()
    '''
def setBorderStyle():
    '''public void setBorderStyle(final int borderStyle)
    '''
def getBorderColor():
    '''public Color getBorderColor()
    '''
def setBorderColor():
    '''public void setBorderColor(final Color borderColor)
    '''
def getBackgroundColor():
    '''public Color getBackgroundColor()
    '''
def setBackgroundColor():
    '''public void setBackgroundColor(final Color backgroundColor)
    '''
def getTextColor():
    '''public Color getTextColor()
    '''
def setTextColor():
    '''public void setTextColor(final Color textColor)
    '''
def getFont():
    '''public BaseFont getFont()
    '''
def setFont():
    '''public void setFont(final BaseFont font)
    '''
def getFontSize():
    '''public float getFontSize()
    '''
def setFontSize():
    '''public void setFontSize(final float fontSize)
    '''
def getAlignment():
    '''public int getAlignment()
    '''
def setAlignment():
    '''public void setAlignment(final int alignment)
    '''
def getText():
    '''public String getText()
    '''
def setText():
    '''public void setText(final String text)
    '''
def getBox():
    '''public Rectangle getBox()
    '''
def setBox():
    '''public void setBox(final Rectangle box)
    '''
def getRotation():
    '''public int getRotation()
    '''
def setRotation():
    '''public void setRotation(int rotation)
    '''
def setRotationFromPage():
    '''public void setRotationFromPage(final Rectangle page)
    '''
def getVisibility():
    '''public int getVisibility()
    '''
def setVisibility():
    '''public void setVisibility(final int visibility)
    '''
def getFieldName():
    '''public String getFieldName()
    '''
def setFieldName():
    '''public void setFieldName(final String fieldName)
    '''
def getOptions():
    '''public int getOptions()
    '''
def setOptions():
    '''public void setOptions(final int options)
    '''
def getMaxCharacterLength():
    '''public int getMaxCharacterLength()
    '''
def setMaxCharacterLength():
    '''public void setMaxCharacterLength(final int maxCharacterLength)
    '''
def getWriter():
    '''public PdfWriter getWriter()
    '''
def setWriter():
    '''public void setWriter(final PdfWriter writer)
    '''
def moveFields():
    '''public static void moveFields(final PdfDictionary from, final PdfDictionary to)
    '''
