def ():
    '''returns ConfigurationFolder\n\n
    ()\n
    (final AncestorInfoArrayProp ancestors, final DateTimeProp creationTime, final TokenProp defaultName, final BooleanProp disabled, final BooleanProp hasChildren, final DateTimeProp modificationTime, final MultilingualTokenProp name, final ClassEnumProp objectClass, final BaseClassArrayProp owner, final BaseClassArrayProp parent, final NmtokenArrayProp permissions, final PolicyArrayProp policies, final NonNegativeIntegerProp position, final StringProp searchPath, final GuidProp storeID, final StringProp tenantID, final NmtokenProp usage, final PositiveIntegerProp version, final StringProp defaultDescription, final StringProp defaultScreenTip, final MultilingualStringProp description, final NonNegativeIntegerProp displaySequence, final BooleanProp hidden, final AnyURIProp iconURI, final MultilingualStringProp screenTip, final BooleanProp shown, final BooleanProp viewed, final IntProp aasAffineConnections, final AuditLevelEnumProp aasAuditLevel, final IntProp aasExecutionTimeLimit, final IntProp aasMaximumProcesses, final IntProp aasNonAffineConnections, final IntProp aasPeakAffineConnections, final IntProp aasPeakMaximumProcesses, final IntProp aasPeakNonAffineConnections, final AnyTypeProp advancedSettings, final DurationProp ansAnnotationLifetime, final AuditLevelEnumProp ansAuditLevel, final AuditLevelEnumProp asAuditLevel, final IntProp asConnections, final IntProp asMaximumEMailAttachmentSize, final IntProp asPeakConnections, final IntProp brsAffineConnections, final AuditLevelEnumProp brsAuditLevel, final BooleanProp brsAuditNativeQuery, final IntProp brsChartHotspotLimit, final DateTimeProp brsDataSourceChange, final IntProp brsExecutionTimeLimit, final IntProp brsMaximumEMailAttachmentSize, final NonNegativeIntegerProp brsMaximumProcesses, final IntProp brsNonAffineConnections, final PdfCharacterEncodingEnumProp brsPDFCharacterEncoding, final IntProp brsPDFCompressionLevel, final PdfCompressionTypeEnumProp brsPDFCompressionType, final PdfFontEmbeddingEnumProp brsPDFEmbedFonts, final IntProp brsPeakAffineConnections, final IntProp brsPeakMaximumProcesses, final IntProp brsPeakNonAffineConnections, final FloatProp capacity, final AuditLevelEnumProp cmcsAuditLevel, final IntProp cmcsHeapLimit, final AuditLevelEnumProp cmsAuditLevel, final IntProp cmsConnections, final IntProp cmsPeakConnections, final AuditLevelEnumProp dasAuditLevel, final IntProp dimsAffineConnections, final AuditLevelEnumProp dimsAuditLevel, final IntProp dimsExecutionTimeLimit, final IntProp dimsMaximumProcesses, final IntProp dimsNonAffineConnections, final IntProp dimsPeakAffineConnections, final IntProp dimsPeakMaximumProcesses, final IntProp dimsPeakNonAffineConnections, final IntProp dimsQueueLimit, final AuditLevelEnumProp disAuditLevel, final IntProp disConnections, final AuditLevelEnumProp dispatcherAuditLevel, final IntProp disPeakConnections, final IntProp dmsAffineConnections, final AuditLevelEnumProp dmsAuditLevel, final IntProp dmsConnections, final IntProp dmsExecutionTimeLimit, final IntProp dmsMaximumProcesses, final IntProp dmsNonAffineConnections, final IntProp dmsPeakAffineConnections, final IntProp dmsPeakMaximumProcesses, final IntProp dmsPeakNonAffineConnections, final IntProp dmsQueueLimit, final AuditLevelEnumProp dsAuditLevel, final IntProp dsCompressAttachmentLimit, final IntProp dsConnections, final IntProp dsMaximumEMailSize, final IntProp dsPeakConnections, final AuditLevelEnumProp emsAuditLevel, final AuditLevelEnumProp evsAuditLevel, final AuditLevelEnumProp gsAuditLevel, final IntProp gsExecutionTimeLimit, final IntProp gsNonAffineConnections, final IntProp gsPeakNonAffineConnections, final IntProp gsQueueLimit, final AuditLevelEnumProp htsAuditLevel, final DurationProp htsCompletedTaskLifetime, final AuditLevelEnumProp idsAuditLevel, final IntProp idsConnections, final IntProp idsPeakConnections, final AuditLevelEnumProp idVizAuditLevel, final AuditLevelEnumProp issAuditLevel, final IntProp issConnections, final IntProp issPeakConnections, final AuditLevelEnumProp iusAuditLevel, final IntProp iusConnections, final IntProp iusPeakConnections, final AuditLevelEnumProp jsAuditLevel, final IntProp jsConnections, final IntProp jsPeakConnections, final LoadBalancingModeEnumProp loadBalancingMode, final AuditLevelEnumProp mbsAuditLevel, final IntProp mbsConnections, final IntProp mbsPeakConnections, final IntProp mdsAffineConnections, final AuditLevelEnumProp mdsAuditLevel, final IntProp mdsExecutionTimeLimit, final IntProp mdsMaximumProcesses, final IntProp mdsNonAffineConnections, final IntProp mdsPeakAffineConnections, final IntProp mdsPeakMaximumProcesses, final IntProp mdsPeakNonAffineConnections, final IntProp mdsQueueLimit, final AuditLevelEnumProp misAuditLevel, final IntProp misConnections, final IntProp misPeakConnections, final AuditLevelEnumProp mmsAuditLevel, final IntProp mmsConnections, final IntProp mmsPeakConnections, final AuditLevelEnumProp msAuditLevel, final IntProp nonPeakDemandBeginHour, final AuditLevelEnumProp pacsAuditLevel, final IntProp pacsConnections, final IntProp pacsPeakConnections, final AuditLevelEnumProp pdsAuditLevel, final IntProp pdsConnections, final IntProp pdsEListAccessCacheLimit, final IntProp pdsMaximumProcesses, final IntProp pdsPeakConnections, final IntProp pdsPeakMaximumProcesses, final BooleanProp pdsShowCellAnnotations, final IntProp peakDemandBeginHour, final IntProp ppsAffineConnections, final AuditLevelEnumProp ppsAuditLevel, final IntProp ppsExecutionTimeLimit, final IntProp ppsMaximumEMailAttachmentSize, final IntProp ppsNonAffineConnections, final IntProp ppsPeakAffineConnections, final IntProp ppsPeakNonAffineConnections, final IntProp ppsQueueLimit, final AuditLevelEnumProp prsAuditLevel, final IntProp prsConnections, final IntProp prsPeakConnections, final AuditLevelEnumProp psAuditLevel, final AuditLevelEnumProp ptsAuditLevel, final IntProp ptsConnections, final IntProp ptsPeakConnections, final StringProp qsAdditionalJVMArguments, final AuditLevelEnumProp qsAuditLevel, final BooleanProp qsDiagnosticsEnabled, final BooleanProp qsDisableQueryPlanCache, final BooleanProp qsDisableVerboseGCLogging, final BooleanProp qsDumpModelToFile, final AnyURIProp qsGCPolicy, final BooleanProp qsGenerateCommentsInNativeSQL, final IntProp qsIdleConnectionTimeout, final IntProp qsInitialJVMHeapSize, final IntProp qsInitialJVMNurserySize, final IntProp qsJVMHeapSizeLimit, final IntProp qsJVMNurserySizeLimit, final BooleanProp qsManualCubeStart, final BooleanProp qsMetricsEnabled, final IntProp qsMultiDimensionalQuerySizeLimit, final BooleanProp qsQueryExecutionTrace, final BooleanProp qsQueryPlanningTrace, final IntProp qsResultSetCacheQueryTimeThreshold, final IntProp qsROLAPCubeAdministrationCommandTimeout, final BaseROLAPCubeConfigurationArrayProp qsROLAPCubeConfigurations, final TokenProp qsROLAPMemberCacheAliasRoot, final IntProp qsVerboseGCLogLimit, final AuditLevelEnumProp rdsAuditLevel, final GatewayMappingArrayProp rdsGatewayMappings, final IntProp rdsMaximumDataSize, final AuditLevelEnumProp reposAuditLevel, final PositiveIntegerProp reposCacheObjTTL, final PositiveIntegerProp reposNumObjDisk, final PositiveIntegerProp reposNumObjMem, final IntProp rmdsAffineConnections, final AuditLevelEnumProp rmdsAuditLevel, final IntProp rmdsConnections, final IntProp rmdsExecutionTimeLimit, final IntProp rmdsNonAffineConnections, final IntProp rmdsPeakAffineConnections, final IntProp rmdsPeakConnections, final IntProp rmdsPeakNonAffineConnections, final IntProp rsAffineConnections, final AuditLevelEnumProp rsAuditLevel, final BooleanProp rsAuditNativeQuery, final IntProp rsChartHotspotLimit, final DateTimeProp rsDataSourceChange, final IntProp rsExecutionTimeLimit, final IntProp rsMaximumEMailAttachmentSize, final NonNegativeIntegerProp rsMaximumProcesses, final IntProp rsNonAffineConnections, final PdfCharacterEncodingEnumProp rsPDFCharacterEncoding, final IntProp rsPDFCompressionLevel, final PdfCompressionTypeEnumProp rsPDFCompressionType, final PdfFontEmbeddingEnumProp rsPDFEmbedFonts, final IntProp rsPeakAffineConnections, final IntProp rsPeakMaximumProcesses, final IntProp rsPeakNonAffineConnections, final PositiveIntegerProp rsQueueLimit, final AuditLevelEnumProp saCAMAuditLevel, final StringProp serverGroup, final AuditLevelEnumProp ssAuditLevel)\n
    '''
