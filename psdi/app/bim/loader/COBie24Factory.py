def makeOmniClassLogger():
    '''returns ClassificationOmniClassLogger\n\n
    makeOmniClassLogger(final MboRemote mbo, final long sessionId, final String messageBundleName)\n
    '''
def makeOptions():
    '''returns ModelLoaderOptions\n\n
    makeOptions(final BIMSessionRemote sessionMbo, final int updateMode)\n
    '''
def makeModelLogger():
    '''returns ProgressLogger<ItemFACILITY>\n\n
    makeModelLogger(final UserInfo userInfo, final long sessionId, final String messageBundleName)\n
    '''
def makeExportLogger():
    '''returns ProgressLogger<ItemFACILITY>\n\n
    makeExportLogger(final UserInfo userInfo, final long sessionId, final String messageBundleName)\n
    '''
def makeModelValidator():
    '''returns ModelValidator\n\n
    makeModelValidator(final BIMProjectRemote projectMbo, final ModelLoaderOptions options, final ProgressLogger<ItemFACILITY> logger)\n
    '''
def makeModelLoader():
    '''returns ModelLoader\n\n
    makeModelLoader(final BIMProjectRemote projectMbo, final ModelLoaderOptions options, final ProgressLogger<ItemFACILITY> logger, final int sessionType)\n
    '''
def makeModelExporter():
    '''returns ModelExporter\n\n
    makeModelExporter(final BIMSessionRemote sessionMbo, final String facilityName, final ModelLoaderOptions options, final ProgressLogger<ItemFACILITY> logger)\n
    '''
def makeParser():
    '''returns BIMProjectParser\n\n
    makeParser(final IdFactory idFactory, final ModelLoaderOptions options, final MessageLogger logger, final Locale locale, final long flags)\n
    '''
def makeAttributeTypeLoader():
    '''returns LoaderAttributeType\n\n
    makeAttributeTypeLoader(final ModelLoaderBase loader)\n
    '''
def makeContactLoader():
    '''returns LoaderContact\n\n
    makeContactLoader(final ModelLoaderBase loader)\n
    '''
def makeCompanyLoader():
    '''returns LoaderCompany\n\n
    makeCompanyLoader(final ModelLoaderBase loader)\n
    '''
def makeFacilityLoader():
    '''returns LoaderFacility\n\n
    makeFacilityLoader(final ModelLoaderBase loader)\n
    '''
def makeDesignSpecLoader():
    '''returns LoaderSpec\n\n
    makeDesignSpecLoader(final ModelLoaderBase loader)\n
    '''
def makeProductLoader():
    '''returns LoaderProduct\n\n
    makeProductLoader(final ModelLoaderBase loader)\n
    '''
def makeToolsLoader():
    '''returns LoaderTools\n\n
    makeToolsLoader(final ModelLoaderBase loader)\n
    '''
def makeJobLoader():
    '''returns LoaderJob\n\n
    makeJobLoader(final ModelLoaderBase loader)\n
    '''
def makeFloorLoader():
    '''returns LoaderFloor\n\n
    makeFloorLoader(final ModelLoaderBase loader)\n
    '''
def makeSpaceLoader():
    '''returns LoaderSpace\n\n
    makeSpaceLoader(final ModelLoaderBase loader)\n
    '''
def makeComponentLoader():
    '''returns LoaderComponent\n\n
    makeComponentLoader(final ModelLoaderBase loader)\n
    '''
def makeAssemblyLoader():
    '''returns LoaderComponentAssembly\n\n
    makeAssemblyLoader(final ModelLoaderBase loader)\n
    '''
def makeCommissioningLogger():
    '''returns CommissioningLogger\n\n
    makeCommissioningLogger(final UserInfo userInfo, final long commissionId, final String messageBundleName)\n
    '''
def makeBuildingCommissioner():
    '''returns BuildingCommissioner\n\n
    makeBuildingCommissioner(final BIMCommissionRemote commissionMbo, final CommissioningLogger logger)\n
    '''
