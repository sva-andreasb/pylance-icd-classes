TYPE_BEGIN = "byte  98"
TYPE_END = "byte  101"
MAXDATALENGTH = "int  32760"
def ():
    '''returns StructuredFieldHeader\n\n
    (final byte sfClass, final byte sfType, final byte sfForm, final byte sfFlags)\n
    (final byte[] array)\n
    '''
def isType():
    '''returns boolean\n\n
    isType(final byte b)\n
    '''
def getType():
    '''returns byte\n\n
    getType()\n
    '''
def isForm():
    '''returns boolean\n\n
    isForm(final byte b)\n
    '''
def getForm():
    '''returns byte\n\n
    getForm()\n
    '''
def getSFClass():
    '''returns int\n\n
    getSFClass()\n
    '''
def isClass():
    '''returns boolean\n\n
    isClass(final int n)\n
    '''
def getInt():
    '''returns int\n\n
    getInt(final byte[] array, final int n)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
