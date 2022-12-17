NAME_NO_PREFERENCE = "int  0"
NAME_NOT_PREFERRED = "int  1"
NAME_PREFERRED = "int  2"
NAME_PREFERRED_RESOURCE_EXISTS = "int  3"
def ():
    '''returns PreferredResources\n\n
    (final InputStream inputStream)\n
    '''
def write():
    '''returns None\n\n
    write(final OutputStream out)\n
    '''
def getDefaultPreference():
    '''returns Boolean\n\n
    getDefaultPreference()\n
    '''
def setNameState():
    '''returns None\n\n
    setNameState(final String s, final int value)\n
    '''
def getNameState():
    '''returns int\n\n
    getNameState(final String s, final boolean b)\n
    '''
def getWildcardPreference():
    '''returns Boolean\n\n
    getWildcardPreference(final String s)\n
    '''
