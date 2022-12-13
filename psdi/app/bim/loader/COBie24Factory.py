def makeOmniClassLogger():
'''public ClassificationOmniClassLogger makeOmniClassLogger(final MboRemote mbo, final long sessionId, final String messageBundleName)
'''
pass
def makeOptions():
'''public ModelLoaderOptions makeOptions(final BIMSessionRemote sessionMbo, final int updateMode)
'''
pass
def makeModelLogger():
'''public ProgressLogger<ItemFACILITY> makeModelLogger(final UserInfo userInfo, final long sessionId, final String messageBundleName)
'''
pass
def makeExportLogger():
'''public ProgressLogger<ItemFACILITY> makeExportLogger(final UserInfo userInfo, final long sessionId, final String messageBundleName)
'''
pass
def makeModelValidator():
'''public ModelValidator makeModelValidator(final BIMProjectRemote projectMbo, final ModelLoaderOptions options, final ProgressLogger<ItemFACILITY> logger)
'''
pass
def makeModelLoader():
'''public ModelLoader makeModelLoader(final BIMProjectRemote projectMbo, final ModelLoaderOptions options, final ProgressLogger<ItemFACILITY> logger, final int sessionType)
'''
pass
def makeModelExporter():
'''public ModelExporter makeModelExporter(final BIMSessionRemote sessionMbo, final String facilityName, final ModelLoaderOptions options, final ProgressLogger<ItemFACILITY> logger)
'''
pass
def makeParser():
'''public BIMProjectParser makeParser(final IdFactory idFactory, final ModelLoaderOptions options, final MessageLogger logger, final Locale locale, final long flags)
'''
pass
def makeAttributeTypeLoader():
'''public LoaderAttributeType makeAttributeTypeLoader(final ModelLoaderBase loader)
'''
pass
def makeContactLoader():
'''public LoaderContact makeContactLoader(final ModelLoaderBase loader)
'''
pass
def makeCompanyLoader():
'''public LoaderCompany makeCompanyLoader(final ModelLoaderBase loader)
'''
pass
def makeFacilityLoader():
'''public LoaderFacility makeFacilityLoader(final ModelLoaderBase loader)
'''
pass
def makeDesignSpecLoader():
'''public LoaderSpec makeDesignSpecLoader(final ModelLoaderBase loader)
'''
pass
def makeProductLoader():
'''public LoaderProduct makeProductLoader(final ModelLoaderBase loader)
'''
pass
def makeToolsLoader():
'''public LoaderTools makeToolsLoader(final ModelLoaderBase loader)
'''
pass
def makeJobLoader():
'''public LoaderJob makeJobLoader(final ModelLoaderBase loader)
'''
pass
def makeFloorLoader():
'''public LoaderFloor makeFloorLoader(final ModelLoaderBase loader)
'''
pass
def makeSpaceLoader():
'''public LoaderSpace makeSpaceLoader(final ModelLoaderBase loader)
'''
pass
def makeComponentLoader():
'''public LoaderComponent makeComponentLoader(final ModelLoaderBase loader)
'''
pass
def makeZoneLoader():
'''public LoaderSystemZone<ItemZONE, ItemSPACE> makeZoneLoader(final ModelLoaderBase loader)
'''
pass
def makeSystemLoader():
'''public LoaderSystemZone<ItemSYSTEM, ItemCOMPONENT> makeSystemLoader(final ModelLoaderBase loader)
'''
pass
def makeAssemblyLoader():
'''public LoaderComponentAssembly makeAssemblyLoader(final ModelLoaderBase loader)
'''
pass
def makeCommissioningLogger():
'''public CommissioningLogger makeCommissioningLogger(final UserInfo userInfo, final long commissionId, final String messageBundleName)
'''
pass
def makeBuildingCommissioner():
'''public BuildingCommissioner makeBuildingCommissioner(final BIMCommissionRemote commissionMbo, final CommissioningLogger logger)
'''
pass
