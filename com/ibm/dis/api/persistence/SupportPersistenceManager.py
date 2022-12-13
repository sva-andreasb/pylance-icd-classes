def SupportPersistenceManager():
'''public SupportPersistenceManager(final Connection conn, final Guid mssGuid)
'''
pass
def deleteMssClassSupport():
'''public void deleteMssClassSupport(final Collection<Guid> classGuids)
'''
pass
def supportsClass():
'''public boolean supportsClass(final Guid classGuid)
'''
pass
def insertMssOperations():
'''public void insertMssOperations(final Guid classGuid, final EnumSet<ClassOperation> operations)
'''
pass
def updateMssOperations():
'''public void updateMssOperations(final Guid classGuid, final EnumSet<ClassOperation> operations)
'''
pass
def getCurrentTS():
'''public Timestamp getCurrentTS()
'''
pass
def forEachTypeAttribute():
'''public static <E> E forEachTypeAttribute(final DataIntegrationServices dis, final String type, E context, final ObjectAttributeAction<E> action)
'''
pass
def registerSupportedAttributes():
'''public void registerSupportedAttributes(final DataIntegrationServices dis, final Guid classGuid, final String className, final List<String> attributes)
'''
pass
def execute():
'''public Integer execute(Integer batch, final ObjectAttribute attr)
'''
pass
def fetchExistingClassAttributes():
'''public Set<Guid> fetchExistingClassAttributes(final Guid classGuid)
'''
pass
