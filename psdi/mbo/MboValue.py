def MboValue():
    '''public MboValue()
    '''
def construct():
    '''public void construct(final Mbo mbo, final MboValueInfo mvInfo)
    '''
def init():
    '''public void init()
    '''
def initValue():
    '''public void initValue()
    '''
def getMboValueData():
    '''public MboValueData getMboValueData()
    public MboValueData getMboValueData(final boolean ignoreFieldFlags)
    '''
def getMbo():
    '''public Mbo getMbo()
    '''
def getDefault():
    '''public String getDefault()
    '''
def hasLongDescription():
    '''public boolean hasLongDescription()
    '''
def setDefault():
    '''public void setDefault(final String val)
    '''
def setValueNull():
    '''public void setValueNull(final long accessModifier)
    public void setValueNull()
    '''
def _setValueNull():
    '''public void _setValueNull()
    '''
def isNull():
    '''public boolean isNull()
    '''
def getCurrentValue():
    '''public MaxType getCurrentValue()
    '''
def getInitialValue():
    '''public MaxType getInitialValue()
    '''
def getPreviousValue():
    '''public MaxType getPreviousValue()
    '''
def getString():
    '''public final String getString()
    '''
def getBoolean():
    '''public final boolean getBoolean()
    '''
def getByte():
    '''public final byte getByte()
    '''
def getInt():
    '''public final int getInt()
    '''
def getLong():
    '''public final long getLong()
    '''
def getFloat():
    '''public final float getFloat()
    '''
def getDouble():
    '''public final double getDouble()
    '''
def getBytes():
    '''public final byte[] getBytes()
    '''
def getMaxType():
    '''public final MaxType getMaxType()
    '''
def setValue():
    '''public final void setValue(final int value)
    public final void setValue(final int val, final long accessModifier)
    public final void setValue(final String value)
    public final void setValue(final String val, final long accessModifier)
    public final void setValue(final boolean value)
    public final void setValue(final boolean val, final long accessModifier)
    public final void setValue(final byte value)
    public final void setValue(final byte val, final long accessModifier)
    public final void setValue(final long value)
    public final void setValue(final long val, final long accessModifier)
    public final void setValue(final float value)
    public final void setValue(final float val, final long accessModifier)
    public final void setValue(final double value)
    public final void setValue(final double val, final long accessModifier)
    public final void setValue(final byte[] value)
    public final void setValue(final byte[] val, final long accessModifier)
    public final void setValue(final java.util.Date value)
    public final void setValue(final java.util.Date val, final long accessModifier)
    '''
def setCurrentFieldAccess():
    '''public void setCurrentFieldAccess(final long access)
    '''
def resetCurrentFieldAccess():
    '''public void resetCurrentFieldAccess()
    '''
def getCurrentFieldAccess():
    '''public long getCurrentFieldAccess()
    '''
def validate():
    '''public final void validate(final long access)
    public final void validate()
    '''
def isModified():
    '''public boolean isModified()
    '''
def isReadOnly():
    '''public boolean isReadOnly()
    '''
def setReadOnly():
    '''public void setReadOnly(final boolean ro)
    '''
def isHidden():
    '''public boolean isHidden()
    '''
def setHidden():
    '''public void setHidden(final boolean val)
    '''
def getName():
    '''public String getName()
    '''
def getAttributeName():
    '''public String getAttributeName()
    '''
def getMboValueInfo():
    '''public MboValueInfo getMboValueInfo()
    '''
def getLength():
    '''public int getLength()
    '''
def getScale():
    '''public int getScale()
    '''
def getColumnTitle():
    '''public String getColumnTitle()
    '''
def hasList():
    '''public boolean hasList()
    '''
def getList():
    '''public MboSetRemote getList()
    '''
def smartFill():
    '''public MboSetRemote smartFill(final String value, final boolean exact)
    '''
def smartFind():
    '''public MboSetRemote smartFind(final String value, final boolean exact)
    public MboSetRemote smartFind(final String object, final String value, final boolean exact)
    '''
def getMatchingAttr():
    '''public String getMatchingAttr()
    public String getMatchingAttr(final String sourceObjectName)
    '''
def isRequired():
    '''public boolean isRequired()
    '''
def setRequired():
    '''public void setRequired(final boolean state)
    '''
def isPersistent():
    '''public boolean isPersistent()
    '''
def isExtended():
    '''public boolean isExtended()
    '''
def isGuaranteedUnique():
    '''public boolean isGuaranteedUnique()
    '''
def setGuaranteedUnique():
    '''public void setGuaranteedUnique(final boolean flag)
    '''
def autoKey():
    '''public void autoKey()
    '''
def autoKeyByMboSiteOrg():
    '''public void autoKeyByMboSiteOrg()
    '''
def addMboValueListener():
    '''public void addMboValueListener(final MboValueListener l)
    '''
def getListeners():
    '''public Vector<MboValueListener> getListeners()
    '''
def removeMboValueListener():
    '''public void removeMboValueListener(final MboValueListener l)
    '''
def checkFieldAccess():
    '''public void checkFieldAccess(final long accessModifier)
    '''
def hasFieldAccess():
    '''public boolean hasFieldAccess(final long accessModifier)
    '''
def setFlags():
    '''public void setFlags(final long flags)
    public void setFlags(final long flags, final MXException mxe)
    '''
def getFlags():
    '''public long getFlags()
    '''
def setFlag():
    '''public void setFlag(final long flag, final boolean state)
    public void setFlag(final long flag, final boolean state, final MXException mxe)
    '''
def isFlagSet():
    '''public boolean isFlagSet(final long flag)
    '''
def getFieldFlagFromMbo():
    '''public void getFieldFlagFromMbo(final long flag)
    '''
def getMXException():
    '''public MXException getMXException()
    '''
def generateUniqueID():
    '''public synchronized void generateUniqueID()
    '''
def isToBeValidated():
    '''public boolean isToBeValidated()
    '''
def setToBeValidated():
    '''public void setToBeValidated(final boolean value)
    '''
def getIntegrationService():
    '''public ServiceRemote getIntegrationService()
    '''
def rollbackToCheckpoint():
    '''public void rollbackToCheckpoint()
    '''
def takeCheckpoint():
    '''public void takeCheckpoint()
    '''
def setValueFromLookup():
    '''public void setValueFromLookup(final MboRemote sourceMbo)
    '''
def getAppLink():
    '''public String[] getAppLink()
    '''
def getLookupName():
    '''public String getLookupName()
    '''
def setBypassOperatorCheck():
    '''public void setBypassOperatorCheck(final boolean val)
    '''
def setApplicationError():
    '''public void setApplicationError(final ApplicationError appError)
    '''
def getApplicationError():
    '''public ApplicationError getApplicationError()
    '''
def setCurProcessValue():
    '''public void setCurProcessValue(final String value)
    '''
def getCurProcessValue():
    '''public String getCurProcessValue()
    '''
def setApplicationRequired():
    '''public void setApplicationRequired(final boolean appRequired)
    '''
def isApplicationRequired():
    '''public boolean isApplicationRequired()
    '''
def isRecordHover():
    '''public boolean isRecordHover()
    '''
def setRecordHover():
    '''public void setRecordHover(final boolean isRecordHover)
    '''
def toString():
    '''public String toString()
    '''
