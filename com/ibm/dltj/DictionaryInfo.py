VIEWABLE_DEFAULT = "boolean  false"
PROPER_CASE_DEFAULT = "boolean  false"
LOWER_CASE_DEFAULT = "boolean  false"
DLT_REL_COMPAT_V53 = "int  5300"
DLT_REL_COMPAT_V60 = "int  6000"
DLT_REL_COMPAT_V61 = "int  6100"
DLT_REL_COMPAT_V70 = "int  7000"
RELEASE_COMPAT_DEFAULT = "int  6100"
LATIN1 = "String  \"Latin1\""
def ():
    '''returns DictionaryInfo\n\n
    ()\n
    (final long n, final boolean b, final boolean b2, final boolean b3, final boolean b4, final boolean b5, final String s)\n
    (final long n, final boolean b, final boolean b2, final boolean b3, final boolean b4, final boolean b5, final String s, final boolean b6, final boolean b7, final boolean b8)\n
    (final long version, final boolean isEditable, final boolean isMinimizable, final boolean isMinimized, final boolean isDeterministic, final boolean isReversed, final String copyrightStatement, final boolean isProperCase, final boolean isLowerCase, final boolean isViewable, final int releaseCompatibility)\n
    '''
def hasFunction():
    '''returns boolean\n\n
    hasFunction(final int value)\n
    '''
def setCopyrightStatement():
    '''returns None\n\n
    setCopyrightStatement(final String copyrightStatement)\n
    '''
def isEditable():
    '''returns boolean\n\n
    isEditable()\n
    '''
def setNotEditable():
    '''returns None\n\n
    setNotEditable()\n
    '''
def setNotViewable():
    '''returns None\n\n
    setNotViewable()\n
    '''
def getVersion():
    '''returns long\n\n
    getVersion()\n
    '''
def setVersion():
    '''returns None\n\n
    setVersion(final int n)\n
    '''
def getReleaseCompatibility():
    '''returns int\n\n
    getReleaseCompatibility()\n
    '''
def isProperCase():
    '''returns boolean\n\n
    isProperCase()\n
    '''
def isLowerCase():
    '''returns boolean\n\n
    isLowerCase()\n
    '''
def isViewable():
    '''returns boolean\n\n
    isViewable()\n
    '''
def getDescription():
    '''returns String\n\n
    getDescription()\n
    '''
def setDescription():
    '''returns None\n\n
    setDescription(final String description)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
