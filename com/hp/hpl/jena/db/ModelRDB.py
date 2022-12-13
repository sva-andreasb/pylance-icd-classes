def ModelRDB():
    '''    public ModelRDB(final Personality<RDFNode> p, final GraphRDB graph)
    public ModelRDB(final GraphRDB graph)
    '''
def open():
    '''    public static ModelRDB open(final IDBConnection dbcon)
    public static ModelRDB open(final IDBConnection dbcon, final String name)
    '''
def createModel():
    '''    public static ModelRDB createModel(final IDBConnection dbcon)
    public static ModelRDB createModel(final IDBConnection dbcon, final Model modelProperties)
    public static ModelRDB createModel(final IDBConnection dbcon, final String name)
    public static ModelRDB createModel(final IDBConnection dbcon, final String name, final Model modelProperties)
    '''
def getModelProperties():
    '''    public Model getModelProperties()
    '''
def getDefaultModelProperties():
    '''    public static Model getDefaultModelProperties(final IDBConnection dbcon)
    '''
def listModels():
    '''    public static ExtendedIterator<String> listModels(final IDBConnection dbcon)
    '''
def close():
    '''    public void close()
    '''
def remove():
    '''    public void remove()
    '''
def getConnection():
    '''    public IDBConnection getConnection()
    '''
def getDoDuplicateCheck():
    '''    public boolean getDoDuplicateCheck()
    '''
def setDoDuplicateCheck():
    '''    public void setDoDuplicateCheck(final boolean bool)
    '''
def setDoFastpath():
    '''    public void setDoFastpath(final boolean val)
    '''
def getDoFastpath():
    '''    public boolean getDoFastpath()
    '''
def setQueryOnlyAsserted():
    '''    public void setQueryOnlyAsserted(final boolean opt)
    '''
def getQueryOnlyAsserted():
    '''    public boolean getQueryOnlyAsserted()
    '''
def setQueryOnlyReified():
    '''    public void setQueryOnlyReified(final boolean opt)
    '''
def getQueryOnlyReified():
    '''    public boolean getQueryOnlyReified()
    '''
def setQueryFullReified():
    '''    public void setQueryFullReified(final boolean opt)
    '''
def getQueryFullReified():
    '''    public boolean getQueryFullReified()
    '''
def setDoImplicitJoin():
    '''    public void setDoImplicitJoin(final boolean val)
    '''
