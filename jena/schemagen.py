NS = "String  \\"\" + nsURI + \"\\";\")"
DEFAULT_CONFIG_URI = "String  \"file:schemagen.rdf\""
DEFAULT_MARKER = "String  \"%\""
DEFAULT_TEMPLATE = "String  \"public static final %valclass% %valname% = m_model.%valcreator%( \\"%valuri%\\" );\""
DEFAULT_INDIVIDUAL_TEMPLATE = "String  \"public static final %valclass% %valname% = m_model.%valcreator%( \\"%valuri%\\", %valtype% );\""
DEFAULT_RDFS_INDIVIDUAL_TEMPLATE = "String  \"public static final %valclass% %valname% = m_model.%valcreator%( \\"%valuri%\\" );\""
DEFAULT_HEADER_TEMPLATE = "String  \"/* CVS $Id: $ */%nl%%package% %nl%%imports% %nl%/**%nl% * Vocabulary definitions from %sourceURI% %nl% * @author Auto-generated by schemagen on %date% %nl% */\""
COMMENT_LENGTH_LIMIT = "int  80"
NAMESPACE = "Resource  m_model.createResource( NS );\")"
m_optionDefinitions = "Object[][]  { { OPT.CONFIG_FILE, new OptionDefinition(\"-c\", \"configFile\") }, { OPT.ROOT, new OptionDefinition(\"-r\", \"root\") }, { OPT.NO_COMMENTS, new OptionDefinition(\"--nocomments\", \"noComments\") }, { OPT.INPUT, new OptionDefinition(\"-i\", \"input\") }, { OPT.LANG_DAML, new OptionDefinition(\"--daml\", \"daml\") }, { OPT.LANG_OWL, new OptionDefinition(\"--owl\", \"owl\") }, { OPT.LANG_RDFS, new OptionDefinition(\"--rdfs\", \"rdfs\") }, { OPT.OUTPUT, new OptionDefinition(\"-o\", \"output\") }, { OPT.HEADER, new OptionDefinition(\"--header\", \"header\") }, { OPT.FOOTER, new OptionDefinition(\"--footer\", \"footer\") }, { OPT.MARKER, new OptionDefinition(\"--marker\", \"marker\") }, { OPT.PACKAGENAME, new OptionDefinition(\"--package\", \"package\") }, { OPT.ONTOLOGY, new OptionDefinition(\"--ontology\", \"ontology\") }, { OPT.CLASSNAME, new OptionDefinition(\"-n\", \"classname\") }, { OPT.CLASSDEC, new OptionDefinition(\"--classdec\", \"classdec\") }, { OPT.NAMESPACE, new OptionDefinition(\"-a\", \"namespace\") }, { OPT.DECLARATIONS, new OptionDefinition(\"--declarations\", \"declarations\") }, { OPT.PROPERTY_SECTION, new OptionDefinition(\"--propSection\", \"propSection\") }, { OPT.CLASS_SECTION, new OptionDefinition(\"--classSection\", \"classSection\") }, { OPT.INDIVIDUALS_SECTION, new OptionDefinition(\"--individualsSection\", \"individualsSection\") }, { OPT.NOPROPERTIES, new OptionDefinition(\"--noproperties\", \"noproperties\") }, { OPT.NOCLASSES, new OptionDefinition(\"--noclasses\", \"noclasses\") }, { OPT.NOINDIVIDUALS, new OptionDefinition(\"--noindividuals\", \"noindividuals\") }, { OPT.PROP_TEMPLATE, new OptionDefinition(\"--propTemplate\", \"propTemplate\") }, { OPT.CLASS_TEMPLATE, new OptionDefinition(\"--classTemplate\", \"classTemplate\") }, { OPT.INDIVIDUAL_TEMPLATE, new OptionDefinition(\"--individualTemplate\", \"individualTemplate\") }, { OPT.UC_NAMES, new OptionDefinition(\"--uppercase\", \"uppercase\") }, { OPT.INCLUDE, new OptionDefinition(\"--include\", \"include\") }, { OPT.CLASSNAME_SUFFIX, new OptionDefinition(\"--classnamesuffix\", \"classnamesuffix\") }, { OPT.NOHEADER, new OptionDefinition(\"--noheader\", \"noheader\") }, { OPT.ENCODING, new OptionDefinition(\"-e\", \"encoding\") }, { OPT.HELP, new OptionDefinition(\"--help\", \"help\") }, { OPT.DOS, new OptionDefinition(\"--dos\", \"dos\") }, { OPT.USE_INF, new OptionDefinition(\"--inference\", \"inference\") }, { OPT.STRICT_INDIVIDUALS, new OptionDefinition(\"--strictIndividuals\", \"strictIndividuals\") }, { OPT.INCLUDE_SOURCE, new OptionDefinition(\"--includeSource\", \"includeSource\") }, { OPT.NO_STRICT, new OptionDefinition(\"--nostrict\", \"noStrict\") } }"
def ():
    '''returns SchemagenException\n\n
    ()\n
    (final String[] args)\n
    (final String msg, final Throwable cause)\n
    '''
