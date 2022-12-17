def ():
    '''returns ClassGen\n\n
    (final String classname, final String superclassname, final String filename, final int modifiers, final String[] interfacenames, final ConstantPool cpool)\n
    (final String classname, final String superclassname, final String filename, final int modifiers, final String[] interfacenames)\n
    (final JavaClass clazz)\n
    '''
def getJavaClass():
    '''returns JavaClass\n\n
    getJavaClass()\n
    '''
def addInterface():
    '''returns None\n\n
    addInterface(final String name)\n
    '''
def removeInterface():
    '''returns None\n\n
    removeInterface(final String name)\n
    '''
def getMajor():
    '''returns int\n\n
    getMajor()\n
    '''
def setMajor():
    '''returns None\n\n
    setMajor(final int major)\n
    '''
def setMinor():
    '''returns None\n\n
    setMinor(final int minor)\n
    '''
def getMinor():
    '''returns int\n\n
    getMinor()\n
    '''
def addAttribute():
    '''returns None\n\n
    addAttribute(final Attribute a)\n
    '''
def addAnnotation():
    '''returns None\n\n
    addAnnotation(final AnnotationGen a)\n
    '''
def addMethod():
    '''returns None\n\n
    addMethod(final Method m)\n
    '''
def addEmptyConstructor():
    '''returns None\n\n
    addEmptyConstructor(final int access_flags)\n
    '''
def addField():
    '''returns None\n\n
    addField(final Field f)\n
    '''
def containsField():
    '''returns Field\n\n
    containsField(final Field f)\n
    containsField(final String name)\n
    '''
def containsMethod():
    '''returns Method\n\n
    containsMethod(final String name, final String signature)\n
    '''
def removeAttribute():
    '''returns None\n\n
    removeAttribute(final Attribute a)\n
    '''
def removeAnnotation():
    '''returns None\n\n
    removeAnnotation(final AnnotationGen a)\n
    '''
def removeMethod():
    '''returns None\n\n
    removeMethod(final Method m)\n
    '''
def replaceMethod():
    '''returns None\n\n
    replaceMethod(final Method old, final Method new_)\n
    '''
def replaceField():
    '''returns None\n\n
    replaceField(final Field old, final Field new_)\n
    '''
def removeField():
    '''returns None\n\n
    removeField(final Field f)\n
    '''
def getClassName():
    '''returns String\n\n
    getClassName()\n
    '''
def getSuperclassName():
    '''returns String\n\n
    getSuperclassName()\n
    '''
def getFileName():
    '''returns String\n\n
    getFileName()\n
    '''
def setClassName():
    '''returns None\n\n
    setClassName(final String name)\n
    '''
def setSuperclassName():
    '''returns None\n\n
    setSuperclassName(final String name)\n
    '''
def getMethods():
    '''returns Method[]\n\n
    getMethods()\n
    '''
def setMethods():
    '''returns None\n\n
    setMethods(final Method[] methods)\n
    '''
def setFields():
    '''returns None\n\n
    setFields(final Field[] fs)\n
    '''
def setMethodAt():
    '''returns None\n\n
    setMethodAt(final Method method, final int pos)\n
    '''
def getMethodAt():
    '''returns Method\n\n
    getMethodAt(final int pos)\n
    '''
def getInterfaceNames():
    '''returns String[]\n\n
    getInterfaceNames()\n
    '''
def getInterfaces():
    '''returns int[]\n\n
    getInterfaces()\n
    '''
def getFields():
    '''returns Field[]\n\n
    getFields()\n
    '''
def getAttributes():
    '''returns Collection<Attribute>\n\n
    getAttributes()\n
    '''
def getAnnotations():
    '''returns AnnotationGen[]\n\n
    getAnnotations()\n
    '''
def getConstantPool():
    '''returns ConstantPool\n\n
    getConstantPool()\n
    '''
def setConstantPool():
    '''returns None\n\n
    setConstantPool(final ConstantPool constant_pool)\n
    '''
def setClassNameIndex():
    '''returns None\n\n
    setClassNameIndex(final int class_name_index)\n
    '''
def setSuperclassNameIndex():
    '''returns None\n\n
    setSuperclassNameIndex(final int superclass_name_index)\n
    '''
def getSuperclassNameIndex():
    '''returns int\n\n
    getSuperclassNameIndex()\n
    '''
def getClassNameIndex():
    '''returns int\n\n
    getClassNameIndex()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def getSUID():
    '''returns long\n\n
    getSUID()\n
    '''
def hasAttribute():
    '''returns boolean\n\n
    hasAttribute(final String attributeName)\n
    '''
def getAttribute():
    '''returns Attribute\n\n
    getAttribute(final String attributeName)\n
    '''
def compare():
    '''returns int\n\n
    compare(final Method m0, final Method m1)\n
    compare(final Field f0, final Field f1)\n
    compare(final Method m0, final Method m1)\n
    '''
