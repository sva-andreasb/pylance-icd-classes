INVALID_CHAR_FOUND = "int  0"
ILLEGAL_CHAR_FOUND = "int  1"
PROHIBITED_ERROR = "int  2"
UNASSIGNED_ERROR = "int  3"
CHECK_BIDI_ERROR = "int  4"
STD3_ASCII_RULES_ERROR = "int  5"
ACE_PREFIX_ERROR = "int  6"
VERIFICATION_ERROR = "int  7"
LABEL_TOO_LONG_ERROR = "int  8"
BUFFER_OVERFLOW_ERROR = "int  9"
ZERO_LENGTH_LABEL = "int  10"
DOMAIN_NAME_TOO_LONG_ERROR = "int  11"
def ():
    '''returns StringPrepParseException\n\n
    (final String message, final int error)\n
    (final String message, final int error, final String rules, final int pos)\n
    (final String message, final int error, final String rules, final int pos, final int lineNumber)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getError():
    '''returns int\n\n
    getError()\n
    '''
