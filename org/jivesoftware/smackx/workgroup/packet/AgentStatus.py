ELEMENT_NAME = "String  \"agent-status\""
NAMESPACE = "String  \"http://jabber.org/protocol/workgroup\""
def getWorkgroupJID():
    '''    public EntityBareJid getWorkgroupJID()
    '''
def getCurrentChats():
    '''    public List<ChatInfo> getCurrentChats()
    '''
def getMaxChats():
    '''    public int getMaxChats()
    '''
def getElementName():
    '''    public String getElementName()
    '''
def getNamespace():
    '''    public String getNamespace()
    '''
def toXML():
    '''    public String toXML(final String enclosingNamespace)
    public String toXML()
    '''
def ChatInfo():
    '''    public ChatInfo(final String sessionID, final String userID, final Date date, final String email, final String username, final String question)
    '''
def getSessionID():
    '''    public String getSessionID()
    '''
def getUserID():
    '''    public String getUserID()
    '''
def getDate():
    '''    public Date getDate()
    '''
def getEmail():
    '''    public String getEmail()
    '''
def getUsername():
    '''    public String getUsername()
    '''
def getQuestion():
    '''    public String getQuestion()
    '''
def parse():
    '''    public AgentStatus parse(final XmlPullParser parser, final int initialDepth)
    '''
