def MutablePatternModifier():
'''public MutablePatternModifier(final boolean isStrong)
'''
pass
def setPatternInfo():
'''public void setPatternInfo(final AffixPatternProvider patternInfo, final NumberFormat.Field field)
'''
pass
def setPatternAttributes():
'''public void setPatternAttributes(final NumberFormatter.SignDisplay signDisplay, final boolean perMille)
'''
pass
def setSymbols():
'''public void setSymbols(final DecimalFormatSymbols symbols, final Currency currency, final NumberFormatter.UnitWidth unitWidth, final PluralRules rules)
'''
pass
def setNumberProperties():
'''public void setNumberProperties(final Signum signum, final StandardPlural plural)
'''
pass
def needsPlurals():
'''public boolean needsPlurals()
'''
pass
def createImmutable():
'''public ImmutablePatternModifier createImmutable()
'''
pass
def addToChain():
'''public MicroPropsGenerator addToChain(final MicroPropsGenerator parent)
public ImmutablePatternModifier addToChain(final MicroPropsGenerator parent)
'''
pass
def processQuantity():
'''public MicroProps processQuantity(final DecimalQuantity fq)
public MicroProps processQuantity(final DecimalQuantity quantity)
'''
pass
def apply():
'''public int apply(final FormattedStringBuilder output, final int leftIndex, final int rightIndex)
'''
pass
def getPrefixLength():
'''public int getPrefixLength()
'''
pass
def getCodePointCount():
'''public int getCodePointCount()
'''
pass
def isStrong():
'''public boolean isStrong()
'''
pass
def containsField():
'''public boolean containsField(final Format.Field field)
'''
pass
def getParameters():
'''public Parameters getParameters()
'''
pass
def semanticallyEquivalent():
'''public boolean semanticallyEquivalent(final Modifier other)
'''
pass
def getSymbol():
'''public CharSequence getSymbol(final int type)
'''
pass
def applyToMicros():
'''public void applyToMicros(final MicroProps micros, final DecimalQuantity quantity)
'''
pass
