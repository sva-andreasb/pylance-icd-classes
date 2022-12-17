local = "String  \"WLMTemplate\""
remote = "String  \"WLMService\""
def ():
    '''returns WLMTemplateImpl\n\n
    (final ORB orb)\n
    '''
def _ids():
    '''returns String[]\n\n
    _ids()\n
    '''
def keyToObject():
    '''returns Object\n\n
    keyToObject(final byte[] key)\n
    '''
def ping():
    '''returns long\n\n
    ping(String domainName, final String clusterName)\n
    '''
def push():
    '''returns None\n\n
    push(final String domainName, final String clusterName, final byte[] modelInformation)\n
    '''
def pull():
    '''returns byte[]\n\n
    pull()\n
    pull(String domainName, final String clusterName)\n
    '''
def pushSelf():
    '''returns byte[]\n\n
    pushSelf(String domainName, final String clusterName, final String member, final String ior)\n
    '''
def registerListener():
    '''returns None\n\n
    registerListener(final DescriptionKey clusterKey, final String member, final String ior)\n
    '''
def removeMember():
    '''returns None\n\n
    removeMember(String member, final String nodeName, final String processName)\n
    '''
def setWeightTable():
    '''returns None\n\n
    setWeightTable(final String clusterName, final ClusterWeightTableEntry[] weightTable)\n
    '''
def deregisterListener():
    '''returns None\n\n
    deregisterListener(final DescriptionKey clusterKey, final String member)\n
    '''
def notifyListeners():
    '''returns None\n\n
    notifyListeners(final DescriptionKey key, final String clusterName, final byte[] clusterInfo)\n
    '''
