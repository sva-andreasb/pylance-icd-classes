def makeOmniClassLogger():
    '''public ClassificationOmniClassLogger makeOmniClassLogger(final MboRemote mbo, final long sessionId, final String messageBundleName)
    '''
def makeOptions():
    '''public ModelLoaderOptions makeOptions(final BIMSessionRemote sessionMbo, final int updateMode)
    '''
def makeModelLogger():
    '''public ProgressLogger<ItemFACILITY> makeModelLogger(final UserInfo userInfo, final long sessionId, final String messageBundleName)
    '''
def makeExportLogger():
    '''public ProgressLogger<ItemFACILITY> makeExportLogger(final UserInfo userInfo, final long sessionId, final String messageBundleName)
    '''
def makeModelValidator():
    '''public ModelValidator makeModelValidator(final BIMProjectRemote projectMbo, final ModelLoaderOptions options, final ProgressLogger<ItemFACILITY> logger)
    '''
def makeModelLoader():
    '''public ModelLoader makeModelLoader(final BIMProjectRemote projectMbo, final ModelLoaderOptions options, final ProgressLogger<ItemFACILITY> logger, final int sessionType)
    '''
def makeModelExporter():
    '''public ModelExporter makeModelExporter(final BIMSessionRemote sessionMbo, final String facilityName, final ModelLoaderOptions options, final ProgressLogger<ItemFACILITY> logger)
    '''
def makeParser():
    '''public BIMProjectParser makeParser(final IdFactory idFactory, final ModelLoaderOptions options, final MessageLogger logger, final Locale locale, final long flags)
    '''
def makeAttributeTypeLoader():
    '''public LoaderAttributeType makeAttributeTypeLoader(final ModelLoaderBase loader)
    '''
def makeContactLoader():
    '''public LoaderContact makeContactLoader(final ModelLoaderBase loader)
    '''
def makeCompanyLoader():
    '''public LoaderCompany makeCompanyLoader(final ModelLoaderBase loader)
    '''
def makeFacilityLoader():
    '''public LoaderFacility makeFacilityLoader(final ModelLoaderBase loader)
    '''
def makeDesignSpecLoader():
    '''public LoaderSpec makeDesignSpecLoader(final ModelLoaderBase loader)
    '''
def makeProductLoader():
    '''public LoaderProduct makeProductLoader(final ModelLoaderBase loader)
    '''
def makeToolsLoader():
    '''public LoaderTools makeToolsLoader(final ModelLoaderBase loader)
    '''
def makeJobLoader():
    '''public LoaderJob makeJobLoader(final ModelLoaderBase loader)
    '''
def makeFloorLoader():
    '''public LoaderFloor makeFloorLoader(final ModelLoaderBase loader)
    '''
def makeSpaceLoader():
    '''public LoaderSpace makeSpaceLoader(final ModelLoaderBase loader)
    '''
def makeComponentLoader():
    '''public LoaderComponent makeComponentLoader(final ModelLoaderBase loader)
    '''
def makeZoneLoader():
    '''public LoaderSystemZone<ItemZONE, ItemSPACE> makeZoneLoader(final ModelLoaderBase loader)
    '''
def makeSystemLoader():
    '''public LoaderSystemZone<ItemSYSTEM, ItemCOMPONENT> makeSystemLoader(final ModelLoaderBase loader)
    '''
def makeAssemblyLoader():
    '''public LoaderComponentAssembly makeAssemblyLoader(final ModelLoaderBase loader)
    '''
def makeCommissioningLogger():
    '''public CommissioningLogger makeCommissioningLogger(final UserInfo userInfo, final long commissionId, final String messageBundleName)
    '''
def makeBuildingCommissioner():
    '''public BuildingCommissioner makeBuildingCommissioner(final BIMCommissionRemote commissionMbo, final CommissioningLogger logger)
    '''
