def GlossPool():
    '''public GlossPool()
    public GlossPool(final Class clazz)
    public GlossPool(final Class mainClass, final byte[] classBytes)
    '''
def instantiate():
    '''public static GlossPool instantiate(final String s, final ClassLoader loader)
    public static GlossPool instantiate(final String s, final BytesClassLoader bytesClassLoader, final byte[] array)
    public static GlossPool instantiate(final int n)
    '''
def getGlossIterator():
    '''public Iterator getGlossIterator()
    '''
def getSize():
    '''public int getSize()
    '''
def getMainClass():
    '''public Class getMainClass()
    '''
def getMainClassBytes():
    '''public byte[] getMainClassBytes()
    '''
def write():
    '''public void write(final DataOutputStream dataOutputStream, final GlossMapper glossMapper)
    '''
def read():
    '''public int read(final DataInputStream dataInputStream, final int n, final BackMapper backMapper)
    '''
def checkIn():
    '''public Gloss checkIn(final Gloss gloss)
    '''
def internGlosses():
    '''public void internGlosses()
    '''
