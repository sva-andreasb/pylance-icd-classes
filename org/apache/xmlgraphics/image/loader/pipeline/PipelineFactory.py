def ():
    '''returns PipelineFactory\n\n
    (final ImageManager manager)\n
    '''
def newImageConverterPipeline():
    '''returns ImageProviderPipeline\n\n
    newImageConverterPipeline(final Image originalImage, final ImageFlavor targetFlavor)\n
    newImageConverterPipeline(final ImageInfo imageInfo, final ImageFlavor targetFlavor)\n
    '''
def determineCandidatePipelines():
    '''returns ImageProviderPipeline[]\n\n
    determineCandidatePipelines(final ImageInfo imageInfo, final ImageFlavor targetFlavor)\n
    determineCandidatePipelines(final ImageInfo imageInfo, final ImageFlavor[] flavors)\n
    determineCandidatePipelines(final Image sourceImage, final ImageFlavor[] flavors)\n
    '''
def compare():
    '''returns int\n\n
    compare(final Object o1, final Object o2)\n
    '''
