QUERY_CHILDREN = "String  \"parentid=:1\""
QUERY_PARENT = "String  \"bimcommentid=:1\""
QUERY_SIBLINGS = "String  \" bimcommentid != :1 and parentid in (select parentid from bimcomment where bimcommentid = :1)\""
QUERY_TOP = "String  \"parentid is null and OWNERTABLE = :1 and OWNERID = :2\""
def ():
    '''returns BIMCommentSet\n\n
    (final MboServerInterface ms)\n
    '''
def addAtIndex():
    '''returns MboRemote\n\n
    addAtIndex(final long accessModifier, final int ind)\n
    '''
def getChildren():
    '''returns MboValueData[][]\n\n
    getChildren(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def getParent():
    '''returns MboValueData[]\n\n
    getParent(final String object, final String key, final String[] attrs)\n
    '''
def getSiblings():
    '''returns MboValueData[][]\n\n
    getSiblings(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def getTop():
    '''returns MboValueData[][]\n\n
    getTop(final String[] attrs, final int maxRows)\n
    '''
def getPathToTop():
    '''returns MboValueData[][]\n\n
    getPathToTop(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def getLastInsert():
    '''returns MboRemote\n\n
    getLastInsert()\n
    '''
def getParentForAdd():
    '''returns MboRemote\n\n
    getParentForAdd()\n
    '''
def setParentForAdd():
    '''returns None\n\n
    setParentForAdd(final MboRemote parent)\n
    '''
