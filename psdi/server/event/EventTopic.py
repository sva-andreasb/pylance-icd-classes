def EventTopic():
    '''    public EventTopic(final String subject)
    '''
def setTree():
    '''    public void setTree(final EventTopicTree tree)
    '''
def setExtendedSubIds():
    '''    public void setExtendedSubIds(final Map<Integer, List<Integer>> idMap)
    '''
def getExtendedSubIds():
    '''    public Map getExtendedSubIds()
    '''
def getTree():
    '''    public EventTopicTree getTree()
    '''
def getSubject():
    '''    public String getSubject()
    '''
def getSubTopicTree():
    '''    public EventTopicTree getSubTopicTree()
    '''
def setActive():
    '''    public void setActive(final boolean value)
    '''
def isActive():
    '''    public boolean isActive()
    '''
def eventValidate():
    '''    public void eventValidate(final EventMessage msg)
    public boolean eventValidate(final EventMessage em)
    '''
def eventAction():
    '''    public void eventAction(final EventMessage msg)
    public void eventAction(final EventMessage em)
    '''
def preSaveEventAction():
    '''    public void preSaveEventAction(final EventMessage msg)
    public void preSaveEventAction(final EventMessage em)
    '''
def preSaveInternalEventAction():
    '''    public void preSaveInternalEventAction(final EventMessage msg)
    public void preSaveInternalEventAction(final EventMessage em)
    '''
def postSaveInternalEventAction():
    '''    public void postSaveInternalEventAction(final EventMessage msg)
    public void postSaveInternalEventAction(final EventMessage em)
    '''
def postCommitEventAction():
    '''    public void postCommitEventAction(final EventMessage msg)
    public void postCommitEventAction(final EventMessage em)
    '''
def addSubTopic():
    '''    public void addSubTopic(final EventTopic ev)
    '''
def getEventTopic():
    '''    public EventTopic getEventTopic(String subject)
    '''
def getListeners():
    '''    public Map<Integer, EventListener> getListeners()
    '''
def getListenerCount():
    '''    public int getListenerCount()
    '''
def getSubscriptionId():
    '''    public int getSubscriptionId(final EventListener evt)
    '''
def getSubscriptionIdByClassName():
    '''    public int getSubscriptionIdByClassName(final EventListener evt)
    '''
def dumpTopic():
    '''    public Map dumpTopic()
    '''
def Subscription():
    '''    public Subscription(final EventListener eval)
    '''
def getId():
    '''    public int getId()
    '''
