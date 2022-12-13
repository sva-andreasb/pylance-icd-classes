def read():
    '''    public static ClassFile read(final File file)
    public static ClassFile read(final Path path)
    public static ClassFile read(final Path path, final Attribute.Factory factory)
    public static ClassFile read(final File file, final Attribute.Factory factory)
    public static ClassFile read(final InputStream inputStream)
    public static ClassFile read(final InputStream inputStream, final Attribute.Factory factory)
    '''
def ClassFile():
    '''    public ClassFile(final int magic, final int minor_version, final int major_version, final ConstantPool constant_pool, final AccessFlags access_flags, final int this_class, final int super_class, final int[] interfaces, final Field[] fields, final Method[] methods, final Attributes attributes)
    '''
def getName():
    '''    public String getName()
    '''
def getSuperclassName():
    '''    public String getSuperclassName()
    '''
def getInterfaceName():
    '''    public String getInterfaceName(final int n)
    '''
def getAttribute():
    '''    public Attribute getAttribute(final String s)
    '''
def isClass():
    '''    public boolean isClass()
    '''
def isInterface():
    '''    public boolean isInterface()
    '''
def byteLength():
    '''    public int byteLength()
    '''
