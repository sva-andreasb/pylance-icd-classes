def AnnotationGen():
    '''public AnnotationGen(final AnnotationGen a, final ConstantPool cpool, final boolean copyPoolEntries)
    public AnnotationGen(final ObjectType type, final List<NameValuePair> pairs, final boolean runtimeVisible, final ConstantPool cpool)
    '''
def read():
    '''public static AnnotationGen read(final DataInputStream dis, final ConstantPool cpool, final boolean b)
    '''
def dump():
    '''public void dump(final DataOutputStream dos)
    '''
def addElementNameValuePair():
    '''public void addElementNameValuePair(final NameValuePair evp)
    '''
def getTypeIndex():
    '''public int getTypeIndex()
    '''
def getTypeSignature():
    '''public String getTypeSignature()
    '''
def getTypeName():
    '''public String getTypeName()
    '''
def getValues():
    '''public List<NameValuePair> getValues()
    '''
def toString():
    '''public String toString()
    '''
def toShortString():
    '''public String toShortString()
    '''
def isRuntimeVisible():
    '''public boolean isRuntimeVisible()
    '''
def hasNameValuePair():
    '''public boolean hasNameValuePair(final String name, final String value)
    '''
def hasNamedValue():
    '''public boolean hasNamedValue(final String name)
    '''
