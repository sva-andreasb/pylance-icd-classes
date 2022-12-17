def ():
    '''returns MutablePatternModifier\n\n
    (final boolean isStrong)\n
    '''
def setPatternInfo():
    '''returns None\n\n
    setPatternInfo(final AffixPatternProvider patternInfo, final NumberFormat.Field field)\n
    '''
def setPatternAttributes():
    '''returns None\n\n
    setPatternAttributes(final NumberFormatter.SignDisplay signDisplay, final boolean perMille)\n
    '''
def setSymbols():
    '''returns None\n\n
    setSymbols(final DecimalFormatSymbols symbols, final Currency currency, final NumberFormatter.UnitWidth unitWidth, final PluralRules rules)\n
    '''
def setNumberProperties():
    '''returns None\n\n
    setNumberProperties(final Signum signum, final StandardPlural plural)\n
    '''
def needsPlurals():
    '''returns boolean\n\n
    needsPlurals()\n
    '''
def createImmutable():
    '''returns ImmutablePatternModifier\n\n
    createImmutable()\n
    '''
def addToChain():
    '''returns ImmutablePatternModifier\n\n
    addToChain(final MicroPropsGenerator parent)\n
    addToChain(final MicroPropsGenerator parent)\n
    '''
def processQuantity():
    '''returns MicroProps\n\n
    processQuantity(final DecimalQuantity fq)\n
    processQuantity(final DecimalQuantity quantity)\n
    '''
def apply():
    '''returns int\n\n
    apply(final FormattedStringBuilder output, final int leftIndex, final int rightIndex)\n
    '''
def getPrefixLength():
    '''returns int\n\n
    getPrefixLength()\n
    '''
def getCodePointCount():
    '''returns int\n\n
    getCodePointCount()\n
    '''
def isStrong():
    '''returns boolean\n\n
    isStrong()\n
    '''
def containsField():
    '''returns boolean\n\n
    containsField(final Format.Field field)\n
    '''
def getParameters():
    '''returns Parameters\n\n
    getParameters()\n
    '''
def semanticallyEquivalent():
    '''returns boolean\n\n
    semanticallyEquivalent(final Modifier other)\n
    '''
def getSymbol():
    '''returns CharSequence\n\n
    getSymbol(final int type)\n
    '''
def applyToMicros():
    '''returns None\n\n
    applyToMicros(final MicroProps micros, final DecimalQuantity quantity)\n
    '''
