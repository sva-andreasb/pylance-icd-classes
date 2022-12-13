def ConfigServiceProxy():
    '''    public ConfigServiceProxy(final AdminClient adminClient)
    '''
def getAdminClient():
    '''    public AdminClient getAdminClient()
    '''
def setProperties():
    '''    public void setProperties(final Session session, final HashMap props)
    '''
def validate():
    '''    public ValidationResult validate(final Session session, final ObjectName scope)
    '''
def save():
    '''    public void save(final Session session, final boolean overwriteOnConflict)
    '''
def discard():
    '''    public void discard(final Session session)
    '''
def getUnsavedChanges():
    '''    public String[] getUnsavedChanges(final Session session)
    '''
def getConflictDocuments():
    '''    public Map getConflictDocuments(final Session session)
    '''
def getSupportedConfigObjectTypes():
    '''    public String[] getSupportedConfigObjectTypes()
    '''
def getAttributesMetaInfo():
    '''    public AttributeList getAttributesMetaInfo(final String configDataType)
    '''
def getRelationshipsMetaInfo():
    '''    public AttributeList getRelationshipsMetaInfo(final String configObjectType)
    '''
def queryConfigObjects():
    '''    public ObjectName[] queryConfigObjects(final Session inSession, final ObjectName scope, final ObjectName name, final QueryExp query)
    '''
def queryTemplates():
    '''    public ObjectName[] queryTemplates(final Session inSession, final String type)
    '''
def resolve():
    '''    public ObjectName[] resolve(final Session inSession, final String containmentPath)
    public ObjectName[] resolve(final Session inSession, final ObjectName scope, final String containmentPath)
    '''
def createConfigDataByTemplate():
    '''    public ObjectName createConfigDataByTemplate(final Session inSession, final ObjectName parent, final String attributeName, final AttributeList attrList, final ObjectName template)
    '''
def createConfigData():
    '''    public ObjectName createConfigData(final Session inSession, final ObjectName parent, final String attributeName, final String type, final AttributeList attrList)
    '''
def setAttributes():
    '''    public void setAttributes(final Session inSession, final ObjectName configData, final AttributeList attrList)
    '''
def addElement():
    '''    public void addElement(final Session inSession, final ObjectName configData, final String attribute, final Object element, final int position)
    '''
def removeElement():
    '''    public void removeElement(final Session inSession, final ObjectName configData, final String attribute, final Object element)
    '''
def unsetAttributes():
    '''    public void unsetAttributes(final Session inSession, final ObjectName configData, final String[] attributes)
    '''
def resetAttributes():
    '''    public void resetAttributes(final Session inSession, final ObjectName configData, final AttributeList attrList)
    '''
def getAttributes():
    '''    public AttributeList getAttributes(final Session inSession, final ObjectName configData, final String[] attributes, final boolean recursive)
    '''
def getAttribute():
    '''    public Object getAttribute(final Session inSession, final ObjectName configData, final String attribute)
    public Object getAttribute(final Session session, final ObjectName configData, final String attribute, final boolean recursive)
    '''
def deleteConfigData():
    '''    public void deleteConfigData(final Session inSession, final ObjectName configData)
    '''
def getRelationships():
    '''    public AttributeList getRelationships(final Session inSession, final ObjectName configData, final String[] relationshipNames)
    '''
def getRelationship():
    '''    public ObjectName[] getRelationship(final Session inSession, final ObjectName configData, final String relationship)
    '''
