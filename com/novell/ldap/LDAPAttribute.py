def ():
    '''returns LDAPAttribute\n\n
    ()\n
    (final LDAPAttribute ldapAttribute)\n
    (final String name)\n
    (final String s, final byte[] array)\n
    (final String s, final String s2)\n
    (final String s, final String[] array)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def addValue():
    '''returns None\n\n
    addValue(final String s)\n
    addValue(final byte[] array)\n
    '''
def addBase64Value():
    '''returns None\n\n
    addBase64Value(final String s)\n
    addBase64Value(final StringBuffer sb, final int n, final int n2)\n
    addBase64Value(final char[] array)\n
    '''
def addURLValue():
    '''returns None\n\n
    addURLValue(final String spec)\n
    addURLValue(final URL url)\n
    '''
def getByteValues():
    '''returns Enumeration\n\n
    getByteValues()\n
    '''
def getStringValues():
    '''returns Enumeration\n\n
    getStringValues()\n
    '''
def getByteValueArray():
    '''returns byte[][]\n\n
    getByteValueArray()\n
    '''
def getStringValueArray():
    '''returns String[]\n\n
    getStringValueArray()\n
    '''
def getStringValue():
    '''returns String\n\n
    getStringValue()\n
    '''
def getByteValue():
    '''returns byte[]\n\n
    getByteValue()\n
    '''
def getLangSubtype():
    '''returns String\n\n
    getLangSubtype()\n
    '''
def getBaseName():
    '''returns String\n\n
    getBaseName()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getSubtypes():
    '''returns String[]\n\n
    getSubtypes()\n
    '''
def hasSubtype():
    '''returns boolean\n\n
    hasSubtype(final String anotherString)\n
    '''
def hasSubtypes():
    '''returns boolean\n\n
    hasSubtypes(final String[] array)\n
    '''
def removeValue():
    '''returns None\n\n
    removeValue(final String s)\n
    removeValue(final byte[] array)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Object o)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def writeDSML():
    '''returns None\n\n
    writeDSML(final OutputStream out)\n
    '''
def writeExternal():
    '''returns None\n\n
    writeExternal(final ObjectOutput objectOutput)\n
    '''
def readExternal():
    '''returns None\n\n
    readExternal(final ObjectInput objectInput)\n
    '''
