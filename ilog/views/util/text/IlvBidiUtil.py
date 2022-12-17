LRM = "String  \"\u200e\""
RLM = "String  \"\u200f\""
LRE = "String  \"\u202a\""
RLE = "String  \"\u202b\""
PDF = "String  \"\u202c\""
UNDEFINED_DIRECTION = "int  0"
INHERITED_DIRECTION = "int  513"
COMPONENT_DIRECTION = "int  514"
LEFT_TO_RIGHT = "int  516"
RIGHT_TO_LEFT = "int  520"
CONTEXTUAL_DIRECTION = "int  527"
CONTEXTUAL_LEFT_TO_RIGHT = "int  526"
CONTEXTUAL_RIGHT_TO_LEFT = "int  525"
UNDEFINED_DIRECTION_NAME = "String  \"Undefined\""
INHERITED_DIRECTION_NAME = "String  \"Inherited\""
COMPONENT_DIRECTION_NAME = "String  \"Component Orientation\""
LEFT_TO_RIGHT_NAME = "String  \"Left-To-Right\""
RIGHT_TO_LEFT_NAME = "String  \"Right-To-Left\""
CONTEXTUAL_DIRECTION_NAME = "String  \"Contextual\""
CONTEXTUAL_LEFT_TO_RIGHT_NAME = "String  \"Contextual Left-To-Right\""
CONTEXTUAL_RIGHT_TO_LEFT_NAME = "String  \"Contextual Right-To-Left\""
ADVANCED_BIDI = "String  \"ilog.jviews.bidi.support.on\""
BASE_TEXT_DIRECTION = "String  \"baseTextDirection\""
def ():
    '''returns BidiDocumentHandler\n\n
    ()\n
    (final JTextComponent a, final ComponentOrientation b)\n
    '''
def bidiTransform():
    '''returns String\n\n
    bidiTransform(final String s, final String s2, final String anObject)\n
    '''
def checkContextual():
    '''returns byte\n\n
    checkContextual(final String s, final String s2)\n
    '''
def insertString():
    '''returns None\n\n
    insertString(final FilterBypass fb, final int offset, final String s, final AttributeSet attr)\n
    '''
def remove():
    '''returns None\n\n
    remove(final FilterBypass fb, final int n, final int length)\n
    '''
def replace():
    '''returns None\n\n
    replace(final FilterBypass fb, final int n, final int length, final String s, final AttributeSet attrs)\n
    '''
def handleDirection():
    '''returns None\n\n
    handleDirection(final String s)\n
    '''
