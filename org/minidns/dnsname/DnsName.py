MAX_LABELS = "int  128"
def writeToStream():
    '''public void writeToStream(final OutputStream os)
    '''
def getBytes():
    '''public byte[] getBytes()
    '''
def getRawBytes():
    '''public byte[] getRawBytes()
    '''
def getRawAce():
    '''public String getRawAce()
    '''
def asIdn():
    '''public String asIdn()
    '''
def getDomainpart():
    '''public String getDomainpart()
    '''
def getHostpart():
    '''public String getHostpart()
    '''
def size():
    '''public int size()
    '''
def length():
    '''public int length()
    '''
def charAt():
    '''public char charAt(final int index)
    '''
def subSequence():
    '''public CharSequence subSequence(final int start, final int end)
    '''
def toString():
    '''public String toString()
    '''
def from():
    '''public static DnsName from(final CharSequence name)
    public static DnsName from(final String name)
    public static DnsName from(final DnsName child, final DnsName parent)
    public static DnsName from(final DnsName... nameComponents)
    public static DnsName from(final String[] parts)
    '''
def parse():
    '''public static DnsName parse(final DataInputStream dis, final byte[] data)
    '''
def compareTo():
    '''public int compareTo(final DnsName other)
    '''
def equals():
    '''public boolean equals(final Object other)
    '''
def hashCode():
    '''public int hashCode()
    '''
def isDirectChildOf():
    '''public boolean isDirectChildOf(final DnsName parent)
    '''
def isChildOf():
    '''public boolean isChildOf(final DnsName parent)
    '''
def getLabelCount():
    '''public int getLabelCount()
    '''
def getLabels():
    '''public DnsLabel[] getLabels()
    '''
def getRawLabels():
    '''public DnsLabel[] getRawLabels()
    '''
def stripToLabels():
    '''public DnsName stripToLabels(final int labelCount)
    '''
def getParent():
    '''public DnsName getParent()
    '''
def isRootLabel():
    '''public boolean isRootLabel()
    '''
