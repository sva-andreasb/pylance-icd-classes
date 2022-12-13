NAMESPACE = "String  \"urn:xmpp:sm:3\""
ELEMENT = "String  \"r\""
def getElementName():
    '''public String getElementName()
    public String getElementName()
    public String getElementName()
    public String getElementName()
    public String getElementName()
    public String getElementName()
    public String getElementName()
    public String getElementName()
    '''
def getNamespace():
    '''public String getNamespace()
    public final String getNamespace()
    public String getNamespace()
    public final String getNamespace()
    public String getNamespace()
    public String getNamespace()
    '''
def toXML():
    '''public CharSequence toXML(final String enclosingNamespace)
    public CharSequence toXML(final String enclosingNamespace)
    public CharSequence toXML(final String enclosingNamespace)
    public CharSequence toXML(final String enclosingNamespace)
    public final XmlStringBuilder toXML(final String enclosingNamespace)
    public CharSequence toXML(final String enclosingNamespace)
    public CharSequence toXML(final String enclosingNamespace)
    '''
def isResumeSet():
    '''public boolean isResumeSet()
    '''
def getMaxResumptionTime():
    '''public int getMaxResumptionTime()
    '''
def Enable():
    '''public Enable(final boolean resume)
    public Enable(final boolean resume, final int max)
    '''
def Enabled():
    '''public Enabled(final String id, final boolean resume)
    public Enabled(final String id, final boolean resume, final String location, final int max)
    '''
def getId():
    '''public String getId()
    '''
def getLocation():
    '''public String getLocation()
    '''
def Failed():
    '''public Failed()
    public Failed(final StanzaError.Condition condition, final List<StanzaErrorTextElement> textElements)
    '''
def getTextElements():
    '''public List<StanzaErrorTextElement> getTextElements()
    '''
def getHandledCount():
    '''public long getHandledCount()
    public long getHandledCount()
    '''
def getPrevId():
    '''public String getPrevId()
    '''
def Resume():
    '''public Resume(final long handledCount, final String previd)
    '''
def Resumed():
    '''public Resumed(final long handledCount, final String previd)
    '''
def AckAnswer():
    '''public AckAnswer(final long handledCount)
    '''
