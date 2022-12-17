def ():
    '''returns DeliveryServiceStub\n\n
    ()\n
    (final URL endpointURL, final Service service)\n
    (final Service service)\n
    '''
def addNotification():
    '''returns AsynchReply\n\n
    addNotification(final SearchPathSingleObject objectPath)\n
    '''
def cancel():
    '''returns None\n\n
    cancel(final AsynchRequest conversation)\n
    '''
def clearNotifications():
    '''returns AsynchReply\n\n
    clearNotifications(final SearchPathSingleObject objectPath)\n
    '''
def deleteAllNotifications():
    '''returns AsynchReply\n\n
    deleteAllNotifications()\n
    '''
def deleteNotification():
    '''returns AsynchReply\n\n
    deleteNotification(final SearchPathSingleObject objectPath)\n
    '''
def queryNotification():
    '''returns AsynchReply\n\n
    queryNotification(final SearchPathSingleObject objectPath)\n
    '''
def release():
    '''returns None\n\n
    release(final AsynchRequest conversation)\n
    '''
def run():
    '''returns AsynchReply\n\n
    run(final SearchPathSingleObject objectPath, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def runSpecification():
    '''returns AsynchReply\n\n
    runSpecification(final AsynchSpecification specification, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
def wait():
    '''returns AsynchReply\n\n
    wait(final AsynchRequest conversation, final ParameterValue[] parameterValues, final Option[] options)\n
    '''
