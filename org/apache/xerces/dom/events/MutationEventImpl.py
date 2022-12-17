DOM_SUBTREE_MODIFIED = "String  \"DOMSubtreeModified\""
DOM_NODE_INSERTED = "String  \"DOMNodeInserted\""
DOM_NODE_REMOVED = "String  \"DOMNodeRemoved\""
DOM_NODE_REMOVED_FROM_DOCUMENT = "String  \"DOMNodeRemovedFromDocument\""
DOM_NODE_INSERTED_INTO_DOCUMENT = "String  \"DOMNodeInsertedIntoDocument\""
DOM_ATTR_MODIFIED = "String  \"DOMAttrModified\""
DOM_CHARACTER_DATA_MODIFIED = "String  \"DOMCharacterDataModified\""
def ():
    '''returns MutationEventImpl\n\n
    ()\n
    '''
def getAttrName():
    '''returns String\n\n
    getAttrName()\n
    '''
def getAttrChange():
    '''returns short\n\n
    getAttrChange()\n
    '''
def getNewValue():
    '''returns String\n\n
    getNewValue()\n
    '''
def getPrevValue():
    '''returns String\n\n
    getPrevValue()\n
    '''
def getRelatedNode():
    '''returns Node\n\n
    getRelatedNode()\n
    '''
def initMutationEvent():
    '''returns None\n\n
    initMutationEvent(final String s, final boolean b, final boolean b2, final Node relatedNode, final String prevValue, final String newValue, final String attrName, final short attrChange)\n
    '''
