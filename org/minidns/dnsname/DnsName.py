MAX_LABELS = "int  128"
def writeToStream():
'''public void writeToStream(final OutputStream os)
'''
pass
def getBytes():
'''public byte[] getBytes()
'''
pass
def getRawBytes():
'''public byte[] getRawBytes()
'''
pass
def getRawAce():
'''public String getRawAce()
'''
pass
def asIdn():
'''public String asIdn()
'''
pass
def getDomainpart():
'''public String getDomainpart()
'''
pass
def getHostpart():
'''public String getHostpart()
'''
pass
def size():
'''public int size()
'''
pass
def length():
'''public int length()
'''
pass
def charAt():
'''public char charAt(final int index)
'''
pass
def subSequence():
'''public CharSequence subSequence(final int start, final int end)
'''
pass
def toString():
'''public String toString()
'''
pass
def from():
'''public static DnsName from(final CharSequence name)
public static DnsName from(final String name)
public static DnsName from(final DnsName child, final DnsName parent)
public static DnsName from(final DnsName... nameComponents)
public static DnsName from(final String[] parts)
'''
pass
def parse():
'''public static DnsName parse(final DataInputStream dis, final byte[] data)
'''
pass
def compareTo():
'''public int compareTo(final DnsName other)
'''
pass
def equals():
'''public boolean equals(final Object other)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def isDirectChildOf():
'''public boolean isDirectChildOf(final DnsName parent)
'''
pass
def isChildOf():
'''public boolean isChildOf(final DnsName parent)
'''
pass
def getLabelCount():
'''public int getLabelCount()
'''
pass
def getLabels():
'''public DnsLabel[] getLabels()
'''
pass
def getRawLabels():
'''public DnsLabel[] getRawLabels()
'''
pass
def stripToLabels():
'''public DnsName stripToLabels(final int labelCount)
'''
pass
def getParent():
'''public DnsName getParent()
'''
pass
def isRootLabel():
'''public boolean isRootLabel()
'''
pass
