def DisRegistrationClient():
'''public DisRegistrationClient(final IDisWrapper wrapper)
public DisRegistrationClient(final JdbcConnectionInfo info)
'''
pass
def registerAbstractResources():
'''public List<ObjectId> registerAbstractResources(final ObjectId mssId, final List<ModelObject> instances)
'''
pass
def registerInstance():
'''public ObjectId registerInstance(final ObjectId mssId, final ModelObject instance)
'''
pass
def registerInstances():
'''public List<ObjectId> registerInstances(final ObjectId mssId, final List<ModelObject> instances)
'''
pass
def registerMss():
'''public ObjectId registerMss(final ManagementSoftwareSystem mss)
'''
pass
def registerRelationship():
'''public ObjectId registerRelationship(final ObjectId mssId, final Relationship relationship)
public ObjectId registerRelationship(final ObjectId mssId, final String relationshipType, final String sourceSourceToken, final String targetSourceToken)
'''
pass
def registerRelationships():
'''public List<ObjectId> registerRelationships(final ObjectId mssId, final List<Relationship> relationships)
'''
pass
def unregisterInstances():
'''public void unregisterInstances(final ObjectId mssId, final List<ObjectId> instanceIds)
public void unregisterInstances(final ObjectId mssId, final ModelObject objectFilter)
'''
pass
def unregisterRelationship():
'''public void unregisterRelationship(final ObjectId mssId, final ObjectId relationshipId)
public void unregisterRelationship(final ObjectId mssId, final Relationship relationshipFilter)
'''
pass
def updateInstance():
'''public void updateInstance(final ObjectId mssId, final ObjectId instanceId, final Map<String, Object> updatedAttributes)
'''
pass
def registerTask():
'''public final void registerTask(final ObjectId mssId, String className, final Task task)
'''
pass
def unregisterTask():
'''public void unregisterTask(final ObjectId mssId, String className, String taskName)
'''
pass
def getDisInstance():
'''public DataIntegrationServices getDisInstance()
'''
pass
def setDisInstance():
'''public void setDisInstance(final DataIntegrationServices dis)
'''
pass
def commit():
'''public void commit()
'''
pass
def rollback():
'''public void rollback()
'''
pass
def close():
'''public void close()
'''
pass
def registerClassSupport():
'''public void registerClassSupport(final ObjectId mssId, final String unvalidatedClassName, final Set<String> attributeNames, final EnumSet<ClassOperation> operations)
'''
pass
def registerNewAttributes():
'''public void registerNewAttributes(final String className, final Set<ObjectAttribute> attributeNames)
'''
pass
def registerNewClass():
'''public void registerNewClass(final ObjectClass newClass)
'''
pass
def unregisterAttributes():
'''public void unregisterAttributes(final String className, final Set<String> attributeNames)
'''
pass
def unregisterClassSupport():
'''public void unregisterClassSupport(final ObjectId mssId, final Set<String> classNames)
'''
pass
def unregisterClasses():
'''public void unregisterClasses(final Set<String> classNames)
'''
pass
