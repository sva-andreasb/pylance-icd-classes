def EventTopic():
'''public EventTopic(final String subject)
'''
pass
def setTree():
'''public void setTree(final EventTopicTree tree)
'''
pass
def setExtendedSubIds():
'''public void setExtendedSubIds(final Map<Integer, List<Integer>> idMap)
'''
pass
def getExtendedSubIds():
'''public Map getExtendedSubIds()
'''
pass
def getTree():
'''public EventTopicTree getTree()
'''
pass
def getSubject():
'''public String getSubject()
'''
pass
def getSubTopicTree():
'''public EventTopicTree getSubTopicTree()
'''
pass
def setActive():
'''public void setActive(final boolean value)
'''
pass
def isActive():
'''public boolean isActive()
'''
pass
def eventValidate():
'''public void eventValidate(final EventMessage msg)
public boolean eventValidate(final EventMessage em)
'''
pass
def eventAction():
'''public void eventAction(final EventMessage msg)
public void eventAction(final EventMessage em)
'''
pass
def preSaveEventAction():
'''public void preSaveEventAction(final EventMessage msg)
public void preSaveEventAction(final EventMessage em)
'''
pass
def preSaveInternalEventAction():
'''public void preSaveInternalEventAction(final EventMessage msg)
public void preSaveInternalEventAction(final EventMessage em)
'''
pass
def postSaveInternalEventAction():
'''public void postSaveInternalEventAction(final EventMessage msg)
public void postSaveInternalEventAction(final EventMessage em)
'''
pass
def postCommitEventAction():
'''public void postCommitEventAction(final EventMessage msg)
public void postCommitEventAction(final EventMessage em)
'''
pass
def addSubTopic():
'''public void addSubTopic(final EventTopic ev)
'''
pass
def getEventTopic():
'''public EventTopic getEventTopic(String subject)
'''
pass
def getListeners():
'''public Map<Integer, EventListener> getListeners()
'''
pass
def getListenerCount():
'''public int getListenerCount()
'''
pass
def getSubscriptionId():
'''public int getSubscriptionId(final EventListener evt)
'''
pass
def getSubscriptionIdByClassName():
'''public int getSubscriptionIdByClassName(final EventListener evt)
'''
pass
def dumpTopic():
'''public Map dumpTopic()
'''
pass
def Subscription():
'''public Subscription(final EventListener eval)
'''
pass
def getId():
'''public int getId()
'''
pass
