def ():
    '''returns DisRegistrationClient\n\n
    (final IDisWrapper wrapper)\n
    (final JdbcConnectionInfo info)\n
    '''
def registerAbstractResources():
    '''returns List<ObjectId>\n\n
    registerAbstractResources(final ObjectId mssId, final List<ModelObject> instances)\n
    '''
def registerInstance():
    '''returns ObjectId\n\n
    registerInstance(final ObjectId mssId, final ModelObject instance)\n
    '''
def registerInstances():
    '''returns List<ObjectId>\n\n
    registerInstances(final ObjectId mssId, final List<ModelObject> instances)\n
    '''
def registerMss():
    '''returns ObjectId\n\n
    registerMss(final ManagementSoftwareSystem mss)\n
    '''
def registerRelationship():
    '''returns ObjectId\n\n
    registerRelationship(final ObjectId mssId, final Relationship relationship)\n
    registerRelationship(final ObjectId mssId, final String relationshipType, final String sourceSourceToken, final String targetSourceToken)\n
    '''
def registerRelationships():
    '''returns List<ObjectId>\n\n
    registerRelationships(final ObjectId mssId, final List<Relationship> relationships)\n
    '''
def unregisterInstances():
    '''returns None\n\n
    unregisterInstances(final ObjectId mssId, final List<ObjectId> instanceIds)\n
    unregisterInstances(final ObjectId mssId, final ModelObject objectFilter)\n
    '''
def unregisterRelationship():
    '''returns None\n\n
    unregisterRelationship(final ObjectId mssId, final ObjectId relationshipId)\n
    unregisterRelationship(final ObjectId mssId, final Relationship relationshipFilter)\n
    '''
def updateInstance():
    '''returns None\n\n
    updateInstance(final ObjectId mssId, final ObjectId instanceId, final Map<String, Object> updatedAttributes)\n
    '''
def unregisterTask():
    '''returns None\n\n
    unregisterTask(final ObjectId mssId, String className, String taskName)\n
    '''
def getDisInstance():
    '''returns DataIntegrationServices\n\n
    getDisInstance()\n
    '''
def setDisInstance():
    '''returns None\n\n
    setDisInstance(final DataIntegrationServices dis)\n
    '''
def commit():
    '''returns None\n\n
    commit()\n
    '''
def rollback():
    '''returns None\n\n
    rollback()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def registerClassSupport():
    '''returns None\n\n
    registerClassSupport(final ObjectId mssId, final String unvalidatedClassName, final Set<String> attributeNames, final EnumSet<ClassOperation> operations)\n
    '''
def registerNewAttributes():
    '''returns None\n\n
    registerNewAttributes(final String className, final Set<ObjectAttribute> attributeNames)\n
    '''
def registerNewClass():
    '''returns None\n\n
    registerNewClass(final ObjectClass newClass)\n
    '''
def unregisterAttributes():
    '''returns None\n\n
    unregisterAttributes(final String className, final Set<String> attributeNames)\n
    '''
def unregisterClassSupport():
    '''returns None\n\n
    unregisterClassSupport(final ObjectId mssId, final Set<String> classNames)\n
    '''
def unregisterClasses():
    '''returns None\n\n
    unregisterClasses(final Set<String> classNames)\n
    '''
