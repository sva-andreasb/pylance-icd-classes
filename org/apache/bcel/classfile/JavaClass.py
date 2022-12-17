HEAP = "byte  1"
FILE = "byte  2"
ZIP = "byte  3"
def ():
    '''returns JavaClass\n\n
    (final int class_name_index, final int superclass_name_index, final String file_name, final int major, final int minor, final int access_flags, final ConstantPool constant_pool, int[] interfaces, Field[] fields, Method[] methods, Attribute[] attributes, final byte source)\n
    (final int class_name_index, final int superclass_name_index, final String file_name, final int major, final int minor, final int access_flags, final ConstantPool constant_pool, final int[] interfaces, final Field[] fields, final Method[] methods, final Attribute[] attributes)\n
    '''
def accept():
    '''returns None\n\n
    accept(final Visitor v)\n
    '''
def dump():
    '''returns None\n\n
    dump(final File file)\n
    dump(final String _file_name)\n
    dump(final OutputStream file)\n
    dump(final DataOutputStream file)\n
    '''
def getBytes():
    '''returns byte[]\n\n
    getBytes()\n
    '''
def getAttributes():
    '''returns Attribute[]\n\n
    getAttributes()\n
    '''
def getClassName():
    '''returns String\n\n
    getClassName()\n
    '''
def getPackageName():
    '''returns String\n\n
    getPackageName()\n
    '''
def getClassNameIndex():
    '''returns int\n\n
    getClassNameIndex()\n
    '''
def getConstantPool():
    '''returns ConstantPool\n\n
    getConstantPool()\n
    '''
def getFields():
    '''returns Field[]\n\n
    getFields()\n
    '''
def getFileName():
    '''returns String\n\n
    getFileName()\n
    '''
def getInterfaceNames():
    '''returns String[]\n\n
    getInterfaceNames()\n
    '''
def getInterfaceIndices():
    '''returns int[]\n\n
    getInterfaceIndices()\n
    '''
def getMajor():
    '''returns int\n\n
    getMajor()\n
    '''
def getMethods():
    '''returns Method[]\n\n
    getMethods()\n
    '''
def getMethod():
    '''returns Method\n\n
    getMethod(final java.lang.reflect.Method m)\n
    '''
def getMinor():
    '''returns int\n\n
    getMinor()\n
    '''
def getSourceFileName():
    '''returns String\n\n
    getSourceFileName()\n
    '''
def getSuperclassName():
    '''returns String\n\n
    getSuperclassName()\n
    '''
def getSuperclassNameIndex():
    '''returns int\n\n
    getSuperclassNameIndex()\n
    '''
def setAttributes():
    '''returns None\n\n
    setAttributes(final Attribute[] attributes)\n
    '''
def setClassName():
    '''returns None\n\n
    setClassName(final String class_name)\n
    '''
def setClassNameIndex():
    '''returns None\n\n
    setClassNameIndex(final int class_name_index)\n
    '''
def setConstantPool():
    '''returns None\n\n
    setConstantPool(final ConstantPool constant_pool)\n
    '''
def setFields():
    '''returns None\n\n
    setFields(final Field[] fields)\n
    '''
def setFileName():
    '''returns None\n\n
    setFileName(final String file_name)\n
    '''
def setInterfaceNames():
    '''returns None\n\n
    setInterfaceNames(final String[] interface_names)\n
    '''
def setInterfaces():
    '''returns None\n\n
    setInterfaces(final int[] interfaces)\n
    '''
def setMajor():
    '''returns None\n\n
    setMajor(final int major)\n
    '''
def setMethods():
    '''returns None\n\n
    setMethods(final Method[] methods)\n
    '''
def setMinor():
    '''returns None\n\n
    setMinor(final int minor)\n
    '''
def setSourceFileName():
    '''returns None\n\n
    setSourceFileName(final String source_file_name)\n
    '''
def setSuperclassName():
    '''returns None\n\n
    setSuperclassName(final String superclass_name)\n
    '''
def setSuperclassNameIndex():
    '''returns None\n\n
    setSuperclassNameIndex(final int superclass_name_index)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def copy():
    '''returns JavaClass\n\n
    copy()\n
    '''
def getRepository():
    '''returns Repository\n\n
    getRepository()\n
    '''
def setRepository():
    '''returns None\n\n
    setRepository(final Repository repository)\n
    '''
def implementationOf():
    '''returns boolean\n\n
    implementationOf(final JavaClass inter)\n
    '''
def getSuperClass():
    '''returns JavaClass\n\n
    getSuperClass()\n
    '''
def getSuperClasses():
    '''returns JavaClass[]\n\n
    getSuperClasses()\n
    '''
def getInterfaces():
    '''returns JavaClass[]\n\n
    getInterfaces()\n
    '''
def getAllInterfaces():
    '''returns JavaClass[]\n\n
    getAllInterfaces()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    equals(final Object o1, final Object o2)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    hashCode(final Object o)\n
    '''
