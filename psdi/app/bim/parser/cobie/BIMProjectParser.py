def BIMProjectParser():
'''public BIMProjectParser(final long flags)
public BIMProjectParser(final IdFactory idFactory, final MessageLogger logger, final Locale locale, final long flags)
'''
pass
def addConvertedField():
'''public void addConvertedField(final String tableName, final String fieldName, final String attributeName)
'''
pass
def getConvertedField():
'''public String getConvertedField(final String tableName, final String fieldName)
'''
pass
def addFile():
'''public void addFile(final InputFile cobieFile)
'''
pass
def addSkippedSpace():
'''public void addSkippedSpace(final String spaceName)
'''
pass
def isSpaceSkipped():
'''public boolean isSpaceSkipped(final String spaceName)
'''
pass
def addFilter():
'''public void addFilter(final Filter filter)
'''
pass
def filters():
'''public Iterator<Filter> filters()
'''
pass
def execute():
'''public void execute()
'''
pass
def deleteFiles():
'''public void deleteFiles(final String workingDirRoot)
'''
pass
def addPage():
'''public void addPage(final Page page)
'''
pass
def clenup():
'''public void clenup()
'''
pass
def resolveReferences():
'''public void resolveReferences()
'''
pass
def categoryFromAttribute():
'''public void categoryFromAttribute(String omniClassAttribute)
'''
pass
def spacesFromAttribute():
'''public void spacesFromAttribute(final String spaceAttrib)
'''
pass
def levelsFromAttribute():
'''public void levelsFromAttribute(final String levelAttrib)
'''
pass
def areaFromAttribute():
'''public void areaFromAttribute(final String areaAttribute)
'''
pass
def perimeterFromAttribute():
'''public void perimeterFromAttribute(final String perimeterAttribute)
'''
pass
def systemsFromAttribute():
'''public void systemsFromAttribute(String systemNameAttrib)
'''
pass
def associateCategoriesWithAttributeTypes():
'''public void associateCategoriesWithAttributeTypes(final String[] pageList)
'''
pass
def getValueList():
'''public ItemValueList getValueList(final HashSet<String> valueSet)
'''
pass
def caculateItemCount():
'''public void caculateItemCount()
'''
pass
def getPage():
'''public Page getPage(final String pageName)
'''
pass
def getItem():
'''public Item getItem(final String pageName, final String key)
'''
pass
def getAttributeType():
'''public ItemAttributeType getAttributeType(final String typeName)
'''
pass
def getCompanyFromContact():
'''public ItemCONTACT getCompanyFromContact(final String companyName)
'''
pass
def convertCase():
'''public String convertCase(final String s)
'''
pass
def getCategoryMap():
'''public AttributeTypeMap getCategoryMap()
'''
pass
def getLocale():
'''public Locale getLocale()
'''
pass
def getItemCount():
'''public int getItemCount()
'''
pass
def getVendorAttribute():
'''public String getVendorAttribute()
'''
pass
def printPage():
'''public void printPage(final Page page)
'''
pass
def printAll():
'''public void printAll()
'''
pass
def getLogger():
'''public MessageLogger getLogger()
'''
pass
def setLogger():
'''public void setLogger(final MessageLogger logger)
'''
pass
def setVendorAttribute():
'''public void setVendorAttribute(final String vendorAttribute)
'''
pass
def export():
'''public void export(final String fileName, final String[] pageList, final InputStream templateStream, final ExportProgressTracker tracker, final Exporter.ExportFormat fileFormat)
'''
pass
def messageFromException():
'''public static String messageFromException(final Throwable t)
'''
pass
def main():
'''public static void main(final String[] args)
'''
pass
