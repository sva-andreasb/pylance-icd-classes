def EventTopicTree():
'''public EventTopicTree()
public EventTopicTree(final EventTopicTree gEventTopicTree)
'''
pass
def setOwnerTree():
'''public void setOwnerTree(final EventTopicTree tree)
'''
pass
def getOwnerTree():
'''public EventTopicTree getOwnerTree()
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
def getEventTopics():
'''public Hashtable getEventTopics()
'''
pass
def findEventTopic():
'''public EventTopic findEventTopic(final String subject)
public EventTopic findEventTopic(String subject, final boolean isTenant)
'''
pass
def getEventTopic():
'''public synchronized EventTopic getEventTopic(final String subject)
public synchronized EventTopic getEventTopic(final String subject, final boolean isTenant)
'''
pass
def dumpEventTopicTree():
'''public Map<String, Object> dumpEventTopicTree(boolean isTenant)
'''
pass
def printEventTopicTree():
'''public String printEventTopicTree(boolean isTenant)
'''
pass
def eventValidate():
'''public void eventValidate(final String subject, final EventMessage msg, final EventTopic topic)
public void eventValidate(final String subject, final EventMessage msg)
'''
pass
def eventAction():
'''public void eventAction(final String subject, final EventMessage msg, final EventTopic topic)
public void eventAction(final String subject, final EventMessage msg)
'''
pass
def preSaveEventAction():
'''public void preSaveEventAction(final String subject, final EventMessage msg, final EventTopic et)
public void preSaveEventAction(final String subject, final EventMessage msg)
'''
pass
def preSaveInternalEventAction():
'''public void preSaveInternalEventAction(final String subject, final EventMessage msg, final EventTopic et)
public void preSaveInternalEventAction(final String subject, final EventMessage msg)
'''
pass
def postSaveInternalEventAction():
'''public void postSaveInternalEventAction(final String subject, final EventMessage msg, final EventTopic et)
public void postSaveInternalEventAction(final String subject, final EventMessage msg)
'''
pass
def postCommitEventAction():
'''public void postCommitEventAction(final String subject, final EventMessage msg)
public void postCommitEventAction(final String subject, final EventMessage msg, final EventTopic et)
'''
pass
def register():
'''public int register(final String topic, final EventListener evt)
public int register(final String topic, final EventListener evt, boolean isTenant)
'''
pass
def unregister():
'''public void unregister(final String topic, final int id)
public void unregister(final String topic, final int id, boolean isTenant)
'''
pass
def registerExtendsTopic():
'''public void registerExtendsTopic(final String topic, final EventTopic et, final EventListener evt, final int parentId)
'''
pass
def getEventTopicId():
'''public int getEventTopicId(final String topic, final EventListener evt)
public int getEventTopicId(final String topic, final EventListener evt, final boolean isTenant)
'''
pass
def setTenantList():
'''public void setTenantList(final List<Integer> tenantList)
'''
pass
