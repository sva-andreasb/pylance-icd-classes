def DBPropGraph():
    '''    public DBPropGraph(final SpecializedGraph g, final String symbolicName, final String type)
    public DBPropGraph(final SpecializedGraph g, final Node n)
    public DBPropGraph(final SpecializedGraph g, final String newSymbolicName, final Graph oldProperties)
    '''
def begin():
    '''    public boolean begin()
    '''
def conditionalCommit():
    '''    public void conditionalCommit(final boolean commit)
    '''
def addLSet():
    '''    public void addLSet(final DBPropLSet lset)
    '''
def addPrefix():
    '''    public void addPrefix(final String prefix, final String uri)
    '''
def bnodeForPrefix():
    '''    public Node bnodeForPrefix(final Node prefixNode)
    '''
def removePrefix():
    '''    public void removePrefix(final String prefix)
    '''
def addGraphId():
    '''    public void addGraphId(final int id)
    '''
def addStmtTable():
    '''    public void addStmtTable(final String table)
    '''
def addReifTable():
    '''    public void addReifTable(final String table)
    '''
def getName():
    '''    public String getName()
    '''
def getType():
    '''    public String getType()
    '''
def getStmtTable():
    '''    public String getStmtTable()
    '''
def getReifTable():
    '''    public String getReifTable()
    '''
def getGraphId():
    '''    public int getGraphId()
    '''
def getAllLSets():
    '''    public ExtendedIterator<DBPropLSet> getAllLSets()
    '''
def getAllPrefixes():
    '''    public ExtendedIterator<DBPropPrefix> getAllPrefixes()
    '''
def listTriples():
    '''    public ExtendedIterator<Triple> listTriples()
    '''
def findPropGraphByName():
    '''    public static DBPropGraph findPropGraphByName(final SpecializedGraph graph, final String name)
    '''
def isDBPropGraphOk():
    '''    public boolean isDBPropGraphOk(final String name)
    '''
def remove():
    '''    public void remove()
    '''
def map1():
    '''    public DBPropLSet map1(final Triple t)
    public DBPropPrefix map1(final Triple t)
    '''
