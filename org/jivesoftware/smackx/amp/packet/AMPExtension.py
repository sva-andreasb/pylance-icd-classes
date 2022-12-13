NAMESPACE = "String  \"http://jabber.org/protocol/amp\""
ELEMENT = "String  \"rule\""
ATTRIBUTE_NAME = "String  \"condition\""
def AMPExtension():
    '''public AMPExtension(final String from, final String to, final Status status)
    public AMPExtension()
    '''
def getFrom():
    '''public String getFrom()
    '''
def getTo():
    '''public String getTo()
    '''
def getStatus():
    '''public Status getStatus()
    '''
def getRules():
    '''public List<Rule> getRules()
    '''
def addRule():
    '''public void addRule(final Rule rule)
    '''
def getRulesCount():
    '''public int getRulesCount()
    '''
def setPerHop():
    '''public synchronized void setPerHop(final boolean enabled)
    '''
def isPerHop():
    '''public synchronized boolean isPerHop()
    '''
def getElementName():
    '''public String getElementName()
    '''
def getNamespace():
    '''public String getNamespace()
    '''
def toXML():
    '''public String toXML(final String enclosingNamespace)
    '''
def getAction():
    '''public Action getAction()
    '''
def getCondition():
    '''public Condition getCondition()
    '''
def Rule():
    '''public Rule(final Action action, final Condition condition)
    '''
