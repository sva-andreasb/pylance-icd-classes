def ():
    '''returns Section\n\n
    ()\n
    (final Section s)\n
    (final byte[] src, final int offset)\n
    '''
def getFormatID():
    '''returns ClassID\n\n
    getFormatID()\n
    '''
def setFormatID():
    '''returns None\n\n
    setFormatID(final ClassID formatID)\n
    setFormatID(final byte[] formatID)\n
    '''
def getOffset():
    '''returns long\n\n
    getOffset()\n
    '''
def getPropertyCount():
    '''returns int\n\n
    getPropertyCount()\n
    '''
def getProperties():
    '''returns Property[]\n\n
    getProperties()\n
    '''
def setProperties():
    '''returns None\n\n
    setProperties(final Property[] properties)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final long id)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final int id, final String value)\n
    setProperty(final int id, final int value)\n
    setProperty(final int id, final long value)\n
    setProperty(final int id, final boolean value)\n
    setProperty(final int id, final long variantType, final Object value)\n
    setProperty(final Property p)\n
    setProperty(final int id, final Object value)\n
    '''
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def wasNull():
    '''returns boolean\n\n
    wasNull()\n
    '''
def getPIDString():
    '''returns String\n\n
    getPIDString(final long pid)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def removeProperty():
    '''returns None\n\n
    removeProperty(final long id)\n
    '''
def write():
    '''returns int\n\n
    write(final OutputStream out)\n
    '''
def setDictionary():
    '''returns None\n\n
    setDictionary(final Map<Long, String> dictionary)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString(final PropertyIDMap idMap)\n
    '''
def getCodepage():
    '''returns int\n\n
    getCodepage()\n
    '''
def setCodepage():
    '''returns None\n\n
    setCodepage(final int codepage)\n
    '''
