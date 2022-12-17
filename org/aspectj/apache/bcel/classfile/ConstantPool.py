def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def ():
    '''returns ConstantPool\n\n
    ()\n
    (final Constant[] constants)\n
    '''
def getConstant():
    '''returns Constant\n\n
    getConstant(final int index, final byte tag)\n
    getConstant(final int index)\n
    '''
def copy():
    '''returns ConstantPool\n\n
    copy()\n
    '''
def getConstantString():
    '''returns String\n\n
    getConstantString(final int index, final byte tag)\n
    '''
def constantToString():
    '''returns String\n\n
    constantToString(Constant c)\n
    constantToString(final int index, final byte tag)\n
    constantToString(final int index)\n
    '''
def accept():
    '''returns None\n\n
    accept(final ClassVisitor v)\n
    '''
def getConstantPool():
    '''returns Constant[]\n\n
    getConstantPool()\n
    '''
def dump():
    '''returns None\n\n
    dump(final DataOutputStream file)\n
    '''
def getConstantUtf8():
    '''returns ConstantUtf8\n\n
    getConstantUtf8(final int index)\n
    '''
def getConstantString_CONSTANTClass():
    '''returns String\n\n
    getConstantString_CONSTANTClass(int index)\n
    '''
def getLength():
    '''returns int\n\n
    getLength()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def lookupInteger():
    '''returns int\n\n
    lookupInteger(final int n)\n
    '''
def lookupUtf8():
    '''returns int\n\n
    lookupUtf8(final String string)\n
    '''
def lookupClass():
    '''returns int\n\n
    lookupClass(final String classname)\n
    '''
def addUtf8():
    '''returns int\n\n
    addUtf8(final String n)\n
    '''
def addInteger():
    '''returns int\n\n
    addInteger(final int n)\n
    '''
def addArrayClass():
    '''returns int\n\n
    addArrayClass(final ArrayType type)\n
    '''
def addClass():
    '''returns int\n\n
    addClass(final ObjectType type)\n
    addClass(final String classname)\n
    '''
def addFieldref():
    '''returns int\n\n
    addFieldref(final String class_name, final String field_name, final String signature)\n
    '''
def lookupFieldref():
    '''returns int\n\n
    lookupFieldref(String searchClassname, final String searchFieldname, final String searchSignature)\n
    '''
def addNameAndType():
    '''returns int\n\n
    addNameAndType(final String name, final String signature)\n
    '''
def lookupNameAndType():
    '''returns int\n\n
    lookupNameAndType(final String searchName, final String searchTypeSignature)\n
    '''
def addFloat():
    '''returns int\n\n
    addFloat(final float f)\n
    '''
def lookupFloat():
    '''returns int\n\n
    lookupFloat(final float f)\n
    '''
def addDouble():
    '''returns int\n\n
    addDouble(final double d)\n
    '''
def lookupDouble():
    '''returns int\n\n
    lookupDouble(final double d)\n
    '''
def addLong():
    '''returns int\n\n
    addLong(final long l)\n
    '''
def lookupString():
    '''returns int\n\n
    lookupString(final String s)\n
    '''
def addString():
    '''returns int\n\n
    addString(final String str)\n
    '''
def lookupLong():
    '''returns int\n\n
    lookupLong(final long l)\n
    '''
def addConstant():
    '''returns int\n\n
    addConstant(final Constant c, final ConstantPool cp)\n
    '''
def addMethodref():
    '''returns int\n\n
    addMethodref(final String class_name, final String method_name, final String signature)\n
    '''
def addInterfaceMethodref():
    '''returns int\n\n
    addInterfaceMethodref(final String class_name, final String method_name, final String signature)\n
    '''
def lookupInterfaceMethodref():
    '''returns int\n\n
    lookupInterfaceMethodref(String searchClassname, final String searchMethodName, final String searchSignature)\n
    '''
def lookupMethodref():
    '''returns int\n\n
    lookupMethodref(String searchClassname, final String searchMethodName, final String searchSignature)\n
    '''
def getFinalConstantPool():
    '''returns ConstantPool\n\n
    getFinalConstantPool()\n
    '''
