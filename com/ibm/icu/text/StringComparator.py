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
