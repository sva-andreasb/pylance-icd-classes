__COOKIE_DELIM = "String  \"\\"\\\n\r\t\f\b%+ ;=\""
__separators = "String  \", \t\""
def formatDate():
    '''public static String formatDate(final long date)
    public String formatDate(final long date)
    '''
def formatCookieDate():
    '''public static void formatCookieDate(final StringBuilder buf, final long date)
    public static String formatCookieDate(final long date)
    public void formatCookieDate(final StringBuilder buf, final long date)
    '''
def parseDate():
    '''public static long parseDate(final String date)
    '''
def HttpFields():
    '''public HttpFields()
    public HttpFields(final int maxCookieVersion)
    '''
def getFieldNames():
    '''public Enumeration<String> getFieldNames()
    '''
def nextElement():
    '''public String nextElement()
    public String nextElement()
    public String nextElement()
    public String nextElement()
    '''
def hasMoreElements():
    '''public boolean hasMoreElements()
    public boolean hasMoreElements()
    public boolean hasMoreElements()
    public boolean hasMoreElements()
    '''
def size():
    '''public int size()
    '''
def getField():
    '''public Field getField(final int i)
    '''
def containsKey():
    '''public boolean containsKey(final Buffer name)
    public boolean containsKey(final String name)
    '''
def getStringField():
    '''public String getStringField(final String name)
    public String getStringField(final Buffer name)
    '''
def get():
    '''public Buffer get(final Buffer name)
    '''
def getValues():
    '''public Enumeration<String> getValues(final String name)
    public Enumeration<String> getValues(final Buffer name)
    public Enumeration<String> getValues(final String name, final String separators)
    '''
def put():
    '''public void put(final String name, final String value)
    public void put(final Buffer name, final String value)
    public void put(Buffer name, Buffer value)
    public void put(final String name, final List<?> list)
    '''
def add():
    '''public void add(final String name, final String value)
    public void add(Buffer name, Buffer value)
    public void add(final HttpFields fields)
    '''
def remove():
    '''public void remove(final String name)
    public void remove(Buffer name)
    '''
def getLongField():
    '''public long getLongField(final String name)
    public long getLongField(final Buffer name)
    '''
def getDateField():
    '''public long getDateField(final String name)
    '''
def putLongField():
    '''public void putLongField(final Buffer name, final long value)
    public void putLongField(final String name, final long value)
    '''
def addLongField():
    '''public void addLongField(final String name, final long value)
    public void addLongField(final Buffer name, final long value)
    '''
def putDateField():
    '''public void putDateField(final Buffer name, final long date)
    public void putDateField(final String name, final long date)
    '''
def addDateField():
    '''public void addDateField(final String name, final long date)
    '''
def addSetCookie():
    '''public void addSetCookie(final HttpCookie cookie)
    public void addSetCookie(final String name, final String value, final String domain, final String path, final long maxAge, final String comment, final boolean isSecure, final boolean isHttpOnly, int version)
    '''
def putTo():
    '''public void putTo(final Buffer buffer)
    public void putTo(final Buffer buffer)
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def clear():
    '''public void clear()
    '''
def valueParameters():
    '''public static String valueParameters(final String value, final Map<String, String> parameters)
    '''
def getQuality():
    '''public static Float getQuality(final String value)
    '''
def qualityList():
    '''public static List qualityList(final Enumeration e)
    '''
def getName():
    '''public String getName()
    '''
def getNameOrdinal():
    '''public int getNameOrdinal()
    '''
def getValue():
    '''public String getValue()
    '''
def getValueBuffer():
    '''public Buffer getValueBuffer()
    '''
def getValueOrdinal():
    '''public int getValueOrdinal()
    '''
def getIntValue():
    '''public int getIntValue()
    '''
def getLongValue():
    '''public long getLongValue()
    '''
