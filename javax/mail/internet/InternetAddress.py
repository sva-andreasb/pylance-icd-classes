def hashCode():
    '''public int hashCode()
    '''
def InternetAddress():
    '''public InternetAddress()
    public InternetAddress(final String address)
    public InternetAddress(final String address, final boolean strict)
    public InternetAddress(final String address, final String personal)
    public InternetAddress(final String address, final String personal, final String charset)
    '''
def validate():
    '''public void validate()
    '''
def isGroup():
    '''public boolean isGroup()
    '''
def clone():
    '''public Object clone()
    '''
def equals():
    '''public boolean equals(final Object a)
    '''
def getAddress():
    '''public String getAddress()
    '''
def getPersonal():
    '''public String getPersonal()
    '''
def getType():
    '''public String getType()
    '''
def toString():
    '''public String toString()
    public static String toString(final Address[] addresses)
    public static String toString(final Address[] addresses, int used)
    '''
def toUnicodeString():
    '''public String toUnicodeString()
    '''
def setAddress():
    '''public void setAddress(final String address)
    '''
def setPersonal():
    '''public void setPersonal(final String name)
    public void setPersonal(final String name, final String charset)
    '''
def getGroup():
    '''public InternetAddress[] getGroup(final boolean strict)
    '''
def parse():
    '''public static InternetAddress[] parse(final String addresslist)
    public static InternetAddress[] parse(final String addresslist, final boolean strict)
    '''
def parseHeader():
    '''public static InternetAddress[] parseHeader(final String addresslist, final boolean strict)
    '''
def getLocalAddress():
    '''public static InternetAddress getLocalAddress(final Session session)
    '''
