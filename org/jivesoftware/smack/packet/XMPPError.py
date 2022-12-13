def XMPPError():
    '''    public XMPPError(final Condition condition)
    public XMPPError(final Condition condition, final String messageText)
    public XMPPError(final int code)
    public XMPPError(final int code, final String message)
    public XMPPError(final int code, final Type type, final String condition, final String message, final List<PacketExtension> extension)
    '''
def getCondition():
    '''    public String getCondition()
    '''
def getType():
    '''    public Type getType()
    '''
def getCode():
    '''    public int getCode()
    '''
def getMessage():
    '''    public String getMessage()
    '''
def toXML():
    '''    public String toXML()
    '''
def toString():
    '''    public String toString()
    public String toString()
    '''
def getExtensions():
    '''    public synchronized List<PacketExtension> getExtensions()
    '''
def getExtension():
    '''    public synchronized PacketExtension getExtension(final String elementName, final String namespace)
    '''
def addExtension():
    '''    public synchronized void addExtension(final PacketExtension extension)
    '''
def setExtension():
    '''    public synchronized void setExtension(final List<PacketExtension> extension)
    '''
def Condition():
    '''    public Condition(final String value)
    '''
