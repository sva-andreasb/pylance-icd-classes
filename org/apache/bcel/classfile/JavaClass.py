HEAP = "byte  1"
FILE = "byte  2"
ZIP = "byte  3"
def JavaClass():
    '''    public JavaClass(final int class_name_index, final int superclass_name_index, final String file_name, final int major, final int minor, final int access_flags, final ConstantPool constant_pool, int[] interfaces, Field[] fields, Method[] methods, Attribute[] attributes, final byte source)
    public JavaClass(final int class_name_index, final int superclass_name_index, final String file_name, final int major, final int minor, final int access_flags, final ConstantPool constant_pool, final int[] interfaces, final Field[] fields, final Method[] methods, final Attribute[] attributes)
    '''
def accept():
    '''    public void accept(final Visitor v)
    '''
def dump():
    '''    public void dump(final File file)
    public void dump(final String _file_name)
    public void dump(final OutputStream file)
    public void dump(final DataOutputStream file)
    '''
def getBytes():
    '''    public byte[] getBytes()
    '''
def getAttributes():
    '''    public Attribute[] getAttributes()
    '''
def getClassName():
    '''    public String getClassName()
    '''
def getPackageName():
    '''    public String getPackageName()
    '''
def getClassNameIndex():
    '''    public int getClassNameIndex()
    '''
def getConstantPool():
    '''    public ConstantPool getConstantPool()
    '''
def getFields():
    '''    public Field[] getFields()
    '''
def getFileName():
    '''    public String getFileName()
    '''
def getInterfaceNames():
    '''    public String[] getInterfaceNames()
    '''
def getInterfaceIndices():
    '''    public int[] getInterfaceIndices()
    '''
def getMajor():
    '''    public int getMajor()
    '''
def getMethods():
    '''    public Method[] getMethods()
    '''
def getMethod():
    '''    public Method getMethod(final java.lang.reflect.Method m)
    '''
def getMinor():
    '''    public int getMinor()
    '''
def getSourceFileName():
    '''    public String getSourceFileName()
    '''
def getSuperclassName():
    '''    public String getSuperclassName()
    '''
def getSuperclassNameIndex():
    '''    public int getSuperclassNameIndex()
    '''
def setAttributes():
    '''    public void setAttributes(final Attribute[] attributes)
    '''
def setClassName():
    '''    public void setClassName(final String class_name)
    '''
def setClassNameIndex():
    '''    public void setClassNameIndex(final int class_name_index)
    '''
def setConstantPool():
    '''    public void setConstantPool(final ConstantPool constant_pool)
    '''
def setFields():
    '''    public void setFields(final Field[] fields)
    '''
def setFileName():
    '''    public void setFileName(final String file_name)
    '''
def setInterfaceNames():
    '''    public void setInterfaceNames(final String[] interface_names)
    '''
def setInterfaces():
    '''    public void setInterfaces(final int[] interfaces)
    '''
def setMajor():
    '''    public void setMajor(final int major)
    '''
def setMethods():
    '''    public void setMethods(final Method[] methods)
    '''
def setMinor():
    '''    public void setMinor(final int minor)
    '''
def setSourceFileName():
    '''    public void setSourceFileName(final String source_file_name)
    '''
def setSuperclassName():
    '''    public void setSuperclassName(final String superclass_name)
    '''
def setSuperclassNameIndex():
    '''    public void setSuperclassNameIndex(final int superclass_name_index)
    '''
def toString():
    '''    public String toString()
    '''
def copy():
    '''    public JavaClass copy()
    '''
def isSuper():
    '''    public final boolean isSuper()
    '''
def isClass():
    '''    public final boolean isClass()
    '''
def getSource():
    '''    public final byte getSource()
    '''
def getRepository():
    '''    public Repository getRepository()
    '''
def setRepository():
    '''    public void setRepository(final Repository repository)
    '''
def instanceOf():
    '''    public final boolean instanceOf(final JavaClass super_class)
    '''
def implementationOf():
    '''    public boolean implementationOf(final JavaClass inter)
    '''
def getSuperClass():
    '''    public JavaClass getSuperClass()
    '''
def getSuperClasses():
    '''    public JavaClass[] getSuperClasses()
    '''
def getInterfaces():
    '''    public JavaClass[] getInterfaces()
    '''
def getAllInterfaces():
    '''    public JavaClass[] getAllInterfaces()
    '''
def getComparator():
    '''    public static BCELComparator getComparator()
    '''
def setComparator():
    '''    public static void setComparator(final BCELComparator comparator)
    '''
def equals():
    '''    public boolean equals(final Object obj)
    public boolean equals(final Object o1, final Object o2)
    '''
def compareTo():
    '''    public int compareTo(final Object obj)
    '''
def hashCode():
    '''    public int hashCode()
    public int hashCode(final Object o)
    '''
