GET_PROPERTY = "int  0"
NEXT = "int  1"
REQUIRE = "int  2"
GET_ELEMENT_TEXT = "int  3"
NEXT_TAG = "int  4"
HAS_NEXT = "int  5"
CLOSE = "int  6"
GET_NAMESPACE_URI_STRING = "int  7"
IS_START_ELEMENT = "int  8"
IS_END_ELEMENT = "int  9"
IS_CHARACTERS = "int  10"
IS_WHITESPACE = "int  11"
GET_ATTRIBUTE_VALUE_STRING_STRING = "int  12"
GET_ATTRIBUTE_COUNT = "int  13"
GET_ATTRIBUTE_NAME = "int  14"
GET_ATTRIBUTE_NAMESPACE = "int  15"
GET_ATTRIBUTE_LOCALNAME = "int  16"
GET_ATTRIBUTE_PREFIX = "int  17"
GET_ATTRIBUTE_TYPE = "int  18"
GET_ATTRIBUTE_VALUE_INT = "int  19"
IS_ATTRIBUTE_SPECIFIED = "int  20"
GET_NAMESPACE_COUNT = "int  21"
GET_NAMESPACE_PREFIX = "int  22"
GET_NAMESPACE_URI_INT = "int  23"
GET_EVENT_TYPE = "int  24"
GET_NAMESPACE_CONTEXT = "int  25"
GET_TEXT = "int  26"
GET_TEXT_CHARACTERS = "int  27"
GET_TEXT_CHARACTERS_ARGS = "int  28"
GET_TEXT_START = "int  29"
GET_TEXT_LENGTH = "int  30"
GET_ENCODING = "int  31"
HAS_TEXT = "int  32"
GET_LOCATION = "int  33"
GET_NAME = "int  34"
GET_LOCAL_NAME = "int  35"
HAS_NAME = "int  36"
GET_NAMESPACE_URI = "int  37"
GET_PREFIX = "int  38"
GET_VERSION = "int  39"
IS_STANDALONE = "int  40"
STANDALONE_SET = "int  41"
GET_CHARACTER_ENCODING_SCHEME = "int  42"
GET_PI_TARGET = "int  43"
GET_PI_DATA = "int  44"
WRITE_START_ELEMENT = "int  101"
WRITE_EMPTY_ELEMENT = "int  102"
WRITE_END_ELEMENT = "int  103"
WRITE_START_DOCUMENT = "int  104"
WRITE_END_DOCUMENT = "int  105"
WRITE_ATTRIBUTE = "int  106"
WRITE_NAMESPACE = "int  107"
WRITE_DEFAULT_NAMESPACE = "int  108"
WRITE_PROCESSING_INSTRUCTION = "int  109"
WRITE_CDATA = "int  110"
WRITE_COMMENT = "int  111"
WRITE_DTD = "int  112"
WRITE_ENTITY_REF = "int  113"
WRITE_CHARACTERS = "int  114"
FLUSH = "int  115"
SET_PREFIX = "int  116"
SET_DEFAULT_NAMESPACE = "int  117"
SET_NAMESPACE_CONTEXT = "int  118"
def ():
    '''returns MethodCallObjects\n\n
    ()\n
    (final int fCode)\n
    (final int n, final int fArg)\n
    (final int n, final String fArg)\n
    (final int n, final Object[] fArgs)\n
    '''
def log():
    '''returns None\n\n
    log(final int n)\n
    log(final int n, final int n2)\n
    log(final int n, final String s)\n
    log(final int n, final String s, final String s2)\n
    log(final int n, final String s, final String s2, final String s3)\n
    log(final int n, final Object[] array)\n
    '''
def logReturn():
    '''returns None\n\n
    logReturn()\n
    logReturn(final int value)\n
    logReturn(final boolean value)\n
    logReturn(final Object o)\n
    '''
def logException():
    '''returns None\n\n
    logException(final Exception ex)\n
    '''
def writeReadableProfile():
    '''returns None\n\n
    writeReadableProfile(final String s)\n
    '''
def writeStAXProfile():
    '''returns None\n\n
    writeStAXProfile(final String s)\n
    '''
def addReturn():
    '''returns None\n\n
    addReturn(final Object fReturnVal)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    '''