def getAasAffineConnections():
    '''returns IntProp\n\n
    getAasAffineConnections()\n
    '''
def setAasAffineConnections():
    '''returns None\n\n
    setAasAffineConnections(final IntProp aasAffineConnections)\n
    '''
def getAasAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getAasAuditLevel()\n
    '''
def setAasAuditLevel():
    '''returns None\n\n
    setAasAuditLevel(final AuditLevelEnumProp aasAuditLevel)\n
    '''
def getAasExecutionTimeLimit():
    '''returns IntProp\n\n
    getAasExecutionTimeLimit()\n
    '''
def setAasExecutionTimeLimit():
    '''returns None\n\n
    setAasExecutionTimeLimit(final IntProp aasExecutionTimeLimit)\n
    '''
def getAasMaximumProcesses():
    '''returns IntProp\n\n
    getAasMaximumProcesses()\n
    '''
def setAasMaximumProcesses():
    '''returns None\n\n
    setAasMaximumProcesses(final IntProp aasMaximumProcesses)\n
    '''
def getAasNonAffineConnections():
    '''returns IntProp\n\n
    getAasNonAffineConnections()\n
    '''
def setAasNonAffineConnections():
    '''returns None\n\n
    setAasNonAffineConnections(final IntProp aasNonAffineConnections)\n
    '''
def getAasPeakAffineConnections():
    '''returns IntProp\n\n
    getAasPeakAffineConnections()\n
    '''
def setAasPeakAffineConnections():
    '''returns None\n\n
    setAasPeakAffineConnections(final IntProp aasPeakAffineConnections)\n
    '''
def getAasPeakMaximumProcesses():
    '''returns IntProp\n\n
    getAasPeakMaximumProcesses()\n
    '''
def setAasPeakMaximumProcesses():
    '''returns None\n\n
    setAasPeakMaximumProcesses(final IntProp aasPeakMaximumProcesses)\n
    '''
def getAasPeakNonAffineConnections():
    '''returns IntProp\n\n
    getAasPeakNonAffineConnections()\n
    '''
def setAasPeakNonAffineConnections():
    '''returns None\n\n
    setAasPeakNonAffineConnections(final IntProp aasPeakNonAffineConnections)\n
    '''
def getAdvancedSettings():
    '''returns AnyTypeProp\n\n
    getAdvancedSettings()\n
    '''
def setAdvancedSettings():
    '''returns None\n\n
    setAdvancedSettings(final AnyTypeProp advancedSettings)\n
    '''
def getAnsAnnotationLifetime():
    '''returns DurationProp\n\n
    getAnsAnnotationLifetime()\n
    '''
def setAnsAnnotationLifetime():
    '''returns None\n\n
    setAnsAnnotationLifetime(final DurationProp ansAnnotationLifetime)\n
    '''
def getAnsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getAnsAuditLevel()\n
    '''
def setAnsAuditLevel():
    '''returns None\n\n
    setAnsAuditLevel(final AuditLevelEnumProp ansAuditLevel)\n
    '''
def getAsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getAsAuditLevel()\n
    '''
def setAsAuditLevel():
    '''returns None\n\n
    setAsAuditLevel(final AuditLevelEnumProp asAuditLevel)\n
    '''
def getAsConnections():
    '''returns IntProp\n\n
    getAsConnections()\n
    '''
def setAsConnections():
    '''returns None\n\n
    setAsConnections(final IntProp asConnections)\n
    '''
def getAsMaximumEMailAttachmentSize():
    '''returns IntProp\n\n
    getAsMaximumEMailAttachmentSize()\n
    '''
def setAsMaximumEMailAttachmentSize():
    '''returns None\n\n
    setAsMaximumEMailAttachmentSize(final IntProp asMaximumEMailAttachmentSize)\n
    '''
def getAsPeakConnections():
    '''returns IntProp\n\n
    getAsPeakConnections()\n
    '''
def setAsPeakConnections():
    '''returns None\n\n
    setAsPeakConnections(final IntProp asPeakConnections)\n
    '''
def getBrsAffineConnections():
    '''returns IntProp\n\n
    getBrsAffineConnections()\n
    '''
def setBrsAffineConnections():
    '''returns None\n\n
    setBrsAffineConnections(final IntProp brsAffineConnections)\n
    '''
def getBrsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getBrsAuditLevel()\n
    '''
def setBrsAuditLevel():
    '''returns None\n\n
    setBrsAuditLevel(final AuditLevelEnumProp brsAuditLevel)\n
    '''
def getBrsAuditNativeQuery():
    '''returns BooleanProp\n\n
    getBrsAuditNativeQuery()\n
    '''
def setBrsAuditNativeQuery():
    '''returns None\n\n
    setBrsAuditNativeQuery(final BooleanProp brsAuditNativeQuery)\n
    '''
def getBrsChartHotspotLimit():
    '''returns IntProp\n\n
    getBrsChartHotspotLimit()\n
    '''
def setBrsChartHotspotLimit():
    '''returns None\n\n
    setBrsChartHotspotLimit(final IntProp brsChartHotspotLimit)\n
    '''
def getBrsDataSourceChange():
    '''returns DateTimeProp\n\n
    getBrsDataSourceChange()\n
    '''
def setBrsDataSourceChange():
    '''returns None\n\n
    setBrsDataSourceChange(final DateTimeProp brsDataSourceChange)\n
    '''
def getBrsExecutionTimeLimit():
    '''returns IntProp\n\n
    getBrsExecutionTimeLimit()\n
    '''
def setBrsExecutionTimeLimit():
    '''returns None\n\n
    setBrsExecutionTimeLimit(final IntProp brsExecutionTimeLimit)\n
    '''
def getBrsMaximumEMailAttachmentSize():
    '''returns IntProp\n\n
    getBrsMaximumEMailAttachmentSize()\n
    '''
