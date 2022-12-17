def ():
    '''returns NamesManager\n\n
    (final Guid[] inputList)\n
    '''
def addNextEntry():
    '''returns boolean\n\n
    addNextEntry(final Guid originalInputGuid, final Guid next)\n
    '''
def addEntryAfter():
    '''returns boolean\n\n
    addEntryAfter(final Guid originalInputGuid, final Guid parentGuid, final Guid supGuid)\n
    '''
def processSuperior():
    '''returns boolean\n\n
    processSuperior(final Guid originalInputGuid, final Guid parentGuid, final Guid supGuid, final int superiorOrder)\n
    '''
def addNamesPart():
    '''returns boolean\n\n
    addNamesPart(final Guid originalInput, final Guid currentInput, final List<String> names)\n
    '''
def addNames():
    '''returns boolean\n\n
    addNames(final Guid originalInput, final Guid currentInput, final List<String> names)\n
    '''
def addName():
    '''returns boolean\n\n
    addName(final Guid originalInput, final Guid currentInput, final String name)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
