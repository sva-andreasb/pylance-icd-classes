def ():
    '''returns MetaFile\n\n
    (final String label, String fn)\n
    '''
def existsMetaData():
    '''returns boolean\n\n
    existsMetaData()\n
    '''
def getFilename():
    '''returns String\n\n
    getFilename()\n
    '''
def hasProperty():
    '''returns boolean\n\n
    hasProperty(final String key)\n
    '''
def getProperty():
    '''returns String\n\n
    getProperty(final String key)\n
    getProperty(final String key, final String defaultString)\n
    '''
def getPropertyAsInteger():
    '''returns int\n\n
    getPropertyAsInteger(final String key)\n
    getPropertyAsInteger(final String key, final int defaultValue)\n
    '''
def getPropertySplit():
    '''returns String[]\n\n
    getPropertySplit(final String key)\n
    getPropertySplit(final String key, final String defaultString)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String key, final String value)\n
    setProperty(final String key, final int value)\n
    '''
def propertyEquals():
    '''returns boolean\n\n
    propertyEquals(final String key, final String value)\n
    '''
def ensurePropertySet():
    '''returns None\n\n
    ensurePropertySet(final String key, final String expected)\n
    '''
def getOrSetDefault():
    '''returns String\n\n
    getOrSetDefault(final String key, final String expected)\n
    '''
def checkOrSetMetadata():
    '''returns None\n\n
    checkOrSetMetadata(final String key, final String expected)\n
    '''
def checkMetadata():
    '''returns None\n\n
    checkMetadata(final String key, final String expected)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def dump():
    '''returns None\n\n
    dump(final PrintStream output)\n
    '''
def sync():
    '''returns None\n\n
    sync()\n
    sync(final boolean force)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def compare():
    '''returns int\n\n
    compare(final String o1, final String o2)\n
    '''
