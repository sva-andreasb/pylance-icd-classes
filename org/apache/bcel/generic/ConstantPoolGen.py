def ():
    '''returns ConstantPoolGen\n\n
    (final Constant[] cs)\n
    (final ConstantPool cp)\n
    ()\n
    '''
def lookupString():
    '''returns int\n\n
    lookupString(final String str)\n
    '''
def addString():
    '''returns int\n\n
    addString(final String str)\n
    '''
def lookupClass():
    '''returns int\n\n
    lookupClass(final String str)\n
    '''
def addClass():
    '''returns int\n\n
    addClass(final String str)\n
    addClass(final ObjectType type)\n
    '''
def addArrayClass():
    '''returns int\n\n
    addArrayClass(final ArrayType type)\n
    '''
def lookupInteger():
    '''returns int\n\n
    lookupInteger(final int n)\n
    '''
def addInteger():
    '''returns int\n\n
    addInteger(final int n)\n
    '''
def lookupFloat():
    '''returns int\n\n
    lookupFloat(final float n)\n
    '''
def addFloat():
    '''returns int\n\n
    addFloat(final float n)\n
    '''
def lookupUtf8():
    '''returns int\n\n
    lookupUtf8(final String n)\n
    '''
def addUtf8():
    '''returns int\n\n
    addUtf8(final String n)\n
    '''
def lookupLong():
    '''returns int\n\n
    lookupLong(final long n)\n
    '''
def addLong():
    '''returns int\n\n
    addLong(final long n)\n
    '''
def lookupDouble():
    '''returns int\n\n
    lookupDouble(final double n)\n
    '''
def addDouble():
    '''returns int\n\n
    addDouble(final double n)\n
    '''
def lookupNameAndType():
    '''returns int\n\n
    lookupNameAndType(final String name, final String signature)\n
    '''
def addNameAndType():
    '''returns int\n\n
    addNameAndType(final String name, final String signature)\n
    '''
def lookupMethodref():
    '''returns int\n\n
    lookupMethodref(final String class_name, final String method_name, final String signature)\n
    lookupMethodref(final MethodGen method)\n
    '''
def addMethodref():
    '''returns int\n\n
    addMethodref(final String class_name, final String method_name, final String signature)\n
    addMethodref(final MethodGen method)\n
    '''
def lookupInterfaceMethodref():
    '''returns int\n\n
    lookupInterfaceMethodref(final String class_name, final String method_name, final String signature)\n
    lookupInterfaceMethodref(final MethodGen method)\n
    '''
def addInterfaceMethodref():
    '''returns int\n\n
    addInterfaceMethodref(final String class_name, final String method_name, final String signature)\n
    addInterfaceMethodref(final MethodGen method)\n
    '''
def lookupFieldref():
    '''returns int\n\n
    lookupFieldref(final String class_name, final String field_name, final String signature)\n
    '''
def addFieldref():
    '''returns int\n\n
    addFieldref(final String class_name, final String field_name, final String signature)\n
    '''
def getConstant():
    '''returns Constant\n\n
    getConstant(final int i)\n
    '''
def setConstant():
    '''returns None\n\n
    setConstant(final int i, final Constant c)\n
    '''
def getConstantPool():
    '''returns ConstantPool\n\n
    getConstantPool()\n
    '''
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def getFinalConstantPool():
    '''returns ConstantPool\n\n
    getFinalConstantPool()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def addConstant():
    '''returns int\n\n
    addConstant(final Constant c, final ConstantPoolGen cp)\n
    '''
