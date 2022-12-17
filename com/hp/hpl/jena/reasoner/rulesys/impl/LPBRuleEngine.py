CYCLES_BETWEEN_COMPLETION_CHECK = "int  3"
def ():
    '''returns Count\n\n
    (final BackwardRuleInfGraphI infGraph, final LPRuleStore rules)\n
    (final BackwardRuleInfGraphI infGraph)\n
    (final RuleClauseCode clause)\n
    '''
def setTraceOn():
    '''returns None\n\n
    setTraceOn(final boolean state)\n
    '''
def isTraceOn():
    '''returns boolean\n\n
    isTraceOn()\n
    '''
def setDerivationLogging():
    '''returns None\n\n
    setDerivationLogging(final boolean recordDerivations)\n
    '''
def getDerivationLogging():
    '''returns boolean\n\n
    getDerivationLogging()\n
    '''
def getRuleStore():
    '''returns LPRuleStore\n\n
    getRuleStore()\n
    '''
def getInfGraph():
    '''returns BackwardRuleInfGraphI\n\n
    getInfGraph()\n
    '''
def checkSafeToUpdate():
    '''returns None\n\n
    checkSafeToUpdate()\n
    '''
def schedule():
    '''returns None\n\n
    schedule(final LPAgendaEntry state)\n
    '''
def pump():
    '''returns None\n\n
    pump(final LPInterpreterContext gen)\n
    '''
def checkForCompletions():
    '''returns None\n\n
    checkForCompletions()\n
    '''
def incrementProfile():
    '''returns None\n\n
    incrementProfile(final RuleClauseCode clause)\n
    '''
def resetProfile():
    '''returns None\n\n
    resetProfile(final boolean enable)\n
    '''
def printProfile():
    '''returns None\n\n
    printProfile()\n
    '''
def getCount():
    '''returns int\n\n
    getCount()\n
    '''
def inc():
    '''returns Count\n\n
    inc()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Count other)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
