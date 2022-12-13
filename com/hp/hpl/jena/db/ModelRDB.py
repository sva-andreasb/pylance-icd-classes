def ModelRDB():
'''public ModelRDB(final Personality<RDFNode> p, final GraphRDB graph)
public ModelRDB(final GraphRDB graph)
'''
pass
def open():
'''public static ModelRDB open(final IDBConnection dbcon)
public static ModelRDB open(final IDBConnection dbcon, final String name)
'''
pass
def createModel():
'''public static ModelRDB createModel(final IDBConnection dbcon)
public static ModelRDB createModel(final IDBConnection dbcon, final Model modelProperties)
public static ModelRDB createModel(final IDBConnection dbcon, final String name)
public static ModelRDB createModel(final IDBConnection dbcon, final String name, final Model modelProperties)
'''
pass
def getModelProperties():
'''public Model getModelProperties()
'''
pass
def getDefaultModelProperties():
'''public static Model getDefaultModelProperties(final IDBConnection dbcon)
'''
pass
def listModels():
'''public static ExtendedIterator<String> listModels(final IDBConnection dbcon)
'''
pass
def close():
'''public void close()
'''
pass
def remove():
'''public void remove()
'''
pass
def getConnection():
'''public IDBConnection getConnection()
'''
pass
def getDoDuplicateCheck():
'''public boolean getDoDuplicateCheck()
'''
pass
def setDoDuplicateCheck():
'''public void setDoDuplicateCheck(final boolean bool)
'''
pass
def setDoFastpath():
'''public void setDoFastpath(final boolean val)
'''
pass
def getDoFastpath():
'''public boolean getDoFastpath()
'''
pass
def setQueryOnlyAsserted():
'''public void setQueryOnlyAsserted(final boolean opt)
'''
pass
def getQueryOnlyAsserted():
'''public boolean getQueryOnlyAsserted()
'''
pass
def setQueryOnlyReified():
'''public void setQueryOnlyReified(final boolean opt)
'''
pass
def getQueryOnlyReified():
'''public boolean getQueryOnlyReified()
'''
pass
def setQueryFullReified():
'''public void setQueryFullReified(final boolean opt)
'''
pass
def getQueryFullReified():
'''public boolean getQueryFullReified()
'''
pass
def setDoImplicitJoin():
'''public void setDoImplicitJoin(final boolean val)
'''
pass
