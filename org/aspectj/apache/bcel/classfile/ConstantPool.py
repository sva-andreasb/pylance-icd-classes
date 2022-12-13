def getSize():
    '''public int getSize()
    '''
def ConstantPool():
    '''public ConstantPool()
    public ConstantPool(final Constant[] constants)
    '''
def getConstant():
    '''public Constant getConstant(final int index, final byte tag)
    public Constant getConstant(final int index)
    '''
def copy():
    '''public ConstantPool copy()
    '''
def getConstantString():
    '''public String getConstantString(final int index, final byte tag)
    '''
def constantToString():
    '''public String constantToString(Constant c)
    public String constantToString(final int index, final byte tag)
    public String constantToString(final int index)
    '''
def accept():
    '''public void accept(final ClassVisitor v)
    '''
def getConstantPool():
    '''public Constant[] getConstantPool()
    '''
def dump():
    '''public void dump(final DataOutputStream file)
    '''
def getConstantUtf8():
    '''public ConstantUtf8 getConstantUtf8(final int index)
    '''
def getConstantString_CONSTANTClass():
    '''public String getConstantString_CONSTANTClass(int index)
    '''
def getLength():
    '''public int getLength()
    '''
def toString():
    '''public String toString()
    '''
def lookupInteger():
    '''public int lookupInteger(final int n)
    '''
def lookupUtf8():
    '''public int lookupUtf8(final String string)
    '''
def lookupClass():
    '''public int lookupClass(final String classname)
    '''
def addUtf8():
    '''public int addUtf8(final String n)
    '''
def addInteger():
    '''public int addInteger(final int n)
    '''
def addArrayClass():
    '''public int addArrayClass(final ArrayType type)
    '''
def addClass():
    '''public int addClass(final ObjectType type)
    public int addClass(final String classname)
    '''
def addFieldref():
    '''public int addFieldref(final String class_name, final String field_name, final String signature)
    '''
def lookupFieldref():
    '''public int lookupFieldref(String searchClassname, final String searchFieldname, final String searchSignature)
    '''
def addNameAndType():
    '''public int addNameAndType(final String name, final String signature)
    '''
def lookupNameAndType():
    '''public int lookupNameAndType(final String searchName, final String searchTypeSignature)
    '''
def addFloat():
    '''public int addFloat(final float f)
    '''
def lookupFloat():
    '''public int lookupFloat(final float f)
    '''
def addDouble():
    '''public int addDouble(final double d)
    '''
def lookupDouble():
    '''public int lookupDouble(final double d)
    '''
def addLong():
    '''public int addLong(final long l)
    '''
def lookupString():
    '''public int lookupString(final String s)
    '''
def addString():
    '''public int addString(final String str)
    '''
def lookupLong():
    '''public int lookupLong(final long l)
    '''
def addConstant():
    '''public int addConstant(final Constant c, final ConstantPool cp)
    '''
def addMethodref():
    '''public int addMethodref(final String class_name, final String method_name, final String signature)
    '''
def addInterfaceMethodref():
    '''public int addInterfaceMethodref(final String class_name, final String method_name, final String signature)
    '''
def lookupInterfaceMethodref():
    '''public int lookupInterfaceMethodref(String searchClassname, final String searchMethodName, final String searchSignature)
    '''
def lookupMethodref():
    '''public int lookupMethodref(String searchClassname, final String searchMethodName, final String searchSignature)
    '''
def getFinalConstantPool():
    '''public ConstantPool getFinalConstantPool()
    '''
