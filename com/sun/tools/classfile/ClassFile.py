def read():
'''public static ClassFile read(final File file)
public static ClassFile read(final Path path)
public static ClassFile read(final Path path, final Attribute.Factory factory)
public static ClassFile read(final File file, final Attribute.Factory factory)
public static ClassFile read(final InputStream inputStream)
public static ClassFile read(final InputStream inputStream, final Attribute.Factory factory)
'''
pass
def ClassFile():
'''public ClassFile(final int magic, final int minor_version, final int major_version, final ConstantPool constant_pool, final AccessFlags access_flags, final int this_class, final int super_class, final int[] interfaces, final Field[] fields, final Method[] methods, final Attributes attributes)
'''
pass
def getName():
'''public String getName()
'''
pass
def getSuperclassName():
'''public String getSuperclassName()
'''
pass
def getInterfaceName():
'''public String getInterfaceName(final int n)
'''
pass
def getAttribute():
'''public Attribute getAttribute(final String s)
'''
pass
def isClass():
'''public boolean isClass()
'''
pass
def isInterface():
'''public boolean isInterface()
'''
pass
def byteLength():
'''public int byteLength()
'''
pass
