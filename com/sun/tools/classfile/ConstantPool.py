CONSTANT_Utf8 = "int  1"
CONSTANT_Integer = "int  3"
CONSTANT_Float = "int  4"
CONSTANT_Long = "int  5"
CONSTANT_Double = "int  6"
CONSTANT_Class = "int  7"
CONSTANT_String = "int  8"
CONSTANT_Fieldref = "int  9"
CONSTANT_Methodref = "int  10"
CONSTANT_InterfaceMethodref = "int  11"
CONSTANT_NameAndType = "int  12"
CONSTANT_MethodHandle = "int  15"
CONSTANT_MethodType = "int  16"
CONSTANT_InvokeDynamic = "int  18"
def ():
    '''returns CONSTANT_Utf8_info\n\n
    (final CPInfo[] pool)\n
    (final ConstantPool constantPool, final int name_index)\n
    (final double value)\n
    (final ConstantPool constantPool, final int n, final int n2)\n
    (final float value)\n
    (final int value)\n
    (final ConstantPool constantPool, final int n, final int n2)\n
    (final ConstantPool constantPool, final int bootstrap_method_attr_index, final int name_and_type_index)\n
    (final long value)\n
    (final ConstantPool constantPool, final RefKind reference_kind, final int reference_index)\n
    (final ConstantPool constantPool, final int descriptor_index)\n
    (final ConstantPool constantPool, final int n, final int n2)\n
    (final ConstantPool constantPool, final int name_index, final int type_index)\n
    (final ConstantPool constantPool, final int string_index)\n
    (final String value)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    size()\n
    size()\n
    size()\n
    '''
def byteLength():
    '''returns int\n\n
    byteLength()\n
    byteLength()\n
    byteLength()\n
    byteLength()\n
    byteLength()\n
    byteLength()\n
    byteLength()\n
    byteLength()\n
    byteLength()\n
    byteLength()\n
    byteLength()\n
    byteLength()\n
    byteLength()\n
    '''
def get():
    '''returns CPInfo\n\n
    get(final int n)\n
    '''
def getUTF8Info():
    '''returns CONSTANT_Utf8_info\n\n
    getUTF8Info(final int n)\n
    '''
def getClassInfo():
    '''returns CONSTANT_Class_info\n\n
    getClassInfo(final int n)\n
    getClassInfo()\n
    '''
def getNameAndTypeInfo():
    '''returns CONSTANT_NameAndType_info\n\n
    getNameAndTypeInfo(final int n)\n
    getNameAndTypeInfo()\n
    getNameAndTypeInfo()\n
    '''
def getUTF8Value():
    '''returns String\n\n
    getUTF8Value(final int n)\n
    '''
def getUTF8Index():
    '''returns int\n\n
    getUTF8Index(final String anObject)\n
    '''
def entries():
    '''returns Iterable<CPInfo>\n\n
    entries()\n
    '''
def iterator():
    '''returns Iterator<CPInfo>\n\n
    iterator()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns CPInfo\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage()\n
    getMessage()\n
    getMessage()\n
    getMessage()\n
    '''
def getTag():
    '''returns int\n\n
    getTag()\n
    getTag()\n
    getTag()\n
    getTag()\n
    getTag()\n
    getTag()\n
    getTag()\n
    getTag()\n
    getTag()\n
    getTag()\n
    getTag()\n
    getTag()\n
    '''
def getClassName():
    '''returns String\n\n
    getClassName()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    getName()\n
    '''
def getBaseName():
    '''returns String\n\n
    getBaseName()\n
    '''
def getDimensionCount():
    '''returns int\n\n
    getDimensionCount()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    '''
def getCPRefInfo():
    '''returns CPRefInfo\n\n
    getCPRefInfo()\n
    '''
def getType():
    '''returns String\n\n
    getType()\n
    getType()\n
    '''
def getString():
    '''returns String\n\n
    getString()\n
    '''
def write():
    '''returns None\n\n
    write(final int n)\n
    '''
