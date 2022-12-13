QUERY_CHILDREN = "String  parentid=:1""
QUERY_PARENT = "String  bimcommentid=:1""
QUERY_SIBLINGS = "String   bimcommentid != :1 and parentid in (select parentid from bimcomment where bimcommentid = :1)""
QUERY_TOP = "String  parentid is null and OWNERTABLE = :1 and OWNERID = :2""
def BIMCommentSet():
'''public BIMCommentSet(final MboServerInterface ms)
'''
pass
def addAtIndex():
'''public MboRemote addAtIndex(final long accessModifier, final int ind)
'''
pass
def getChildren():
'''public MboValueData[][] getChildren(final String object, final String key, final String[] attrs, final int maxRows)
'''
pass
def getParent():
'''public MboValueData[] getParent(final String object, final String key, final String[] attrs)
'''
pass
def getSiblings():
'''public MboValueData[][] getSiblings(final String object, final String key, final String[] attrs, final int maxRows)
'''
pass
def getTop():
'''public MboValueData[][] getTop(final String[] attrs, final int maxRows)
'''
pass
def getPathToTop():
'''public MboValueData[][] getPathToTop(final String object, final String key, final String[] attrs, final int maxRows)
'''
pass
def getLastInsert():
'''public MboRemote getLastInsert()
'''
pass
def getParentForAdd():
'''public MboRemote getParentForAdd()
'''
pass
def setParentForAdd():
'''public void setParentForAdd(final MboRemote parent)
'''
pass
