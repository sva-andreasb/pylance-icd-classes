def ClassGen():
'''public ClassGen(final String classname, final String superclassname, final String filename, final int modifiers, final String[] interfacenames, final ConstantPool cpool)
public ClassGen(final String classname, final String superclassname, final String filename, final int modifiers, final String[] interfacenames)
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
def addAnnotation():
'''public void addAnnotation(final AnnotationGen a)
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
def removeAnnotation():
'''public void removeAnnotation(final AnnotationGen a)
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
def setFields():
'''public void setFields(final Field[] fs)
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
'''public Collection<Attribute> getAttributes()
'''
pass
def getAnnotations():
'''public AnnotationGen[] getAnnotations()
'''
pass
def getConstantPool():
'''public ConstantPool getConstantPool()
'''
pass
def setConstantPool():
'''public void setConstantPool(final ConstantPool constant_pool)
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
def clone():
'''public Object clone()
'''
pass
def isAnnotation():
'''public final boolean isAnnotation()
'''
pass
def isEnum():
'''public final boolean isEnum()
'''
pass
def getSUID():
'''public long getSUID()
'''
pass
def hasAttribute():
'''public boolean hasAttribute(final String attributeName)
'''
pass
def getAttribute():
'''public Attribute getAttribute(final String attributeName)
'''
pass
def compare():
'''public int compare(final Method m0, final Method m1)
public int compare(final Field f0, final Field f1)
public int compare(final Method m0, final Method m1)
'''
pass
