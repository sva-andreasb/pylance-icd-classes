ELEMENT = "String  \"set\""
NAMESPACE = "String  \"http://jabber.org/protocol/rsm\""
def RSMSet():
    '''    public RSMSet(final int max)
    public RSMSet(final int max, final int index)
    public RSMSet(final String item, final PageDirection pageDirection)
    public RSMSet(final int max, final String item, final PageDirection pageDirection)
    public RSMSet(final String after, final String before, final int count, final int index, final String last, final int max, final String firstString, final int firstIndex)
    '''
def getAfter():
    '''    public String getAfter()
    '''
def getBefore():
    '''    public String getBefore()
    '''
def getCount():
    '''    public int getCount()
    '''
def getIndex():
    '''    public int getIndex()
    '''
def getLast():
    '''    public String getLast()
    '''
def getMax():
    '''    public int getMax()
    '''
def getFirst():
    '''    public String getFirst()
    '''
def getFirstIndex():
    '''    public int getFirstIndex()
    '''
def getElementName():
    '''    public String getElementName()
    '''
def getNamespace():
    '''    public String getNamespace()
    '''
def toXML():
    '''    public XmlStringBuilder toXML(final String enclosingNamespace)
    '''
def from():
    '''    public static RSMSet from(final Stanza packet)
    '''
def newAfter():
    '''    public static RSMSet newAfter(final String after)
    '''
def newBefore():
    '''    public static RSMSet newBefore(final String before)
    '''
