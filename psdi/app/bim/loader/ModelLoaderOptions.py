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
def ():
    '''returns ModelLoaderOptions\n\n
    (final BIMSessionRemote sessionMbo, final int updateMode)\n
    '''
def filtersNames():
    '''returns Iterator<String>\n\n
    filtersNames()\n
    '''
def getAttributeMapName():
    '''returns String\n\n
    getAttributeMapName()\n
    '''
def getAttribTypeIdConfig():
    '''returns int\n\n
    getAttribTypeIdConfig()\n
    '''
def getAttributeTypeLevel():
    '''returns int\n\n
    getAttributeTypeLevel()\n
    '''
def getBarcodeAttribute():
    '''returns String\n\n
    getBarcodeAttribute()\n
    '''
def getBillToAddress():
    '''returns String\n\n
    getBillToAddress()\n
    '''
def getChangeDateFilter():
    '''returns String\n\n
    getChangeDateFilter()\n
    '''
def getComponentAttribLoc():
    '''returns long\n\n
    getComponentAttribLoc()\n
    '''
def getComponentIdConfig():
    '''returns int\n\n
    getComponentIdConfig()\n
    '''
def getContactTreatement():
    '''returns int\n\n
    getContactTreatement()\n
    '''
def getFacilityClassification():
    '''returns String\n\n
    getFacilityClassification()\n
    '''
def getFacilityIdConfig():
    '''returns int\n\n
    getFacilityIdConfig()\n
    '''
def getFloorIdConfig():
    '''returns int\n\n
    getFloorIdConfig()\n
    '''
def getGLAccount():
    '''returns String\n\n
    getGLAccount()\n
    '''
def getIdSeperatorCharacter():
    '''returns String\n\n
    getIdSeperatorCharacter()\n
    '''
def getInitialAssetStatus():
    '''returns String\n\n
    getInitialAssetStatus()\n
    '''
def getInitialAssetType():
    '''returns String\n\n
    getInitialAssetType()\n
    '''
def getInitialJobPlanStatus():
    '''returns String\n\n
    getInitialJobPlanStatus()\n
    '''
def getInitialLocationStatus():
    '''returns String\n\n
    getInitialLocationStatus()\n
    '''
def getInitialProductStatus():
    '''returns String\n\n
    getInitialProductStatus()\n
    '''
def getJobPlanLevel():
    '''returns int\n\n
    getJobPlanLevel()\n
    '''
def getLevelAttributeName():
    '''returns String\n\n
    getLevelAttributeName()\n
    '''
def getLogLevel():
    '''returns long\n\n
    getLogLevel()\n
    '''
def getMergeFacility():
    '''returns String\n\n
    getMergeFacility()\n
    '''
def getOomniClassAttributeName():
    '''returns String\n\n
    getOomniClassAttributeName()\n
    '''
def getOperatingLocIdConfig():
    '''returns int\n\n
    getOperatingLocIdConfig()\n
    '''
def getParserFlags():
    '''returns long\n\n
    getParserFlags()\n
    '''
def getProjectAddress():
    '''returns String\n\n
    getProjectAddress()\n
    '''
def getServiceAddress():
    '''returns String\n\n
    getServiceAddress()\n
    '''
def getShipToAddress():
    '''returns String\n\n
    getShipToAddress()\n
    '''
def getSpaceIdConfig():
    '''returns int\n\n
    getSpaceIdConfig()\n
    '''
def getSpaceAttributeName():
    '''returns String\n\n
    getSpaceAttributeName()\n
    '''
def getSpecificationMapName():
    '''returns String\n\n
    getSpecificationMapName()\n
    '''
def getSystemNameAttributeName():
    '''returns String\n\n
    getSystemNameAttributeName()\n
    '''
def getTargetFacility():
    '''returns String\n\n
    getTargetFacility()\n
    '''
def getUnitTreatment():
    '''returns int\n\n
    getUnitTreatment()\n
    '''
def getUpdateBehavior():
    '''returns int\n\n
    getUpdateBehavior()\n
    '''
def getVendorAttribute():
    '''returns String\n\n
    getVendorAttribute()\n
    '''
def getWarrantyCalcMethod():
    '''returns int\n\n
    getWarrantyCalcMethod()\n
    '''
def isAssocaiteAttributeTypes():
    '''returns boolean\n\n
    isAssocaiteAttributeTypes()\n
    '''
def isAutoNumber():
    '''returns boolean\n\n
    isAutoNumber()\n
    '''
def isConvertGuid():
    '''returns boolean\n\n
    isConvertGuid()\n
    '''
