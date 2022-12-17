def ():
    '''returns LPInterpreter\n\n
    (final LPBRuleEngine engine, final TriplePattern goal)\n
    (final LPBRuleEngine engine, final TriplePattern goal, final boolean isTop)\n
    (final LPBRuleEngine engine, final TriplePattern goal, final List<RuleClauseCode> clauses, final boolean isTop)\n
    '''
def setTopInterpreter():
    '''returns None\n\n
    setTopInterpreter(final LPInterpreterContext context)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def setState():
    '''returns None\n\n
    setState(final LPInterpreterState state)\n
    '''
def next():
    '''returns Object\n\n
    next()\n
    '''
def getEngine():
    '''returns LPBRuleEngine\n\n
    getEngine()\n
    '''
def getChoiceFrame():
    '''returns FrameObject\n\n
    getChoiceFrame()\n
    '''
def getContext():
    '''returns LPInterpreterContext\n\n
    getContext()\n
    '''
def preserveState():
    '''returns None\n\n
    preserveState(final ConsumerChoicePointFrame ccp)\n
    '''
def restoreState():
    '''returns None\n\n
    restoreState(final ConsumerChoicePointFrame ccp)\n
    '''
def unify():
    '''returns boolean\n\n
    unify(final Node n1, final Node n2)\n
    '''
def bind():
    '''returns None\n\n
    bind(final Node var, final Node val)\n
    '''
def unwindTrail():
    '''returns None\n\n
    unwindTrail(final int mark)\n
    '''
