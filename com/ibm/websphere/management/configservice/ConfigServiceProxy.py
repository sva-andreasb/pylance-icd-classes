def ():
    '''returns ConfigServiceProxy\n\n
    (final AdminClient adminClient)\n
    '''
def getAdminClient():
    '''returns AdminClient\n\n
    getAdminClient()\n
    '''
def setProperties():
    '''returns None\n\n
    setProperties(final Session session, final HashMap props)\n
    '''
def validate():
    '''returns ValidationResult\n\n
    validate(final Session session, final ObjectName scope)\n
    '''
def save():
    '''returns None\n\n
    save(final Session session, final boolean overwriteOnConflict)\n
    '''
def discard():
    '''returns None\n\n
    discard(final Session session)\n
    '''
def getUnsavedChanges():
    '''returns String[]\n\n
    getUnsavedChanges(final Session session)\n
    '''
def getConflictDocuments():
    '''returns Map\n\n
    getConflictDocuments(final Session session)\n
    '''
def getSupportedConfigObjectTypes():
    '''returns String[]\n\n
    getSupportedConfigObjectTypes()\n
    '''
def getAttributesMetaInfo():
    '''returns AttributeList\n\n
    getAttributesMetaInfo(final String configDataType)\n
    '''
def getRelationshipsMetaInfo():
    '''returns AttributeList\n\n
    getRelationshipsMetaInfo(final String configObjectType)\n
    '''
def queryConfigObjects():
    '''returns ObjectName[]\n\n
    queryConfigObjects(final Session inSession, final ObjectName scope, final ObjectName name, final QueryExp query)\n
    '''
def queryTemplates():
    '''returns ObjectName[]\n\n
    queryTemplates(final Session inSession, final String type)\n
    '''
def resolve():
    '''returns ObjectName[]\n\n
    resolve(final Session inSession, final String containmentPath)\n
    resolve(final Session inSession, final ObjectName scope, final String containmentPath)\n
    '''
def createConfigDataByTemplate():
    '''returns ObjectName\n\n
    createConfigDataByTemplate(final Session inSession, final ObjectName parent, final String attributeName, final AttributeList attrList, final ObjectName template)\n
    '''
def createConfigData():
    '''returns ObjectName\n\n
    createConfigData(final Session inSession, final ObjectName parent, final String attributeName, final String type, final AttributeList attrList)\n
    '''
def setAttributes():
    '''returns None\n\n
    setAttributes(final Session inSession, final ObjectName configData, final AttributeList attrList)\n
    '''
def addElement():
    '''returns None\n\n
    addElement(final Session inSession, final ObjectName configData, final String attribute, final Object element, final int position)\n
    '''
def removeElement():
    '''returns None\n\n
    removeElement(final Session inSession, final ObjectName configData, final String attribute, final Object element)\n
    '''
def unsetAttributes():
    '''returns None\n\n
    unsetAttributes(final Session inSession, final ObjectName configData, final String[] attributes)\n
    '''
def resetAttributes():
    '''returns None\n\n
    resetAttributes(final Session inSession, final ObjectName configData, final AttributeList attrList)\n
    '''
def getAttributes():
    '''returns AttributeList\n\n
    getAttributes(final Session inSession, final ObjectName configData, final String[] attributes, final boolean recursive)\n
    '''
def getAttribute():
    '''returns Object\n\n
    getAttribute(final Session inSession, final ObjectName configData, final String attribute)\n
    getAttribute(final Session session, final ObjectName configData, final String attribute, final boolean recursive)\n
    '''
def deleteConfigData():
    '''returns None\n\n
    deleteConfigData(final Session inSession, final ObjectName configData)\n
    '''
def getRelationships():
    '''returns AttributeList\n\n
    getRelationships(final Session inSession, final ObjectName configData, final String[] relationshipNames)\n
    '''
def getRelationship():
    '''returns ObjectName[]\n\n
    getRelationship(final Session inSession, final ObjectName configData, final String relationship)\n
    '''
