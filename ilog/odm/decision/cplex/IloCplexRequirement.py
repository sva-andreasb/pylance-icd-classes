COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns Base\n\n
    (final IloConstraint constraint, final int explainPrio)\n
    (final String name, final IloReqPropertiesDef props)\n
    '''
def getConstraint():
    '''returns IloConstraint\n\n
    getConstraint()\n
    '''
def getExplainPrio():
    '''returns int\n\n
    getExplainPrio()\n
    '''
def needEngineUpdate():
    '''returns boolean\n\n
    needEngineUpdate(final int propIndex)\n
    '''
def getExplanationPriority():
    '''returns int\n\n
    getExplanationPriority(final int defaultVal)\n
    '''
def getRelaxationEps():
    '''returns double\n\n
    getRelaxationEps(final double defaultVal)\n
    '''
def getRelaxationMsg():
    '''returns IloMessage\n\n
    getRelaxationMsg()\n
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
def getFormattedRelaxationMsg():
    '''returns String\n\n
    getFormattedRelaxationMsg(final IloCplexController ctl)\n
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
def onChangeProperty():
    '''returns None\n\n
    onChangeProperty(final int propIndex, final Object oldValue, final IloEngineController ctler)\n
    '''
def onChangePriority():
    '''returns None\n\n
    onChangePriority(final IloEngineController ctler)\n
    '''
def getExplanation():
    '''returns IloMessage\n\n
    getExplanation()\n
    '''
