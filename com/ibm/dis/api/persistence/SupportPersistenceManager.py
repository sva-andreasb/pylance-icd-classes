def ():
    '''returns SupportPersistenceManager\n\n
    (final Connection conn, final Guid mssGuid)\n
    '''
def deleteMssClassSupport():
    '''returns None\n\n
    deleteMssClassSupport(final Collection<Guid> classGuids)\n
    '''
def supportsClass():
    '''returns boolean\n\n
    supportsClass(final Guid classGuid)\n
    '''
def insertMssOperations():
    '''returns None\n\n
    insertMssOperations(final Guid classGuid, final EnumSet<ClassOperation> operations)\n
    '''
def updateMssOperations():
    '''returns None\n\n
    updateMssOperations(final Guid classGuid, final EnumSet<ClassOperation> operations)\n
    '''
def getCurrentTS():
    '''returns Timestamp\n\n
    getCurrentTS()\n
    '''
def registerSupportedAttributes():
    '''returns None\n\n
    registerSupportedAttributes(final DataIntegrationServices dis, final Guid classGuid, final String className, final List<String> attributes)\n
    '''
def execute():
    '''returns Integer\n\n
    execute(Integer batch, final ObjectAttribute attr)\n
    '''
def fetchExistingClassAttributes():
    '''returns Set<Guid>\n\n
    fetchExistingClassAttributes(final Guid classGuid)\n
    '''
