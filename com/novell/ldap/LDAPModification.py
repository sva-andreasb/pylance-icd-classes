ADD = "int  0"
DELETE = "int  1"
REPLACE = "int  2"
def ():
    '''returns LDAPModification\n\n
    ()\n
    (final int op, final LDAPAttribute attr)\n
    '''
def getAttribute():
    '''returns LDAPAttribute\n\n
    getAttribute()\n
    '''
def getOp():
    '''returns int\n\n
    getOp()\n
    '''
def writeDSML():
    '''returns None\n\n
    writeDSML(final OutputStream out)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def writeExternal():
    '''returns None\n\n
    writeExternal(final ObjectOutput objectOutput)\n
    '''
def readExternal():
    '''returns None\n\n
    readExternal(final ObjectInput objectInput)\n
    '''