def setBrsMaximumEMailAttachmentSize():
    '''returns None\n\n
    setBrsMaximumEMailAttachmentSize(final IntProp brsMaximumEMailAttachmentSize)\n
    '''
def getBrsMaximumProcesses():
    '''returns NonNegativeIntegerProp\n\n
    getBrsMaximumProcesses()\n
    '''
def setBrsMaximumProcesses():
    '''returns None\n\n
    setBrsMaximumProcesses(final NonNegativeIntegerProp brsMaximumProcesses)\n
    '''
def getBrsNonAffineConnections():
    '''returns IntProp\n\n
    getBrsNonAffineConnections()\n
    '''
def setBrsNonAffineConnections():
    '''returns None\n\n
    setBrsNonAffineConnections(final IntProp brsNonAffineConnections)\n
    '''
def getBrsPDFCharacterEncoding():
    '''returns PdfCharacterEncodingEnumProp\n\n
    getBrsPDFCharacterEncoding()\n
    '''
def setBrsPDFCharacterEncoding():
    '''returns None\n\n
    setBrsPDFCharacterEncoding(final PdfCharacterEncodingEnumProp brsPDFCharacterEncoding)\n
    '''
def getBrsPDFCompressionLevel():
    '''returns IntProp\n\n
    getBrsPDFCompressionLevel()\n
    '''
def setBrsPDFCompressionLevel():
    '''returns None\n\n
    setBrsPDFCompressionLevel(final IntProp brsPDFCompressionLevel)\n
    '''
def getBrsPDFCompressionType():
    '''returns PdfCompressionTypeEnumProp\n\n
    getBrsPDFCompressionType()\n
    '''
def setBrsPDFCompressionType():
    '''returns None\n\n
    setBrsPDFCompressionType(final PdfCompressionTypeEnumProp brsPDFCompressionType)\n
    '''
def getBrsPDFEmbedFonts():
    '''returns PdfFontEmbeddingEnumProp\n\n
    getBrsPDFEmbedFonts()\n
    '''
def setBrsPDFEmbedFonts():
    '''returns None\n\n
    setBrsPDFEmbedFonts(final PdfFontEmbeddingEnumProp brsPDFEmbedFonts)\n
    '''
def getBrsPeakAffineConnections():
    '''returns IntProp\n\n
    getBrsPeakAffineConnections()\n
    '''
def setBrsPeakAffineConnections():
    '''returns None\n\n
    setBrsPeakAffineConnections(final IntProp brsPeakAffineConnections)\n
    '''
def getBrsPeakMaximumProcesses():
    '''returns IntProp\n\n
    getBrsPeakMaximumProcesses()\n
    '''
def setBrsPeakMaximumProcesses():
    '''returns None\n\n
    setBrsPeakMaximumProcesses(final IntProp brsPeakMaximumProcesses)\n
    '''
def getBrsPeakNonAffineConnections():
    '''returns IntProp\n\n
    getBrsPeakNonAffineConnections()\n
    '''
def setBrsPeakNonAffineConnections():
    '''returns None\n\n
    setBrsPeakNonAffineConnections(final IntProp brsPeakNonAffineConnections)\n
    '''
def getCapacity():
    '''returns FloatProp\n\n
    getCapacity()\n
    '''
def setCapacity():
    '''returns None\n\n
    setCapacity(final FloatProp capacity)\n
    '''
def getCmcsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getCmcsAuditLevel()\n
    '''
def setCmcsAuditLevel():
    '''returns None\n\n
    setCmcsAuditLevel(final AuditLevelEnumProp cmcsAuditLevel)\n
    '''
def getCmcsHeapLimit():
    '''returns IntProp\n\n
    getCmcsHeapLimit()\n
    '''
def setCmcsHeapLimit():
    '''returns None\n\n
    setCmcsHeapLimit(final IntProp cmcsHeapLimit)\n
    '''
def getCmsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getCmsAuditLevel()\n
    '''
def setCmsAuditLevel():
    '''returns None\n\n
    setCmsAuditLevel(final AuditLevelEnumProp cmsAuditLevel)\n
    '''
def getCmsConnections():
    '''returns IntProp\n\n
    getCmsConnections()\n
    '''
def setCmsConnections():
    '''returns None\n\n
    setCmsConnections(final IntProp cmsConnections)\n
    '''
def getCmsPeakConnections():
    '''returns IntProp\n\n
    getCmsPeakConnections()\n
    '''
def setCmsPeakConnections():
    '''returns None\n\n
    setCmsPeakConnections(final IntProp cmsPeakConnections)\n
    '''
def getDasAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getDasAuditLevel()\n
    '''
def setDasAuditLevel():
    '''returns None\n\n
    setDasAuditLevel(final AuditLevelEnumProp dasAuditLevel)\n
    '''
def getDimsAffineConnections():
    '''returns IntProp\n\n
    getDimsAffineConnections()\n
    '''
def setDimsAffineConnections():
    '''returns None\n\n
    setDimsAffineConnections(final IntProp dimsAffineConnections)\n
    '''
def getDimsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getDimsAuditLevel()\n
    '''
def setDimsAuditLevel():
    '''returns None\n\n
    setDimsAuditLevel(final AuditLevelEnumProp dimsAuditLevel)\n
    '''
def getDimsExecutionTimeLimit():
    '''returns IntProp\n\n
    getDimsExecutionTimeLimit()\n
    '''
def setDimsExecutionTimeLimit():
    '''returns None\n\n
    setDimsExecutionTimeLimit(final IntProp dimsExecutionTimeLimit)\n
    '''
def getDimsMaximumProcesses():
    '''returns IntProp\n\n
    getDimsMaximumProcesses()\n
    '''
def setDimsMaximumProcesses():
    '''returns None\n\n
    setDimsMaximumProcesses(final IntProp dimsMaximumProcesses)\n
    '''
def getDimsNonAffineConnections():
    '''returns IntProp\n\n
    getDimsNonAffineConnections()\n
    '''
def setDimsNonAffineConnections():
    '''returns None\n\n
    setDimsNonAffineConnections(final IntProp dimsNonAffineConnections)\n
    '''
def getDimsPeakAffineConnections():
    '''returns IntProp\n\n
    getDimsPeakAffineConnections()\n
    '''
def setDimsPeakAffineConnections():
    '''returns None\n\n
    setDimsPeakAffineConnections(final IntProp dimsPeakAffineConnections)\n
    '''
def getDimsPeakMaximumProcesses():
    '''returns IntProp\n\n
    getDimsPeakMaximumProcesses()\n
    '''
def setDimsPeakMaximumProcesses():
    '''returns None\n\n
    setDimsPeakMaximumProcesses(final IntProp dimsPeakMaximumProcesses)\n
    '''
def getDimsPeakNonAffineConnections():
    '''returns IntProp\n\n
    getDimsPeakNonAffineConnections()\n
    '''
def setDimsPeakNonAffineConnections():
    '''returns None\n\n
    setDimsPeakNonAffineConnections(final IntProp dimsPeakNonAffineConnections)\n
    '''
def getDimsQueueLimit():
    '''returns IntProp\n\n
    getDimsQueueLimit()\n
    '''
def setDimsQueueLimit():
    '''returns None\n\n
    setDimsQueueLimit(final IntProp dimsQueueLimit)\n
    '''
def getDisAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getDisAuditLevel()\n
    '''
def setDisAuditLevel():
    '''returns None\n\n
    setDisAuditLevel(final AuditLevelEnumProp disAuditLevel)\n
    '''
def getDisConnections():
    '''returns IntProp\n\n
    getDisConnections()\n
    '''
def setDisConnections():
    '''returns None\n\n
    setDisConnections(final IntProp disConnections)\n
    '''
def getDispatcherAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getDispatcherAuditLevel()\n
    '''
