DOM_SUBTREE_MODIFIED = "String  \"DOMSubtreeModified\""
DOM_NODE_INSERTED = "String  \"DOMNodeInserted\""
DOM_NODE_REMOVED = "String  \"DOMNodeRemoved\""
DOM_NODE_REMOVED_FROM_DOCUMENT = "String  \"DOMNodeRemovedFromDocument\""
DOM_NODE_INSERTED_INTO_DOCUMENT = "String  \"DOMNodeInsertedIntoDocument\""
DOM_ATTR_MODIFIED = "String  \"DOMAttrModified\""
DOM_CHARACTER_DATA_MODIFIED = "String  \"DOMCharacterDataModified\""
def MutationEventImpl():
    '''public MutationEventImpl()
    '''
def getAttrName():
    '''public String getAttrName()
    '''
def getAttrChange():
    '''public short getAttrChange()
    '''
def getNewValue():
    '''public String getNewValue()
    '''
def getPrevValue():
    '''public String getPrevValue()
    '''
def getRelatedNode():
    '''public Node getRelatedNode()
    '''
def initMutationEvent():
    '''public void initMutationEvent(final String s, final boolean b, final boolean b2, final Node relatedNode, final String prevValue, final String newValue, final String attrName, final short attrChange)
    '''
