def IndexElement():
    '''    public IndexElement(final String name, final Namespace namespace)
    public IndexElement(final String name)
    public IndexElement(final String name, final String uri)
    public IndexElement(final String name, final String prefix, final String uri)
    public IndexElement(final String tbname, final String ixname, final HashMap newIndex, final HashMap oldIndex)
    '''
def getIndexName():
    '''    public String getIndexName()
    '''
def getIndexAttributes():
    '''    public List getIndexAttributes()
    '''
def getKeys():
    '''    public List getKeys()
    '''
def getColNames():
    '''    public String[] getColNames()
    '''
def getAddSql():
    '''    public ArrayList getAddSql(final String tbname, final String ixname, final Connection con, final Util util, HashMap oldIndex)
    '''
def getDropSql():
    '''    public ArrayList getDropSql(final String tbname, final String ixname, final Connection con, final Util util, final HashMap oldIndex)
    '''
def getStatus():
    '''    public String getStatus()
    '''
def getNewChanged():
    '''    public String getNewChanged()
    '''
def setNewChanged():
    '''    public void setNewChanged(final String in)
    '''
def getSequenceName():
    '''    public String getSequenceName(final String table, final String column)
    '''
def toHashmap():
    '''    public HashMap toHashmap(final HashMap oldMap)
    '''
