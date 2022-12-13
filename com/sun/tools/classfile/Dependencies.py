def setFinder():
    '''public void setFinder(final Dependency.Finder finder)
    '''
def setFilter():
    '''public void setFilter(final Dependency.Filter filter)
    '''
def findAllDependencies():
    '''public Set<Dependency> findAllDependencies(final ClassFileReader classFileReader, final Set<String> set, final boolean b)
    public void findAllDependencies(final ClassFileReader classFileReader, final Set<String> c, final boolean b, final Recorder recorder)
    '''
def addDependency():
    '''public void addDependency(final Dependency dependency)
    '''
def ClassFileNotFoundException():
    '''public ClassFileNotFoundException(final String s)
    public ClassFileNotFoundException(final String s, final Throwable cause)
    '''
def ClassFileError():
    '''public ClassFileError(final Throwable cause)
    '''
def SimpleLocation():
    '''public SimpleLocation(final String name)
    '''
def getName():
    '''public String getName()
    '''
def getClassName():
    '''public String getClassName()
    '''
def getPackageName():
    '''public String getPackageName()
    '''
def equals():
    '''public boolean equals(final Object o)
    public boolean equals(final Object o)
    '''
def hashCode():
    '''public int hashCode()
    public int hashCode()
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def SimpleDependency():
    '''public SimpleDependency(final Location origin, final Location target)
    '''
def getOrigin():
    '''public Location getOrigin()
    '''
def getTarget():
    '''public Location getTarget()
    '''
def accepts():
    '''public boolean accepts(final Dependency dependency)
    public boolean accepts(final Dependency dependency)
    public boolean accepts(final Dependency dependency)
    '''
def visitClass():
    '''public Void visitClass(final ConstantPool.CONSTANT_Class_info constant_Class_info, final Void void1)
    '''
def visitDouble():
    '''public Void visitDouble(final ConstantPool.CONSTANT_Double_info constant_Double_info, final Void void1)
    '''
def visitFieldref():
    '''public Void visitFieldref(final ConstantPool.CONSTANT_Fieldref_info constant_Fieldref_info, final Void void1)
    '''
def visitFloat():
    '''public Void visitFloat(final ConstantPool.CONSTANT_Float_info constant_Float_info, final Void void1)
    '''
def visitInteger():
    '''public Void visitInteger(final ConstantPool.CONSTANT_Integer_info constant_Integer_info, final Void void1)
    '''
def visitInterfaceMethodref():
    '''public Void visitInterfaceMethodref(final ConstantPool.CONSTANT_InterfaceMethodref_info constant_InterfaceMethodref_info, final Void void1)
    '''
def visitInvokeDynamic():
    '''public Void visitInvokeDynamic(final ConstantPool.CONSTANT_InvokeDynamic_info constant_InvokeDynamic_info, final Void void1)
    '''
def visitLong():
    '''public Void visitLong(final ConstantPool.CONSTANT_Long_info constant_Long_info, final Void void1)
    '''
def visitMethodHandle():
    '''public Void visitMethodHandle(final ConstantPool.CONSTANT_MethodHandle_info constant_MethodHandle_info, final Void void1)
    '''
def visitMethodType():
    '''public Void visitMethodType(final ConstantPool.CONSTANT_MethodType_info constant_MethodType_info, final Void void1)
    public Void visitMethodType(final Type.MethodType methodType, final Void void1)
    '''
def visitMethodref():
    '''public Void visitMethodref(final ConstantPool.CONSTANT_Methodref_info constant_Methodref_info, final Void void1)
    '''
def visitNameAndType():
    '''public Void visitNameAndType(final ConstantPool.CONSTANT_NameAndType_info constant_NameAndType_info, final Void void1)
    '''
def visitString():
    '''public Void visitString(final ConstantPool.CONSTANT_String_info constant_String_info, final Void void1)
    '''
def visitUtf8():
    '''public Void visitUtf8(final ConstantPool.CONSTANT_Utf8_info constant_Utf8_info, final Void void1)
    '''
def visitSimpleType():
    '''public Void visitSimpleType(final Type.SimpleType simpleType, final Void void1)
    '''
def visitArrayType():
    '''public Void visitArrayType(final Type.ArrayType arrayType, final Void void1)
    '''
def visitClassSigType():
    '''public Void visitClassSigType(final Type.ClassSigType classSigType, final Void void1)
    '''
def visitClassType():
    '''public Void visitClassType(final Type.ClassType classType, final Void void1)
    '''
def visitTypeParamType():
    '''public Void visitTypeParamType(final Type.TypeParamType typeParamType, final Void void1)
    '''
def visitWildcardType():
    '''public Void visitWildcardType(final Type.WildcardType wildcardType, final Void void1)
    '''
