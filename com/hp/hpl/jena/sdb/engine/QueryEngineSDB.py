def QueryEngineSDB():
    '''public QueryEngineSDB(final Store store, final Query q)
    public QueryEngineSDB(final DatasetStoreGraph dsg, final Query query, final Binding initialBinding, final Context context)
    public QueryEngineSDB(final DatasetStoreGraph dsg, final Op op, final Binding initialBinding, final Context context)
    '''
def getRequest():
    '''public SDBRequest getRequest()
    '''
def close():
    '''public void close()
    '''
def eval():
    '''public QueryIterator eval(final Op op, final DatasetGraph dsg, final Binding binding, final Context context)
    '''
def getFactory():
    '''public static QueryEngineFactory getFactory()
    '''
def register():
    '''public static void register()
    '''
def unregister():
    '''public static void unregister()
    '''
def accept():
    '''public boolean accept(final Query query, final DatasetGraph dataset, final Context context)
    public boolean accept(final Op op, final DatasetGraph dataset, final Context context)
    '''
def create():
    '''public Plan create(final Query query, final DatasetGraph dataset, final Binding inputBinding, final Context context)
    public Plan create(final Op op, final DatasetGraph dataset, Binding inputBinding, final Context context)
    '''
