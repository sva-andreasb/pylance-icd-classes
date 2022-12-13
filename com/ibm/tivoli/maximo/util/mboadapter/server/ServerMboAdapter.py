def ServerMboAdapter():
    '''public ServerMboAdapter(final Mbo mbo)
    '''
def getMbo():
    '''public Mbo getMbo()
    '''
def getMboSet():
    '''public MboSetAdapter getMboSet(final String relationshipName)
    '''
def getThisMboSet():
    '''public MboSetAdapter getThisMboSet()
    '''
def setValue():
    '''public void setValue(final String attributeName, final String value)
    public void setValue(final String attributeName, final String value, final long flags)
    public void setValue(final String attributeName, final boolean value)
    public void setValue(final String attributeName, final boolean value, final long flags)
    public void setValue(final String attributeName, final int value)
    public void setValue(final String attributeName, final int value, final long flags)
    public void setValue(final String attributeName, final Date value)
    public void setValue(final String attributeName, final Date value, final long flags)
    '''
def setValueIfDifferent():
    '''public void setValueIfDifferent(final String attributeName, final boolean value)
    public void setValueIfDifferent(final String attributeName, final boolean value, final long flags)
    '''
def getString():
    '''public String getString(final String attributeName)
    '''
def getBoolean():
    '''public boolean getBoolean(final String attributeName)
    '''
def getInt():
    '''public int getInt(final String attributeName)
    '''
def getDate():
    '''public Date getDate(final String attributeName)
    '''
def isNull():
    '''public boolean isNull(final String attributeName)
    '''
def isReadOnly():
    '''public boolean isReadOnly(final String attributeName)
    '''
def setReadOnly():
    '''public void setReadOnly(final String attributeName, final boolean readOnly)
    '''
def getName():
    '''public String getName()
    '''
def getOwner():
    '''public MboAdapter getOwner()
    '''
def newApplicationException():
    '''public Exception newApplicationException(final String group, final String key, final Object[] params)
    public Exception newApplicationException(final String group, final String key)
    '''
def getMaxVarString():
    '''public String getMaxVarString(final String maxvarName)
    '''
def getMaxVarInt():
    '''public int getMaxVarInt(final String maxvarName)
    '''
def getMaxVarBoolean():
    '''public boolean getMaxVarBoolean(final String maxvarName)
    '''
def toBeDeleted():
    '''public boolean toBeDeleted()
    '''
def wrapException():
    '''public static void wrapException(final Exception e)
    '''