def map1():
    '''returns Resource\n\n
    map1(final Statement s)\n
    '''
def compare():
    '''returns int\n\n
    compare(final RDFNode n0, final RDFNode n1)\n
    '''
def hasConfigFileOption():
    '''returns boolean\n\n
    hasConfigFileOption()\n
    '''
def getConfigFileOption():
    '''returns String\n\n
    getConfigFileOption()\n
    '''
def hasRootOption():
    '''returns boolean\n\n
    hasRootOption()\n
    '''
def getRootOption():
    '''returns String\n\n
    getRootOption()\n
    '''
def hasNoCommentsOption():
    '''returns boolean\n\n
    hasNoCommentsOption()\n
    '''
def getNoCommentsOption():
    '''returns String\n\n
    getNoCommentsOption()\n
    '''
def hasInputOption():
    '''returns boolean\n\n
    hasInputOption()\n
    '''
def getInputOption():
    '''returns Resource\n\n
    getInputOption()\n
    '''
def hasLangDamlOption():
    '''returns boolean\n\n
    hasLangDamlOption()\n
    '''
def getLangDamlOption():
    '''returns String\n\n
    getLangDamlOption()\n
    '''
def hasLangOwlOption():
    '''returns boolean\n\n
    hasLangOwlOption()\n
    '''
def getLangOwlOption():
    '''returns String\n\n
    getLangOwlOption()\n
    '''
def hasLangRdfsOption():
    '''returns boolean\n\n
    hasLangRdfsOption()\n
    '''
def getLangRdfsOption():
    '''returns String\n\n
    getLangRdfsOption()\n
    '''
def hasOutputOption():
    '''returns boolean\n\n
    hasOutputOption()\n
    '''
def getOutputOption():
    '''returns String\n\n
    getOutputOption()\n
    '''
def hasHeaderOption():
    '''returns boolean\n\n
    hasHeaderOption()\n
    '''
def getHeaderOption():
    '''returns String\n\n
    getHeaderOption()\n
    '''
def hasFooterOption():
    '''returns boolean\n\n
    hasFooterOption()\n
    '''
def getFooterOption():
    '''returns String\n\n
    getFooterOption()\n
    '''
def hasMarkerOption():
    '''returns boolean\n\n
    hasMarkerOption()\n
    '''
def getMarkerOption():
    '''returns String\n\n
    getMarkerOption()\n
    '''
def hasPackagenameOption():
    '''returns boolean\n\n
    hasPackagenameOption()\n
    '''
def getPackagenameOption():
    '''returns String\n\n
    getPackagenameOption()\n
    '''
def hasOntologyOption():
    '''returns boolean\n\n
    hasOntologyOption()\n
    '''
def getOntologyOption():
    '''returns String\n\n
    getOntologyOption()\n
    '''
def hasClassnameOption():
    '''returns boolean\n\n
    hasClassnameOption()\n
    '''
def getClassnameOption():
    '''returns String\n\n
    getClassnameOption()\n
    '''
