def EventTopicTree():
    '''public EventTopicTree()
    public EventTopicTree(final EventTopicTree gEventTopicTree)
    '''
def setOwnerTree():
    '''public void setOwnerTree(final EventTopicTree tree)
    '''
def getOwnerTree():
    '''public EventTopicTree getOwnerTree()
    '''
def setActive():
    '''public void setActive(final boolean value)
    '''
def isActive():
    '''public boolean isActive()
    '''
def getEventTopics():
    '''public Hashtable getEventTopics()
    '''
def findEventTopic():
    '''public EventTopic findEventTopic(final String subject)
    public EventTopic findEventTopic(String subject, final boolean isTenant)
    '''
def getEventTopic():
    '''public synchronized EventTopic getEventTopic(final String subject)
    public synchronized EventTopic getEventTopic(final String subject, final boolean isTenant)
    '''
def dumpEventTopicTree():
    '''public Map<String, Object> dumpEventTopicTree(boolean isTenant)
    '''
def printEventTopicTree():
    '''public String printEventTopicTree(boolean isTenant)
    '''
def eventValidate():
    '''public void eventValidate(final String subject, final EventMessage msg, final EventTopic topic)
    public void eventValidate(final String subject, final EventMessage msg)
    '''
def eventAction():
    '''public void eventAction(final String subject, final EventMessage msg, final EventTopic topic)
    public void eventAction(final String subject, final EventMessage msg)
    '''
def preSaveEventAction():
    '''public void preSaveEventAction(final String subject, final EventMessage msg, final EventTopic et)
    public void preSaveEventAction(final String subject, final EventMessage msg)
    '''
def preSaveInternalEventAction():
    '''public void preSaveInternalEventAction(final String subject, final EventMessage msg, final EventTopic et)
    public void preSaveInternalEventAction(final String subject, final EventMessage msg)
    '''
def postSaveInternalEventAction():
    '''public void postSaveInternalEventAction(final String subject, final EventMessage msg, final EventTopic et)
    public void postSaveInternalEventAction(final String subject, final EventMessage msg)
    '''
def postCommitEventAction():
    '''public void postCommitEventAction(final String subject, final EventMessage msg)
    public void postCommitEventAction(final String subject, final EventMessage msg, final EventTopic et)
    '''
def register():
    '''public int register(final String topic, final EventListener evt)
    public int register(final String topic, final EventListener evt, boolean isTenant)
    '''
def unregister():
    '''public void unregister(final String topic, final int id)
    public void unregister(final String topic, final int id, boolean isTenant)
    '''
def registerExtendsTopic():
    '''public void registerExtendsTopic(final String topic, final EventTopic et, final EventListener evt, final int parentId)
    '''
def getEventTopicId():
    '''public int getEventTopicId(final String topic, final EventListener evt)
    public int getEventTopicId(final String topic, final EventListener evt, final boolean isTenant)
    '''
def setTenantList():
    '''public void setTenantList(final List<Integer> tenantList)
    '''
