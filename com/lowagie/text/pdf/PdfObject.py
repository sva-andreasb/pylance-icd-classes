BOOLEAN = "int  1"
NUMBER = "int  2"
STRING = "int  3"
NAME = "int  4"
ARRAY = "int  5"
DICTIONARY = "int  6"
STREAM = "int  7"
NULL = "int  8"
INDIRECT = "int  10"
NOTHING = "String  \"\""
TEXT_PDFDOCENCODING = "String  \"PDF\""
TEXT_UNICODE = "String  \"UnicodeBig\""
def toPdf():
    '''returns None\n\n
    toPdf(final PdfWriter writer, final OutputStream os)\n
    '''
def getBytes():
    '''returns byte[]\n\n
    getBytes()\n
    '''
def canBeInObjStm():
    '''returns boolean\n\n
    canBeInObjStm()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def length():
    '''returns int\n\n
    length()\n
    '''
def type():
    '''returns int\n\n
    type()\n
    '''
def isNull():
    '''returns boolean\n\n
    isNull()\n
    '''
def isBoolean():
    '''returns boolean\n\n
    isBoolean()\n
    '''
def isNumber():
    '''returns boolean\n\n
    isNumber()\n
    '''
def isString():
    '''returns boolean\n\n
    isString()\n
    '''
def isName():
    '''returns boolean\n\n
    isName()\n
    '''
def isArray():
    '''returns boolean\n\n
    isArray()\n
    '''
def isDictionary():
    '''returns boolean\n\n
    isDictionary()\n
    '''
def isStream():
    '''returns boolean\n\n
    isStream()\n
    '''
def isIndirect():
    '''returns boolean\n\n
    isIndirect()\n
    '''
def getIndRef():
    '''returns PRIndirectReference\n\n
    getIndRef()\n
    '''
def setIndRef():
    '''returns None\n\n
    setIndRef(final PRIndirectReference indRef)\n
    '''
