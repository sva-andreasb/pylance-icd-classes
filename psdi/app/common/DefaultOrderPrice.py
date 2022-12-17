FULLFUNDTRACKING = "int  1"
LIMITEDFUNDTRACKING = "int  2"
NOFUNDTRACKING = "int  4"
NOFUNDCHECKING = "int  5"
priceMANUFACTURER = "int  101"
priceMODELNUM = "int  102"
priceCATALOGCODE = "int  103"
priceORDERUNIT = "int  104"
priceCONTRACTNUM = "int  106"
priceREVISIONNUM = "int  107"
priceCONTRACTID = "int  108"
priceORDERQTY = "int  109"
priceCURRENCY = "int  110"
priceUNITCOST = "int  111"
def ():
    '''returns DefaultOrderPrice\n\n
    ()\n
    (final int options)\n
    '''
def getItemNumFlag():
    '''returns int\n\n
    getItemNumFlag()\n
    '''
def getDefaultOrderPrice():
    '''returns double\n\n
    getDefaultOrderPrice(String currencyCode, double quantity, final boolean considerBlanket, final boolean considerPrice, final Mbo mbo)\n
    '''
def setPriceAttribute():
    '''returns None\n\n
    setPriceAttribute(final Mbo mbo, final String attribute, final int identifier, final long flags)\n
    setPriceAttribute(final Mbo mbo, final String attribute, final int identifier)\n
    '''
def isBlanketPrice():
    '''returns boolean\n\n
    isBlanketPrice()\n
    '''
def isContractPrice():
    '''returns boolean\n\n
    isContractPrice()\n
    '''
def isVendorPrice():
    '''returns boolean\n\n
    isVendorPrice()\n
    '''
def isInventoryPrice():
    '''returns boolean\n\n
    isInventoryPrice()\n
    '''
def isNoPriceFound():
    '''returns boolean\n\n
    isNoPriceFound()\n
    '''
