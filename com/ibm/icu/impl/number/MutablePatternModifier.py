def MutablePatternModifier():
    '''public MutablePatternModifier(final boolean isStrong)
    '''
def setPatternInfo():
    '''public void setPatternInfo(final AffixPatternProvider patternInfo, final NumberFormat.Field field)
    '''
def setPatternAttributes():
    '''public void setPatternAttributes(final NumberFormatter.SignDisplay signDisplay, final boolean perMille)
    '''
def setSymbols():
    '''public void setSymbols(final DecimalFormatSymbols symbols, final Currency currency, final NumberFormatter.UnitWidth unitWidth, final PluralRules rules)
    '''
def setNumberProperties():
    '''public void setNumberProperties(final Signum signum, final StandardPlural plural)
    '''
def needsPlurals():
    '''public boolean needsPlurals()
    '''
def createImmutable():
    '''public ImmutablePatternModifier createImmutable()
    '''
def addToChain():
    '''public MicroPropsGenerator addToChain(final MicroPropsGenerator parent)
    public ImmutablePatternModifier addToChain(final MicroPropsGenerator parent)
    '''
def processQuantity():
    '''public MicroProps processQuantity(final DecimalQuantity fq)
    public MicroProps processQuantity(final DecimalQuantity quantity)
    '''
def apply():
    '''public int apply(final FormattedStringBuilder output, final int leftIndex, final int rightIndex)
    '''
def getPrefixLength():
    '''public int getPrefixLength()
    '''
def getCodePointCount():
    '''public int getCodePointCount()
    '''
def isStrong():
    '''public boolean isStrong()
    '''
def containsField():
    '''public boolean containsField(final Format.Field field)
    '''
def getParameters():
    '''public Parameters getParameters()
    '''
def semanticallyEquivalent():
    '''public boolean semanticallyEquivalent(final Modifier other)
    '''
def getSymbol():
    '''public CharSequence getSymbol(final int type)
    '''
def applyToMicros():
    '''public void applyToMicros(final MicroProps micros, final DecimalQuantity quantity)
    '''
