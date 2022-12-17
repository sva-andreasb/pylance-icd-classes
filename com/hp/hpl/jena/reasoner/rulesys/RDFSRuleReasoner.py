DEFAULT_RULES = "String  \"default\""
FULL_RULES = "String  \"full\""
SIMPLE_RULES = "String  \"simple\""
def ():
    '''returns RDFSRuleReasoner\n\n
    (final ReasonerFactory parent)\n
    (final ReasonerFactory factory, final Resource configuration)\n
    '''
def bind():
    '''returns InfGraph\n\n
    bind(final Graph data)\n
    '''
def bindSchema():
    '''returns Reasoner\n\n
    bindSchema(final Graph tbox)\n
    '''
def getGraphCapabilities():
    '''returns Capabilities\n\n
    getGraphCapabilities()\n
    '''
