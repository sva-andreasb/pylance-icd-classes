LOG_ERRORS = "long  1L"
LOG_WARNINGS = "long  2L"
LOG_MESSAGES = "long  4L"
LOG_ALL = "long  255L"
ATTRIB_LOC_OPPER_LOC = "long  1L"
ATTRIB_LOC_ASSET = "long  2L"
CONTACT_PERSON = "int  1"
CONTACT_USE = "int  2"
CONTACT_BOTH = "int  3"
CONTACT_COMPANY = "int  4"
ATTRIB_TYPE_ID_AUTOKEY = "int  1"
ATTRIB_TYPE_ID_IMPORT = "int  2"
ATTRIB_TYPE_ID_NAME = "int  3"
ATTRIB_TYPE_ID_TRUNCATE = "int  4"
FACILITY_ID_AUTOKEY = "int  1"
FACILITY_ID_IMPORT = "int  2"
FACILITY_ID_PREFIX = "int  3"
FACILITY_ID_NAME = "int  4"
FLOOR_ID_AUTOKEY = "int  1"
FLOOR_ID_IMPORT = "int  2"
FLOOR_ID_PREFIXTAG = "int  3"
FLOOR_ID_PREFIXNAME = "int  6"
FLOOR_ID_TAG = "int  4"
FLOOR_ID_NAME = "int  5"
OBJETLEVEL_SYSTEM = "int  1"
OBJETLEVEL_ORG = "int  2"
OBJETLEVEL_SITE = "int  3"
SPACE_ID_AUTOKEY = "int  1"
SPACE_ID_IMPORT = "int  2"
SPACE_ID_PREFIXTAG = "int  3"
SPACE_ID_PREFIXNAME = "int  6"
SPACE_ID_PREFIXFLOORNAME = "int  7"
SPACE_ID_TAG = "int  4"
SPACE_ID_NAME = "int  5"
OPRLOC_ID_AUTOKEY = "int  1"
OPRLOC_ID_IMPORT = "int  2"
OPRLOC_ID_ASSET = "int  3"
COMPONENT_ID_AUTOKEY = "int  1"
COMPONENT_ID_IMPORT = "int  2"
COMPONENT_ID_BARCODE = "int  3"
COMPONENT_ID_NAME = "int  4"
COMPONENT_ID_PREFIXBAR = "int  5"
COMPONENT_ID_PREFIXNAME = "int  6"
UNITS_LAX = "int  1"
UNITS_IMPORT = "int  2"
UNITS_ENFORCE = "int  3"
UPDATE_VALIDATE_ONLY = "int  1"
UPDATE_INCREMENTAL = "int  2"
UPDATE_BLANKONLY = "int  3"
UPDATE_TIMESTAMP = "int  4"
UPDATE_OVERWRITE = "int  5"
UPDATE_EXPORT = "int  -1"
WARRANTY_NONE = "int  0"
WARRANTY_PARTS = "int  1"
WARRANTY_LABOR = "int  2"
WARRANTY_SHORT = "int  3"
WARRANTY_LONG = "int  4"
def ModelLoaderOptions():
    '''    public ModelLoaderOptions(final BIMSessionRemote sessionMbo, final int updateMode)
    '''
def filtersNames():
    '''    public Iterator<String> filtersNames()
    '''
def getAttributeMapName():
    '''    public String getAttributeMapName()
    '''
def getAttribTypeIdConfig():
    '''    public int getAttribTypeIdConfig()
    '''
def getAttributeTypeLevel():
    '''    public int getAttributeTypeLevel()
    '''
def getBarcodeAttribute():
    '''    public String getBarcodeAttribute()
    '''
def getBillToAddress():
    '''    public String getBillToAddress()
    '''
def getChangeDateFilter():
    '''    public String getChangeDateFilter()
    '''
def getComponentAttribLoc():
    '''    public long getComponentAttribLoc()
    '''
def getComponentIdConfig():
    '''    public int getComponentIdConfig()
    '''
def getContactTreatement():
    '''    public int getContactTreatement()
    '''
def getFacilityClassification():
    '''    public String getFacilityClassification()
    '''
def getFacilityIdConfig():
    '''    public int getFacilityIdConfig()
    '''
def getFloorIdConfig():
    '''    public int getFloorIdConfig()
    '''
def getGLAccount():
    '''    public String getGLAccount()
    '''
def getIdSeperatorCharacter():
    '''    public String getIdSeperatorCharacter()
    '''
def getInitialAssetStatus():
    '''    public String getInitialAssetStatus()
    '''
def getInitialAssetType():
    '''    public String getInitialAssetType()
    '''
def getInitialJobPlanStatus():
    '''    public String getInitialJobPlanStatus()
    '''
def getInitialLocationStatus():
    '''    public String getInitialLocationStatus()
    '''
def getInitialProductStatus():
    '''    public String getInitialProductStatus()
    '''
def getJobPlanLevel():
    '''    public int getJobPlanLevel()
    '''
def getLevelAttributeName():
    '''    public String getLevelAttributeName()
    '''
def getLogLevel():
    '''    public long getLogLevel()
    '''
def getMergeFacility():
    '''    public String getMergeFacility()
    '''
