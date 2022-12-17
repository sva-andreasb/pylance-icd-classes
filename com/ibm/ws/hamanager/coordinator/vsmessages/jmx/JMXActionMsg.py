CMD_ENABLE_MEMBER = "int  1"
CMD_DISABLE_MEMBER = "int  2"
CMD_ACTIVATE_MEMBER = "int  3"
CMD_DEACTIVATE_MEMBER = "int  4"
CMD_ENABLE_GROUP = "int  10"
CMD_DISABLE_GROUP = "int  20"
def ():
    '''returns JMXActionMsg\n\n
    (final int command, final GroupName groupName, final String cellName, final String nodeName, final String serverName)\n
    (final int command, final GroupName groupName)\n
    '''
def getDescription():
    '''returns String\n\n
    getDescription()\n
    '''
def getCommand():
    '''returns int\n\n
    getCommand()\n
    '''
def getCommandAsString():
    '''returns String\n\n
    getCommandAsString()\n
    '''
def getGroupName():
    '''returns GroupName\n\n
    getGroupName()\n
    '''
def getServerName():
    '''returns String\n\n
    getServerName()\n
    '''
def isGroupAction():
    '''returns boolean\n\n
    isGroupAction()\n
    '''
