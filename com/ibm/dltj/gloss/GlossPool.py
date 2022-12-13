def GlossPool():
'''public GlossPool()
public GlossPool(final Class clazz)
public GlossPool(final Class mainClass, final byte[] classBytes)
'''
pass
def instantiate():
'''public static GlossPool instantiate(final String s, final ClassLoader loader)
public static GlossPool instantiate(final String s, final BytesClassLoader bytesClassLoader, final byte[] array)
public static GlossPool instantiate(final int n)
'''
pass
def getGlossIterator():
'''public Iterator getGlossIterator()
'''
pass
def getSize():
'''public int getSize()
'''
pass
def getMainClass():
'''public Class getMainClass()
'''
pass
def getMainClassBytes():
'''public byte[] getMainClassBytes()
'''
pass
def write():
'''public void write(final DataOutputStream dataOutputStream, final GlossMapper glossMapper)
'''
pass
def read():
'''public int read(final DataInputStream dataInputStream, final int n, final BackMapper backMapper)
'''
pass
def checkIn():
'''public Gloss checkIn(final Gloss gloss)
'''
pass
def internGlosses():
'''public void internGlosses()
'''
pass
