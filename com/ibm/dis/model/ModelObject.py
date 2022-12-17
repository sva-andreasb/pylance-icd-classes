def ():
    '''returns ModelObject\n\n
    ()\n
    (final String className, final String sourceToken, final Map<String, Object> attributes)\n
    (final String className, final String sourceToken, final Map<String, Object> attributes, final Map<String, List<IModelObjectRef>> relationshipAttributes)\n
    '''
def getClassName():
    '''returns String\n\n
    getClassName()\n
    '''
def getSourceToken():
    '''returns String\n\n
    getSourceToken()\n
    '''
def getAttributeValue():
    '''returns Object\n\n
    getAttributeValue(final String attributeName)\n
    '''
def getRelationshipAttributeValue():
    '''returns List<IModelObjectRef>\n\n
    getRelationshipAttributeValue(final String attributeName)\n
    '''
def getObjectIds():
    '''returns List<ObjectId>\n\n
    getObjectIds()\n
    '''
def setClassName():
    '''returns None\n\n
    setClassName(final String className)\n
    '''
def setSourceToken():
    '''returns None\n\n
    setSourceToken(final String sourceToken)\n
    '''
def setAttributes():
    '''returns None\n\n
    setAttributes(final Map<String, Object> attributes)\n
    '''
def setAttributeValue():
    '''returns None\n\n
    setAttributeValue(final String attributeName, final Object value)\n
    '''
def setRelationshipAttributes():
    '''returns None\n\n
    setRelationshipAttributes(final Map<String, List<IModelObjectRef>> relationshipAttributes)\n
    '''
def addRelationshipAttributeValue():
    '''returns None\n\n
    addRelationshipAttributeValue(final String relationshipAttributeName, final IModelObjectRef value)\n
    '''
def addObjectId():
    '''returns None\n\n
    addObjectId(final ObjectId id)\n
    '''
