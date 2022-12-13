def ConfigServiceProxy():
'''public ConfigServiceProxy(final AdminClient adminClient)
'''
pass
def getAdminClient():
'''public AdminClient getAdminClient()
'''
pass
def setProperties():
'''public void setProperties(final Session session, final HashMap props)
'''
pass
def validate():
'''public ValidationResult validate(final Session session, final ObjectName scope)
'''
pass
def save():
'''public void save(final Session session, final boolean overwriteOnConflict)
'''
pass
def discard():
'''public void discard(final Session session)
'''
pass
def getUnsavedChanges():
'''public String[] getUnsavedChanges(final Session session)
'''
pass
def getConflictDocuments():
'''public Map getConflictDocuments(final Session session)
'''
pass
def getSupportedConfigObjectTypes():
'''public String[] getSupportedConfigObjectTypes()
'''
pass
def getAttributesMetaInfo():
'''public AttributeList getAttributesMetaInfo(final String configDataType)
'''
pass
def getRelationshipsMetaInfo():
'''public AttributeList getRelationshipsMetaInfo(final String configObjectType)
'''
pass
def queryConfigObjects():
'''public ObjectName[] queryConfigObjects(final Session inSession, final ObjectName scope, final ObjectName name, final QueryExp query)
'''
pass
def queryTemplates():
'''public ObjectName[] queryTemplates(final Session inSession, final String type)
'''
pass
def resolve():
'''public ObjectName[] resolve(final Session inSession, final String containmentPath)
public ObjectName[] resolve(final Session inSession, final ObjectName scope, final String containmentPath)
'''
pass
def createConfigDataByTemplate():
'''public ObjectName createConfigDataByTemplate(final Session inSession, final ObjectName parent, final String attributeName, final AttributeList attrList, final ObjectName template)
'''
pass
def createConfigData():
'''public ObjectName createConfigData(final Session inSession, final ObjectName parent, final String attributeName, final String type, final AttributeList attrList)
'''
pass
def setAttributes():
'''public void setAttributes(final Session inSession, final ObjectName configData, final AttributeList attrList)
'''
pass
def addElement():
'''public void addElement(final Session inSession, final ObjectName configData, final String attribute, final Object element, final int position)
'''
pass
def removeElement():
'''public void removeElement(final Session inSession, final ObjectName configData, final String attribute, final Object element)
'''
pass
def unsetAttributes():
'''public void unsetAttributes(final Session inSession, final ObjectName configData, final String[] attributes)
'''
pass
def resetAttributes():
'''public void resetAttributes(final Session inSession, final ObjectName configData, final AttributeList attrList)
'''
pass
def getAttributes():
'''public AttributeList getAttributes(final Session inSession, final ObjectName configData, final String[] attributes, final boolean recursive)
'''
pass
def getAttribute():
'''public Object getAttribute(final Session inSession, final ObjectName configData, final String attribute)
public Object getAttribute(final Session session, final ObjectName configData, final String attribute, final boolean recursive)
'''
pass
def deleteConfigData():
'''public void deleteConfigData(final Session inSession, final ObjectName configData)
'''
pass
def getRelationships():
'''public AttributeList getRelationships(final Session inSession, final ObjectName configData, final String[] relationshipNames)
'''
pass
def getRelationship():
'''public ObjectName[] getRelationship(final Session inSession, final ObjectName configData, final String relationship)
'''
pass
