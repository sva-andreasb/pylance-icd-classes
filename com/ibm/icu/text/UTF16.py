SINGLE_CHAR_BOUNDARY = "int  1"
LEAD_SURROGATE_BOUNDARY = "int  2"
TRAIL_SURROGATE_BOUNDARY = "int  5"
CODEPOINT_MIN_VALUE = "int  0"
CODEPOINT_MAX_VALUE = "int  1114111"
SUPPLEMENTARY_MIN_VALUE = "int  65536"
LEAD_SURROGATE_MIN_VALUE = "int  55296"
TRAIL_SURROGATE_MIN_VALUE = "int  56320"
LEAD_SURROGATE_MAX_VALUE = "int  56319"
TRAIL_SURROGATE_MAX_VALUE = "int  57343"
SURROGATE_MIN_VALUE = "int  55296"
SURROGATE_MAX_VALUE = "int  57343"
FOLD_CASE_DEFAULT = "int  0"
FOLD_CASE_EXCLUDE_SPECIAL_I = "int  1"
def ():
    '''returns StringComparator\n\n
    ()\n
    (final boolean codepointcompare, final boolean ignorecase, final int foldcaseoption)\n
    '''
def setCodePointCompare():
    '''returns None\n\n
    setCodePointCompare(final boolean flag)\n
    '''
def setIgnoreCase():
    '''returns None\n\n
    setIgnoreCase(final boolean ignorecase, final int foldcaseoption)\n
    '''
def getCodePointCompare():
    '''returns boolean\n\n
    getCodePointCompare()\n
    '''
def getIgnoreCase():
    '''returns boolean\n\n
    getIgnoreCase()\n
    '''
def getIgnoreCaseOption():
    '''returns int\n\n
    getIgnoreCaseOption()\n
    '''
def compare():
    '''returns int\n\n
    compare(final String a, final String b)\n
    '''
