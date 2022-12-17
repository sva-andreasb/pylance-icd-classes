def refetchNumtax():
    '''returns None\n\n
    refetchNumtax()\n
    '''
def setTaxattrValue():
    '''returns None\n\n
    setTaxattrValue(final MboRemote mbo, final String taxattr, final MboRemote mbofrom)\n
    setTaxattrValue(final MboRemote mbo, final String taxattr, final MboRemote mbofrom, final long accessModifier)\n
    setTaxattrValue(final MboRemote mbo, final String taxattr, final boolean booleanValue, final boolean checkDefaultValue)\n
    setTaxattrValue(final MboRemote mbo, final String taxattr, final boolean booleanValue, final boolean checkDefaultValue, final long accessModifier)\n
    setTaxattrValue(final MboRemote mbo, final String taxattr, final double doubleValue, final long accessModifier)\n
    '''
def nullAllTaxcodes():
    '''returns None\n\n
    nullAllTaxcodes(final MboRemote mbo, final String taxattr)\n
    nullAllTaxcodes(final MboRemote mbo, final String taxattr, final long accessModifier)\n
    '''
def setTaxesReadonly():
    '''returns None\n\n
    setTaxesReadonly(final MboRemote mbo, final String taxattr, final boolean readonly)\n
    '''
def setBaseTaxes():
    '''returns None\n\n
    setBaseTaxes(final MboRemote mbofrom, final MboRemote mbo, final String fromTaxAttr, final String taxAttr, final double exchangeRate, final long accessModifier)\n
    '''
def zeroAllTaxes():
    '''returns None\n\n
    zeroAllTaxes(final MboRemote mbo, final String taxattr)\n
    zeroAllTaxes(final MboRemote mbo, final String taxattr, final long accessModifier)\n
    '''
def taxcodeDefined():
    '''returns boolean\n\n
    taxcodeDefined(final MboRemote mbo, final String taxattr)\n
    '''
def getNumberofTaxes():
    '''returns int\n\n
    getNumberofTaxes()\n
    '''
def compareTaxattrValue():
    '''returns boolean\n\n
    compareTaxattrValue(final MboRemote firstMbo, final String taxattr, final MboRemote secondMbo)\n
    '''
def setTaxattrFieldFlag():
    '''returns None\n\n
    setTaxattrFieldFlag(final MboRemote mbo, final String taxattr, final long flag, final boolean state)\n
    '''
def resetTaxOrder():
    '''returns None\n\n
    resetTaxOrder()\n
    '''
def setTaxOrder():
    '''returns None\n\n
    setTaxOrder(final MboRemote mbo)\n
    '''
def getTaxExemptOrder():
    '''returns String[]\n\n
    getTaxExemptOrder(final MboRemote mbo)\n
    '''
def getTaxCodeOrder():
    '''returns String[]\n\n
    getTaxCodeOrder(final MboRemote mbo)\n
    '''
def getTaxesArray():
    '''returns double[]\n\n
    getTaxesArray(final MboRemote mbo)\n
    '''
