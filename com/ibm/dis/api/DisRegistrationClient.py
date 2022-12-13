def DisRegistrationClient():
    '''public DisRegistrationClient(final IDisWrapper wrapper)
    public DisRegistrationClient(final JdbcConnectionInfo info)
    '''
def registerAbstractResources():
    '''public List<ObjectId> registerAbstractResources(final ObjectId mssId, final List<ModelObject> instances)
    '''
def registerInstance():
    '''public ObjectId registerInstance(final ObjectId mssId, final ModelObject instance)
    '''
def registerInstances():
    '''public List<ObjectId> registerInstances(final ObjectId mssId, final List<ModelObject> instances)
    '''
def registerMss():
    '''public ObjectId registerMss(final ManagementSoftwareSystem mss)
    '''
def registerRelationship():
    '''public ObjectId registerRelationship(final ObjectId mssId, final Relationship relationship)
    public ObjectId registerRelationship(final ObjectId mssId, final String relationshipType, final String sourceSourceToken, final String targetSourceToken)
    '''
def registerRelationships():
    '''public List<ObjectId> registerRelationships(final ObjectId mssId, final List<Relationship> relationships)
    '''
def unregisterInstances():
    '''public void unregisterInstances(final ObjectId mssId, final List<ObjectId> instanceIds)
    public void unregisterInstances(final ObjectId mssId, final ModelObject objectFilter)
    '''
def unregisterRelationship():
    '''public void unregisterRelationship(final ObjectId mssId, final ObjectId relationshipId)
    public void unregisterRelationship(final ObjectId mssId, final Relationship relationshipFilter)
    '''
def updateInstance():
    '''public void updateInstance(final ObjectId mssId, final ObjectId instanceId, final Map<String, Object> updatedAttributes)
    '''
def registerTask():
    '''public final void registerTask(final ObjectId mssId, String className, final Task task)
    '''
def unregisterTask():
    '''public void unregisterTask(final ObjectId mssId, String className, String taskName)
    '''
def getDisInstance():
    '''public DataIntegrationServices getDisInstance()
    '''
def setDisInstance():
    '''public void setDisInstance(final DataIntegrationServices dis)
    '''
def commit():
    '''public void commit()
    '''
def rollback():
    '''public void rollback()
    '''
def close():
    '''public void close()
    '''
def registerClassSupport():
    '''public void registerClassSupport(final ObjectId mssId, final String unvalidatedClassName, final Set<String> attributeNames, final EnumSet<ClassOperation> operations)
    '''
def registerNewAttributes():
    '''public void registerNewAttributes(final String className, final Set<ObjectAttribute> attributeNames)
    '''
def registerNewClass():
    '''public void registerNewClass(final ObjectClass newClass)
    '''
def unregisterAttributes():
    '''public void unregisterAttributes(final String className, final Set<String> attributeNames)
    '''
def unregisterClassSupport():
    '''public void unregisterClassSupport(final ObjectId mssId, final Set<String> classNames)
    '''
def unregisterClasses():
    '''public void unregisterClasses(final Set<String> classNames)
    '''
