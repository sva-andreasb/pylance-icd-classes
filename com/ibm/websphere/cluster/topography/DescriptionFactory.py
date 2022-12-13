TYPE_MEMBER_ADDED = "String  \"member.added\""
TYPE_MEMBER_REMOVED = "String  \"member.removed\""
TYPE_ADD_EXTRINSIC = "String  \"type.add.extrinsic\""
TYPE_REMOVE_EXTRINSIC = "String  \"type.remove.extrinsic\""
TYPE_CLUSTER_WEIGHT = "String  \"type.cluster.weight.update\""
TYPE_CLUSTER_UPDATED = "String  \"type.cluster.updated\""
TYPE_MEMENTO_UPDATED = "String  \"type.memento.updated\""
CLUSTER_ACTIVE = "String  \"cluster.active\""
CLUSTER_DEACTIVE = "String  \"cluster.deactive\""
TYPE_CLUSTER_SCOPED_DATA_ADDED = "String  \"type.cluster.scoped.data.added\""
TYPE_CLUSTER_SCOPED_DATA_REMOVED = "String  \"type.cluster.scoped.data.removed\""
TYPE_MEMBER_SCOPED_DATA_ADDED = "String  \"type.member.scoped.data.added\""
def getInstance():
    '''public static DescriptionFactory getInstance()
    '''
def createDescription():
    '''public Description createDescription(final DescriptionKey key, final String implKey)
    '''
def createLocalDescription():
    '''public Description createLocalDescription(final DescriptionKey key, final String implementationKey)
    '''
def registerNotificationListener():
    '''public synchronized void registerNotificationListener(final DescriptionModificationListener listener, final String key, final String type)
    '''
def deregisterNotificationListener():
    '''public synchronized void deregisterNotificationListener(final DescriptionModificationListener listener, final String key, final String type)
    '''
def notifyListeners():
    '''public void notifyListeners(final DescriptionKey key, final String type, final Object data)
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def run():
    '''public void run()
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def hashCode():
    '''public int hashCode()
    '''