def isConvertUniqueIds():
    '''returns boolean\n\n
    isConvertUniqueIds()\n
    '''
def isCopyTypeAttribsToAsset():
    '''returns boolean\n\n
    isCopyTypeAttribsToAsset()\n
    '''
def isCopyTypeAttribsToItem():
    '''returns boolean\n\n
    isCopyTypeAttribsToItem()\n
    '''
def isCopyDocsToAsset():
    '''returns boolean\n\n
    isCopyDocsToAsset()\n
    '''
def isCreateAttributeTypes():
    '''returns boolean\n\n
    isCreateAttributeTypes()\n
    '''
def isCreateClassifications():
    '''returns boolean\n\n
    isCreateClassifications()\n
    '''
def isCreateCompanies():
    '''returns boolean\n\n
    isCreateCompanies()\n
    '''
def isCreateCompanyMasters():
    '''returns boolean\n\n
    isCreateCompanyMasters()\n
    '''
def isCreateItemMaster():
    '''returns boolean\n\n
    isCreateItemMaster()\n
    '''
def isCreateMasterPM():
    '''returns boolean\n\n
    isCreateMasterPM()\n
    '''
def isCreatePM():
    '''returns boolean\n\n
    isCreatePM()\n
    '''
def isCreateProduct():
    '''returns boolean\n\n
    isCreateProduct()\n
    '''
def isCreateOpperatingLocation():
    '''returns boolean\n\n
    isCreateOpperatingLocation()\n
    '''
def isDeleteDocOnCopy():
    '''returns boolean\n\n
    isDeleteDocOnCopy()\n
    '''
def isDeleteFiles():
    '''returns boolean\n\n
    isDeleteFiles()\n
    '''
def isDeleteSystemMemebrs():
    '''returns boolean\n\n
    isDeleteSystemMemebrs()\n
    '''
def isExportFloor():
    '''returns boolean\n\n
    isExportFloor()\n
    '''
def isExportSpace():
    '''returns boolean\n\n
    isExportSpace()\n
    '''
def isExportComponent():
    '''returns boolean\n\n
    isExportComponent()\n
    '''
def isExportType():
    '''returns boolean\n\n
    isExportType()\n
    '''
def isExportSystem():
    '''returns boolean\n\n
    isExportSystem()\n
    '''
def isExportZone():
    '''returns boolean\n\n
    isExportZone()\n
    '''
def isExportAttribute():
    '''returns boolean\n\n
    isExportAttribute()\n
    '''
def isExportContact():
    '''returns boolean\n\n
    isExportContact()\n
    '''
def isExportDocument():
    '''returns boolean\n\n
    isExportDocument()\n
    '''
def isExportJob():
    '''returns boolean\n\n
    isExportJob()\n
    '''
def isExportResource():
    '''returns boolean\n\n
    isExportResource()\n
    '''
def isExportSpare():
    '''returns boolean\n\n
    isExportSpare()\n
    '''
def isExportAssembly():
    '''returns boolean\n\n
    isExportAssembly()\n
    '''
def isExportNullAttributes():
    '''returns boolean\n\n
    isExportNullAttributes()\n
    '''
def isMapExtensionCols():
    '''returns boolean\n\n
    isMapExtensionCols()\n
    '''
def isInferLevels():
    '''returns boolean\n\n
    isInferLevels()\n
    '''
def isInferOmniClass():
    '''returns boolean\n\n
    isInferOmniClass()\n
    '''
def isInferSpaces():
    '''returns boolean\n\n
    isInferSpaces()\n
    '''
def isInferSystems():
    '''returns boolean\n\n
    isInferSystems()\n
    '''
def isOverwriteAttachments():
    '''returns boolean\n\n
    isOverwriteAttachments()\n
    '''
def isPersonNameIsEMail():
    '''returns boolean\n\n
    isPersonNameIsEMail()\n
    '''
def isPopulateSystemMap():
    '''returns boolean\n\n
    isPopulateSystemMap()\n
    '''
def isPromoteComponents():
    '''returns boolean\n\n
    isPromoteComponents()\n
    '''
def isPromoteSpaces():
    '''returns boolean\n\n
    isPromoteSpaces()\n
    '''
def isUpdateCategories():
    '''returns boolean\n\n
    isUpdateCategories()\n
    '''
def isUpdateSpecs():
    '''returns boolean\n\n
    isUpdateSpecs()\n
    '''
def isSkipEmptySystems():
    '''returns boolean\n\n
    isSkipEmptySystems()\n
    '''
def isTypesAreSpecs():
    '''returns boolean\n\n
    isTypesAreSpecs()\n
    '''
