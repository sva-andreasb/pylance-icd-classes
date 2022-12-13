COPYRIGHT = "String  \"IBM Confidential OCO Source Material\n5725-E24 (C) COPYRIGHT International Business Machines Corp. 2007, 2017\nThe source code for this program is not published or otherwise divested\nof its trade secrets, irrespective of what has been deposited with the\nU.S. Copyright Office.\""
def PmScCRSpec():
    '''public PmScCRSpec(final MboSet ms)
    '''
def add():
    '''public void add()
    '''
def hasSpecifications():
    '''public boolean hasSpecifications()
    '''
def copyToTicketSpec():
    '''public void copyToTicketSpec()
    '''
def getMaxTableDomainObject():
    '''public MboRemote getMaxTableDomainObject(final String columnNumber)
    '''
def setMaxTableDomainObject():
    '''public void setMaxTableDomainObject(final String columnNumber, final MboRemote passedDomain)
    '''
def appValidate():
    '''public String appValidate(final String dataAttribute, final String newValue)
    public String appValidate(final String dataAttribute, final String newValue, final MboRemote spSR)
    '''
def appPrepopulate():
    '''public String appPrepopulate()
    public String appPrepopulate(final MboRemote spSR)
    '''
def appAddtoCartValidation():
    '''public ArrayList<String> appAddtoCartValidation(final OfferingRemote offering, MboRemote srMbo, final boolean findAll)
    '''
def getValue():
    '''public String getValue(final String attributeName)
    '''
def setNewValue():
    '''public void setNewValue(final String attributeName, final String val)
    '''
def attributeFind():
    '''public String attributeFind(final String attrID, final int ticketspecid)
    '''
def copySpecAttributes():
    '''public void copySpecAttributes(final PmScCRSpecRemote copySpecMbo)
    '''
def validateAttributes():
    '''public String validateAttributes(final SRRemote sr, final boolean findAll)
    '''
def setValue():
    '''public void setValue(final String attribute, final String val, final long accessModifier)
    public void setValue(final String attribute, final double val, final long accessModifier)
    public void setValue(final String attribute, final long val, final long accessModifier)
    public void setValue(final String attribute, final int val, final long accessModifier)
    public void setValue(final String attribute, final float val, final long accessModifier)
    public void setValue(final String attribute, final short val, final long accessModifier)
    public void setValue(final String attribute, final boolean val, final long accessModifier)
    public void setValue(final String attribute, final byte val, final long accessModifier)
    '''
def getNumValueBeforeFormat():
    '''public String getNumValueBeforeFormat()
    '''
