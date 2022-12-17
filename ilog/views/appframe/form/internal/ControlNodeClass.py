CONTROL_NODE_CLASS_DEVICE_PROPERTY = "String  \"JAppFrame:ControlNodeClassDevice\""
def ():
    '''returns ControlNodeClass\n\n
    ()\n
    '''
def createControlNode():
    '''returns AbstractControlNode\n\n
    createControlNode(final IlvForm ilvForm, final String className, Class clazz)\n
    '''
def registerControlType():
    '''returns None\n\n
    registerControlType(final String s, final Class clazz)\n
    registerControlType(final String s, final Class clazz, final ControlNodeFactory controlNodeFactory)\n
    '''
def findClosestControlType():
    '''returns String\n\n
    findClosestControlType(Class superclass)\n
    '''
