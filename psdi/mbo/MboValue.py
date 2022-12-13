def MboValue():
'''public MboValue()
'''
pass
def construct():
'''public void construct(final Mbo mbo, final MboValueInfo mvInfo)
'''
pass
def init():
'''public void init()
'''
pass
def initValue():
'''public void initValue()
'''
pass
def getMboValueData():
'''public MboValueData getMboValueData()
public MboValueData getMboValueData(final boolean ignoreFieldFlags)
'''
pass
def getMbo():
'''public Mbo getMbo()
'''
pass
def getDefault():
'''public String getDefault()
'''
pass
def hasLongDescription():
'''public boolean hasLongDescription()
'''
pass
def setDefault():
'''public void setDefault(final String val)
'''
pass
def setValueNull():
'''public void setValueNull(final long accessModifier)
public void setValueNull()
'''
pass
def _setValueNull():
'''public void _setValueNull()
'''
pass
def isNull():
'''public boolean isNull()
'''
pass
def getCurrentValue():
'''public MaxType getCurrentValue()
'''
pass
def getInitialValue():
'''public MaxType getInitialValue()
'''
pass
def getPreviousValue():
'''public MaxType getPreviousValue()
'''
pass
def getString():
'''public final String getString()
'''
pass
def getBoolean():
'''public final boolean getBoolean()
'''
pass
def getByte():
'''public final byte getByte()
'''
pass
def getInt():
'''public final int getInt()
'''
pass
def getLong():
'''public final long getLong()
'''
pass
def getFloat():
'''public final float getFloat()
'''
pass
def getDouble():
'''public final double getDouble()
'''
pass
def getBytes():
'''public final byte[] getBytes()
'''
pass
def getMaxType():
'''public final MaxType getMaxType()
'''
pass
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
pass
def setCurrentFieldAccess():
'''public void setCurrentFieldAccess(final long access)
'''
pass
def resetCurrentFieldAccess():
'''public void resetCurrentFieldAccess()
'''
pass
def getCurrentFieldAccess():
'''public long getCurrentFieldAccess()
'''
pass
def validate():
'''public final void validate(final long access)
public final void validate()
'''
pass
def isModified():
'''public boolean isModified()
'''
pass
def isReadOnly():
'''public boolean isReadOnly()
'''
pass
def setReadOnly():
'''public void setReadOnly(final boolean ro)
'''
pass
def isHidden():
'''public boolean isHidden()
'''
pass
def setHidden():
'''public void setHidden(final boolean val)
'''
pass
def getName():
'''public String getName()
'''
pass
def getAttributeName():
'''public String getAttributeName()
'''
pass
def getMboValueInfo():
'''public MboValueInfo getMboValueInfo()
'''
pass
def getLength():
'''public int getLength()
'''
pass
def getScale():
'''public int getScale()
'''
pass
def getColumnTitle():
'''public String getColumnTitle()
'''
pass
def hasList():
'''public boolean hasList()
'''
pass
def getList():
'''public MboSetRemote getList()
'''
pass
def smartFill():
'''public MboSetRemote smartFill(final String value, final boolean exact)
'''
pass
def smartFind():
'''public MboSetRemote smartFind(final String value, final boolean exact)
public MboSetRemote smartFind(final String object, final String value, final boolean exact)
'''
pass
def getMatchingAttr():
'''public String getMatchingAttr()
public String getMatchingAttr(final String sourceObjectName)
'''
pass
def isRequired():
'''public boolean isRequired()
'''
pass
def setRequired():
'''public void setRequired(final boolean state)
'''
pass
def isPersistent():
'''public boolean isPersistent()
'''
pass
def isExtended():
'''public boolean isExtended()
'''
pass
def isGuaranteedUnique():
'''public boolean isGuaranteedUnique()
'''
pass
def setGuaranteedUnique():
'''public void setGuaranteedUnique(final boolean flag)
'''
pass
def autoKey():
'''public void autoKey()
'''
pass
def autoKeyByMboSiteOrg():
'''public void autoKeyByMboSiteOrg()
'''
pass
def addMboValueListener():
'''public void addMboValueListener(final MboValueListener l)
'''
pass
def getListeners():
'''public Vector<MboValueListener> getListeners()
'''
pass
def removeMboValueListener():
'''public void removeMboValueListener(final MboValueListener l)
'''
pass
def checkFieldAccess():
'''public void checkFieldAccess(final long accessModifier)
'''
pass
def hasFieldAccess():
'''public boolean hasFieldAccess(final long accessModifier)
'''
pass
def setFlags():
'''public void setFlags(final long flags)
public void setFlags(final long flags, final MXException mxe)
'''
pass
def getFlags():
'''public long getFlags()
'''
pass
def setFlag():
'''public void setFlag(final long flag, final boolean state)
public void setFlag(final long flag, final boolean state, final MXException mxe)
'''
pass
def isFlagSet():
'''public boolean isFlagSet(final long flag)
'''
pass
def getFieldFlagFromMbo():
'''public void getFieldFlagFromMbo(final long flag)
'''
pass
def getMXException():
'''public MXException getMXException()
'''
pass
def generateUniqueID():
'''public synchronized void generateUniqueID()
'''
pass
def isToBeValidated():
'''public boolean isToBeValidated()
'''
pass
def setToBeValidated():
'''public void setToBeValidated(final boolean value)
'''
pass
def getIntegrationService():
'''public ServiceRemote getIntegrationService()
'''
pass
def rollbackToCheckpoint():
'''public void rollbackToCheckpoint()
'''
pass
def takeCheckpoint():
'''public void takeCheckpoint()
'''
pass
def setValueFromLookup():
'''public void setValueFromLookup(final MboRemote sourceMbo)
'''
pass
def getAppLink():
'''public String[] getAppLink()
'''
pass
def getLookupName():
'''public String getLookupName()
'''
pass
def setBypassOperatorCheck():
'''public void setBypassOperatorCheck(final boolean val)
'''
pass
def setApplicationError():
'''public void setApplicationError(final ApplicationError appError)
'''
pass
def getApplicationError():
'''public ApplicationError getApplicationError()
'''
pass
def setCurProcessValue():
'''public void setCurProcessValue(final String value)
'''
pass
def getCurProcessValue():
'''public String getCurProcessValue()
'''
pass
def setApplicationRequired():
'''public void setApplicationRequired(final boolean appRequired)
'''
pass
def isApplicationRequired():
'''public boolean isApplicationRequired()
'''
pass
def isRecordHover():
'''public boolean isRecordHover()
'''
pass
def setRecordHover():
'''public void setRecordHover(final boolean isRecordHover)
'''
pass
def toString():
'''public String toString()
'''
pass
