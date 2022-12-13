def ClassGen():
    '''    public ClassGen(final String class_name, final String super_class_name, final String file_name, final int access_flags, final String[] interfaces, final ConstantPoolGen cp)
    public ClassGen(final String class_name, final String super_class_name, final String file_name, final int access_flags, final String[] interfaces)
    public ClassGen(final JavaClass clazz)
    '''
def getJavaClass():
    '''    public JavaClass getJavaClass()
    '''
def addInterface():
    '''    public void addInterface(final String name)
    '''
def removeInterface():
    '''    public void removeInterface(final String name)
    '''
def getMajor():
    '''    public int getMajor()
    '''
def setMajor():
    '''    public void setMajor(final int major)
    '''
def setMinor():
    '''    public void setMinor(final int minor)
    '''
def getMinor():
    '''    public int getMinor()
    '''
def addAttribute():
    '''    public void addAttribute(final Attribute a)
    '''
def addMethod():
    '''    public void addMethod(final Method m)
    '''
def addEmptyConstructor():
    '''    public void addEmptyConstructor(final int access_flags)
    '''
def addField():
    '''    public void addField(final Field f)
    '''
def containsField():
    '''    public boolean containsField(final Field f)
    public Field containsField(final String name)
    '''
def containsMethod():
    '''    public Method containsMethod(final String name, final String signature)
    '''
def removeAttribute():
    '''    public void removeAttribute(final Attribute a)
    '''
def removeMethod():
    '''    public void removeMethod(final Method m)
    '''
def replaceMethod():
    '''    public void replaceMethod(final Method old, final Method new_)
    '''
def replaceField():
    '''    public void replaceField(final Field old, final Field new_)
    '''
def removeField():
    '''    public void removeField(final Field f)
    '''
def getClassName():
    '''    public String getClassName()
    '''
def getSuperclassName():
    '''    public String getSuperclassName()
    '''
def getFileName():
    '''    public String getFileName()
    '''
def setClassName():
    '''    public void setClassName(final String name)
    '''
def setSuperclassName():
    '''    public void setSuperclassName(final String name)
    '''
def getMethods():
    '''    public Method[] getMethods()
    '''
def setMethods():
    '''    public void setMethods(final Method[] methods)
    '''
def setMethodAt():
    '''    public void setMethodAt(final Method method, final int pos)
    '''
def getMethodAt():
    '''    public Method getMethodAt(final int pos)
    '''
def getInterfaceNames():
    '''    public String[] getInterfaceNames()
    '''
def getInterfaces():
    '''    public int[] getInterfaces()
    '''
def getFields():
    '''    public Field[] getFields()
    '''
def getAttributes():
    '''    public Attribute[] getAttributes()
    '''
def getConstantPool():
    '''    public ConstantPoolGen getConstantPool()
    '''
def setConstantPool():
    '''    public void setConstantPool(final ConstantPoolGen constant_pool)
    '''
def setClassNameIndex():
    '''    public void setClassNameIndex(final int class_name_index)
    '''
def setSuperclassNameIndex():
    '''    public void setSuperclassNameIndex(final int superclass_name_index)
    '''
def getSuperclassNameIndex():
    '''    public int getSuperclassNameIndex()
    '''
def getClassNameIndex():
    '''    public int getClassNameIndex()
    '''
def addObserver():
    '''    public void addObserver(final ClassObserver o)
    '''
def removeObserver():
    '''    public void removeObserver(final ClassObserver o)
    '''
def update():
    '''    public void update()
    '''
def clone():
    '''    public Object clone()
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
def hashCode():
    '''    public int hashCode()
    public int hashCode(final Object o)
    '''
