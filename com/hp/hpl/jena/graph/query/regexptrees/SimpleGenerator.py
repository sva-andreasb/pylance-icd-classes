def getAnySingle():
    '''returns RegexpTree\n\n
    getAnySingle()\n
    '''
def getStartOfLine():
    '''returns RegexpTree\n\n
    getStartOfLine()\n
    '''
def getEndOfLine():
    '''returns RegexpTree\n\n
    getEndOfLine()\n
    '''
def getNothing():
    '''returns RegexpTree\n\n
    getNothing()\n
    '''
def getText():
    '''returns RegexpTree\n\n
    getText(final char ch)\n
    '''
def getZeroOrMore():
    '''returns RegexpTree\n\n
    getZeroOrMore(final RegexpTree d)\n
    '''
def getOneOrMore():
    '''returns RegexpTree\n\n
    getOneOrMore(final RegexpTree d)\n
    '''
def getOptional():
    '''returns RegexpTree\n\n
    getOptional(final RegexpTree d)\n
    '''
def getSequence():
    '''returns RegexpTree\n\n
    getSequence(final List<? extends RegexpTree> operands)\n
    '''
def getAlternatives():
    '''returns RegexpTree\n\n
    getAlternatives(final List<? extends RegexpTree> operands)\n
    '''
def getBackReference():
    '''returns RegexpTree\n\n
    getBackReference(final int n)\n
    '''
def getClass():
    '''returns RegexpTree\n\n
    getClass(final String chars, final boolean reject)\n
    '''
def getParen():
    '''returns RegexpTree\n\n
    getParen(final RegexpTree operand, final int index)\n
    '''
