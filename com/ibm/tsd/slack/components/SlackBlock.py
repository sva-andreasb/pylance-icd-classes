TYPE_INPUT = "String  \"input\""
TYPE_SECTION = "String  \"section\""
TYPE_DIVIDER = "String  \"divider\""
TYPE_CONTEXT = "String  \"context\""
TYPE_ACTIONS = "String  \"actions\""
def ():
    '''returns SlackBlock\n\n
    (final String type)\n
    '''
def setBlockId():
    '''returns None\n\n
    setBlockId(final String blockId)\n
    '''
def setText():
    '''returns None\n\n
    setText(final String text)\n
    '''
def setElement():
    '''returns None\n\n
    setElement(final SlackElement element)\n
    '''
def setFields():
    '''returns None\n\n
    setFields(final JSONArray fields)\n
    '''
def setAccessory():
    '''returns None\n\n
    setAccessory(final SlackElement accessory)\n
    '''
def setLabel():
    '''returns None\n\n
    setLabel(final String label)\n
    '''
def setHint():
    '''returns None\n\n
    setHint(final String text)\n
    '''
def setOptional():
    '''returns None\n\n
    setOptional(final boolean optional)\n
    '''
def getBlockId():
    '''returns String\n\n
    getBlockId()\n
    '''
def getText():
    '''returns String\n\n
    getText()\n
    '''
def getElement():
    '''returns SlackElement\n\n
    getElement()\n
    '''
def getFields():
    '''returns JSONArray\n\n
    getFields()\n
    '''
def getAccessory():
    '''returns SlackElement\n\n
    getAccessory()\n
    '''
def getLabel():
    '''returns String\n\n
    getLabel()\n
    '''
def getHint():
    '''returns String\n\n
    getHint()\n
    '''
def getOptional():
    '''returns boolean\n\n
    getOptional()\n
    '''
