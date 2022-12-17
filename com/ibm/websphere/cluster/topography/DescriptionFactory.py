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
def createDescription():
    '''returns Description\n\n
    createDescription(final DescriptionKey key, final String implKey)\n
    '''
def createLocalDescription():
    '''returns Description\n\n
    createLocalDescription(final DescriptionKey key, final String implementationKey)\n
    '''
def notifyListeners():
    '''returns None\n\n
    notifyListeners(final DescriptionKey key, final String type, final Object data)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
