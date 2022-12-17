def ():
    '''returns IloSolution\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    ()\n
    (final IloSolution solution)\n
    (final IloEnv mem, final String name)\n
    (final IloEnv mem)\n
    '''
def setOwn():
    '''returns None\n\n
    setOwn(final boolean cMemoryOwn)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def add():
    '''returns None\n\n
    add(final IloNumVar v)\n
    add(final IloIntVar v)\n
    add(final IloIntVar[] a)\n
    add(final IloIntervalVar v)\n
    add(final IloIntervalVar[] a)\n
    add(final ilog.concert.cppimpl.IloNumVar var)\n
    add(final ilog.concert.cppimpl.IloIntVar var)\n
    add(final ilog.concert.cppimpl.IloIntervalVar a)\n
    add(final IloIntervalVarArray a)\n
    '''
def getValue():
    '''returns int\n\n
    getValue(final IloNumVar v)\n
    getValue(final IloIntVar v)\n
    getValue(final IloObjective obj)\n
    getValue(final ilog.concert.cppimpl.IloNumVar var)\n
    getValue(final ilog.concert.cppimpl.IloIntVar var)\n
    '''
def getStart():
    '''returns int\n\n
    getStart(final IloIntervalVar v)\n
    getStart(final ilog.concert.cppimpl.IloIntervalVar a)\n
    '''
def getStartMin():
    '''returns int\n\n
    getStartMin(final IloIntervalVar v)\n
    getStartMin(final ilog.concert.cppimpl.IloIntervalVar a)\n
    '''
def getStartMax():
    '''returns int\n\n
    getStartMax(final IloIntervalVar v)\n
    getStartMax(final ilog.concert.cppimpl.IloIntervalVar a)\n
    '''
def getEnd():
    '''returns int\n\n
    getEnd(final IloIntervalVar v)\n
    getEnd(final ilog.concert.cppimpl.IloIntervalVar a)\n
    '''
def getEndMin():
    '''returns int\n\n
    getEndMin(final IloIntervalVar v)\n
    getEndMin(final ilog.concert.cppimpl.IloIntervalVar a)\n
    '''
def getEndMax():
    '''returns int\n\n
    getEndMax(final IloIntervalVar v)\n
    getEndMax(final ilog.concert.cppimpl.IloIntervalVar a)\n
    '''
def getLength():
    '''returns int\n\n
    getLength(final IloIntervalVar v)\n
    getLength(final ilog.concert.cppimpl.IloIntervalVar a)\n
    '''
def getLengthMin():
    '''returns int\n\n
    getLengthMin(final IloIntervalVar v)\n
    getLengthMin(final ilog.concert.cppimpl.IloIntervalVar a)\n
    '''
def getLengthMax():
    '''returns int\n\n
    getLengthMax(final IloIntervalVar v)\n
    getLengthMax(final ilog.concert.cppimpl.IloIntervalVar a)\n
    '''
def getSize():
    '''returns int\n\n
    getSize(final IloIntervalVar v)\n
    getSize(final ilog.concert.cppimpl.IloIntervalVar a)\n
    '''
def getSizeMin():
    '''returns int\n\n
    getSizeMin(final IloIntervalVar v)\n
    getSizeMin(final ilog.concert.cppimpl.IloIntervalVar a)\n
    '''
def getSizeMax():
    '''returns int\n\n
    getSizeMax(final IloIntervalVar v)\n
    getSizeMax(final ilog.concert.cppimpl.IloIntervalVar a)\n
    '''
def isFixed():
    '''returns boolean\n\n
    isFixed(final IloIntVar v)\n
    isFixed(final ilog.concert.cppimpl.IloIntVar var)\n
    '''
def isInDomain():
    '''returns boolean\n\n
    isInDomain(final IloIntVar v, final int value)\n
    isInDomain(final ilog.concert.cppimpl.IloIntVar var, final int value)\n
    '''
def isPresent():
    '''returns boolean\n\n
    isPresent(final IloIntervalVar v)\n
    isPresent(final ilog.concert.cppimpl.IloIntervalVar a)\n
    '''
def isAbsent():
    '''returns boolean\n\n
    isAbsent(final IloIntervalVar v)\n
    isAbsent(final ilog.concert.cppimpl.IloIntervalVar a)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IloIntVar v)\n
    contains(final IloIntervalVar v)\n
    contains(final IloExtractable extr)\n
    '''
def remove():
    '''returns None\n\n
    remove(final IloIntVar v)\n
    remove(final IloIntVar[] v)\n
    remove(final IloIntervalVar v)\n
    remove(final IloIntervalVar[] v)\n
    remove(final IloExtractable extr)\n
    remove(final IloExtractableArray extr)\n
    '''
def setDomain():
    '''returns None\n\n
    setDomain(final IloIntVar v, final int min, final int max)\n
    setDomain(final ilog.concert.cppimpl.IloIntVar var, final int min, final int max)\n
    '''
def setAbsent():
    '''returns None\n\n
    setAbsent(final IloIntervalVar v)\n
    setAbsent(final ilog.concert.cppimpl.IloIntervalVar a)\n
    '''
def setPresent():
    '''returns None\n\n
    setPresent(final IloIntervalVar v)\n
    setPresent(final ilog.concert.cppimpl.IloIntervalVar a)\n
    '''
def setOptional():
    '''returns None\n\n
    setOptional(final IloIntervalVar v)\n
    setOptional(final ilog.concert.cppimpl.IloIntervalVar a)\n
    '''
def setStart():
    '''returns None\n\n
    setStart(final IloIntervalVar v, final int val)\n
    setStart(final ilog.concert.cppimpl.IloIntervalVar a, final int v)\n
    '''
def setStartMin():
    '''returns None\n\n
    setStartMin(final IloIntervalVar v, final int min)\n
    setStartMin(final ilog.concert.cppimpl.IloIntervalVar a, final int min)\n
    '''
def setStartMax():
    '''returns None\n\n
    setStartMax(final IloIntervalVar v, final int max)\n
    setStartMax(final ilog.concert.cppimpl.IloIntervalVar a, final int max)\n
    '''
def setEnd():
    '''returns None\n\n
    setEnd(final IloIntervalVar v, final int val)\n
    setEnd(final ilog.concert.cppimpl.IloIntervalVar a, final int v)\n
    '''
def setEndMin():
    '''returns None\n\n
    setEndMin(final IloIntervalVar v, final int min)\n
    setEndMin(final ilog.concert.cppimpl.IloIntervalVar a, final int min)\n
    '''
def setEndMax():
    '''returns None\n\n
    setEndMax(final IloIntervalVar v, final int max)\n
    setEndMax(final ilog.concert.cppimpl.IloIntervalVar a, final int max)\n
    '''
def setLength():
    '''returns None\n\n
    setLength(final IloIntervalVar v, final int val)\n
    setLength(final ilog.concert.cppimpl.IloIntervalVar a, final int v)\n
    '''
def setLengthMin():
    '''returns None\n\n
    setLengthMin(final IloIntervalVar v, final int min)\n
    setLengthMin(final ilog.concert.cppimpl.IloIntervalVar a, final int min)\n
    '''
def setLengthMax():
    '''returns None\n\n
    setLengthMax(final IloIntervalVar v, final int max)\n
    setLengthMax(final ilog.concert.cppimpl.IloIntervalVar a, final int max)\n
    '''
def setSize():
    '''returns None\n\n
    setSize(final IloIntervalVar v, final int val)\n
    setSize(final ilog.concert.cppimpl.IloIntervalVar a, final int v)\n
    '''
def setSizeMin():
    '''returns None\n\n
    setSizeMin(final IloIntervalVar v, final int min)\n
    setSizeMin(final ilog.concert.cppimpl.IloIntervalVar a, final int min)\n
    '''
def setSizeMax():
    '''returns None\n\n
    setSizeMax(final IloIntervalVar v, final int max)\n
    setSizeMax(final ilog.concert.cppimpl.IloIntervalVar a, final int max)\n
    '''
def setMin():
    '''returns None\n\n
    setMin(final IloNumVar var, final double value)\n
    setMin(final IloIntVar var, final int value)\n
    setMin(final ilog.concert.cppimpl.IloNumVar var, final double min)\n
    setMin(final ilog.concert.cppimpl.IloIntVar var, final int min)\n
    '''
def setMax():
    '''returns None\n\n
    setMax(final IloNumVar var, final double value)\n
    setMax(final IloIntVar var, final int value)\n
    setMax(final ilog.concert.cppimpl.IloNumVar var, final double max)\n
    setMax(final ilog.concert.cppimpl.IloIntVar var, final int max)\n
    '''
def getMin():
    '''returns int\n\n
    getMin(final IloNumVar var)\n
    getMin(final IloIntVar var)\n
    getMin(final ilog.concert.cppimpl.IloNumVar var)\n
    getMin(final ilog.concert.cppimpl.IloIntVar var)\n
    '''
def getMax():
    '''returns int\n\n
    getMax(final IloNumVar var)\n
    getMax(final IloIntVar var)\n
    getMax(final ilog.concert.cppimpl.IloNumVar var)\n
    getMax(final ilog.concert.cppimpl.IloIntVar var)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final IloNumVar var, final double value)\n
    setValue(final IloIntVar var, final int value)\n
    setValue(final IloObjective objective, final double value)\n
    setValue(final ilog.concert.cppimpl.IloNumVar var, final double value)\n
    setValue(final ilog.concert.cppimpl.IloIntVar var, final int value)\n
    '''
def store():
    '''returns None\n\n
    store()\n
    store(final IloAlgorithm algorithm)\n
    store(final IloExtractable extr, final IloAlgorithm algorithm)\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def isBetterThan():
    '''returns boolean\n\n
    isBetterThan(final IloSolution solution)\n
    '''
def isRestorable():
    '''returns boolean\n\n
    isRestorable(final IloExtractable extr)\n
    '''
def isWorseThan():
    '''returns boolean\n\n
    isWorseThan(final IloSolution solution)\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def setLocation():
    '''returns None\n\n
    setLocation(final String fileName, final int lineNumber)\n
    '''
