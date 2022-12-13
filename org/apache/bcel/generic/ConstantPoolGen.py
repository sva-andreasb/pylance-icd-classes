def ConstantPoolGen():
    '''    public ConstantPoolGen(final Constant[] cs)
    public ConstantPoolGen(final ConstantPool cp)
    public ConstantPoolGen()
    '''
def lookupString():
    '''    public int lookupString(final String str)
    '''
def addString():
    '''    public int addString(final String str)
    '''
def lookupClass():
    '''    public int lookupClass(final String str)
    '''
def addClass():
    '''    public int addClass(final String str)
    public int addClass(final ObjectType type)
    '''
def addArrayClass():
    '''    public int addArrayClass(final ArrayType type)
    '''
def lookupInteger():
    '''    public int lookupInteger(final int n)
    '''
def addInteger():
    '''    public int addInteger(final int n)
    '''
def lookupFloat():
    '''    public int lookupFloat(final float n)
    '''
def addFloat():
    '''    public int addFloat(final float n)
    '''
def lookupUtf8():
    '''    public int lookupUtf8(final String n)
    '''
def addUtf8():
    '''    public int addUtf8(final String n)
    '''
def lookupLong():
    '''    public int lookupLong(final long n)
    '''
def addLong():
    '''    public int addLong(final long n)
    '''
def lookupDouble():
    '''    public int lookupDouble(final double n)
    '''
def addDouble():
    '''    public int addDouble(final double n)
    '''
def lookupNameAndType():
    '''    public int lookupNameAndType(final String name, final String signature)
    '''
def addNameAndType():
    '''    public int addNameAndType(final String name, final String signature)
    '''
def lookupMethodref():
    '''    public int lookupMethodref(final String class_name, final String method_name, final String signature)
    public int lookupMethodref(final MethodGen method)
    '''
def addMethodref():
    '''    public int addMethodref(final String class_name, final String method_name, final String signature)
    public int addMethodref(final MethodGen method)
    '''
def lookupInterfaceMethodref():
    '''    public int lookupInterfaceMethodref(final String class_name, final String method_name, final String signature)
    public int lookupInterfaceMethodref(final MethodGen method)
    '''
def addInterfaceMethodref():
    '''    public int addInterfaceMethodref(final String class_name, final String method_name, final String signature)
    public int addInterfaceMethodref(final MethodGen method)
    '''
def lookupFieldref():
    '''    public int lookupFieldref(final String class_name, final String field_name, final String signature)
    '''
def addFieldref():
    '''    public int addFieldref(final String class_name, final String field_name, final String signature)
    '''
def getConstant():
    '''    public Constant getConstant(final int i)
    '''
def setConstant():
    '''    public void setConstant(final int i, final Constant c)
    '''
def getConstantPool():
    '''    public ConstantPool getConstantPool()
    '''
def getSize():
    '''    public int getSize()
    '''
def getFinalConstantPool():
    '''    public ConstantPool getFinalConstantPool()
    '''
def toString():
    '''    public String toString()
    '''
def addConstant():
    '''    public int addConstant(final Constant c, final ConstantPoolGen cp)
    '''
