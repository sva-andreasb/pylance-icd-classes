def hashCode():
'''public int hashCode()
'''
pass
def InternetAddress():
'''public InternetAddress()
public InternetAddress(final String address)
public InternetAddress(final String address, final boolean strict)
public InternetAddress(final String address, final String personal)
public InternetAddress(final String address, final String personal, final String charset)
'''
pass
def validate():
'''public void validate()
'''
pass
def isGroup():
'''public boolean isGroup()
'''
pass
def clone():
'''public Object clone()
'''
pass
def equals():
'''public boolean equals(final Object a)
'''
pass
def getAddress():
'''public String getAddress()
'''
pass
def getPersonal():
'''public String getPersonal()
'''
pass
def getType():
'''public String getType()
'''
pass
def toString():
'''public String toString()
public static String toString(final Address[] addresses)
public static String toString(final Address[] addresses, int used)
'''
pass
def toUnicodeString():
'''public String toUnicodeString()
'''
pass
def setAddress():
'''public void setAddress(final String address)
'''
pass
def setPersonal():
'''public void setPersonal(final String name)
public void setPersonal(final String name, final String charset)
'''
pass
def getGroup():
'''public InternetAddress[] getGroup(final boolean strict)
'''
pass
def parse():
'''public static InternetAddress[] parse(final String addresslist)
public static InternetAddress[] parse(final String addresslist, final boolean strict)
'''
pass
def parseHeader():
'''public static InternetAddress[] parseHeader(final String addresslist, final boolean strict)
'''
pass
def getLocalAddress():
'''public static InternetAddress getLocalAddress(final Session session)
'''
pass
