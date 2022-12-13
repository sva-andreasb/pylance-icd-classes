def BIMProjectParser():
    '''    public BIMProjectParser(final long flags)
    public BIMProjectParser(final IdFactory idFactory, final MessageLogger logger, final Locale locale, final long flags)
    '''
def addConvertedField():
    '''    public void addConvertedField(final String tableName, final String fieldName, final String attributeName)
    '''
def getConvertedField():
    '''    public String getConvertedField(final String tableName, final String fieldName)
    '''
def addFile():
    '''    public void addFile(final InputFile cobieFile)
    '''
def addSkippedSpace():
    '''    public void addSkippedSpace(final String spaceName)
    '''
def isSpaceSkipped():
    '''    public boolean isSpaceSkipped(final String spaceName)
    '''
def addFilter():
    '''    public void addFilter(final Filter filter)
    '''
def filters():
    '''    public Iterator<Filter> filters()
    '''
def execute():
    '''    public void execute()
    '''
def deleteFiles():
    '''    public void deleteFiles(final String workingDirRoot)
    '''
def addPage():
    '''    public void addPage(final Page page)
    '''
def clenup():
    '''    public void clenup()
    '''
def resolveReferences():
    '''    public void resolveReferences()
    '''
def categoryFromAttribute():
    '''    public void categoryFromAttribute(String omniClassAttribute)
    '''
def spacesFromAttribute():
    '''    public void spacesFromAttribute(final String spaceAttrib)
    '''
def levelsFromAttribute():
    '''    public void levelsFromAttribute(final String levelAttrib)
    '''
def areaFromAttribute():
    '''    public void areaFromAttribute(final String areaAttribute)
    '''
def perimeterFromAttribute():
    '''    public void perimeterFromAttribute(final String perimeterAttribute)
    '''
def systemsFromAttribute():
    '''    public void systemsFromAttribute(String systemNameAttrib)
    '''
def associateCategoriesWithAttributeTypes():
    '''    public void associateCategoriesWithAttributeTypes(final String[] pageList)
    '''
def getValueList():
    '''    public ItemValueList getValueList(final HashSet<String> valueSet)
    '''
def caculateItemCount():
    '''    public void caculateItemCount()
    '''
def getPage():
    '''    public Page getPage(final String pageName)
    '''
def getItem():
    '''    public Item getItem(final String pageName, final String key)
    '''
def getAttributeType():
    '''    public ItemAttributeType getAttributeType(final String typeName)
    '''
def getCompanyFromContact():
    '''    public ItemCONTACT getCompanyFromContact(final String companyName)
    '''
def convertCase():
    '''    public String convertCase(final String s)
    '''
def getCategoryMap():
    '''    public AttributeTypeMap getCategoryMap()
    '''
def getLocale():
    '''    public Locale getLocale()
    '''
def getItemCount():
    '''    public int getItemCount()
    '''
def getVendorAttribute():
    '''    public String getVendorAttribute()
    '''
def printPage():
    '''    public void printPage(final Page page)
    '''
def printAll():
    '''    public void printAll()
    '''
def getLogger():
    '''    public MessageLogger getLogger()
    '''
def setLogger():
    '''    public void setLogger(final MessageLogger logger)
    '''
def setVendorAttribute():
    '''    public void setVendorAttribute(final String vendorAttribute)
    '''
def export():
    '''    public void export(final String fileName, final String[] pageList, final InputStream templateStream, final ExportProgressTracker tracker, final Exporter.ExportFormat fileFormat)
    '''
def messageFromException():
    '''    public static String messageFromException(final Throwable t)
    '''
def main():
    '''    public static void main(final String[] args)
    '''
