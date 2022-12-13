NAMESPACE = "String  \"urn:xmpp:tmp:jingle\""
NODENAME = "String  \"jingle\""
def Jingle():
    '''public Jingle(final List<JingleContent> contents, final JingleContentInfo mi, final String sid)
    public Jingle(final JingleContent content)
    public Jingle(final JingleContentInfo info)
    public Jingle(final JingleActionEnum action)
    public Jingle(final String sid)
    public Jingle()
    '''
def setSid():
    '''public final void setSid(final String sid)
    '''
def getSid():
    '''public String getSid()
    '''
def getElementName():
    '''public static String getElementName()
    '''
def getNamespace():
    '''public static String getNamespace()
    '''
def getContentInfo():
    '''public JingleContentInfo getContentInfo()
    '''
def setContentInfo():
    '''public void setContentInfo(final JingleContentInfo contentInfo)
    '''
def getContents():
    '''public Iterator<JingleContent> getContents()
    '''
def getContentsList():
    '''public List<JingleContent> getContentsList()
    '''
def addContent():
    '''public void addContent(final JingleContent content)
    '''
def addContents():
    '''public void addContents(final List<JingleContent> contentList)
    '''
def getAction():
    '''public JingleActionEnum getAction()
    '''
def setAction():
    '''public void setAction(final JingleActionEnum action)
    '''
def getInitiator():
    '''public Jid getInitiator()
    '''
def setInitiator():
    '''public void setInitiator(final Jid initiator)
    '''
def getResponder():
    '''public Jid getResponder()
    '''
def setResponder():
    '''public void setResponder(final Jid resp)
    '''
def getSessionHash():
    '''public static int getSessionHash(final String sid, final Jid initiator)
    '''
