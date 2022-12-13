def JavaClass():
    '''public JavaClass(final int classnameIndex, final int superclassnameIndex, final String filename, final int major, final int minor, final int access_flags, final ConstantPool cpool, int[] interfaces, final Field[] fields, final Method[] methods, final Attribute[] attributes)
    '''
def accept():
    '''public void accept(final ClassVisitor v)
    '''
def dump():
    '''public void dump(final File file)
    public void dump(final String file_name)
    public void dump(final OutputStream file)
    public void dump(final DataOutputStream file)
    '''
def getBytes():
    '''public byte[] getBytes()
    '''
def getAttributes():
    '''public Attribute[] getAttributes()
    '''
def getAnnotations():
    '''public AnnotationGen[] getAnnotations()
    '''
def getClassName():
    '''public String getClassName()
    '''
def getPackageName():
    '''public String getPackageName()
    '''
def getClassNameIndex():
    '''public int getClassNameIndex()
    '''
def getConstantPool():
    '''public ConstantPool getConstantPool()
    '''
def getFields():
    '''public Field[] getFields()
    '''
def getFileName():
    '''public String getFileName()
    '''
def getInterfaceNames():
    '''public String[] getInterfaceNames()
    '''
def getInterfaceIndices():
    '''public int[] getInterfaceIndices()
    '''
def getMajor():
    '''public int getMajor()
    '''
def getMethods():
    '''public Method[] getMethods()
    '''
def getMethod():
    '''public Method getMethod(final java.lang.reflect.Method m)
    public Method getMethod(final Constructor<?> c)
    '''
def getField():
    '''public Field getField(final java.lang.reflect.Field field)
    '''
def getMinor():
    '''public int getMinor()
    '''
def getSourceFileName():
    '''public String getSourceFileName()
    '''
def getSuperclassName():
    '''public String getSuperclassName()
    '''
def getSuperclassNameIndex():
    '''public int getSuperclassNameIndex()
    '''
def setAttributes():
    '''public void setAttributes(final Attribute[] attributes)
    '''
def setClassName():
    '''public void setClassName(final String class_name)
    '''
def setClassNameIndex():
    '''public void setClassNameIndex(final int class_name_index)
    '''
def setConstantPool():
    '''public void setConstantPool(final ConstantPool constant_pool)
    '''
def setFields():
    '''public void setFields(final Field[] fields)
    '''
def setFileName():
    '''public void setFileName(final String file_name)
    '''
def setInterfaceNames():
    '''public void setInterfaceNames(final String[] interface_names)
    '''
def setInterfaces():
    '''public void setInterfaces(final int[] interfaces)
    '''
def setMajor():
    '''public void setMajor(final int major)
    '''
def setMethods():
    '''public void setMethods(final Method[] methods)
    '''
def setMinor():
    '''public void setMinor(final int minor)
    '''
def setSourceFileName():
    '''public void setSourceFileName(final String source_file_name)
    '''
def setSuperclassName():
    '''public void setSuperclassName(final String superclass_name)
    '''
def setSuperclassNameIndex():
    '''public void setSuperclassNameIndex(final int superclass_name_index)
    '''
def toString():
    '''public String toString()
    '''
def isSuper():
    '''public final boolean isSuper()
    '''
def isClass():
    '''public final boolean isClass()
    '''
def isAnonymous():
    '''public final boolean isAnonymous()
    '''
def isNested():
    '''public final boolean isNested()
    '''
def isAnnotation():
    '''public final boolean isAnnotation()
    '''
def isEnum():
    '''public final boolean isEnum()
    '''
def getRepository():
    '''public Repository getRepository()
    '''
def setRepository():
    '''public void setRepository(final Repository repository)
    '''
def instanceOf():
    '''public final boolean instanceOf(final JavaClass super_class)
    '''
def implementationOf():
    '''public boolean implementationOf(final JavaClass inter)
    '''
def getSuperClass():
    '''public JavaClass getSuperClass()
    '''
def getSuperClasses():
    '''public JavaClass[] getSuperClasses()
    '''
def getInterfaces():
    '''public JavaClass[] getInterfaces()
    '''
def getAllInterfaces():
    '''public Collection<JavaClass> getAllInterfaces()
    '''
def getGenericSignature():
    '''public final String getGenericSignature()
    '''
def isGeneric():
    '''public boolean isGeneric()
    '''
def getSignatureAttribute():
    '''public final Signature getSignatureAttribute()
    '''
