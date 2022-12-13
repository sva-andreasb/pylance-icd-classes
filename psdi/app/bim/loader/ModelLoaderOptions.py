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
'''public ModelLoaderOptions(final BIMSessionRemote sessionMbo, final int updateMode)
'''
pass
def filtersNames():
'''public Iterator<String> filtersNames()
'''
pass
def getAttributeMapName():
'''public String getAttributeMapName()
'''
pass
def getAttribTypeIdConfig():
'''public int getAttribTypeIdConfig()
'''
pass
def getAttributeTypeLevel():
'''public int getAttributeTypeLevel()
'''
pass
def getBarcodeAttribute():
'''public String getBarcodeAttribute()
'''
pass
def getBillToAddress():
'''public String getBillToAddress()
'''
pass
def getChangeDateFilter():
'''public String getChangeDateFilter()
'''
pass
def getComponentAttribLoc():
'''public long getComponentAttribLoc()
'''
pass
def getComponentIdConfig():
'''public int getComponentIdConfig()
'''
pass
def getContactTreatement():
'''public int getContactTreatement()
'''
pass
def getFacilityClassification():
'''public String getFacilityClassification()
'''
pass
def getFacilityIdConfig():
'''public int getFacilityIdConfig()
'''
pass
def getFloorIdConfig():
'''public int getFloorIdConfig()
'''
pass
def getGLAccount():
'''public String getGLAccount()
'''
pass
def getIdSeperatorCharacter():
'''public String getIdSeperatorCharacter()
'''
pass
def getInitialAssetStatus():
'''public String getInitialAssetStatus()
'''
pass
def getInitialAssetType():
'''public String getInitialAssetType()
'''
pass
def getInitialJobPlanStatus():
'''public String getInitialJobPlanStatus()
'''
pass
def getInitialLocationStatus():
'''public String getInitialLocationStatus()
'''
pass
def getInitialProductStatus():
'''public String getInitialProductStatus()
'''
pass
def getJobPlanLevel():
'''public int getJobPlanLevel()
'''
pass
def getLevelAttributeName():
'''public String getLevelAttributeName()
'''
pass
def getLogLevel():
'''public long getLogLevel()
'''
pass
def getMergeFacility():
'''public String getMergeFacility()
'''
pass
def getOomniClassAttributeName():
'''public String getOomniClassAttributeName()
'''
pass
def getOperatingLocIdConfig():
'''public int getOperatingLocIdConfig()
'''
pass
def getParserFlags():
'''public long getParserFlags()
'''
pass
def getProjectAddress():
'''public String getProjectAddress()
'''
pass
def getServiceAddress():
'''public String getServiceAddress()
'''
pass
def getShipToAddress():
'''public String getShipToAddress()
'''
pass
def getSpaceIdConfig():
'''public int getSpaceIdConfig()
'''
pass
def getSpaceAttributeName():
'''public String getSpaceAttributeName()
'''
pass
def getSpecificationMapName():
'''public String getSpecificationMapName()
'''
pass
def getSystemNameAttributeName():
'''public String getSystemNameAttributeName()
'''
pass
def getTargetFacility():
'''public String getTargetFacility()
'''
pass
def getUnitTreatment():
'''public int getUnitTreatment()
'''
pass
def getUpdateBehavior():
'''public int getUpdateBehavior()
'''
pass
def getVendorAttribute():
'''public String getVendorAttribute()
'''
pass
def getWarrantyCalcMethod():
'''public int getWarrantyCalcMethod()
'''
pass
def isAssocaiteAttributeTypes():
'''public boolean isAssocaiteAttributeTypes()
'''
pass
def isAutoNumber():
'''public boolean isAutoNumber()
'''
pass
def isConvertGuid():
'''public boolean isConvertGuid()
'''
pass
def isConvertUniqueIds():
'''public boolean isConvertUniqueIds()
'''
pass
def isCopyTypeAttribsToAsset():
'''public boolean isCopyTypeAttribsToAsset()
'''
pass
def isCopyTypeAttribsToItem():
'''public boolean isCopyTypeAttribsToItem()
'''
pass
def isCopyDocsToAsset():
'''public boolean isCopyDocsToAsset()
'''
pass
def isCreateAttributeTypes():
'''public boolean isCreateAttributeTypes()
'''
pass
def isCreateClassifications():
'''public boolean isCreateClassifications()
'''
pass
def isCreateCompanies():
'''public boolean isCreateCompanies()
'''
pass
def isCreateCompanyMasters():
'''public boolean isCreateCompanyMasters()
'''
pass
def isCreateItemMaster():
'''public boolean isCreateItemMaster()
'''
pass
def isCreateMasterPM():
'''public boolean isCreateMasterPM()
'''
pass
def isCreatePM():
'''public boolean isCreatePM()
'''
pass
def isCreateProduct():
'''public boolean isCreateProduct()
'''
pass
def isCreateOpperatingLocation():
'''public boolean isCreateOpperatingLocation()
'''
pass
def isDeleteDocOnCopy():
'''public boolean isDeleteDocOnCopy()
'''
pass
def isDeleteFiles():
'''public boolean isDeleteFiles()
'''
pass
def isDeleteSystemMemebrs():
'''public boolean isDeleteSystemMemebrs()
'''
pass
def isExportFloor():
'''public boolean isExportFloor()
'''
pass
def isExportSpace():
'''public boolean isExportSpace()
'''
pass
def isExportComponent():
'''public boolean isExportComponent()
'''
pass
def isExportType():
'''public boolean isExportType()
'''
pass
def isExportSystem():
'''public boolean isExportSystem()
'''
pass
def isExportZone():
'''public boolean isExportZone()
'''
pass
def isExportAttribute():
'''public boolean isExportAttribute()
'''
pass
def isExportContact():
'''public boolean isExportContact()
'''
pass
def isExportDocument():
'''public boolean isExportDocument()
'''
pass
def isExportJob():
'''public boolean isExportJob()
'''
pass
def isExportResource():
'''public boolean isExportResource()
'''
pass
def isExportSpare():
'''public boolean isExportSpare()
'''
pass
def isExportAssembly():
'''public boolean isExportAssembly()
'''
pass
def isExportNullAttributes():
'''public boolean isExportNullAttributes()
'''
pass
def isMapExtensionCols():
'''public boolean isMapExtensionCols()
'''
pass
def isInferLevels():
'''public boolean isInferLevels()
'''
pass
def isInferOmniClass():
'''public boolean isInferOmniClass()
'''
pass
def isInferSpaces():
'''public boolean isInferSpaces()
'''
pass
def isInferSystems():
'''public boolean isInferSystems()
'''
pass
def isOverwriteAttachments():
'''public boolean isOverwriteAttachments()
'''
pass
def isPersonNameIsEMail():
'''public boolean isPersonNameIsEMail()
'''
pass
def isPopulateSystemMap():
'''public boolean isPopulateSystemMap()
'''
pass
def isPromoteComponents():
'''public boolean isPromoteComponents()
'''
pass
def isPromoteSpaces():
'''public boolean isPromoteSpaces()
'''
pass
def isUpdateCategories():
'''public boolean isUpdateCategories()
'''
pass
def isUpdateSpecs():
'''public boolean isUpdateSpecs()
'''
pass
def isSkipEmptySystems():
'''public boolean isSkipEmptySystems()
'''
pass
def isTypesAreSpecs():
'''public boolean isTypesAreSpecs()
'''
pass
