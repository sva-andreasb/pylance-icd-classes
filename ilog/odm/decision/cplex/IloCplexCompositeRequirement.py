COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def postToCplex():
    '''returns None\n\n
    postToCplex(final IloCplexController ctl, final boolean propagate)\n
    '''
def removeFromCplex():
    '''returns None\n\n
    removeFromCplex(final IloCplexController ctl, final boolean propagate)\n
    '''
def changeRangesPriority():
    '''returns None\n\n
    changeRangesPriority(final IloCplexController ctl)\n
    '''
def needEngineUpdate():
    '''returns boolean\n\n
    needEngineUpdate(final int propIndex)\n
    '''
def getRelaxationEps():
    '''returns double\n\n
    getRelaxationEps(final double defaultVal)\n
    '''
def getRelaxationMsg():
    '''returns IloMessage\n\n
    getRelaxationMsg()\n
    '''
def getFormattedRelaxationMsg():
    '''returns String\n\n
    getFormattedRelaxationMsg(final IloCplexController ctl)\n
    '''
def getRelaxationPref():
    '''returns double\n\n
    getRelaxationPref(final double defaultVal)\n
    '''
def setExplanationPriority():
    '''returns None\n\n
    setExplanationPriority(final int v)\n
    '''
def setRelaxationMsg():
    '''returns None\n\n
    setRelaxationMsg(final IloMessage msg)\n
    setRelaxationMsg(final String msg)\n
    '''
def setRelaxationEps():
    '''returns None\n\n
    setRelaxationEps(final Double v)\n
    setRelaxationEps(final double v)\n
    '''
def setRelaxationPref():
    '''returns None\n\n
    setRelaxationPref(final double v)\n
    setRelaxationPref(final Double v)\n
    '''
def onChangePriority():
    '''returns None\n\n
    onChangePriority(final IloEngineController ctler)\n
    '''
def onChangeProperty():
    '''returns None\n\n
    onChangeProperty(final int index, final Object oldValue, final IloEngineController ctler)\n
    '''
def registerRequirement():
    '''returns None\n\n
    registerRequirement(final IloRequirement r)\n
    '''
