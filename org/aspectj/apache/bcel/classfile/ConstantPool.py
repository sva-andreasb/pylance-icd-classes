def getSize():
'''public int getSize()
'''
pass
def ConstantPool():
'''public ConstantPool()
public ConstantPool(final Constant[] constants)
'''
pass
def getConstant():
'''public Constant getConstant(final int index, final byte tag)
public Constant getConstant(final int index)
'''
pass
def copy():
'''public ConstantPool copy()
'''
pass
def getConstantString():
'''public String getConstantString(final int index, final byte tag)
'''
pass
def constantToString():
'''public String constantToString(Constant c)
public String constantToString(final int index, final byte tag)
public String constantToString(final int index)
'''
pass
def accept():
'''public void accept(final ClassVisitor v)
'''
pass
def getConstantPool():
'''public Constant[] getConstantPool()
'''
pass
def dump():
'''public void dump(final DataOutputStream file)
'''
pass
def getConstantUtf8():
'''public ConstantUtf8 getConstantUtf8(final int index)
'''
pass
def getConstantString_CONSTANTClass():
'''public String getConstantString_CONSTANTClass(int index)
'''
pass
def getLength():
'''public int getLength()
'''
pass
def toString():
'''public String toString()
'''
pass
def lookupInteger():
'''public int lookupInteger(final int n)
'''
pass
def lookupUtf8():
'''public int lookupUtf8(final String string)
'''
pass
def lookupClass():
'''public int lookupClass(final String classname)
'''
pass
def addUtf8():
'''public int addUtf8(final String n)
'''
pass
def addInteger():
'''public int addInteger(final int n)
'''
pass
def addArrayClass():
'''public int addArrayClass(final ArrayType type)
'''
pass
def addClass():
'''public int addClass(final ObjectType type)
public int addClass(final String classname)
'''
pass
def addFieldref():
'''public int addFieldref(final String class_name, final String field_name, final String signature)
'''
pass
def lookupFieldref():
'''public int lookupFieldref(String searchClassname, final String searchFieldname, final String searchSignature)
'''
pass
def addNameAndType():
'''public int addNameAndType(final String name, final String signature)
'''
pass
def lookupNameAndType():
'''public int lookupNameAndType(final String searchName, final String searchTypeSignature)
'''
pass
def addFloat():
'''public int addFloat(final float f)
'''
pass
def lookupFloat():
'''public int lookupFloat(final float f)
'''
pass
def addDouble():
'''public int addDouble(final double d)
'''
pass
def lookupDouble():
'''public int lookupDouble(final double d)
'''
pass
def addLong():
'''public int addLong(final long l)
'''
pass
def lookupString():
'''public int lookupString(final String s)
'''
pass
def addString():
'''public int addString(final String str)
'''
pass
def lookupLong():
'''public int lookupLong(final long l)
'''
pass
def addConstant():
'''public int addConstant(final Constant c, final ConstantPool cp)
'''
pass
def addMethodref():
'''public int addMethodref(final String class_name, final String method_name, final String signature)
'''
pass
def addInterfaceMethodref():
'''public int addInterfaceMethodref(final String class_name, final String method_name, final String signature)
'''
pass
def lookupInterfaceMethodref():
'''public int lookupInterfaceMethodref(String searchClassname, final String searchMethodName, final String searchSignature)
'''
pass
def lookupMethodref():
'''public int lookupMethodref(String searchClassname, final String searchMethodName, final String searchSignature)
'''
pass
def getFinalConstantPool():
'''public ConstantPool getFinalConstantPool()
'''
pass
