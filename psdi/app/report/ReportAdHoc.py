def ReportAdHoc():
    '''public ReportAdHoc(final MboSet ms)
    '''
def add():
    '''public void add()
    '''
def delete():
    '''public void delete(final long accessModifier)
    '''
def addAllAttributes():
    '''public void addAllAttributes()
    '''
def removeAllAttributes():
    '''public void removeAllAttributes()
    '''
def toggleAttribute():
    '''public void toggleAttribute(final String attributeName, final boolean toBeAdded)
    public void toggleAttribute(final MboRemote attribute, final boolean toBeAdded)
    '''
def addToExpressionList():
    '''public void addToExpressionList()
    '''
def addToSummaryList():
    '''public void addToSummaryList()
    '''
def addAttrToExpr():
    '''public void addAttrToExpr(final MboRemote attribute, final boolean toBeAdded)
    '''
def setSelectedCalcCategory():
    '''public void setSelectedCalcCategory(final String category)
    '''
def getSelectedCalcCategory():
    '''public String getSelectedCalcCategory()
    '''
def addAttrToSum():
    '''public void addAttrToSum(final MboRemote attribute)
    '''
def initializeObjectStructureInfo():
    '''public void initializeObjectStructureInfo()
    '''
def isParentSelected():
    '''public boolean isParentSelected(final int objectID)
    '''
def isParentSelectedCalc():
    '''public boolean isParentSelectedCalc(final int objectID)
    '''
def objectDependencyCheck():
    '''public void objectDependencyCheck(final int id)
    '''
def getObjectName():
    '''public String getObjectName(final int objectID)
    '''
def getValidAttributes():
    '''public Set<String> getValidAttributes(final int objectID)
    '''
def updateAvailableAttributes():
    '''public void updateAvailableAttributes()
    '''
def updateAvailableAttributesCalc():
    '''public void updateAvailableAttributesCalc()
    '''
def updateAvailableAttributesSum():
    '''public void updateAvailableAttributesSum()
    '''
def getAvailableAttributesSet():
    '''public MboSetRemote getAvailableAttributesSet()
    '''
def getAvailableAttributesSetCalc():
    '''public MboSetRemote getAvailableAttributesSetCalc()
    '''
def reorderColumns():
    '''public void reorderColumns()
    '''
def reorderCalculations():
    '''public void reorderCalculations()
    '''
def reorderSummaries():
    '''public void reorderSummaries()
    '''
def suggestUniqueName():
    '''public String suggestUniqueName()
    public String suggestUniqueName(String reportName)
    '''
def disableScheduleFields():
    '''public void disableScheduleFields(final boolean disable)
    '''
def createReport():
    '''public void createReport()
    '''
def getReportNum():
    '''public int getReportNum()
    '''
def getReportXML():
    '''public String getReportXML()
    '''
def getPresentationForThisDialog():
    '''public String getPresentationForThisDialog()
    '''
def setDefaultObjectID():
    '''public void setDefaultObjectID()
    '''
def setSelectedObjectID():
    '''public void setSelectedObjectID(final int objectID)
    '''
def getSelectedObjectID():
    '''public int getSelectedObjectID()
    '''
def setSelectedObjectIDCalc():
    '''public void setSelectedObjectIDCalc(final int objectID)
    '''
def getSelectedObjectIDCalc():
    '''public int getSelectedObjectIDCalc()
    '''
def setSelectedObjectIDSum():
    '''public void setSelectedObjectIDSum(final int objectID)
    '''
def getSelectedObjectIDSum():
    '''public int getSelectedObjectIDSum()
    '''
def clearFields():
    '''public void clearFields(final String fieldType)
    '''
def getLevelCount():
    '''public int getLevelCount(final String fieldType)
    '''
def isGroupOrSortField():
    '''public boolean isGroupOrSortField(final MboRemote attribute, final String fieldType)
    '''
def hasDuplicateReportTitle():
    '''public boolean hasDuplicateReportTitle()
    '''
def getDuplicateReportName():
    '''public String getDuplicateReportName()
    '''
def init():
    '''public void init()
    '''
def initFieldFlagsOnMbo():
    '''public void initFieldFlagsOnMbo(final String attrName)
    '''
def sigopGranted():
    '''public boolean sigopGranted(final String app, final String optionname)
    '''
def getCategory():
    '''public String getCategory(final int objectID)
    '''
def setObjectOnlyDefaults():
    '''public void setObjectOnlyDefaults()
    '''
def setSelectedAttributes():
    '''public void setSelectedAttributes()
    '''
def copyChildrenForInit():
    '''public void copyChildrenForInit()
    '''
def copyChildrenForSave():
    '''public void copyChildrenForSave()
    '''
def createReportName():
    '''public String createReportName()
    '''
def clearCalcTempFields():
    '''public void clearCalcTempFields()
    '''
def setLabelSyncFlag():
    '''public void setLabelSyncFlag()
    '''
def setTransientBROSInfo():
    '''public void setTransientBROSInfo(final String brosID, final Hashtable reportParams, final String csrfToken)
    '''
