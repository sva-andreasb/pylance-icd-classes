STATE_STARTING = "int  0"
STATE_RUNNING = "int  1"
STATE_STOPPING = "int  2"
STATE_STOPPED = "int  3"
STATE_FAILED = "int  4"
ATTR_CHANGED_NOTIF_TYPE = "String  \"j2ee.attribute.changed\""
def ():
    '''returns J2EEManagedObjectCollaborator\n\n
    ()\n
    (final int initialState)\n
    '''
def getObjectNameStr():
    '''returns String\n\n
    getObjectNameStr()\n
    '''
def isEventProvider():
    '''returns boolean\n\n
    isEventProvider()\n
    '''
def isStateManageable():
    '''returns boolean\n\n
    isStateManageable()\n
    '''
def getEventTypes():
    '''returns String[]\n\n
    getEventTypes()\n
    '''
def getJ2EEState():
    '''returns int\n\n
    getJ2EEState()\n
    '''
def getStartTime():
    '''returns long\n\n
    getStartTime()\n
    '''
def bindMBean():
    '''returns None\n\n
    bindMBean(final ModelMBeanInfo info, final ModelMBean bean)\n
    '''
def handleNotification():
    '''returns None\n\n
    handleNotification(final Notification notif, final Object obj)\n
    '''
