NONE = "int  -1"
STRING = "int  0"
BINARY = "int  1"
TABLE = "int  2"
INT = "int  7"
ARRAY = "int  8"
INT_VECTOR = "int  14"
def getBundleInstance():
    '''public static UResourceBundle getBundleInstance(final String baseName, final String localeName)
    public static UResourceBundle getBundleInstance(final String baseName, final String localeName, final ClassLoader root)
    public static UResourceBundle getBundleInstance(ULocale locale)
    public static UResourceBundle getBundleInstance(String baseName)
    public static UResourceBundle getBundleInstance(String baseName, final Locale locale)
    public static UResourceBundle getBundleInstance(String baseName, ULocale locale)
    public static UResourceBundle getBundleInstance(String baseName, final Locale locale, final ClassLoader loader)
    public static UResourceBundle getBundleInstance(String baseName, ULocale locale, final ClassLoader loader)
    '''
def getLocale():
    '''public Locale getLocale()
    '''
def getBinary():
    '''public ByteBuffer getBinary()
    public byte[] getBinary(final byte[] ba)
    '''
def getString():
    '''public String getString()
    public String getString(final int index)
    '''
def getStringArray():
    '''public String[] getStringArray()
    '''
def getIntVector():
    '''public int[] getIntVector()
    '''
def getInt():
    '''public int getInt()
    '''
def getUInt():
    '''public int getUInt()
    '''
def get():
    '''public UResourceBundle get(final String aKey)
    public UResourceBundle get(final int index)
    '''
def getKeys():
    '''public Enumeration<String> getKeys()
    '''
def keySet():
    '''public Set<String> keySet()
    '''
def getSize():
    '''public int getSize()
    '''
def getType():
    '''public int getType()
    '''
def getVersion():
    '''public VersionInfo getVersion()
    '''
def getIterator():
    '''public UResourceBundleIterator getIterator()
    '''
def getKey():
    '''public String getKey()
    '''
