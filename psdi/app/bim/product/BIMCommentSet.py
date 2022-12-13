QUERY_CHILDREN = "String  \"parentid=:1\""
QUERY_PARENT = "String  \"bimcommentid=:1\""
QUERY_SIBLINGS = "String  \" bimcommentid != :1 and parentid in (select parentid from bimcomment where bimcommentid = :1)\""
QUERY_TOP = "String  \"parentid is null and OWNERTABLE = :1 and OWNERID = :2\""
def BIMCommentSet():
    '''    public BIMCommentSet(final MboServerInterface ms)
    '''
def addAtIndex():
    '''    public MboRemote addAtIndex(final long accessModifier, final int ind)
    '''
def getChildren():
    '''    public MboValueData[][] getChildren(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getParent():
    '''    public MboValueData[] getParent(final String object, final String key, final String[] attrs)
    '''
def getSiblings():
    '''    public MboValueData[][] getSiblings(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getTop():
    '''    public MboValueData[][] getTop(final String[] attrs, final int maxRows)
    '''
def getPathToTop():
    '''    public MboValueData[][] getPathToTop(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getLastInsert():
    '''    public MboRemote getLastInsert()
    '''
def getParentForAdd():
    '''    public MboRemote getParentForAdd()
    '''
def setParentForAdd():
    '''    public void setParentForAdd(final MboRemote parent)
    '''
