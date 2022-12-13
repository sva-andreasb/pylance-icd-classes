def DBPropGraph():
'''public DBPropGraph(final SpecializedGraph g, final String symbolicName, final String type)
public DBPropGraph(final SpecializedGraph g, final Node n)
public DBPropGraph(final SpecializedGraph g, final String newSymbolicName, final Graph oldProperties)
'''
pass
def begin():
'''public boolean begin()
'''
pass
def conditionalCommit():
'''public void conditionalCommit(final boolean commit)
'''
pass
def addLSet():
'''public void addLSet(final DBPropLSet lset)
'''
pass
def addPrefix():
'''public void addPrefix(final String prefix, final String uri)
'''
pass
def bnodeForPrefix():
'''public Node bnodeForPrefix(final Node prefixNode)
'''
pass
def removePrefix():
'''public void removePrefix(final String prefix)
'''
pass
def addGraphId():
'''public void addGraphId(final int id)
'''
pass
def addStmtTable():
'''public void addStmtTable(final String table)
'''
pass
def addReifTable():
'''public void addReifTable(final String table)
'''
pass
def getName():
'''public String getName()
'''
pass
def getType():
'''public String getType()
'''
pass
def getStmtTable():
'''public String getStmtTable()
'''
pass
def getReifTable():
'''public String getReifTable()
'''
pass
def getGraphId():
'''public int getGraphId()
'''
pass
def getAllLSets():
'''public ExtendedIterator<DBPropLSet> getAllLSets()
'''
pass
def getAllPrefixes():
'''public ExtendedIterator<DBPropPrefix> getAllPrefixes()
'''
pass
def listTriples():
'''public ExtendedIterator<Triple> listTriples()
'''
pass
def findPropGraphByName():
'''public static DBPropGraph findPropGraphByName(final SpecializedGraph graph, final String name)
'''
pass
def isDBPropGraphOk():
'''public boolean isDBPropGraphOk(final String name)
'''
pass
def remove():
'''public void remove()
'''
pass
def map1():
'''public DBPropLSet map1(final Triple t)
public DBPropPrefix map1(final Triple t)
'''
pass