def setDispatcherAuditLevel():
    '''returns None\n\n
    setDispatcherAuditLevel(final AuditLevelEnumProp dispatcherAuditLevel)\n
    '''
def getDisPeakConnections():
    '''returns IntProp\n\n
    getDisPeakConnections()\n
    '''
def setDisPeakConnections():
    '''returns None\n\n
    setDisPeakConnections(final IntProp disPeakConnections)\n
    '''
def getDmsAffineConnections():
    '''returns IntProp\n\n
    getDmsAffineConnections()\n
    '''
def setDmsAffineConnections():
    '''returns None\n\n
    setDmsAffineConnections(final IntProp dmsAffineConnections)\n
    '''
def getDmsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getDmsAuditLevel()\n
    '''
def setDmsAuditLevel():
    '''returns None\n\n
    setDmsAuditLevel(final AuditLevelEnumProp dmsAuditLevel)\n
    '''
def getDmsConnections():
    '''returns IntProp\n\n
    getDmsConnections()\n
    '''
def setDmsConnections():
    '''returns None\n\n
    setDmsConnections(final IntProp dmsConnections)\n
    '''
def getDmsExecutionTimeLimit():
    '''returns IntProp\n\n
    getDmsExecutionTimeLimit()\n
    '''
def setDmsExecutionTimeLimit():
    '''returns None\n\n
    setDmsExecutionTimeLimit(final IntProp dmsExecutionTimeLimit)\n
    '''
def getDmsMaximumProcesses():
    '''returns IntProp\n\n
    getDmsMaximumProcesses()\n
    '''
def setDmsMaximumProcesses():
    '''returns None\n\n
    setDmsMaximumProcesses(final IntProp dmsMaximumProcesses)\n
    '''
def getDmsNonAffineConnections():
    '''returns IntProp\n\n
    getDmsNonAffineConnections()\n
    '''
def setDmsNonAffineConnections():
    '''returns None\n\n
    setDmsNonAffineConnections(final IntProp dmsNonAffineConnections)\n
    '''
def getDmsPeakAffineConnections():
    '''returns IntProp\n\n
    getDmsPeakAffineConnections()\n
    '''
def setDmsPeakAffineConnections():
    '''returns None\n\n
    setDmsPeakAffineConnections(final IntProp dmsPeakAffineConnections)\n
    '''
def getDmsPeakMaximumProcesses():
    '''returns IntProp\n\n
    getDmsPeakMaximumProcesses()\n
    '''
def setDmsPeakMaximumProcesses():
    '''returns None\n\n
    setDmsPeakMaximumProcesses(final IntProp dmsPeakMaximumProcesses)\n
    '''
def getDmsPeakNonAffineConnections():
    '''returns IntProp\n\n
    getDmsPeakNonAffineConnections()\n
    '''
def setDmsPeakNonAffineConnections():
    '''returns None\n\n
    setDmsPeakNonAffineConnections(final IntProp dmsPeakNonAffineConnections)\n
    '''
def getDmsQueueLimit():
    '''returns IntProp\n\n
    getDmsQueueLimit()\n
    '''
def setDmsQueueLimit():
    '''returns None\n\n
    setDmsQueueLimit(final IntProp dmsQueueLimit)\n
    '''
def getDsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getDsAuditLevel()\n
    '''
def setDsAuditLevel():
    '''returns None\n\n
    setDsAuditLevel(final AuditLevelEnumProp dsAuditLevel)\n
    '''
def getDsCompressAttachmentLimit():
    '''returns IntProp\n\n
    getDsCompressAttachmentLimit()\n
    '''
def setDsCompressAttachmentLimit():
    '''returns None\n\n
    setDsCompressAttachmentLimit(final IntProp dsCompressAttachmentLimit)\n
    '''
def getDsConnections():
    '''returns IntProp\n\n
    getDsConnections()\n
    '''
def setDsConnections():
    '''returns None\n\n
    setDsConnections(final IntProp dsConnections)\n
    '''
def getDsMaximumEMailSize():
    '''returns IntProp\n\n
    getDsMaximumEMailSize()\n
    '''
def setDsMaximumEMailSize():
    '''returns None\n\n
    setDsMaximumEMailSize(final IntProp dsMaximumEMailSize)\n
    '''
def getDsPeakConnections():
    '''returns IntProp\n\n
    getDsPeakConnections()\n
    '''
def setDsPeakConnections():
    '''returns None\n\n
    setDsPeakConnections(final IntProp dsPeakConnections)\n
    '''
def getEmsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getEmsAuditLevel()\n
    '''
def setEmsAuditLevel():
    '''returns None\n\n
    setEmsAuditLevel(final AuditLevelEnumProp emsAuditLevel)\n
    '''
def getEvsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getEvsAuditLevel()\n
    '''
def setEvsAuditLevel():
    '''returns None\n\n
    setEvsAuditLevel(final AuditLevelEnumProp evsAuditLevel)\n
    '''
def getGsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getGsAuditLevel()\n
    '''
def setGsAuditLevel():
    '''returns None\n\n
    setGsAuditLevel(final AuditLevelEnumProp gsAuditLevel)\n
    '''
def getGsExecutionTimeLimit():
    '''returns IntProp\n\n
    getGsExecutionTimeLimit()\n
    '''
def setGsExecutionTimeLimit():
    '''returns None\n\n
    setGsExecutionTimeLimit(final IntProp gsExecutionTimeLimit)\n
    '''
def getGsNonAffineConnections():
    '''returns IntProp\n\n
    getGsNonAffineConnections()\n
    '''
def setGsNonAffineConnections():
    '''returns None\n\n
    setGsNonAffineConnections(final IntProp gsNonAffineConnections)\n
    '''
def getGsPeakNonAffineConnections():
    '''returns IntProp\n\n
    getGsPeakNonAffineConnections()\n
    '''
def setGsPeakNonAffineConnections():
    '''returns None\n\n
    setGsPeakNonAffineConnections(final IntProp gsPeakNonAffineConnections)\n
    '''
def getGsQueueLimit():
    '''returns IntProp\n\n
    getGsQueueLimit()\n
    '''
def setGsQueueLimit():
    '''returns None\n\n
    setGsQueueLimit(final IntProp gsQueueLimit)\n
    '''
def getHtsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getHtsAuditLevel()\n
    '''
def setHtsAuditLevel():
    '''returns None\n\n
    setHtsAuditLevel(final AuditLevelEnumProp htsAuditLevel)\n
    '''
def getHtsCompletedTaskLifetime():
    '''returns DurationProp\n\n
    getHtsCompletedTaskLifetime()\n
    '''
def setHtsCompletedTaskLifetime():
    '''returns None\n\n
    setHtsCompletedTaskLifetime(final DurationProp htsCompletedTaskLifetime)\n
    '''
def getIdsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getIdsAuditLevel()\n
    '''
def setIdsAuditLevel():
    '''returns None\n\n
    setIdsAuditLevel(final AuditLevelEnumProp idsAuditLevel)\n
    '''
def getIdsConnections():
    '''returns IntProp\n\n
    getIdsConnections()\n
    '''
def setIdsConnections():
    '''returns None\n\n
    setIdsConnections(final IntProp idsConnections)\n
    '''
def getIdsPeakConnections():
    '''returns IntProp\n\n
    getIdsPeakConnections()\n
    '''
def setIdsPeakConnections():
    '''returns None\n\n
    setIdsPeakConnections(final IntProp idsPeakConnections)\n
    '''
def getIdVizAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getIdVizAuditLevel()\n
    '''
def setIdVizAuditLevel():
    '''returns None\n\n
    setIdVizAuditLevel(final AuditLevelEnumProp idVizAuditLevel)\n
    '''
def getIssAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getIssAuditLevel()\n
    '''
def setIssAuditLevel():
    '''returns None\n\n
    setIssAuditLevel(final AuditLevelEnumProp issAuditLevel)\n
    '''
def getIssConnections():
    '''returns IntProp\n\n
    getIssConnections()\n
    '''
def setIssConnections():
    '''returns None\n\n
    setIssConnections(final IntProp issConnections)\n
    '''
def getIssPeakConnections():
    '''returns IntProp\n\n
    getIssPeakConnections()\n
    '''
def setIssPeakConnections():
    '''returns None\n\n
    setIssPeakConnections(final IntProp issPeakConnections)\n
    '''
def getIusAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getIusAuditLevel()\n
    '''
def setIusAuditLevel():
    '''returns None\n\n
    setIusAuditLevel(final AuditLevelEnumProp iusAuditLevel)\n
    '''
def getIusConnections():
    '''returns IntProp\n\n
    getIusConnections()\n
    '''
def setIusConnections():
    '''returns None\n\n
    setIusConnections(final IntProp iusConnections)\n
    '''
def getIusPeakConnections():
    '''returns IntProp\n\n
    getIusPeakConnections()\n
    '''
def setIusPeakConnections():
    '''returns None\n\n
    setIusPeakConnections(final IntProp iusPeakConnections)\n
    '''
def getJsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getJsAuditLevel()\n
    '''
def setJsAuditLevel():
    '''returns None\n\n
    setJsAuditLevel(final AuditLevelEnumProp jsAuditLevel)\n
    '''
def getJsConnections():
    '''returns IntProp\n\n
    getJsConnections()\n
    '''
def setJsConnections():
    '''returns None\n\n
    setJsConnections(final IntProp jsConnections)\n
    '''
def getJsPeakConnections():
    '''returns IntProp\n\n
    getJsPeakConnections()\n
    '''
def setJsPeakConnections():
    '''returns None\n\n
    setJsPeakConnections(final IntProp jsPeakConnections)\n
    '''
def getLoadBalancingMode():
    '''returns LoadBalancingModeEnumProp\n\n
    getLoadBalancingMode()\n
    '''
def setLoadBalancingMode():
    '''returns None\n\n
    setLoadBalancingMode(final LoadBalancingModeEnumProp loadBalancingMode)\n
    '''
def getMbsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getMbsAuditLevel()\n
    '''
def setMbsAuditLevel():
    '''returns None\n\n
    setMbsAuditLevel(final AuditLevelEnumProp mbsAuditLevel)\n
    '''
def getMbsConnections():
    '''returns IntProp\n\n
    getMbsConnections()\n
    '''
def setMbsConnections():
    '''returns None\n\n
    setMbsConnections(final IntProp mbsConnections)\n
    '''
def getMbsPeakConnections():
    '''returns IntProp\n\n
    getMbsPeakConnections()\n
    '''
def setMbsPeakConnections():
    '''returns None\n\n
    setMbsPeakConnections(final IntProp mbsPeakConnections)\n
    '''
def getMdsAffineConnections():
    '''returns IntProp\n\n
    getMdsAffineConnections()\n
    '''
def setMdsAffineConnections():
    '''returns None\n\n
    setMdsAffineConnections(final IntProp mdsAffineConnections)\n
    '''
def getMdsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getMdsAuditLevel()\n
    '''
def setMdsAuditLevel():
    '''returns None\n\n
    setMdsAuditLevel(final AuditLevelEnumProp mdsAuditLevel)\n
    '''
def getMdsExecutionTimeLimit():
    '''returns IntProp\n\n
    getMdsExecutionTimeLimit()\n
    '''
def setMdsExecutionTimeLimit():
    '''returns None\n\n
    setMdsExecutionTimeLimit(final IntProp mdsExecutionTimeLimit)\n
    '''
def getMdsMaximumProcesses():
    '''returns IntProp\n\n
    getMdsMaximumProcesses()\n
    '''
def setMdsMaximumProcesses():
    '''returns None\n\n
    setMdsMaximumProcesses(final IntProp mdsMaximumProcesses)\n
    '''
def getMdsNonAffineConnections():
    '''returns IntProp\n\n
    getMdsNonAffineConnections()\n
    '''
def setMdsNonAffineConnections():
    '''returns None\n\n
    setMdsNonAffineConnections(final IntProp mdsNonAffineConnections)\n
    '''
def getMdsPeakAffineConnections():
    '''returns IntProp\n\n
    getMdsPeakAffineConnections()\n
    '''
def setMdsPeakAffineConnections():
    '''returns None\n\n
    setMdsPeakAffineConnections(final IntProp mdsPeakAffineConnections)\n
    '''
def getMdsPeakMaximumProcesses():
    '''returns IntProp\n\n
    getMdsPeakMaximumProcesses()\n
    '''
def setMdsPeakMaximumProcesses():
    '''returns None\n\n
    setMdsPeakMaximumProcesses(final IntProp mdsPeakMaximumProcesses)\n
    '''
def getMdsPeakNonAffineConnections():
    '''returns IntProp\n\n
    getMdsPeakNonAffineConnections()\n
    '''
def setMdsPeakNonAffineConnections():
    '''returns None\n\n
    setMdsPeakNonAffineConnections(final IntProp mdsPeakNonAffineConnections)\n
    '''
def getMdsQueueLimit():
    '''returns IntProp\n\n
    getMdsQueueLimit()\n
    '''
def setMdsQueueLimit():
    '''returns None\n\n
    setMdsQueueLimit(final IntProp mdsQueueLimit)\n
    '''
def getMisAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getMisAuditLevel()\n
    '''
def setMisAuditLevel():
    '''returns None\n\n
    setMisAuditLevel(final AuditLevelEnumProp misAuditLevel)\n
    '''
def getMisConnections():
    '''returns IntProp\n\n
    getMisConnections()\n
    '''
def setMisConnections():
    '''returns None\n\n
    setMisConnections(final IntProp misConnections)\n
    '''
def getMisPeakConnections():
    '''returns IntProp\n\n
    getMisPeakConnections()\n
    '''
def setMisPeakConnections():
    '''returns None\n\n
    setMisPeakConnections(final IntProp misPeakConnections)\n
    '''
def getMmsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getMmsAuditLevel()\n
    '''
def setMmsAuditLevel():
    '''returns None\n\n
    setMmsAuditLevel(final AuditLevelEnumProp mmsAuditLevel)\n
    '''
def getMmsConnections():
    '''returns IntProp\n\n
    getMmsConnections()\n
    '''
def setMmsConnections():
    '''returns None\n\n
    setMmsConnections(final IntProp mmsConnections)\n
    '''
def getMmsPeakConnections():
    '''returns IntProp\n\n
    getMmsPeakConnections()\n
    '''
def setMmsPeakConnections():
    '''returns None\n\n
    setMmsPeakConnections(final IntProp mmsPeakConnections)\n
    '''
def getMsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getMsAuditLevel()\n
    '''
def setMsAuditLevel():
    '''returns None\n\n
    setMsAuditLevel(final AuditLevelEnumProp msAuditLevel)\n
    '''
def getNonPeakDemandBeginHour():
    '''returns IntProp\n\n
    getNonPeakDemandBeginHour()\n
    '''
def setNonPeakDemandBeginHour():
    '''returns None\n\n
    setNonPeakDemandBeginHour(final IntProp nonPeakDemandBeginHour)\n
    '''
def getPacsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getPacsAuditLevel()\n
    '''
def setPacsAuditLevel():
    '''returns None\n\n
    setPacsAuditLevel(final AuditLevelEnumProp pacsAuditLevel)\n
    '''
def getPacsConnections():
    '''returns IntProp\n\n
    getPacsConnections()\n
    '''
def setPacsConnections():
    '''returns None\n\n
    setPacsConnections(final IntProp pacsConnections)\n
    '''
def getPacsPeakConnections():
    '''returns IntProp\n\n
    getPacsPeakConnections()\n
    '''
def setPacsPeakConnections():
    '''returns None\n\n
    setPacsPeakConnections(final IntProp pacsPeakConnections)\n
    '''
def getPdsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getPdsAuditLevel()\n
    '''
