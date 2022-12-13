NAME = "String  IFACECONTROL""
def ControlsCacheImpl():
'''public ControlsCacheImpl()
'''
pass
def init():
'''public void init()
'''
pass
def reload():
'''public void reload()
public void reload(final String key)
'''
pass
def getName():
'''public String getName()
'''
pass
def getAllControls():
'''public Map<String, MaxIfaceControlInfo> getAllControls(final String extSystem)
'''
pass
def getIfaceControlInfo():
'''public MaxIfaceControlInfo getIfaceControlInfo(final String extSystem, final String name)
'''
pass
def getControlType():
'''public String getControlType(final String extSystem, final String name)
'''
pass
def getInternalControlType():
'''public String getInternalControlType(final String extSystem, final String name)
'''
pass
def isControlEqual():
'''public boolean isControlEqual(final String extsys, final String name, final String value)
public boolean isControlEqual(final String extsys, final String name, final String orgid, final String siteid, final String value)
'''
pass
def getValueControl():
'''public String getValueControl(final String extsys, final String name)
public String getValueControl(final String extsys, final String name, final String orgid, final String siteid)
'''
pass
def getValueOrBooleanControl():
'''public String getValueOrBooleanControl(final String extsys, final String name, final String orgid, final String siteid)
'''
pass
def isValueControlNull():
'''public boolean isValueControlNull(final String extsys, final String name)
public boolean isValueControlNull(final String extsys, final String name, final String orgid, final String siteid)
'''
pass
def isControlExists():
'''public boolean isControlExists(final String extsys, final String controlName)
'''
pass
def getXREFControl():
'''public List getXREFControl(final String extsys, final String name, final String currentValue, final boolean fromMaximo)
public List<String> getXREFControl(final String extsys, final String name, final String orgid, final String siteid, String currentValue, final boolean fromMaximo)
'''
pass
def getXREFControlValue():
'''public String getXREFControlValue(final String extsys, final String name, final String orgid, final String siteid, final String currentValue, final boolean fromMaximo)
'''
pass
def getXREFControlValues():
'''public List getXREFControlValues(final String extsys, final String name)
'''
pass
def doesXREFExist():
'''public boolean doesXREFExist(final String extsys, final String name, final String orgid, final String siteid, String currentValue, final boolean fromMaximo)
'''
pass
def getListControl():
'''public List<String> getListControl(final String extsys, final String name)
public ArrayList<String> getListControl(final String extsys, final String name, final String orgid, final String siteid)
'''
pass
def isControlTrue():
'''public boolean isControlTrue(final String extsys, final String name)
public boolean isControlTrue(final String extsys, final String name, final String orgid, final String siteid)
'''
pass
def setXREFValues():
'''public void setXREFValues(final Map<String, Object> inMap, final String key, final String val1, final String val2)
'''
pass
