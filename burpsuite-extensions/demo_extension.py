from burp import IBurpExtender

# https://portswigger.net/burp/help/extender.html
# https://www.foote.pub/2015/04/08/burp-extender-python.html


class BurpExtender(IBurpExtender):

    def registerExtenderCallbacks(self, callbacks):
        import sys
        sys.stdout = callbacks.getStdout()
        sys.stderr = callbacks.getStderr()

        import pdb; pdb.set_trace()

        return

        # 'callbacks.'TOOL_COMPARER',
        # 'callbacks.TOOL_DECODER',
        # 'callbacks.TOOL_EXTENDER',
        # 'callbacks.TOOL_INTRUDER',
        # 'callbacks.TOOL_PROXY',
        # 'callbacks.TOOL_REPEATER',
        # 'callbacks.TOOL_SCANNER',
        # 'callbacks.TOOL_SEQUENCER',
        # 'callbacks.TOOL_SPIDER',
        # 'callbacks.TOOL_SUITE',
        # 'callbacks.TOOL_TARGET',
        # 'callbacks.addScanIssue',
        # 'callbacks.addSuiteTab',
        # 'callbacks.addToSiteMap',
        # 'callbacks.applyMarkers',
        # 'callbacks.burpVersion',
        # 'callbacks.class',
        # 'callbacks.commandLineArguments',
        # 'callbacks.contextMenuFactories',
        # 'callbacks.cookieJarContents',
        # 'callbacks.createBurpCollaboratorClientContext',
        # 'callbacks.createMessageEditor',
        # 'callbacks.createTextEditor',
        # 'callbacks.customizeUiComponent',
        # 'callbacks.doActiveScan',
        # 'callbacks.doPassiveScan',
        # 'callbacks.equals',
        # 'callbacks.excludeFromScope',
        # 'callbacks.exitSuite',
        # 'callbacks.extensionBapp',
        # 'callbacks.extensionFilename',
        # 'callbacks.extensionName',
        # 'callbacks.extensionStateListeners',
        # 'callbacks.generateScanReport',
        # 'callbacks.getBurpVersion',
        # 'callbacks.getClass',
        # 'callbacks.getCommandLineArguments',
        # 'callbacks.getContextMenuFactories',
        # 'callbacks.getCookieJarContents',
        # 'callbacks.getExtensionFilename',
        # 'callbacks.getExtensionStateListeners',
        # 'callbacks.getHeaders',
        # 'callbacks.getHelpers',
        # 'callbacks.getHttpListeners',
        # 'callbacks.getIntruderPayloadGeneratorFactories',
        # 'callbacks.getIntruderPayloadProcessors',
        # 'callbacks.getMessageEditorTabFactories',
        # 'callbacks.getParameters',
        # 'callbacks.getProxyHistory',
        # 'callbacks.getProxyListeners',
        # 'callbacks.getScanIssues',
        # 'callbacks.getScannerChecks',
        # 'callbacks.getScannerInsertionPointProviders',
        # 'callbacks.getScannerListeners',
        # 'callbacks.getScopeChangeListeners',
        # 'callbacks.getSessionHandlingActions',
        # 'callbacks.getSiteMap',
        # 'callbacks.getStderr',
        # 'callbacks.getStdout',
        # 'callbacks.getToolName',
        # 'callbacks.hashCode',
        # 'callbacks.helpers',
        # 'callbacks.httpListeners',
        # 'callbacks.includeInScope',
        # 'callbacks.intruderPayloadGeneratorFactories',
        # 'callbacks.intruderPayloadProcessors',
        # 'callbacks.isExtensionBapp',
        # 'callbacks.isInScope',
        # 'callbacks.issueAlert',
        # 'callbacks.loadConfig',
        # 'callbacks.loadConfigFromJson',
        # 'callbacks.loadExtensionSetting',
        # 'callbacks.makeHttpRequest',
        # 'callbacks.messageEditorTabFactories',
        # 'callbacks.notify',
        # 'callbacks.notifyAll',
        # 'callbacks.printError',
        # 'callbacks.printOutput',
        # 'callbacks.proxyHistory',
        # 'callbacks.proxyInterceptionEnabled',
        # 'callbacks.proxyListeners',
        # 'callbacks.registerContextMenuFactory',
        # 'callbacks.registerExtensionStateListener',
        # 'callbacks.registerHttpListener',
        # 'callbacks.registerIntruderPayloadGeneratorFactory',
        # 'callbacks.registerIntruderPayloadProcessor',
        # 'callbacks.registerMenuItem',
        # 'callbacks.registerMessageEditorTabFactory',
        # 'callbacks.registerProxyListener',
        # 'callbacks.registerScannerCheck',
        # 'callbacks.registerScannerInsertionPointProvider',
        # 'callbacks.registerScannerListener',
        # 'callbacks.registerScopeChangeListener',
        # 'callbacks.registerSessionHandlingAction',
        # 'callbacks.removeContextMenuFactory',
        # 'callbacks.removeExtensionStateListener',
        # 'callbacks.removeHttpListener',
        # 'callbacks.removeIntruderPayloadGeneratorFactory',
        # 'callbacks.removeIntruderPayloadProcessor',
        # 'callbacks.removeMessageEditorTabFactory',
        # 'callbacks.removeProxyListener',
        # 'callbacks.removeScannerCheck',
        # 'callbacks.removeScannerInsertionPointProvider',
        # 'callbacks.removeScannerListener',
        # 'callbacks.removeScopeChangeListener',
        # 'callbacks.removeSessionHandlingAction',
        # 'callbacks.removeSuiteTab',
        # 'callbacks.restoreState',
        # 'callbacks.saveBuffersToTempFiles',
        # 'callbacks.saveConfig',
        # 'callbacks.saveConfigAsJson',
        # 'callbacks.saveExtensionSetting',
        # 'callbacks.saveState',
        # 'callbacks.saveToTempFile',
        # 'callbacks.scannerChecks',
        # 'callbacks.scannerInsertionPointProviders',
        # 'callbacks.scannerListeners',
        # 'callbacks.scopeChangeListeners',
        # 'callbacks.sendToComparer',
        # 'callbacks.sendToIntruder',
        # 'callbacks.sendToRepeater',
        # 'callbacks.sendToSpider',
        # 'callbacks.sessionHandlingActions',
        # 'callbacks.setExtensionName',
        # 'callbacks.setProxyInterceptionEnabled',
        # 'callbacks.stderr',
        # 'callbacks.stdout',
        # 'callbacks.toString',
        # 'callbacks.unloadExtension',
        # 'callbacks.updateCookieJar',
        # 'callbacks.wait']