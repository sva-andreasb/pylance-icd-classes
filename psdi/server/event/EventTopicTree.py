def ():
    '''returns EventTopicTree\n\n
    ()\n
    (final EventTopicTree gEventTopicTree)\n
    '''
def setOwnerTree():
    '''returns None\n\n
    setOwnerTree(final EventTopicTree tree)\n
    '''
def getOwnerTree():
    '''returns EventTopicTree\n\n
    getOwnerTree()\n
    '''
def setActive():
    '''returns None\n\n
    setActive(final boolean value)\n
    '''
def isActive():
    '''returns boolean\n\n
    isActive()\n
    '''
def getEventTopics():
    '''returns Hashtable\n\n
    getEventTopics()\n
    '''
def findEventTopic():
    '''returns EventTopic\n\n
    findEventTopic(final String subject)\n
    findEventTopic(String subject, final boolean isTenant)\n
    '''
def printEventTopicTree():
    '''returns String\n\n
    printEventTopicTree(boolean isTenant)\n
    '''
def eventValidate():
    '''returns None\n\n
    eventValidate(final String subject, final EventMessage msg, final EventTopic topic)\n
    eventValidate(final String subject, final EventMessage msg)\n
    '''
def eventAction():
    '''returns None\n\n
    eventAction(final String subject, final EventMessage msg, final EventTopic topic)\n
    eventAction(final String subject, final EventMessage msg)\n
    '''
def preSaveEventAction():
    '''returns None\n\n
    preSaveEventAction(final String subject, final EventMessage msg, final EventTopic et)\n
    preSaveEventAction(final String subject, final EventMessage msg)\n
    '''
def preSaveInternalEventAction():
    '''returns None\n\n
    preSaveInternalEventAction(final String subject, final EventMessage msg, final EventTopic et)\n
    preSaveInternalEventAction(final String subject, final EventMessage msg)\n
    '''
def postSaveInternalEventAction():
    '''returns None\n\n
    postSaveInternalEventAction(final String subject, final EventMessage msg, final EventTopic et)\n
    postSaveInternalEventAction(final String subject, final EventMessage msg)\n
    '''
def postCommitEventAction():
    '''returns None\n\n
    postCommitEventAction(final String subject, final EventMessage msg)\n
    postCommitEventAction(final String subject, final EventMessage msg, final EventTopic et)\n
    '''
def register():
    '''returns int\n\n
    register(final String topic, final EventListener evt)\n
    register(final String topic, final EventListener evt, boolean isTenant)\n
    '''
def unregister():
    '''returns None\n\n
    unregister(final String topic, final int id)\n
    unregister(final String topic, final int id, boolean isTenant)\n
    '''
def registerExtendsTopic():
    '''returns None\n\n
    registerExtendsTopic(final String topic, final EventTopic et, final EventListener evt, final int parentId)\n
    '''
def getEventTopicId():
    '''returns int\n\n
    getEventTopicId(final String topic, final EventListener evt)\n
    getEventTopicId(final String topic, final EventListener evt, final boolean isTenant)\n
    '''
def setTenantList():
    '''returns None\n\n
    setTenantList(final List<Integer> tenantList)\n
    '''
