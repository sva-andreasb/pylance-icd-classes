def ():
    '''returns ClassFile\n\n
    (final int magic, final int minor_version, final int major_version, final ConstantPool constant_pool, final AccessFlags access_flags, final int this_class, final int super_class, final int[] interfaces, final Field[] fields, final Method[] methods, final Attributes attributes)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getSuperclassName():
    '''returns String\n\n
    getSuperclassName()\n
    '''
def getInterfaceName():
    '''returns String\n\n
    getInterfaceName(final int n)\n
    '''
def getAttribute():
    '''returns Attribute\n\n
    getAttribute(final String s)\n
    '''
def isClass():
    '''returns boolean\n\n
    isClass()\n
    '''
def isInterface():
    '''returns boolean\n\n
    isInterface()\n
    '''
def byteLength():
    '''returns int\n\n
    byteLength()\n
    '''
