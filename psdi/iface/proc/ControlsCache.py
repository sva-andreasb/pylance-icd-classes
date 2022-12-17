def getName():
    '''returns String\n\n
    getName()\n
    '''
def getIfaceControlInfo():
    '''returns MaxIfaceControlInfo\n\n
    getIfaceControlInfo(final String extSystem, final String name)\n
    '''
def getControlType():
    '''returns String\n\n
    getControlType(final String extSystem, final String name)\n
    '''
def getInternalControlType():
    '''returns String\n\n
    getInternalControlType(final String extSystem, final String name)\n
    '''
def isControlEqual():
    '''returns boolean\n\n
    isControlEqual(final String extsys, final String name, final String value)\n
    isControlEqual(final String extsys, final String name, final String orgid, final String siteid, final String value)\n
    '''
def getValueControl():
    '''returns String\n\n
    getValueControl(final String extsys, final String name)\n
    getValueControl(final String extsys, final String name, final String orgid, final String siteid)\n
    '''
def getValueOrBooleanControl():
    '''returns String\n\n
    getValueOrBooleanControl(final String extsys, final String name, final String orgid, final String siteid)\n
    '''
def isValueControlNull():
    '''returns boolean\n\n
    isValueControlNull(final String extsys, final String name)\n
    isValueControlNull(final String extsys, final String name, final String orgid, final String siteid)\n
    '''
def isControlExists():
    '''returns boolean\n\n
    isControlExists(final String extsys, final String controlName)\n
    '''
def getXREFControl():
    '''returns List<String>\n\n
    getXREFControl(final String extsys, final String name, final String currentValue, final boolean fromMaximo)\n
    getXREFControl(final String extsys, final String name, final String orgid, final String siteid, final String currentValue, final boolean fromMaximo)\n
    '''
def getXREFControlValue():
    '''returns String\n\n
    getXREFControlValue(final String extsys, final String name, final String orgid, final String siteid, final String currentValue, final boolean fromMaximo)\n
    '''
def getXREFControlValues():
    '''returns List\n\n
    getXREFControlValues(final String extsys, final String name)\n
    '''
def doesXREFExist():
    '''returns boolean\n\n
    doesXREFExist(final String extsys, final String name, final String orgid, final String siteid, final String currentValue, final boolean fromMaximo)\n
    '''
def getListControl():
    '''returns ArrayList<String>\n\n
    getListControl(final String extsys, final String name)\n
    getListControl(final String extsys, final String name, final String orgid, final String siteid)\n
    '''
def isControlTrue():
    '''returns boolean\n\n
    isControlTrue(final String extsys, final String name)\n
    isControlTrue(final String extsys, final String name, final String orgid, final String siteid)\n
    '''
def setXREFValues():
    '''returns None\n\n
    setXREFValues(final Map<String, Object> inMap, final String key, final String val1, final String val2)\n
    '''
