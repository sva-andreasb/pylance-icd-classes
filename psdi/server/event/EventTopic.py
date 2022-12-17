def ():
    '''returns Subscription\n\n
    (final String subject)\n
    (final EventListener eval)\n
    '''
def setTree():
    '''returns None\n\n
    setTree(final EventTopicTree tree)\n
    '''
def setExtendedSubIds():
    '''returns None\n\n
    setExtendedSubIds(final Map<Integer, List<Integer>> idMap)\n
    '''
def getExtendedSubIds():
    '''returns Map\n\n
    getExtendedSubIds()\n
    '''
def getTree():
    '''returns EventTopicTree\n\n
    getTree()\n
    '''
def getSubject():
    '''returns String\n\n
    getSubject()\n
    '''
def getSubTopicTree():
    '''returns EventTopicTree\n\n
    getSubTopicTree()\n
    '''
def setActive():
    '''returns None\n\n
    setActive(final boolean value)\n
    '''
def isActive():
    '''returns boolean\n\n
    isActive()\n
    '''
def eventValidate():
    '''returns boolean\n\n
    eventValidate(final EventMessage msg)\n
    eventValidate(final EventMessage em)\n
    '''
def eventAction():
    '''returns None\n\n
    eventAction(final EventMessage msg)\n
    eventAction(final EventMessage em)\n
    '''
def preSaveEventAction():
    '''returns None\n\n
    preSaveEventAction(final EventMessage msg)\n
    preSaveEventAction(final EventMessage em)\n
    '''
def preSaveInternalEventAction():
    '''returns None\n\n
    preSaveInternalEventAction(final EventMessage msg)\n
    preSaveInternalEventAction(final EventMessage em)\n
    '''
def postSaveInternalEventAction():
    '''returns None\n\n
    postSaveInternalEventAction(final EventMessage msg)\n
    postSaveInternalEventAction(final EventMessage em)\n
    '''
def postCommitEventAction():
    '''returns None\n\n
    postCommitEventAction(final EventMessage msg)\n
    postCommitEventAction(final EventMessage em)\n
    '''
def addSubTopic():
    '''returns None\n\n
    addSubTopic(final EventTopic ev)\n
    '''
def getEventTopic():
    '''returns EventTopic\n\n
    getEventTopic(String subject)\n
    '''
def getListenerCount():
    '''returns int\n\n
    getListenerCount()\n
    '''
def getSubscriptionId():
    '''returns int\n\n
    getSubscriptionId(final EventListener evt)\n
    '''
def getSubscriptionIdByClassName():
    '''returns int\n\n
    getSubscriptionIdByClassName(final EventListener evt)\n
    '''
def dumpTopic():
    '''returns Map\n\n
    dumpTopic()\n
    '''
def getId():
    '''returns int\n\n
    getId()\n
    '''
