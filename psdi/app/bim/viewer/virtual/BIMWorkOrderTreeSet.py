def BIMWorkOrderTreeSet():
    '''    public BIMWorkOrderTreeSet(final MboServerInterface ms)
    '''
def clear():
    '''    public void clear()
    '''
def getChildren():
    '''    public MboValueData[][] getChildren(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getParent():
    '''    public MboValueData[] getParent(final String object, String key, final String[] attrs)
    '''
def getSiblings():
    '''    public MboValueData[][] getSiblings(final String object, String key, final String[] attrs, final int maxRows)
    '''
def getTop():
    '''    public MboValueData[][] getTop(final String[] attrs, final int maxRows)
    '''
def getPathToTop():
    '''    public MboValueData[][] getPathToTop(final String object, String key, final String[] attrs, final int maxRows)
    '''
def count():
    '''    public int count()
    '''
def toBeSaved():
    '''    public boolean toBeSaved()
    '''
def setMboSetInfo():
    '''    public void setMboSetInfo(final MboSetInfo ms)
    '''
def setup():
    '''    public MboRemote setup()
    '''
def execute():
    '''    public void execute()
    public void execute(final MboRemote mbo)
    '''
def getMboForUniqueId():
    '''    public MboRemote getMboForUniqueId(final long uid)
    '''
def getAllHierarchies():
    '''    public MboValueData[][] getAllHierarchies(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getHierarchy():
    '''    public MboValueData[] getHierarchy(final String object, final String key)
    '''
def setHierarchy():
    '''    public void setHierarchy(final String object, final String key, final String hierarchy)
    '''
def getUniqueIDValue():
    '''    public MboValueData getUniqueIDValue(final String object, final String[] attributes, final String[] values)
    '''
