HEAP = "byte  1"
FILE = "byte  2"
ZIP = "byte  3"
def JavaClass():
'''public JavaClass(final int class_name_index, final int superclass_name_index, final String file_name, final int major, final int minor, final int access_flags, final ConstantPool constant_pool, int[] interfaces, Field[] fields, Method[] methods, Attribute[] attributes, final byte source)
public JavaClass(final int class_name_index, final int superclass_name_index, final String file_name, final int major, final int minor, final int access_flags, final ConstantPool constant_pool, final int[] interfaces, final Field[] fields, final Method[] methods, final Attribute[] attributes)
'''
pass
def accept():
'''public void accept(final Visitor v)
'''
pass
def dump():
'''public void dump(final File file)
public void dump(final String _file_name)
public void dump(final OutputStream file)
public void dump(final DataOutputStream file)
'''
pass
def getBytes():
'''public byte[] getBytes()
'''
pass
def getAttributes():
'''public Attribute[] getAttributes()
'''
pass
def getClassName():
'''public String getClassName()
'''
pass
def getPackageName():
'''public String getPackageName()
'''
pass
def getClassNameIndex():
'''public int getClassNameIndex()
'''
pass
def getConstantPool():
'''public ConstantPool getConstantPool()
'''
pass
def getFields():
'''public Field[] getFields()
'''
pass
def getFileName():
'''public String getFileName()
'''
pass
def getInterfaceNames():
'''public String[] getInterfaceNames()
'''
pass
def getInterfaceIndices():
'''public int[] getInterfaceIndices()
'''
pass
def getMajor():
'''public int getMajor()
'''
pass
def getMethods():
'''public Method[] getMethods()
'''
pass
def getMethod():
'''public Method getMethod(final java.lang.reflect.Method m)
'''
pass
def getMinor():
'''public int getMinor()
'''
pass
def getSourceFileName():
'''public String getSourceFileName()
'''
pass
def getSuperclassName():
'''public String getSuperclassName()
'''
pass
def getSuperclassNameIndex():
'''public int getSuperclassNameIndex()
'''
pass
def setAttributes():
'''public void setAttributes(final Attribute[] attributes)
'''
pass
def setClassName():
'''public void setClassName(final String class_name)
'''
pass
def setClassNameIndex():
'''public void setClassNameIndex(final int class_name_index)
'''
pass
def setConstantPool():
'''public void setConstantPool(final ConstantPool constant_pool)
'''
pass
def setFields():
'''public void setFields(final Field[] fields)
'''
pass
def setFileName():
'''public void setFileName(final String file_name)
'''
pass
def setInterfaceNames():
'''public void setInterfaceNames(final String[] interface_names)
'''
pass
def setInterfaces():
'''public void setInterfaces(final int[] interfaces)
'''
pass
def setMajor():
'''public void setMajor(final int major)
'''
pass
def setMethods():
'''public void setMethods(final Method[] methods)
'''
pass
def setMinor():
'''public void setMinor(final int minor)
'''
pass
def setSourceFileName():
'''public void setSourceFileName(final String source_file_name)
'''
pass
def setSuperclassName():
'''public void setSuperclassName(final String superclass_name)
'''
pass
def setSuperclassNameIndex():
'''public void setSuperclassNameIndex(final int superclass_name_index)
'''
pass
def toString():
'''public String toString()
'''
pass
def copy():
'''public JavaClass copy()
'''
pass
def isSuper():
'''public final boolean isSuper()
'''
pass
def isClass():
'''public final boolean isClass()
'''
pass
def getSource():
'''public final byte getSource()
'''
pass
def getRepository():
'''public Repository getRepository()
'''
pass
def setRepository():
'''public void setRepository(final Repository repository)
'''
pass
def instanceOf():
'''public final boolean instanceOf(final JavaClass super_class)
'''
pass
def implementationOf():
'''public boolean implementationOf(final JavaClass inter)
'''
pass
def getSuperClass():
'''public JavaClass getSuperClass()
'''
pass
def getSuperClasses():
'''public JavaClass[] getSuperClasses()
'''
pass
def getInterfaces():
'''public JavaClass[] getInterfaces()
'''
pass
def getAllInterfaces():
'''public JavaClass[] getAllInterfaces()
'''
pass
def getComparator():
'''public static BCELComparator getComparator()
'''
pass
def setComparator():
'''public static void setComparator(final BCELComparator comparator)
'''
pass
def equals():
'''public boolean equals(final Object obj)
public boolean equals(final Object o1, final Object o2)
'''
pass
def compareTo():
'''public int compareTo(final Object obj)
'''
pass
def hashCode():
'''public int hashCode()
public int hashCode(final Object o)
'''
pass