def hasClassdecOption():
    '''returns boolean\n\n
    hasClassdecOption()\n
    '''
def getClassdecOption():
    '''returns String\n\n
    getClassdecOption()\n
    '''
def hasNamespaceOption():
    '''returns boolean\n\n
    hasNamespaceOption()\n
    '''
def getNamespaceOption():
    '''returns Resource\n\n
    getNamespaceOption()\n
    '''
def hasDeclarationsOption():
    '''returns boolean\n\n
    hasDeclarationsOption()\n
    '''
def getDeclarationsOption():
    '''returns String\n\n
    getDeclarationsOption()\n
    '''
def hasPropertySectionOption():
    '''returns boolean\n\n
    hasPropertySectionOption()\n
    '''
def getPropertySectionOption():
    '''returns String\n\n
    getPropertySectionOption()\n
    '''
def hasClassSectionOption():
    '''returns boolean\n\n
    hasClassSectionOption()\n
    '''
def getClassSectionOption():
    '''returns String\n\n
    getClassSectionOption()\n
    '''
def hasIndividualsSectionOption():
    '''returns boolean\n\n
    hasIndividualsSectionOption()\n
    '''
def getIndividualsSectionOption():
    '''returns String\n\n
    getIndividualsSectionOption()\n
    '''
def hasNopropertiesOption():
    '''returns boolean\n\n
    hasNopropertiesOption()\n
    '''
def hasNoclassesOption():
    '''returns boolean\n\n
    hasNoclassesOption()\n
    '''
def hasNoindividualsOption():
    '''returns boolean\n\n
    hasNoindividualsOption()\n
    '''
def hasPropTemplateOption():
    '''returns boolean\n\n
    hasPropTemplateOption()\n
    '''
def getPropTemplateOption():
    '''returns String\n\n
    getPropTemplateOption()\n
    '''
def hasClassTemplateOption():
    '''returns boolean\n\n
    hasClassTemplateOption()\n
    '''
def getClassTemplateOption():
    '''returns String\n\n
    getClassTemplateOption()\n
    '''
def hasIndividualTemplateOption():
    '''returns boolean\n\n
    hasIndividualTemplateOption()\n
    '''
def getIndividualTemplateOption():
    '''returns String\n\n
    getIndividualTemplateOption()\n
    '''
def hasUcNamesOption():
    '''returns boolean\n\n
    hasUcNamesOption()\n
    '''
def hasIncludeOption():
    '''returns boolean\n\n
    hasIncludeOption()\n
    '''
def getIncludeOption():
    '''returns List<String>\n\n
    getIncludeOption()\n
    '''
def hasClassnameSuffixOption():
    '''returns boolean\n\n
    hasClassnameSuffixOption()\n
    '''
def getClassnameSuffixOption():
    '''returns String\n\n
    getClassnameSuffixOption()\n
    '''
def hasNoheaderOption():
    '''returns boolean\n\n
    hasNoheaderOption()\n
    '''
def hasEncodingOption():
    '''returns boolean\n\n
    hasEncodingOption()\n
    '''
def getEncodingOption():
    '''returns String\n\n
    getEncodingOption()\n
    '''
def hasHelpOption():
    '''returns boolean\n\n
    hasHelpOption()\n
    '''
def getHelpOption():
    '''returns String\n\n
    getHelpOption()\n
    '''
def hasDosOption():
    '''returns boolean\n\n
    hasDosOption()\n
    '''
def hasUseInfOption():
    '''returns boolean\n\n
    hasUseInfOption()\n
    '''
def hasStrictIndividualsOption():
    '''returns boolean\n\n
    hasStrictIndividualsOption()\n
    '''
def hasIncludeSourceOption():
    '''returns boolean\n\n
    hasIncludeSourceOption()\n
    '''
def hasNoStrictOption():
    '''returns boolean\n\n
    hasNoStrictOption()\n
    '''
def getDeclarationProperty():
    '''returns Property\n\n
    getDeclarationProperty()\n
    '''
def getCommandLineForm():
    '''returns String\n\n
    getCommandLineForm()\n
    '''
