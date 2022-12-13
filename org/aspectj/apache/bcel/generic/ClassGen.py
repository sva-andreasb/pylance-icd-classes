def ClassGen():
    '''public ClassGen(final String classname, final String superclassname, final String filename, final int modifiers, final String[] interfacenames, final ConstantPool cpool)
    public ClassGen(final String classname, final String superclassname, final String filename, final int modifiers, final String[] interfacenames)
    public ClassGen(final JavaClass clazz)
    '''
def getJavaClass():
    '''public JavaClass getJavaClass()
    '''
def addInterface():
    '''public void addInterface(final String name)
    '''
def removeInterface():
    '''public void removeInterface(final String name)
    '''
def getMajor():
    '''public int getMajor()
    '''
def setMajor():
    '''public void setMajor(final int major)
    '''
def setMinor():
    '''public void setMinor(final int minor)
    '''
def getMinor():
    '''public int getMinor()
    '''
def addAttribute():
    '''public void addAttribute(final Attribute a)
    '''
def addAnnotation():
    '''public void addAnnotation(final AnnotationGen a)
    '''
def addMethod():
    '''public void addMethod(final Method m)
    '''
def addEmptyConstructor():
    '''public void addEmptyConstructor(final int access_flags)
    '''
def addField():
    '''public void addField(final Field f)
    '''
def containsField():
    '''public boolean containsField(final Field f)
    public Field containsField(final String name)
    '''
def containsMethod():
    '''public Method containsMethod(final String name, final String signature)
    '''
def removeAttribute():
    '''public void removeAttribute(final Attribute a)
    '''
def removeAnnotation():
    '''public void removeAnnotation(final AnnotationGen a)
    '''
def removeMethod():
    '''public void removeMethod(final Method m)
    '''
def replaceMethod():
    '''public void replaceMethod(final Method old, final Method new_)
    '''
def replaceField():
    '''public void replaceField(final Field old, final Field new_)
    '''
def removeField():
    '''public void removeField(final Field f)
    '''
def getClassName():
    '''public String getClassName()
    '''
def getSuperclassName():
    '''public String getSuperclassName()
    '''
def getFileName():
    '''public String getFileName()
    '''
def setClassName():
    '''public void setClassName(final String name)
    '''
def setSuperclassName():
    '''public void setSuperclassName(final String name)
    '''
def getMethods():
    '''public Method[] getMethods()
    '''
def setMethods():
    '''public void setMethods(final Method[] methods)
    '''
def setFields():
    '''public void setFields(final Field[] fs)
    '''
def setMethodAt():
    '''public void setMethodAt(final Method method, final int pos)
    '''
def getMethodAt():
    '''public Method getMethodAt(final int pos)
    '''
def getInterfaceNames():
    '''public String[] getInterfaceNames()
    '''
def getInterfaces():
    '''public int[] getInterfaces()
    '''
def getFields():
    '''public Field[] getFields()
    '''
def getAttributes():
    '''public Collection<Attribute> getAttributes()
    '''
def getAnnotations():
    '''public AnnotationGen[] getAnnotations()
    '''
def getConstantPool():
    '''public ConstantPool getConstantPool()
    '''
def setConstantPool():
    '''public void setConstantPool(final ConstantPool constant_pool)
    '''
def setClassNameIndex():
    '''public void setClassNameIndex(final int class_name_index)
    '''
def setSuperclassNameIndex():
    '''public void setSuperclassNameIndex(final int superclass_name_index)
    '''
def getSuperclassNameIndex():
    '''public int getSuperclassNameIndex()
    '''
def getClassNameIndex():
    '''public int getClassNameIndex()
    '''
def clone():
    '''public Object clone()
    '''
def isAnnotation():
    '''public final boolean isAnnotation()
    '''
def isEnum():
    '''public final boolean isEnum()
    '''
def getSUID():
    '''public long getSUID()
    '''
def hasAttribute():
    '''public boolean hasAttribute(final String attributeName)
    '''
def getAttribute():
    '''public Attribute getAttribute(final String attributeName)
    '''
def compare():
    '''public int compare(final Method m0, final Method m1)
    public int compare(final Field f0, final Field f1)
    public int compare(final Method m0, final Method m1)
    '''