def setPdsAuditLevel():
    '''returns None\n\n
    setPdsAuditLevel(final AuditLevelEnumProp pdsAuditLevel)\n
    '''
def getPdsConnections():
    '''returns IntProp\n\n
    getPdsConnections()\n
    '''
def setPdsConnections():
    '''returns None\n\n
    setPdsConnections(final IntProp pdsConnections)\n
    '''
def getPdsEListAccessCacheLimit():
    '''returns IntProp\n\n
    getPdsEListAccessCacheLimit()\n
    '''
def setPdsEListAccessCacheLimit():
    '''returns None\n\n
    setPdsEListAccessCacheLimit(final IntProp pdsEListAccessCacheLimit)\n
    '''
def getPdsMaximumProcesses():
    '''returns IntProp\n\n
    getPdsMaximumProcesses()\n
    '''
def setPdsMaximumProcesses():
    '''returns None\n\n
    setPdsMaximumProcesses(final IntProp pdsMaximumProcesses)\n
    '''
def getPdsPeakConnections():
    '''returns IntProp\n\n
    getPdsPeakConnections()\n
    '''
def setPdsPeakConnections():
    '''returns None\n\n
    setPdsPeakConnections(final IntProp pdsPeakConnections)\n
    '''
def getPdsPeakMaximumProcesses():
    '''returns IntProp\n\n
    getPdsPeakMaximumProcesses()\n
    '''
def setPdsPeakMaximumProcesses():
    '''returns None\n\n
    setPdsPeakMaximumProcesses(final IntProp pdsPeakMaximumProcesses)\n
    '''
def getPdsShowCellAnnotations():
    '''returns BooleanProp\n\n
    getPdsShowCellAnnotations()\n
    '''
def setPdsShowCellAnnotations():
    '''returns None\n\n
    setPdsShowCellAnnotations(final BooleanProp pdsShowCellAnnotations)\n
    '''
def getPeakDemandBeginHour():
    '''returns IntProp\n\n
    getPeakDemandBeginHour()\n
    '''
def setPeakDemandBeginHour():
    '''returns None\n\n
    setPeakDemandBeginHour(final IntProp peakDemandBeginHour)\n
    '''
def getPpsAffineConnections():
    '''returns IntProp\n\n
    getPpsAffineConnections()\n
    '''
def setPpsAffineConnections():
    '''returns None\n\n
    setPpsAffineConnections(final IntProp ppsAffineConnections)\n
    '''
def getPpsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getPpsAuditLevel()\n
    '''
def setPpsAuditLevel():
    '''returns None\n\n
    setPpsAuditLevel(final AuditLevelEnumProp ppsAuditLevel)\n
    '''
def getPpsExecutionTimeLimit():
    '''returns IntProp\n\n
    getPpsExecutionTimeLimit()\n
    '''
def setPpsExecutionTimeLimit():
    '''returns None\n\n
    setPpsExecutionTimeLimit(final IntProp ppsExecutionTimeLimit)\n
    '''
def getPpsMaximumEMailAttachmentSize():
    '''returns IntProp\n\n
    getPpsMaximumEMailAttachmentSize()\n
    '''
def setPpsMaximumEMailAttachmentSize():
    '''returns None\n\n
    setPpsMaximumEMailAttachmentSize(final IntProp ppsMaximumEMailAttachmentSize)\n
    '''
def getPpsNonAffineConnections():
    '''returns IntProp\n\n
    getPpsNonAffineConnections()\n
    '''
def setPpsNonAffineConnections():
    '''returns None\n\n
    setPpsNonAffineConnections(final IntProp ppsNonAffineConnections)\n
    '''
def getPpsPeakAffineConnections():
    '''returns IntProp\n\n
    getPpsPeakAffineConnections()\n
    '''
def setPpsPeakAffineConnections():
    '''returns None\n\n
    setPpsPeakAffineConnections(final IntProp ppsPeakAffineConnections)\n
    '''
def getPpsPeakNonAffineConnections():
    '''returns IntProp\n\n
    getPpsPeakNonAffineConnections()\n
    '''
def setPpsPeakNonAffineConnections():
    '''returns None\n\n
    setPpsPeakNonAffineConnections(final IntProp ppsPeakNonAffineConnections)\n
    '''
def getPpsQueueLimit():
    '''returns IntProp\n\n
    getPpsQueueLimit()\n
    '''
def setPpsQueueLimit():
    '''returns None\n\n
    setPpsQueueLimit(final IntProp ppsQueueLimit)\n
    '''
def getPrsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getPrsAuditLevel()\n
    '''
def setPrsAuditLevel():
    '''returns None\n\n
    setPrsAuditLevel(final AuditLevelEnumProp prsAuditLevel)\n
    '''
def getPrsConnections():
    '''returns IntProp\n\n
    getPrsConnections()\n
    '''
def setPrsConnections():
    '''returns None\n\n
    setPrsConnections(final IntProp prsConnections)\n
    '''
def getPrsPeakConnections():
    '''returns IntProp\n\n
    getPrsPeakConnections()\n
    '''
def setPrsPeakConnections():
    '''returns None\n\n
    setPrsPeakConnections(final IntProp prsPeakConnections)\n
    '''
def getPsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getPsAuditLevel()\n
    '''
def setPsAuditLevel():
    '''returns None\n\n
    setPsAuditLevel(final AuditLevelEnumProp psAuditLevel)\n
    '''
def getPtsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getPtsAuditLevel()\n
    '''
def setPtsAuditLevel():
    '''returns None\n\n
    setPtsAuditLevel(final AuditLevelEnumProp ptsAuditLevel)\n
    '''
def getPtsConnections():
    '''returns IntProp\n\n
    getPtsConnections()\n
    '''
def setPtsConnections():
    '''returns None\n\n
    setPtsConnections(final IntProp ptsConnections)\n
    '''
def getPtsPeakConnections():
    '''returns IntProp\n\n
    getPtsPeakConnections()\n
    '''
def setPtsPeakConnections():
    '''returns None\n\n
    setPtsPeakConnections(final IntProp ptsPeakConnections)\n
    '''
def getQsAdditionalJVMArguments():
    '''returns StringProp\n\n
    getQsAdditionalJVMArguments()\n
    '''
def setQsAdditionalJVMArguments():
    '''returns None\n\n
    setQsAdditionalJVMArguments(final StringProp qsAdditionalJVMArguments)\n
    '''
def getQsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getQsAuditLevel()\n
    '''
def setQsAuditLevel():
    '''returns None\n\n
    setQsAuditLevel(final AuditLevelEnumProp qsAuditLevel)\n
    '''
def getQsDiagnosticsEnabled():
    '''returns BooleanProp\n\n
    getQsDiagnosticsEnabled()\n
    '''
def setQsDiagnosticsEnabled():
    '''returns None\n\n
    setQsDiagnosticsEnabled(final BooleanProp qsDiagnosticsEnabled)\n
    '''
def getQsDisableQueryPlanCache():
    '''returns BooleanProp\n\n
    getQsDisableQueryPlanCache()\n
    '''
def setQsDisableQueryPlanCache():
    '''returns None\n\n
    setQsDisableQueryPlanCache(final BooleanProp qsDisableQueryPlanCache)\n
    '''
def getQsDisableVerboseGCLogging():
    '''returns BooleanProp\n\n
    getQsDisableVerboseGCLogging()\n
    '''
def setQsDisableVerboseGCLogging():
    '''returns None\n\n
    setQsDisableVerboseGCLogging(final BooleanProp qsDisableVerboseGCLogging)\n
    '''
def getQsDumpModelToFile():
    '''returns BooleanProp\n\n
    getQsDumpModelToFile()\n
    '''
def setQsDumpModelToFile():
    '''returns None\n\n
    setQsDumpModelToFile(final BooleanProp qsDumpModelToFile)\n
    '''
def getQsGCPolicy():
    '''returns AnyURIProp\n\n
    getQsGCPolicy()\n
    '''
def setQsGCPolicy():
    '''returns None\n\n
    setQsGCPolicy(final AnyURIProp qsGCPolicy)\n
    '''
def getQsGenerateCommentsInNativeSQL():
    '''returns BooleanProp\n\n
    getQsGenerateCommentsInNativeSQL()\n
    '''
def setQsGenerateCommentsInNativeSQL():
    '''returns None\n\n
    setQsGenerateCommentsInNativeSQL(final BooleanProp qsGenerateCommentsInNativeSQL)\n
    '''
def getQsIdleConnectionTimeout():
    '''returns IntProp\n\n
    getQsIdleConnectionTimeout()\n
    '''
def setQsIdleConnectionTimeout():
    '''returns None\n\n
    setQsIdleConnectionTimeout(final IntProp qsIdleConnectionTimeout)\n
    '''
def getQsInitialJVMHeapSize():
    '''returns IntProp\n\n
    getQsInitialJVMHeapSize()\n
    '''
def setQsInitialJVMHeapSize():
    '''returns None\n\n
    setQsInitialJVMHeapSize(final IntProp qsInitialJVMHeapSize)\n
    '''
def getQsInitialJVMNurserySize():
    '''returns IntProp\n\n
    getQsInitialJVMNurserySize()\n
    '''
def setQsInitialJVMNurserySize():
    '''returns None\n\n
    setQsInitialJVMNurserySize(final IntProp qsInitialJVMNurserySize)\n
    '''
def getQsJVMHeapSizeLimit():
    '''returns IntProp\n\n
    getQsJVMHeapSizeLimit()\n
    '''
def setQsJVMHeapSizeLimit():
    '''returns None\n\n
    setQsJVMHeapSizeLimit(final IntProp qsJVMHeapSizeLimit)\n
    '''
def getQsJVMNurserySizeLimit():
    '''returns IntProp\n\n
    getQsJVMNurserySizeLimit()\n
    '''
def setQsJVMNurserySizeLimit():
    '''returns None\n\n
    setQsJVMNurserySizeLimit(final IntProp qsJVMNurserySizeLimit)\n
    '''
def getQsManualCubeStart():
    '''returns BooleanProp\n\n
    getQsManualCubeStart()\n
    '''
def setQsManualCubeStart():
    '''returns None\n\n
    setQsManualCubeStart(final BooleanProp qsManualCubeStart)\n
    '''
def getQsMetricsEnabled():
    '''returns BooleanProp\n\n
    getQsMetricsEnabled()\n
    '''
def setQsMetricsEnabled():
    '''returns None\n\n
    setQsMetricsEnabled(final BooleanProp qsMetricsEnabled)\n
    '''
def getQsMultiDimensionalQuerySizeLimit():
    '''returns IntProp\n\n
    getQsMultiDimensionalQuerySizeLimit()\n
    '''
def setQsMultiDimensionalQuerySizeLimit():
    '''returns None\n\n
    setQsMultiDimensionalQuerySizeLimit(final IntProp qsMultiDimensionalQuerySizeLimit)\n
    '''
def getQsQueryExecutionTrace():
    '''returns BooleanProp\n\n
    getQsQueryExecutionTrace()\n
    '''
def setQsQueryExecutionTrace():
    '''returns None\n\n
    setQsQueryExecutionTrace(final BooleanProp qsQueryExecutionTrace)\n
    '''
def getQsQueryPlanningTrace():
    '''returns BooleanProp\n\n
    getQsQueryPlanningTrace()\n
    '''
def setQsQueryPlanningTrace():
    '''returns None\n\n
    setQsQueryPlanningTrace(final BooleanProp qsQueryPlanningTrace)\n
    '''
def getQsResultSetCacheQueryTimeThreshold():
    '''returns IntProp\n\n
    getQsResultSetCacheQueryTimeThreshold()\n
    '''
def setQsResultSetCacheQueryTimeThreshold():
    '''returns None\n\n
    setQsResultSetCacheQueryTimeThreshold(final IntProp qsResultSetCacheQueryTimeThreshold)\n
    '''
def getQsROLAPCubeAdministrationCommandTimeout():
    '''returns IntProp\n\n
    getQsROLAPCubeAdministrationCommandTimeout()\n
    '''
def setQsROLAPCubeAdministrationCommandTimeout():
    '''returns None\n\n
    setQsROLAPCubeAdministrationCommandTimeout(final IntProp qsROLAPCubeAdministrationCommandTimeout)\n
    '''
def getQsROLAPCubeConfigurations():
    '''returns BaseROLAPCubeConfigurationArrayProp\n\n
    getQsROLAPCubeConfigurations()\n
    '''
def setQsROLAPCubeConfigurations():
    '''returns None\n\n
    setQsROLAPCubeConfigurations(final BaseROLAPCubeConfigurationArrayProp qsROLAPCubeConfigurations)\n
    '''
def getQsROLAPMemberCacheAliasRoot():
    '''returns TokenProp\n\n
    getQsROLAPMemberCacheAliasRoot()\n
    '''
def setQsROLAPMemberCacheAliasRoot():
    '''returns None\n\n
    setQsROLAPMemberCacheAliasRoot(final TokenProp qsROLAPMemberCacheAliasRoot)\n
    '''
def getQsVerboseGCLogLimit():
    '''returns IntProp\n\n
    getQsVerboseGCLogLimit()\n
    '''
def setQsVerboseGCLogLimit():
    '''returns None\n\n
    setQsVerboseGCLogLimit(final IntProp qsVerboseGCLogLimit)\n
    '''
def getRdsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getRdsAuditLevel()\n
    '''
def setRdsAuditLevel():
    '''returns None\n\n
    setRdsAuditLevel(final AuditLevelEnumProp rdsAuditLevel)\n
    '''
def getRdsGatewayMappings():
    '''returns GatewayMappingArrayProp\n\n
    getRdsGatewayMappings()\n
    '''
def setRdsGatewayMappings():
    '''returns None\n\n
    setRdsGatewayMappings(final GatewayMappingArrayProp rdsGatewayMappings)\n
    '''
def getRdsMaximumDataSize():
    '''returns IntProp\n\n
    getRdsMaximumDataSize()\n
    '''
def setRdsMaximumDataSize():
    '''returns None\n\n
    setRdsMaximumDataSize(final IntProp rdsMaximumDataSize)\n
    '''
def getReposAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getReposAuditLevel()\n
    '''
def setReposAuditLevel():
    '''returns None\n\n
    setReposAuditLevel(final AuditLevelEnumProp reposAuditLevel)\n
    '''
def getReposCacheObjTTL():
    '''returns PositiveIntegerProp\n\n
    getReposCacheObjTTL()\n
    '''
def setReposCacheObjTTL():
    '''returns None\n\n
    setReposCacheObjTTL(final PositiveIntegerProp reposCacheObjTTL)\n
    '''
def getReposNumObjDisk():
    '''returns PositiveIntegerProp\n\n
    getReposNumObjDisk()\n
    '''
def setReposNumObjDisk():
    '''returns None\n\n
    setReposNumObjDisk(final PositiveIntegerProp reposNumObjDisk)\n
    '''
def getReposNumObjMem():
    '''returns PositiveIntegerProp\n\n
    getReposNumObjMem()\n
    '''
def setReposNumObjMem():
    '''returns None\n\n
    setReposNumObjMem(final PositiveIntegerProp reposNumObjMem)\n
    '''
def getRmdsAffineConnections():
    '''returns IntProp\n\n
    getRmdsAffineConnections()\n
    '''
def setRmdsAffineConnections():
    '''returns None\n\n
    setRmdsAffineConnections(final IntProp rmdsAffineConnections)\n
    '''
def getRmdsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getRmdsAuditLevel()\n
    '''
