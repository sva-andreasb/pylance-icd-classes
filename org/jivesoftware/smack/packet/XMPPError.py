def XMPPError():
'''public XMPPError(final Condition condition)
public XMPPError(final Condition condition, final String messageText)
public XMPPError(final int code)
public XMPPError(final int code, final String message)
public XMPPError(final int code, final Type type, final String condition, final String message, final List<PacketExtension> extension)
'''
pass
def getCondition():
'''public String getCondition()
'''
pass
def getType():
'''public Type getType()
'''
pass
def getCode():
'''public int getCode()
'''
pass
def getMessage():
'''public String getMessage()
'''
pass
def toXML():
'''public String toXML()
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def getExtensions():
'''public synchronized List<PacketExtension> getExtensions()
'''
pass
def getExtension():
'''public synchronized PacketExtension getExtension(final String elementName, final String namespace)
'''
pass
def addExtension():
'''public synchronized void addExtension(final PacketExtension extension)
'''
pass
def setExtension():
'''public synchronized void setExtension(final List<PacketExtension> extension)
'''
pass
def Condition():
'''public Condition(final String value)
'''
pass
