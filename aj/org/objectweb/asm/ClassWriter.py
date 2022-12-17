COMPUTE_MAXS = "int  1"
COMPUTE_FRAMES = "int  2"
def ():
    '''returns ClassWriter\n\n
    (final int n)\n
    (final ClassReader m, final int n)\n
    '''
def toByteArray():
    '''returns byte[]\n\n
    toByteArray()\n
    '''
def newConst():
    '''returns int\n\n
    newConst(final Object o)\n
    '''
def newUTF8():
    '''returns int\n\n
    newUTF8(final String s)\n
    '''
def newClass():
    '''returns int\n\n
    newClass(final String s)\n
    '''
def newMethodType():
    '''returns int\n\n
    newMethodType(final String s)\n
    '''
def newHandle():
    '''returns int\n\n
    newHandle(final int n, final String s, final String s2, final String s3)\n
    '''
def newInvokeDynamic():
    '''returns int\n\n
    newInvokeDynamic(final String s, final String s2, final Handle handle, final Object... array)\n
    '''
def newField():
    '''returns int\n\n
    newField(final String s, final String s2, final String s3)\n
    '''
def newMethod():
    '''returns int\n\n
    newMethod(final String s, final String s2, final String s3, final boolean b)\n
    '''
def newNameType():
    '''returns int\n\n
    newNameType(final String s, final String s2)\n
    '''
