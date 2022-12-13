def WSIOTreeSet():
'''public WSIOTreeSet(final MboServerInterface ms)
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
def fill():
'''public void fill(final WSIO wsio, final boolean top, final LinkedHashMap<String, String> removeMap)
public void fill(final MboRemote parentMbo, final boolean top)
'''
pass
def setup():
'''public MboRemote setup()
'''
pass
def getUniqueIDValue():
'''public MboValueData getUniqueIDValue(final String object, final String[] attributes, final String[] values)
'''
pass
def setHierarchy():
'''public void setHierarchy(final String object, final String key, final String hierarchy)
'''
pass
def getAllHierarchies():
'''public MboValueData[][] getAllHierarchies(final String object, final String key, final String[] attrs, final int maxRows)
'''
pass
def getHierarchy():
'''public MboValueData[] getHierarchy(final String object, final String key)
'''
pass
def findMbo():
'''public MboRemote findMbo(final MboRemote mbo, final String key)
'''
pass
