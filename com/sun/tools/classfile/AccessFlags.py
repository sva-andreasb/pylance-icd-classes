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
def ():
    '''returns AccessFlags\n\n
    (final int flags)\n
    '''
def ignore():
    '''returns AccessFlags\n\n
    ignore(final int n)\n
    '''
def is():
    '''returns boolean\n\n
    is(final int n)\n
    '''
def byteLength():
    '''returns int\n\n
    byteLength()\n
    '''
def getClassModifiers():
    '''returns Set<String>\n\n
    getClassModifiers()\n
    '''
def getClassFlags():
    '''returns Set<String>\n\n
    getClassFlags()\n
    '''
def getInnerClassModifiers():
    '''returns Set<String>\n\n
    getInnerClassModifiers()\n
    '''
def getInnerClassFlags():
    '''returns Set<String>\n\n
    getInnerClassFlags()\n
    '''
def getFieldModifiers():
    '''returns Set<String>\n\n
    getFieldModifiers()\n
    '''
def getFieldFlags():
    '''returns Set<String>\n\n
    getFieldFlags()\n
    '''
def getMethodModifiers():
    '''returns Set<String>\n\n
    getMethodModifiers()\n
    '''
def getMethodFlags():
    '''returns Set<String>\n\n
    getMethodFlags()\n
    '''