def setRmdsAuditLevel():
    '''returns None\n\n
    setRmdsAuditLevel(final AuditLevelEnumProp rmdsAuditLevel)\n
    '''
def getRmdsConnections():
    '''returns IntProp\n\n
    getRmdsConnections()\n
    '''
def setRmdsConnections():
    '''returns None\n\n
    setRmdsConnections(final IntProp rmdsConnections)\n
    '''
def getRmdsExecutionTimeLimit():
    '''returns IntProp\n\n
    getRmdsExecutionTimeLimit()\n
    '''
def setRmdsExecutionTimeLimit():
    '''returns None\n\n
    setRmdsExecutionTimeLimit(final IntProp rmdsExecutionTimeLimit)\n
    '''
def getRmdsNonAffineConnections():
    '''returns IntProp\n\n
    getRmdsNonAffineConnections()\n
    '''
def setRmdsNonAffineConnections():
    '''returns None\n\n
    setRmdsNonAffineConnections(final IntProp rmdsNonAffineConnections)\n
    '''
def getRmdsPeakAffineConnections():
    '''returns IntProp\n\n
    getRmdsPeakAffineConnections()\n
    '''
def setRmdsPeakAffineConnections():
    '''returns None\n\n
    setRmdsPeakAffineConnections(final IntProp rmdsPeakAffineConnections)\n
    '''
def getRmdsPeakConnections():
    '''returns IntProp\n\n
    getRmdsPeakConnections()\n
    '''
def setRmdsPeakConnections():
    '''returns None\n\n
    setRmdsPeakConnections(final IntProp rmdsPeakConnections)\n
    '''
def getRmdsPeakNonAffineConnections():
    '''returns IntProp\n\n
    getRmdsPeakNonAffineConnections()\n
    '''
def setRmdsPeakNonAffineConnections():
    '''returns None\n\n
    setRmdsPeakNonAffineConnections(final IntProp rmdsPeakNonAffineConnections)\n
    '''
def getRsAffineConnections():
    '''returns IntProp\n\n
    getRsAffineConnections()\n
    '''
def setRsAffineConnections():
    '''returns None\n\n
    setRsAffineConnections(final IntProp rsAffineConnections)\n
    '''
def getRsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getRsAuditLevel()\n
    '''
def setRsAuditLevel():
    '''returns None\n\n
    setRsAuditLevel(final AuditLevelEnumProp rsAuditLevel)\n
    '''
def getRsAuditNativeQuery():
    '''returns BooleanProp\n\n
    getRsAuditNativeQuery()\n
    '''
def setRsAuditNativeQuery():
    '''returns None\n\n
    setRsAuditNativeQuery(final BooleanProp rsAuditNativeQuery)\n
    '''
def getRsChartHotspotLimit():
    '''returns IntProp\n\n
    getRsChartHotspotLimit()\n
    '''
def setRsChartHotspotLimit():
    '''returns None\n\n
    setRsChartHotspotLimit(final IntProp rsChartHotspotLimit)\n
    '''
def getRsDataSourceChange():
    '''returns DateTimeProp\n\n
    getRsDataSourceChange()\n
    '''
def setRsDataSourceChange():
    '''returns None\n\n
    setRsDataSourceChange(final DateTimeProp rsDataSourceChange)\n
    '''
def getRsExecutionTimeLimit():
    '''returns IntProp\n\n
    getRsExecutionTimeLimit()\n
    '''
def setRsExecutionTimeLimit():
    '''returns None\n\n
    setRsExecutionTimeLimit(final IntProp rsExecutionTimeLimit)\n
    '''
def getRsMaximumEMailAttachmentSize():
    '''returns IntProp\n\n
    getRsMaximumEMailAttachmentSize()\n
    '''
def setRsMaximumEMailAttachmentSize():
    '''returns None\n\n
    setRsMaximumEMailAttachmentSize(final IntProp rsMaximumEMailAttachmentSize)\n
    '''
def getRsMaximumProcesses():
    '''returns NonNegativeIntegerProp\n\n
    getRsMaximumProcesses()\n
    '''
def setRsMaximumProcesses():
    '''returns None\n\n
    setRsMaximumProcesses(final NonNegativeIntegerProp rsMaximumProcesses)\n
    '''
def getRsNonAffineConnections():
    '''returns IntProp\n\n
    getRsNonAffineConnections()\n
    '''
def setRsNonAffineConnections():
    '''returns None\n\n
    setRsNonAffineConnections(final IntProp rsNonAffineConnections)\n
    '''
def getRsPDFCharacterEncoding():
    '''returns PdfCharacterEncodingEnumProp\n\n
    getRsPDFCharacterEncoding()\n
    '''
def setRsPDFCharacterEncoding():
    '''returns None\n\n
    setRsPDFCharacterEncoding(final PdfCharacterEncodingEnumProp rsPDFCharacterEncoding)\n
    '''
def getRsPDFCompressionLevel():
    '''returns IntProp\n\n
    getRsPDFCompressionLevel()\n
    '''
def setRsPDFCompressionLevel():
    '''returns None\n\n
    setRsPDFCompressionLevel(final IntProp rsPDFCompressionLevel)\n
    '''
def getRsPDFCompressionType():
    '''returns PdfCompressionTypeEnumProp\n\n
    getRsPDFCompressionType()\n
    '''
def setRsPDFCompressionType():
    '''returns None\n\n
    setRsPDFCompressionType(final PdfCompressionTypeEnumProp rsPDFCompressionType)\n
    '''
def getRsPDFEmbedFonts():
    '''returns PdfFontEmbeddingEnumProp\n\n
    getRsPDFEmbedFonts()\n
    '''
def setRsPDFEmbedFonts():
    '''returns None\n\n
    setRsPDFEmbedFonts(final PdfFontEmbeddingEnumProp rsPDFEmbedFonts)\n
    '''
def getRsPeakAffineConnections():
    '''returns IntProp\n\n
    getRsPeakAffineConnections()\n
    '''
def setRsPeakAffineConnections():
    '''returns None\n\n
    setRsPeakAffineConnections(final IntProp rsPeakAffineConnections)\n
    '''
def getRsPeakMaximumProcesses():
    '''returns IntProp\n\n
    getRsPeakMaximumProcesses()\n
    '''
def setRsPeakMaximumProcesses():
    '''returns None\n\n
    setRsPeakMaximumProcesses(final IntProp rsPeakMaximumProcesses)\n
    '''
def getRsPeakNonAffineConnections():
    '''returns IntProp\n\n
    getRsPeakNonAffineConnections()\n
    '''
def setRsPeakNonAffineConnections():
    '''returns None\n\n
    setRsPeakNonAffineConnections(final IntProp rsPeakNonAffineConnections)\n
    '''
def getRsQueueLimit():
    '''returns PositiveIntegerProp\n\n
    getRsQueueLimit()\n
    '''
def setRsQueueLimit():
    '''returns None\n\n
    setRsQueueLimit(final PositiveIntegerProp rsQueueLimit)\n
    '''
def getSaCAMAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getSaCAMAuditLevel()\n
    '''
def setSaCAMAuditLevel():
    '''returns None\n\n
    setSaCAMAuditLevel(final AuditLevelEnumProp saCAMAuditLevel)\n
    '''
def getServerGroup():
    '''returns StringProp\n\n
    getServerGroup()\n
    '''
def setServerGroup():
    '''returns None\n\n
    setServerGroup(final StringProp serverGroup)\n
    '''
def getSsAuditLevel():
    '''returns AuditLevelEnumProp\n\n
    getSsAuditLevel()\n
    '''
def setSsAuditLevel():
    '''returns None\n\n
    setSsAuditLevel(final AuditLevelEnumProp ssAuditLevel)\n
    '''
