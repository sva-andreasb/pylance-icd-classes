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
def DefaultOrderPrice():
    '''public DefaultOrderPrice()
    public DefaultOrderPrice(final int options)
    '''
def getItemNumFlag():
    '''public int getItemNumFlag()
    '''
def getDefaultOrderPrice():
    '''public double getDefaultOrderPrice(String currencyCode, double quantity, final boolean considerBlanket, final boolean considerPrice, final Mbo mbo)
    '''
def setPriceAttribute():
    '''public void setPriceAttribute(final Mbo mbo, final String attribute, final int identifier, final long flags)
    public void setPriceAttribute(final Mbo mbo, final String attribute, final int identifier)
    '''
def isBlanketPrice():
    '''public boolean isBlanketPrice()
    '''
def isContractPrice():
    '''public boolean isContractPrice()
    '''
def isVendorPrice():
    '''public boolean isVendorPrice()
    '''
def isInventoryPrice():
    '''public boolean isInventoryPrice()
    '''
def isNoPriceFound():
    '''public boolean isNoPriceFound()
    '''
