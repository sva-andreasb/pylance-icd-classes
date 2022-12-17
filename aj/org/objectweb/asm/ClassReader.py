SKIP_CODE = "int  1"
SKIP_DEBUG = "int  2"
SKIP_FRAMES = "int  4"
EXPAND_FRAMES = "int  8"
def ():
    '''returns ClassReader\n\n
    (final byte[] array)\n
    (final byte[] b, final int n, final int n2)\n
    (final InputStream inputStream)\n
    (final String s)\n
    '''
def getAccess():
    '''returns int\n\n
    getAccess()\n
    '''
def getClassName():
    '''returns String\n\n
    getClassName()\n
    '''
def getSuperName():
    '''returns String\n\n
    getSuperName()\n
    '''
def getInterfaces():
    '''returns String[]\n\n
    getInterfaces()\n
    '''
def accept():
    '''returns None\n\n
    accept(final ClassVisitor classVisitor, final int n)\n
    accept(final ClassVisitor classVisitor, final Attribute[] array, final int n)\n
    '''
def getItemCount():
    '''returns int\n\n
    getItemCount()\n
    '''
def getItem():
    '''returns int\n\n
    getItem(final int n)\n
    '''
def getMaxStringLength():
    '''returns int\n\n
    getMaxStringLength()\n
    '''
def readByte():
    '''returns int\n\n
    readByte(final int n)\n
    '''
def readUnsignedShort():
    '''returns int\n\n
    readUnsignedShort(final int n)\n
    '''
def readShort():
    '''returns short\n\n
    readShort(final int n)\n
    '''
def readInt():
    '''returns int\n\n
    readInt(final int n)\n
    '''
def readLong():
    '''returns long\n\n
    readLong(final int n)\n
    '''
def readUTF8():
    '''returns String\n\n
    readUTF8(int n, final char[] array)\n
    '''
def readClass():
    '''returns String\n\n
    readClass(final int n, final char[] array)\n
    '''
def readConst():
    '''returns Object\n\n
    readConst(final int n, final char[] array)\n
    '''
