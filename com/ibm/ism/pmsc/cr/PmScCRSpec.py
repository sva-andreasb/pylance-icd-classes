COPYRIGHT = "String  \"IBM Confidential OCO Source Material\n5725-E24 (C) COPYRIGHT International Business Machines Corp. 2007, 2017\nThe source code for this program is not published or otherwise divested\nof its trade secrets, irrespective of what has been deposited with the\nU.S. Copyright Office.\""
def ():
    '''returns PmScCRSpec\n\n
    (final MboSet ms)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def hasSpecifications():
    '''returns boolean\n\n
    hasSpecifications()\n
    '''
def copyToTicketSpec():
    '''returns None\n\n
    copyToTicketSpec()\n
    '''
def getMaxTableDomainObject():
    '''returns MboRemote\n\n
    getMaxTableDomainObject(final String columnNumber)\n
    '''
def setMaxTableDomainObject():
    '''returns None\n\n
    setMaxTableDomainObject(final String columnNumber, final MboRemote passedDomain)\n
    '''
def appValidate():
    '''returns String\n\n
    appValidate(final String dataAttribute, final String newValue)\n
    appValidate(final String dataAttribute, final String newValue, final MboRemote spSR)\n
    '''
def appPrepopulate():
    '''returns String\n\n
    appPrepopulate()\n
    appPrepopulate(final MboRemote spSR)\n
    '''
def appAddtoCartValidation():
    '''returns ArrayList<String>\n\n
    appAddtoCartValidation(final OfferingRemote offering, MboRemote srMbo, final boolean findAll)\n
    '''
def getValue():
    '''returns String\n\n
    getValue(final String attributeName)\n
    '''
def setNewValue():
    '''returns None\n\n
    setNewValue(final String attributeName, final String val)\n
    '''
def attributeFind():
    '''returns String\n\n
    attributeFind(final String attrID, final int ticketspecid)\n
    '''
def copySpecAttributes():
    '''returns None\n\n
    copySpecAttributes(final PmScCRSpecRemote copySpecMbo)\n
    '''
def validateAttributes():
    '''returns String\n\n
    validateAttributes(final SRRemote sr, final boolean findAll)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final String attribute, final String val, final long accessModifier)\n
    setValue(final String attribute, final double val, final long accessModifier)\n
    setValue(final String attribute, final long val, final long accessModifier)\n
    setValue(final String attribute, final int val, final long accessModifier)\n
    setValue(final String attribute, final float val, final long accessModifier)\n
    setValue(final String attribute, final short val, final long accessModifier)\n
    setValue(final String attribute, final boolean val, final long accessModifier)\n
    setValue(final String attribute, final byte val, final long accessModifier)\n
    '''
def getNumValueBeforeFormat():
    '''returns String\n\n
    getNumValueBeforeFormat()\n
    '''
