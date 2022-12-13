def getInstance():
    '''public static synchronized ControlsCache getInstance()
    '''
def getName():
    '''public String getName()
    '''
def getAllControls():
    '''public Map<String, MaxIfaceControlInfo> getAllControls(final String extSystem)
    '''
def getIfaceControlInfo():
    '''public MaxIfaceControlInfo getIfaceControlInfo(final String extSystem, final String name)
    '''
def getControlType():
    '''public String getControlType(final String extSystem, final String name)
    '''
def getInternalControlType():
    '''public String getInternalControlType(final String extSystem, final String name)
    '''
def isControlEqual():
    '''public boolean isControlEqual(final String extsys, final String name, final String value)
    public boolean isControlEqual(final String extsys, final String name, final String orgid, final String siteid, final String value)
    '''
def getValueControl():
    '''public String getValueControl(final String extsys, final String name)
    public String getValueControl(final String extsys, final String name, final String orgid, final String siteid)
    '''
def getValueOrBooleanControl():
    '''public String getValueOrBooleanControl(final String extsys, final String name, final String orgid, final String siteid)
    '''
def isValueControlNull():
    '''public boolean isValueControlNull(final String extsys, final String name)
    public boolean isValueControlNull(final String extsys, final String name, final String orgid, final String siteid)
    '''
def isControlExists():
    '''public boolean isControlExists(final String extsys, final String controlName)
    '''
def getXREFControl():
    '''public List getXREFControl(final String extsys, final String name, final String currentValue, final boolean fromMaximo)
    public List<String> getXREFControl(final String extsys, final String name, final String orgid, final String siteid, final String currentValue, final boolean fromMaximo)
    '''
def getXREFControlValue():
    '''public String getXREFControlValue(final String extsys, final String name, final String orgid, final String siteid, final String currentValue, final boolean fromMaximo)
    '''
def getXREFControlValues():
    '''public List getXREFControlValues(final String extsys, final String name)
    '''
def doesXREFExist():
    '''public boolean doesXREFExist(final String extsys, final String name, final String orgid, final String siteid, final String currentValue, final boolean fromMaximo)
    '''
def getListControl():
    '''public List<String> getListControl(final String extsys, final String name)
    public ArrayList<String> getListControl(final String extsys, final String name, final String orgid, final String siteid)
    '''
def isControlTrue():
    '''public boolean isControlTrue(final String extsys, final String name)
    public boolean isControlTrue(final String extsys, final String name, final String orgid, final String siteid)
    '''
def setXREFValues():
    '''public void setXREFValues(final Map<String, Object> inMap, final String key, final String val1, final String val2)
    '''
