DATATYPE_XS_STRING = "String  \"xs:string\""
ELEMENT = "String  \"list-range\""
NAMESPACE = "String  \"http://jabber.org/protocol/xdata-validate\""
METHOD = "String  \"regex\""
def getDatatype():
    '''    public String getDatatype()
    '''
def getElementName():
    '''    public String getElementName()
    public String getElementName()
    '''
def getNamespace():
    '''    public String getNamespace()
    '''
def toXML():
    '''    public XmlStringBuilder toXML(final String enclosingNamespace)
    public XmlStringBuilder toXML(final String enclosingNamespace)
    '''
def setListRange():
    '''    public void setListRange(final ListRange listRange)
    '''
def getListRange():
    '''    public ListRange getListRange()
    '''
def BasicValidateElement():
    '''    public BasicValidateElement(final String dataType)
    '''
def checkConsistency():
    '''    public void checkConsistency(final FormField formField)
    public void checkConsistency(final FormField formField)
    public void checkConsistency(final FormField formField)
    public void checkConsistency(final FormField formField)
    '''
def OpenValidateElement():
    '''    public OpenValidateElement(final String dataType)
    '''
def RangeValidateElement():
    '''    public RangeValidateElement(final String dataType, final String min, final String max)
    '''
def getMin():
    '''    public String getMin()
    public Long getMin()
    '''
def getMax():
    '''    public String getMax()
    public Long getMax()
    '''
def RegexValidateElement():
    '''    public RegexValidateElement(final String dataType, final String regex)
    '''
def getRegex():
    '''    public String getRegex()
    '''
def ListRange():
    '''    public ListRange(final Long min, final Long max)
    '''
