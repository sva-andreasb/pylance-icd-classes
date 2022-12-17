def ():
    '''returns GenericRuleReasoner\n\n
    (final List<Rule> rules)\n
    (final ReasonerFactory factory, final Resource configuration)\n
    (final List<Rule> rules, final ReasonerFactory factory)\n
    '''
def setMode():
    '''returns None\n\n
    setMode(final RuleMode mode)\n
    '''
def setRules():
    '''returns None\n\n
    setRules(final List<Rule> rules)\n
    '''
def setOWLTranslation():
    '''returns None\n\n
    setOWLTranslation(final boolean enableOWLTranslation)\n
    '''
def setTransitiveClosureCaching():
    '''returns None\n\n
    setTransitiveClosureCaching(final boolean enableTGCCaching)\n
    '''
def setFunctorFiltering():
    '''returns None\n\n
    setFunctorFiltering(final boolean param)\n
    '''
def addPreprocessingHook():
    '''returns None\n\n
    addPreprocessingHook(final RulePreprocessHook hook)\n
    '''
def removePreprocessingHook():
    '''returns None\n\n
    removePreprocessingHook(final RulePreprocessHook hook)\n
    '''
def bindSchema():
    '''returns Reasoner\n\n
    bindSchema(final Graph tbox)\n
    '''
def bind():
    '''returns InfGraph\n\n
    bind(final Graph data)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
