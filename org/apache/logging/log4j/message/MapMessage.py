def MapMessage():
'''public MapMessage()
public MapMessage(final int initialCapacity)
public MapMessage(final Map<String, V> map)
'''
pass
def getFormats():
'''public String[] getFormats()
'''
pass
def getParameters():
'''public Object[] getParameters()
'''
pass
def getFormat():
'''public String getFormat()
'''
pass
def getData():
'''public Map<String, V> getData()
'''
pass
def getIndexedReadOnlyStringMap():
'''public IndexedReadOnlyStringMap getIndexedReadOnlyStringMap()
'''
pass
def clear():
'''public void clear()
'''
pass
def containsKey():
'''public boolean containsKey(final String key)
'''
pass
def put():
'''public void put(final String candidateKey, final String value)
'''
pass
def putAll():
'''public void putAll(final Map<String, String> map)
'''
pass
def get():
'''public String get(final String key)
'''
pass
def remove():
'''public String remove(final String key)
'''
pass
def asString():
'''public String asString()
public String asString(final String format)
'''
pass
def forEach():
'''public <CV> void forEach(final BiConsumer<String, ? super CV> action)
public <CV, S> void forEach(final TriConsumer<String, ? super CV, S> action, final S state)
'''
pass
def asXml():
'''public void asXml(final StringBuilder sb)
'''
pass
def getFormattedMessage():
'''public String getFormattedMessage()
public String getFormattedMessage(final String[] formats)
'''
pass
def newInstance():
'''public M newInstance(final Map<String, V> map)
'''
pass
def toString():
'''public String toString()
'''
pass
def formatTo():
'''public void formatTo(final StringBuilder buffer)
public void formatTo(final String[] formats, final StringBuilder buffer)
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def getThrowable():
'''public Throwable getThrowable()
'''
pass
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
pass
def lookupIgnoreCase():
'''public static MapFormat lookupIgnoreCase(final String format)
'''
pass
def names():
'''public static String[] names()
'''
pass
