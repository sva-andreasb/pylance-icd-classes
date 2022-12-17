def setFinder():
    '''returns None\n\n
    setFinder(final Dependency.Finder finder)\n
    '''
def setFilter():
    '''returns None\n\n
    setFilter(final Dependency.Filter filter)\n
    '''
def findAllDependencies():
    '''returns None\n\n
    findAllDependencies(final ClassFileReader classFileReader, final Set<String> set, final boolean b)\n
    findAllDependencies(final ClassFileReader classFileReader, final Set<String> c, final boolean b, final Recorder recorder)\n
    '''
def addDependency():
    '''returns None\n\n
    addDependency(final Dependency dependency)\n
    '''
def ():
    '''returns SimpleDependency\n\n
    (final String s)\n
    (final String s, final Throwable cause)\n
    (final Throwable cause)\n
    (final String name)\n
    (final Location origin, final Location target)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getClassName():
    '''returns String\n\n
    getClassName()\n
    '''
def getPackageName():
    '''returns String\n\n
    getPackageName()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def getOrigin():
    '''returns Location\n\n
    getOrigin()\n
    '''
def getTarget():
    '''returns Location\n\n
    getTarget()\n
    '''
def accepts():
    '''returns boolean\n\n
    accepts(final Dependency dependency)\n
    accepts(final Dependency dependency)\n
    accepts(final Dependency dependency)\n
    '''
def visitClass():
    '''returns Void\n\n
    visitClass(final ConstantPool.CONSTANT_Class_info constant_Class_info, final Void void1)\n
    '''
def visitDouble():
    '''returns Void\n\n
    visitDouble(final ConstantPool.CONSTANT_Double_info constant_Double_info, final Void void1)\n
    '''
def visitFieldref():
    '''returns Void\n\n
    visitFieldref(final ConstantPool.CONSTANT_Fieldref_info constant_Fieldref_info, final Void void1)\n
    '''
def visitFloat():
    '''returns Void\n\n
    visitFloat(final ConstantPool.CONSTANT_Float_info constant_Float_info, final Void void1)\n
    '''
def visitInteger():
    '''returns Void\n\n
    visitInteger(final ConstantPool.CONSTANT_Integer_info constant_Integer_info, final Void void1)\n
    '''
def visitInterfaceMethodref():
    '''returns Void\n\n
    visitInterfaceMethodref(final ConstantPool.CONSTANT_InterfaceMethodref_info constant_InterfaceMethodref_info, final Void void1)\n
    '''
def visitInvokeDynamic():
    '''returns Void\n\n
    visitInvokeDynamic(final ConstantPool.CONSTANT_InvokeDynamic_info constant_InvokeDynamic_info, final Void void1)\n
    '''
def visitLong():
    '''returns Void\n\n
    visitLong(final ConstantPool.CONSTANT_Long_info constant_Long_info, final Void void1)\n
    '''
def visitMethodHandle():
    '''returns Void\n\n
    visitMethodHandle(final ConstantPool.CONSTANT_MethodHandle_info constant_MethodHandle_info, final Void void1)\n
    '''
def visitMethodType():
    '''returns Void\n\n
    visitMethodType(final ConstantPool.CONSTANT_MethodType_info constant_MethodType_info, final Void void1)\n
    visitMethodType(final Type.MethodType methodType, final Void void1)\n
    '''
def visitMethodref():
    '''returns Void\n\n
    visitMethodref(final ConstantPool.CONSTANT_Methodref_info constant_Methodref_info, final Void void1)\n
    '''
def visitNameAndType():
    '''returns Void\n\n
    visitNameAndType(final ConstantPool.CONSTANT_NameAndType_info constant_NameAndType_info, final Void void1)\n
    '''
def visitString():
    '''returns Void\n\n
    visitString(final ConstantPool.CONSTANT_String_info constant_String_info, final Void void1)\n
    '''
def visitUtf8():
    '''returns Void\n\n
    visitUtf8(final ConstantPool.CONSTANT_Utf8_info constant_Utf8_info, final Void void1)\n
    '''
def visitSimpleType():
    '''returns Void\n\n
    visitSimpleType(final Type.SimpleType simpleType, final Void void1)\n
    '''
def visitArrayType():
    '''returns Void\n\n
    visitArrayType(final Type.ArrayType arrayType, final Void void1)\n
    '''
def visitClassSigType():
    '''returns Void\n\n
    visitClassSigType(final Type.ClassSigType classSigType, final Void void1)\n
    '''
def visitClassType():
    '''returns Void\n\n
    visitClassType(final Type.ClassType classType, final Void void1)\n
    '''
def visitTypeParamType():
    '''returns Void\n\n
    visitTypeParamType(final Type.TypeParamType typeParamType, final Void void1)\n
    '''
def visitWildcardType():
    '''returns Void\n\n
    visitWildcardType(final Type.WildcardType wildcardType, final Void void1)\n
    '''
