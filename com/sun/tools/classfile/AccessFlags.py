ACC_PUBLIC = "int  1"
ACC_PRIVATE = "int  2"
ACC_PROTECTED = "int  4"
ACC_STATIC = "int  8"
ACC_FINAL = "int  16"
ACC_SUPER = "int  32"
ACC_SYNCHRONIZED = "int  32"
ACC_VOLATILE = "int  64"
ACC_BRIDGE = "int  64"
ACC_TRANSIENT = "int  128"
ACC_VARARGS = "int  128"
ACC_NATIVE = "int  256"
ACC_INTERFACE = "int  512"
ACC_ABSTRACT = "int  1024"
ACC_STRICT = "int  2048"
ACC_SYNTHETIC = "int  4096"
ACC_ANNOTATION = "int  8192"
ACC_ENUM = "int  16384"
ACC_MANDATED = "int  32768"
def AccessFlags():
    '''    public AccessFlags(final int flags)
    '''
def ignore():
    '''    public AccessFlags ignore(final int n)
    '''
def is():
    '''    public boolean is(final int n)
    '''
def byteLength():
    '''    public int byteLength()
    '''
def getClassModifiers():
    '''    public Set<String> getClassModifiers()
    '''
def getClassFlags():
    '''    public Set<String> getClassFlags()
    '''
def getInnerClassModifiers():
    '''    public Set<String> getInnerClassModifiers()
    '''
def getInnerClassFlags():
    '''    public Set<String> getInnerClassFlags()
    '''
def getFieldModifiers():
    '''    public Set<String> getFieldModifiers()
    '''
def getFieldFlags():
    '''    public Set<String> getFieldFlags()
    '''
def getMethodModifiers():
    '''    public Set<String> getMethodModifiers()
    '''
def getMethodFlags():
    '''    public Set<String> getMethodFlags()
    '''
