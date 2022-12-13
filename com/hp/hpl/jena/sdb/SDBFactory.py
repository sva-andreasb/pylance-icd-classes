def createConnection():
    '''public static SDBConnection createConnection(final String jdbcURL, final String user, final String password)
    public static SDBConnection createConnection(final SDBConnectionDesc desc)
    public static SDBConnection createConnection(final Connection conn)
    public static SDBConnection createConnection(final String configFile)
    '''
def createSqlConnection():
    '''public static Connection createSqlConnection(final SDBConnectionDesc desc)
    public static Connection createSqlConnection(final String configFile)
    public static Connection createSqlConnection(final Model model)
    '''
def connectStore():
    '''public static Store connectStore(final String configFile)
    public static Store connectStore(final StoreDesc desc)
    public static Store connectStore(final SDBConnection sdbConnection, final StoreDesc desc)
    public static Store connectStore(final Connection sqlConnection, final StoreDesc desc)
    '''
def connectDataset():
    '''public static Dataset connectDataset(final Store store)
    public static Dataset connectDataset(final StoreDesc desc)
    public static Dataset connectDataset(final SDBConnection sdbConnection, final StoreDesc desc)
    public static Dataset connectDataset(final Connection jdbcConnection, final StoreDesc desc)
    public static Dataset connectDataset(final String configFile)
    '''
def connectGraphStore():
    '''public static GraphStore connectGraphStore(final Store store)
    public static GraphStore connectGraphStore(final StoreDesc desc)
    public static GraphStore connectGraphStore(final SDBConnection sdbConnection, final StoreDesc desc)
    public static GraphStore connectGraphStore(final Connection jdbcConnection, final StoreDesc desc)
    public static GraphStore connectGraphStore(final String configFile)
    '''
def connectDefaultGraph():
    '''public static Graph connectDefaultGraph(final String configFile)
    public static Graph connectDefaultGraph(final StoreDesc desc)
    public static Graph connectDefaultGraph(final Store store)
    '''
def connectNamedGraph():
    '''public static Graph connectNamedGraph(final String configFile, final String iri)
    public static Graph connectNamedGraph(final StoreDesc desc, final String iri)
    public static Graph connectNamedGraph(final Store store, final String iri)
    public static Graph connectNamedGraph(final String configFile, final Node node)
    public static Graph connectNamedGraph(final StoreDesc desc, final Node node)
    public static Graph connectNamedGraph(final Store store, final Node node)
    '''
def connectDefaultModel():
    '''public static Model connectDefaultModel(final String configFile)
    public static Model connectDefaultModel(final StoreDesc desc)
    public static Model connectDefaultModel(final Store store)
    '''
def connectNamedModel():
    '''public static Model connectNamedModel(final StoreDesc desc, final String iri)
    public static Model connectNamedModel(final Store store, final String iri)
    public static Model connectNamedModel(final String configFile, final String iri)
    public static Model connectNamedModel(final StoreDesc desc, final Resource resource)
    public static Model connectNamedModel(final Store store, final Resource resource)
    public static Model connectNamedModel(final String configFile, final Resource resource)
    '''
