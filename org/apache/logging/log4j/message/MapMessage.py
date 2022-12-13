def MapMessage():
    '''public MapMessage()
    public MapMessage(final int initialCapacity)
    public MapMessage(final Map<String, V> map)
    '''
def getFormats():
    '''public String[] getFormats()
    '''
def getParameters():
    '''public Object[] getParameters()
    '''
def getFormat():
    '''public String getFormat()
    '''
def getData():
    '''public Map<String, V> getData()
    '''
def getIndexedReadOnlyStringMap():
    '''public IndexedReadOnlyStringMap getIndexedReadOnlyStringMap()
    '''
def clear():
    '''public void clear()
    '''
def containsKey():
    '''public boolean containsKey(final String key)
    '''
def put():
    '''public void put(final String candidateKey, final String value)
    '''
def putAll():
    '''public void putAll(final Map<String, String> map)
    '''
def get():
    '''public String get(final String key)
    '''
def remove():
    '''public String remove(final String key)
    '''
def asString():
    '''public String asString()
    public String asString(final String format)
    '''
def forEach():
    '''public <CV> void forEach(final BiConsumer<String, ? super CV> action)
    public <CV, S> void forEach(final TriConsumer<String, ? super CV, S> action, final S state)
    '''
def asXml():
    '''public void asXml(final StringBuilder sb)
    '''
def getFormattedMessage():
    '''public String getFormattedMessage()
    public String getFormattedMessage(final String[] formats)
    '''
def newInstance():
    '''public M newInstance(final Map<String, V> map)
    '''
def toString():
    '''public String toString()
    '''
def formatTo():
    '''public void formatTo(final StringBuilder buffer)
    public void formatTo(final String[] formats, final StringBuilder buffer)
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def hashCode():
    '''public int hashCode()
    '''
def getThrowable():
    '''public Throwable getThrowable()
    '''
def with():
    '''public M with(final String candidateKey, final boolean value)
    public M with(final String candidateKey, final byte value)
    public M with(final String candidateKey, final char value)
    public M with(final String candidateKey, final double value)
    public M with(final String candidateKey, final float value)
    public M with(final String candidateKey, final int value)
    public M with(final String candidateKey, final long value)
    public M with(final String candidateKey, final Object value)
    public M with(final String candidateKey, final short value)
    public M with(final String candidateKey, final String value)
    '''
def lookupIgnoreCase():
    '''public static MapFormat lookupIgnoreCase(final String format)
    '''
def names():
    '''public static String[] names()
    '''
