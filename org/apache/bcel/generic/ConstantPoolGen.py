def ConstantPoolGen():
'''public ConstantPoolGen(final Constant[] cs)
public ConstantPoolGen(final ConstantPool cp)
public ConstantPoolGen()
'''
pass
def lookupString():
'''public int lookupString(final String str)
'''
pass
def addString():
'''public int addString(final String str)
'''
pass
def lookupClass():
'''public int lookupClass(final String str)
'''
pass
def addClass():
'''public int addClass(final String str)
public int addClass(final ObjectType type)
'''
pass
def addArrayClass():
'''public int addArrayClass(final ArrayType type)
'''
pass
def lookupInteger():
'''public int lookupInteger(final int n)
'''
pass
def addInteger():
'''public int addInteger(final int n)
'''
pass
def lookupFloat():
'''public int lookupFloat(final float n)
'''
pass
def addFloat():
'''public int addFloat(final float n)
'''
pass
def lookupUtf8():
'''public int lookupUtf8(final String n)
'''
pass
def addUtf8():
'''public int addUtf8(final String n)
'''
pass
def lookupLong():
'''public int lookupLong(final long n)
'''
pass
def addLong():
'''public int addLong(final long n)
'''
pass
def lookupDouble():
'''public int lookupDouble(final double n)
'''
pass
def addDouble():
'''public int addDouble(final double n)
'''
pass
def lookupNameAndType():
'''public int lookupNameAndType(final String name, final String signature)
'''
pass
def addNameAndType():
'''public int addNameAndType(final String name, final String signature)
'''
pass
def lookupMethodref():
'''public int lookupMethodref(final String class_name, final String method_name, final String signature)
public int lookupMethodref(final MethodGen method)
'''
pass
def addMethodref():
'''public int addMethodref(final String class_name, final String method_name, final String signature)
public int addMethodref(final MethodGen method)
'''
pass
def lookupInterfaceMethodref():
'''public int lookupInterfaceMethodref(final String class_name, final String method_name, final String signature)
public int lookupInterfaceMethodref(final MethodGen method)
'''
pass
def addInterfaceMethodref():
'''public int addInterfaceMethodref(final String class_name, final String method_name, final String signature)
public int addInterfaceMethodref(final MethodGen method)
'''
pass
def lookupFieldref():
'''public int lookupFieldref(final String class_name, final String field_name, final String signature)
'''
pass
def addFieldref():
'''public int addFieldref(final String class_name, final String field_name, final String signature)
'''
pass
def getConstant():
'''public Constant getConstant(final int i)
'''
pass
def setConstant():
'''public void setConstant(final int i, final Constant c)
'''
pass
def getConstantPool():
'''public ConstantPool getConstantPool()
'''
pass
def getSize():
'''public int getSize()
'''
pass
def getFinalConstantPool():
'''public ConstantPool getFinalConstantPool()
'''
pass
def toString():
'''public String toString()
'''
pass
def addConstant():
'''public int addConstant(final Constant c, final ConstantPoolGen cp)
'''
pass
