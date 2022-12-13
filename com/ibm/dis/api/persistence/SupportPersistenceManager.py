def SupportPersistenceManager():
    '''public SupportPersistenceManager(final Connection conn, final Guid mssGuid)
    '''
def deleteMssClassSupport():
    '''public void deleteMssClassSupport(final Collection<Guid> classGuids)
    '''
def supportsClass():
    '''public boolean supportsClass(final Guid classGuid)
    '''
def insertMssOperations():
    '''public void insertMssOperations(final Guid classGuid, final EnumSet<ClassOperation> operations)
    '''
def updateMssOperations():
    '''public void updateMssOperations(final Guid classGuid, final EnumSet<ClassOperation> operations)
    '''
def getCurrentTS():
    '''public Timestamp getCurrentTS()
    '''
def forEachTypeAttribute():
    '''public static <E> E forEachTypeAttribute(final DataIntegrationServices dis, final String type, E context, final ObjectAttributeAction<E> action)
    '''
def registerSupportedAttributes():
    '''public void registerSupportedAttributes(final DataIntegrationServices dis, final Guid classGuid, final String className, final List<String> attributes)
    '''
def execute():
    '''public Integer execute(Integer batch, final ObjectAttribute attr)
    '''
def fetchExistingClassAttributes():
    '''public Set<Guid> fetchExistingClassAttributes(final Guid classGuid)
    '''
