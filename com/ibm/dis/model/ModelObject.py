def ModelObject():
    '''public ModelObject()
    public ModelObject(final String className, final String sourceToken, final Map<String, Object> attributes)
    public ModelObject(final String className, final String sourceToken, final Map<String, Object> attributes, final Map<String, List<IModelObjectRef>> relationshipAttributes)
    '''
def getClassName():
    '''public String getClassName()
    '''
def getSourceToken():
    '''public String getSourceToken()
    '''
def getAttributes():
    '''public Map<String, Object> getAttributes()
    '''
def getAttributeValue():
    '''public Object getAttributeValue(final String attributeName)
    '''
def getRelationshipAttributes():
    '''public Map<String, List<IModelObjectRef>> getRelationshipAttributes()
    '''
def getRelationshipAttributeValue():
    '''public List<IModelObjectRef> getRelationshipAttributeValue(final String attributeName)
    '''
def getObjectIds():
    '''public List<ObjectId> getObjectIds()
    '''
def setClassName():
    '''public void setClassName(final String className)
    '''
def setSourceToken():
    '''public void setSourceToken(final String sourceToken)
    '''
def setAttributes():
    '''public void setAttributes(final Map<String, Object> attributes)
    '''
def setAttributeValue():
    '''public void setAttributeValue(final String attributeName, final Object value)
    '''
def setRelationshipAttributes():
    '''public void setRelationshipAttributes(final Map<String, List<IModelObjectRef>> relationshipAttributes)
    '''
def addRelationshipAttributeValue():
    '''public void addRelationshipAttributeValue(final String relationshipAttributeName, final IModelObjectRef value)
    '''
def addObjectId():
    '''public void addObjectId(final ObjectId id)
    '''
