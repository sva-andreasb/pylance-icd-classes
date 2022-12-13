CONSTANT_Utf8 = "int  1"
CONSTANT_Integer = "int  3"
CONSTANT_Float = "int  4"
CONSTANT_Long = "int  5"
CONSTANT_Double = "int  6"
CONSTANT_Class = "int  7"
CONSTANT_String = "int  8"
CONSTANT_Fieldref = "int  9"
CONSTANT_Methodref = "int  10"
CONSTANT_InterfaceMethodref = "int  11"
CONSTANT_NameAndType = "int  12"
CONSTANT_MethodHandle = "int  15"
CONSTANT_MethodType = "int  16"
CONSTANT_InvokeDynamic = "int  18"
def ConstantPool():
    '''    public ConstantPool(final CPInfo[] pool)
    '''
def size():
    '''    public int size()
    public int size()
    public int size()
    public int size()
    '''
def byteLength():
    '''    public int byteLength()
    public int byteLength()
    public int byteLength()
    public int byteLength()
    public int byteLength()
    public int byteLength()
    public int byteLength()
    public int byteLength()
    public int byteLength()
    public int byteLength()
    public int byteLength()
    public int byteLength()
    public int byteLength()
    '''
def get():
    '''    public CPInfo get(final int n)
    '''
def getUTF8Info():
    '''    public CONSTANT_Utf8_info getUTF8Info(final int n)
    '''
def getClassInfo():
    '''    public CONSTANT_Class_info getClassInfo(final int n)
    public CONSTANT_Class_info getClassInfo()
    '''
def getNameAndTypeInfo():
    '''    public CONSTANT_NameAndType_info getNameAndTypeInfo(final int n)
    public CONSTANT_NameAndType_info getNameAndTypeInfo()
    public CONSTANT_NameAndType_info getNameAndTypeInfo()
    '''
def getUTF8Value():
    '''    public String getUTF8Value(final int n)
    '''
def getUTF8Index():
    '''    public int getUTF8Index(final String anObject)
    '''
def entries():
    '''    public Iterable<CPInfo> entries()
    '''
def iterator():
    '''    public Iterator<CPInfo> iterator()
    '''
def hasNext():
    '''    public boolean hasNext()
    '''
def next():
    '''    public CPInfo next()
    '''
def remove():
    '''    public void remove()
    '''
def getMessage():
    '''    public String getMessage()
    public String getMessage()
    public String getMessage()
    public String getMessage()
    '''
def getTag():
    '''    public int getTag()
    public int getTag()
    public int getTag()
    public int getTag()
    public int getTag()
    public int getTag()
    public int getTag()
    public int getTag()
    public int getTag()
    public int getTag()
    public int getTag()
    public int getTag()
    '''
def getClassName():
    '''    public String getClassName()
    '''
def CONSTANT_Class_info():
    '''    public CONSTANT_Class_info(final ConstantPool constantPool, final int name_index)
    '''
def getName():
    '''    public String getName()
    public String getName()
    '''
def getBaseName():
    '''    public String getBaseName()
    '''
def getDimensionCount():
    '''    public int getDimensionCount()
    '''
def toString():
    '''    public String toString()
    public String toString()
    public String toString()
    public String toString()
    public String toString()
    public String toString()
    public String toString()
    public String toString()
    public String toString()
    public String toString()
    public String toString()
    public String toString()
    public String toString()
    public String toString()
    '''
def accept():
    '''    public <R, D> R accept(final Visitor<R, D> visitor, final D n)
    public <R, D> R accept(final Visitor<R, D> visitor, final D n)
    public <R, D> R accept(final Visitor<R, D> visitor, final D n)
    public <R, D> R accept(final Visitor<R, D> visitor, final D n)
    public <R, D> R accept(final Visitor<R, D> visitor, final D n)
    public <R, D> R accept(final Visitor<R, D> visitor, final D n)
    public <R, D> R accept(final Visitor<R, D> visitor, final D n)
    public <R, D> R accept(final Visitor<R, D> visitor, final D n)
    public <R, D> R accept(final Visitor<R, D> visitor, final D n)
    public <R, D> R accept(final Visitor<R, D> visitor, final D n)
    public <R, D> R accept(final Visitor<R, D> visitor, final D n)
    public <R, D> R accept(final Visitor<R, D> visitor, final D n)
    public <R, D> R accept(final Visitor<R, D> visitor, final D n)
    public <R, D> R accept(final Visitor<R, D> visitor, final D n)
    '''
def CONSTANT_Double_info():
    '''    public CONSTANT_Double_info(final double value)
    '''
def CONSTANT_Fieldref_info():
    '''    public CONSTANT_Fieldref_info(final ConstantPool constantPool, final int n, final int n2)
    '''
def CONSTANT_Float_info():
    '''    public CONSTANT_Float_info(final float value)
    '''
def CONSTANT_Integer_info():
    '''    public CONSTANT_Integer_info(final int value)
    '''
def CONSTANT_InterfaceMethodref_info():
    '''    public CONSTANT_InterfaceMethodref_info(final ConstantPool constantPool, final int n, final int n2)
    '''
def CONSTANT_InvokeDynamic_info():
    '''    public CONSTANT_InvokeDynamic_info(final ConstantPool constantPool, final int bootstrap_method_attr_index, final int name_and_type_index)
    '''
def CONSTANT_Long_info():
    '''    public CONSTANT_Long_info(final long value)
    '''
def CONSTANT_MethodHandle_info():
    '''    public CONSTANT_MethodHandle_info(final ConstantPool constantPool, final RefKind reference_kind, final int reference_index)
    '''
def getCPRefInfo():
    '''    public CPRefInfo getCPRefInfo()
    '''
def CONSTANT_MethodType_info():
    '''    public CONSTANT_MethodType_info(final ConstantPool constantPool, final int descriptor_index)
    '''
def getType():
    '''    public String getType()
    public String getType()
    '''
def CONSTANT_Methodref_info():
    '''    public CONSTANT_Methodref_info(final ConstantPool constantPool, final int n, final int n2)
    '''
def CONSTANT_NameAndType_info():
    '''    public CONSTANT_NameAndType_info(final ConstantPool constantPool, final int name_index, final int type_index)
    '''
def CONSTANT_String_info():
    '''    public CONSTANT_String_info(final ConstantPool constantPool, final int string_index)
    '''
def getString():
    '''    public String getString()
    '''
def CONSTANT_Utf8_info():
    '''    public CONSTANT_Utf8_info(final String value)
    '''
def write():
    '''    public void write(final int n)
    '''