def getOomniClassAttributeName():
    '''    public String getOomniClassAttributeName()
    '''
def getOperatingLocIdConfig():
    '''    public int getOperatingLocIdConfig()
    '''
def getParserFlags():
    '''    public long getParserFlags()
    '''
def getProjectAddress():
    '''    public String getProjectAddress()
    '''
def getServiceAddress():
    '''    public String getServiceAddress()
    '''
def getShipToAddress():
    '''    public String getShipToAddress()
    '''
def getSpaceIdConfig():
    '''    public int getSpaceIdConfig()
    '''
def getSpaceAttributeName():
    '''    public String getSpaceAttributeName()
    '''
def getSpecificationMapName():
    '''    public String getSpecificationMapName()
    '''
def getSystemNameAttributeName():
    '''    public String getSystemNameAttributeName()
    '''
def getTargetFacility():
    '''    public String getTargetFacility()
    '''
def getUnitTreatment():
    '''    public int getUnitTreatment()
    '''
def getUpdateBehavior():
    '''    public int getUpdateBehavior()
    '''
def getVendorAttribute():
    '''    public String getVendorAttribute()
    '''
def getWarrantyCalcMethod():
    '''    public int getWarrantyCalcMethod()
    '''
def isAssocaiteAttributeTypes():
    '''    public boolean isAssocaiteAttributeTypes()
    '''
def isAutoNumber():
    '''    public boolean isAutoNumber()
    '''
def isConvertGuid():
    '''    public boolean isConvertGuid()
    '''
def isConvertUniqueIds():
    '''    public boolean isConvertUniqueIds()
    '''
def isCopyTypeAttribsToAsset():
    '''    public boolean isCopyTypeAttribsToAsset()
    '''
def isCopyTypeAttribsToItem():
    '''    public boolean isCopyTypeAttribsToItem()
    '''
def isCopyDocsToAsset():
    '''    public boolean isCopyDocsToAsset()
    '''
def isCreateAttributeTypes():
    '''    public boolean isCreateAttributeTypes()
    '''
def isCreateClassifications():
    '''    public boolean isCreateClassifications()
    '''
def isCreateCompanies():
    '''    public boolean isCreateCompanies()
    '''
def isCreateCompanyMasters():
    '''    public boolean isCreateCompanyMasters()
    '''
def isCreateItemMaster():
    '''    public boolean isCreateItemMaster()
    '''
def isCreateMasterPM():
    '''    public boolean isCreateMasterPM()
    '''
def isCreatePM():
    '''    public boolean isCreatePM()
    '''
def isCreateProduct():
    '''    public boolean isCreateProduct()
    '''
def isCreateOpperatingLocation():
    '''    public boolean isCreateOpperatingLocation()
    '''
def isDeleteDocOnCopy():
    '''    public boolean isDeleteDocOnCopy()
    '''
def isDeleteFiles():
    '''    public boolean isDeleteFiles()
    '''
def isDeleteSystemMemebrs():
    '''    public boolean isDeleteSystemMemebrs()
    '''
def isExportFloor():
    '''    public boolean isExportFloor()
    '''
def isExportSpace():
    '''    public boolean isExportSpace()
    '''
def isExportComponent():
    '''    public boolean isExportComponent()
    '''
def isExportType():
    '''    public boolean isExportType()
    '''
def isExportSystem():
    '''    public boolean isExportSystem()
    '''
def isExportZone():
    '''    public boolean isExportZone()
    '''
def isExportAttribute():
    '''    public boolean isExportAttribute()
    '''
def isExportContact():
    '''    public boolean isExportContact()
    '''
def isExportDocument():
    '''    public boolean isExportDocument()
    '''
def isExportJob():
    '''    public boolean isExportJob()
    '''
def isExportResource():
    '''    public boolean isExportResource()
    '''
def isExportSpare():
    '''    public boolean isExportSpare()
    '''
def isExportAssembly():
    '''    public boolean isExportAssembly()
    '''
def isExportNullAttributes():
    '''    public boolean isExportNullAttributes()
    '''
def isMapExtensionCols():
    '''    public boolean isMapExtensionCols()
    '''
def isInferLevels():
    '''    public boolean isInferLevels()
    '''
def isInferOmniClass():
    '''    public boolean isInferOmniClass()
    '''
def isInferSpaces():
    '''    public boolean isInferSpaces()
    '''
def isInferSystems():
    '''    public boolean isInferSystems()
    '''
def isOverwriteAttachments():
    '''    public boolean isOverwriteAttachments()
    '''
def isPersonNameIsEMail():
    '''    public boolean isPersonNameIsEMail()
    '''
def isPopulateSystemMap():
    '''    public boolean isPopulateSystemMap()
    '''
def isPromoteComponents():
    '''    public boolean isPromoteComponents()
    '''
def isPromoteSpaces():
    '''    public boolean isPromoteSpaces()
    '''
def isUpdateCategories():
    '''    public boolean isUpdateCategories()
    '''
def isUpdateSpecs():
    '''    public boolean isUpdateSpecs()
    '''
def isSkipEmptySystems():
    '''    public boolean isSkipEmptySystems()
    '''
def isTypesAreSpecs():
    '''    public boolean isTypesAreSpecs()
    '''
