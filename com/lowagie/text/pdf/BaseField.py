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
pass
def getBorderWidth():
'''public float getBorderWidth()
'''
pass
def setBorderWidth():
'''public void setBorderWidth(final float borderWidth)
'''
pass
def getBorderStyle():
'''public int getBorderStyle()
'''
pass
def setBorderStyle():
'''public void setBorderStyle(final int borderStyle)
'''
pass
def getBorderColor():
'''public Color getBorderColor()
'''
pass
def setBorderColor():
'''public void setBorderColor(final Color borderColor)
'''
pass
def getBackgroundColor():
'''public Color getBackgroundColor()
'''
pass
def setBackgroundColor():
'''public void setBackgroundColor(final Color backgroundColor)
'''
pass
def getTextColor():
'''public Color getTextColor()
'''
pass
def setTextColor():
'''public void setTextColor(final Color textColor)
'''
pass
def getFont():
'''public BaseFont getFont()
'''
pass
def setFont():
'''public void setFont(final BaseFont font)
'''
pass
def getFontSize():
'''public float getFontSize()
'''
pass
def setFontSize():
'''public void setFontSize(final float fontSize)
'''
pass
def getAlignment():
'''public int getAlignment()
'''
pass
def setAlignment():
'''public void setAlignment(final int alignment)
'''
pass
def getText():
'''public String getText()
'''
pass
def setText():
'''public void setText(final String text)
'''
pass
def getBox():
'''public Rectangle getBox()
'''
pass
def setBox():
'''public void setBox(final Rectangle box)
'''
pass
def getRotation():
'''public int getRotation()
'''
pass
def setRotation():
'''public void setRotation(int rotation)
'''
pass
def setRotationFromPage():
'''public void setRotationFromPage(final Rectangle page)
'''
pass
def getVisibility():
'''public int getVisibility()
'''
pass
def setVisibility():
'''public void setVisibility(final int visibility)
'''
pass
def getFieldName():
'''public String getFieldName()
'''
pass
def setFieldName():
'''public void setFieldName(final String fieldName)
'''
pass
def getOptions():
'''public int getOptions()
'''
pass
def setOptions():
'''public void setOptions(final int options)
'''
pass
def getMaxCharacterLength():
'''public int getMaxCharacterLength()
'''
pass
def setMaxCharacterLength():
'''public void setMaxCharacterLength(final int maxCharacterLength)
'''
pass
def getWriter():
'''public PdfWriter getWriter()
'''
pass
def setWriter():
'''public void setWriter(final PdfWriter writer)
'''
pass
def moveFields():
'''public static void moveFields(final PdfDictionary from, final PdfDictionary to)
'''
pass
