def ClassGen():
'''public ClassGen(final String class_name, final String super_class_name, final String file_name, final int access_flags, final String[] interfaces, final ConstantPoolGen cp)
public ClassGen(final String class_name, final String super_class_name, final String file_name, final int access_flags, final String[] interfaces)
public ClassGen(final JavaClass clazz)
'''
pass
def getJavaClass():
'''public JavaClass getJavaClass()
'''
pass
def addInterface():
'''public void addInterface(final String name)
'''
pass
def removeInterface():
'''public void removeInterface(final String name)
'''
pass
def getMajor():
'''public int getMajor()
'''
pass
def setMajor():
'''public void setMajor(final int major)
'''
pass
def setMinor():
'''public void setMinor(final int minor)
'''
pass
def getMinor():
'''public int getMinor()
'''
pass
def addAttribute():
'''public void addAttribute(final Attribute a)
'''
pass
def addMethod():
'''public void addMethod(final Method m)
'''
pass
def addEmptyConstructor():
'''public void addEmptyConstructor(final int access_flags)
'''
pass
def addField():
'''public void addField(final Field f)
'''
pass
def containsField():
'''public boolean containsField(final Field f)
public Field containsField(final String name)
'''
pass
def containsMethod():
'''public Method containsMethod(final String name, final String signature)
'''
pass
def removeAttribute():
'''public void removeAttribute(final Attribute a)
'''
pass
def removeMethod():
'''public void removeMethod(final Method m)
'''
pass
def replaceMethod():
'''public void replaceMethod(final Method old, final Method new_)
'''
pass
def replaceField():
'''public void replaceField(final Field old, final Field new_)
'''
pass
def removeField():
'''public void removeField(final Field f)
'''
pass
def getClassName():
'''public String getClassName()
'''
pass
def getSuperclassName():
'''public String getSuperclassName()
'''
pass
def getFileName():
'''public String getFileName()
'''
pass
def setClassName():
'''public void setClassName(final String name)
'''
pass
def setSuperclassName():
'''public void setSuperclassName(final String name)
'''
pass
def getMethods():
'''public Method[] getMethods()
'''
pass
def setMethods():
'''public void setMethods(final Method[] methods)
'''
pass
def setMethodAt():
'''public void setMethodAt(final Method method, final int pos)
'''
pass
def getMethodAt():
'''public Method getMethodAt(final int pos)
'''
pass
def getInterfaceNames():
'''public String[] getInterfaceNames()
'''
pass
def getInterfaces():
'''public int[] getInterfaces()
'''
pass
def getFields():
'''public Field[] getFields()
'''
pass
def getAttributes():
'''public Attribute[] getAttributes()
'''
pass
def getConstantPool():
'''public ConstantPoolGen getConstantPool()
'''
pass
def setConstantPool():
'''public void setConstantPool(final ConstantPoolGen constant_pool)
'''
pass
def setClassNameIndex():
'''public void setClassNameIndex(final int class_name_index)
'''
pass
def setSuperclassNameIndex():
'''public void setSuperclassNameIndex(final int superclass_name_index)
'''
pass
def getSuperclassNameIndex():
'''public int getSuperclassNameIndex()
'''
pass
def getClassNameIndex():
'''public int getClassNameIndex()
'''
pass
def addObserver():
'''public void addObserver(final ClassObserver o)
'''
pass
def removeObserver():
'''public void removeObserver(final ClassObserver o)
'''
pass
def update():
'''public void update()
'''
pass
def clone():
'''public Object clone()
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
def hashCode():
'''public int hashCode()
public int hashCode(final Object o)
'''
pass
