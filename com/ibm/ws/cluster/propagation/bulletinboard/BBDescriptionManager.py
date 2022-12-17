def ():
    '''returns UpdateThread\n\n
    ()\n
    (final LinkedBlockingQueue<Map<String, SubjectValue[]>> aQueue, final int num)\n
    '''
def getDescription():
    '''returns Description\n\n
    getDescription(final DescriptionKey key, final String implKey)\n
    '''
def publish():
    '''returns boolean\n\n
    publish(final String identifier, final byte[] data)\n
    '''
def updated():
    '''returns None\n\n
    updated(final SubjectSubscription subjectSubscription, final SubjectValue[] values)\n
    '''
def lookupClusterCallback():
    '''returns None\n\n
    lookupClusterCallback(final String clusterName, final Contract contract, final URL location, final DescriptionCallback callback, final Object handback)\n
    '''
def registerService():
    '''returns None\n\n
    registerService(final Connection remoteConnection)\n
    '''
def setThreadForLocalPosting():
    '''returns None\n\n
    setThreadForLocalPosting()\n
    '''
def unsetThreadForLocalPosting():
    '''returns None\n\n
    unsetThreadForLocalPosting()\n
    '''
def removeDuplicateProxyPosts():
    '''returns SubjectValue[]\n\n
    removeDuplicateProxyPosts(final SubjectValue[] values)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
