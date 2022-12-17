NAMESPACE = "String  \"http://jabber.org/protocol/amp\""
ELEMENT = "String  \"rule\""
ATTRIBUTE_NAME = "String  \"condition\""
def ():
    '''returns Rule\n\n
    (final String from, final String to, final Status status)\n
    ()\n
    (final Action action, final Condition condition)\n
    '''
def getFrom():
    '''returns String\n\n
    getFrom()\n
    '''
def getTo():
    '''returns String\n\n
    getTo()\n
    '''
def getStatus():
    '''returns Status\n\n
    getStatus()\n
    '''
def getRules():
    '''returns List<Rule>\n\n
    getRules()\n
    '''
def addRule():
    '''returns None\n\n
    addRule(final Rule rule)\n
    '''
def getRulesCount():
    '''returns int\n\n
    getRulesCount()\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def toXML():
    '''returns String\n\n
    toXML(final String enclosingNamespace)\n
    '''
def getAction():
    '''returns Action\n\n
    getAction()\n
    '''
def getCondition():
    '''returns Condition\n\n
    getCondition()\n
    '''
