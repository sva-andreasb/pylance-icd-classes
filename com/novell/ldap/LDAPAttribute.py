def LDAPAttribute():
    '''    public LDAPAttribute()
    public LDAPAttribute(final LDAPAttribute ldapAttribute)
    public LDAPAttribute(final String name)
    public LDAPAttribute(final String s, final byte[] array)
    public LDAPAttribute(final String s, final String s2)
    public LDAPAttribute(final String s, final String[] array)
    '''
def clone():
    '''    public Object clone()
    '''
def addValue():
    '''    public void addValue(final String s)
    public void addValue(final byte[] array)
    '''
def addBase64Value():
    '''    public void addBase64Value(final String s)
    public void addBase64Value(final StringBuffer sb, final int n, final int n2)
    public void addBase64Value(final char[] array)
    '''
def addURLValue():
    '''    public void addURLValue(final String spec)
    public void addURLValue(final URL url)
    '''
def getByteValues():
    '''    public Enumeration getByteValues()
    '''
def getStringValues():
    '''    public Enumeration getStringValues()
    '''
def getByteValueArray():
    '''    public byte[][] getByteValueArray()
    '''
def getStringValueArray():
    '''    public String[] getStringValueArray()
    '''
def getStringValue():
    '''    public String getStringValue()
    '''
def getByteValue():
    '''    public byte[] getByteValue()
    '''
def getLangSubtype():
    '''    public String getLangSubtype()
    '''
def getBaseName():
    '''    public String getBaseName()
    public static String getBaseName(final String s)
    '''
def getName():
    '''    public String getName()
    '''
def getSubtypes():
    '''    public String[] getSubtypes()
    public static String[] getSubtypes(final String str)
    '''
def hasSubtype():
    '''    public boolean hasSubtype(final String anotherString)
    '''
def hasSubtypes():
    '''    public boolean hasSubtypes(final String[] array)
    '''
def removeValue():
    '''    public void removeValue(final String s)
    public void removeValue(final byte[] array)
    '''
def size():
    '''    public int size()
    '''
def compareTo():
    '''    public int compareTo(final Object o)
    '''
def toString():
    '''    public String toString()
    '''
def writeDSML():
    '''    public void writeDSML(final OutputStream out)
    '''
def readDSML():
    '''    public static Object readDSML(final InputStream inputStream)
    '''
def writeExternal():
    '''    public void writeExternal(final ObjectOutput objectOutput)
    '''
def readExternal():
    '''    public void readExternal(final ObjectInput objectInput)
    '''
