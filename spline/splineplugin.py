# -*- coding: utf-8 -*-
"""
/***************************************************************************
                     SplinePlugin QGIS plugin
                              -------------------
        begin                : 2014-02-05
        copyright            : (C) 2014 by Radim Blažek
        email                : radim.blazek@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
import os.path

from splinetool import SplineTool

from settingsdialog import SettingsDialog

class SplinePlugin:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

        # There is bug in SIP (Transfer of QgsMapRenderer) 
        # http://lists.osgeo.org/pipermail/qgis-developer/2013-December/029816.html
        # so we have to keep reference to QgsMapRenderer
        self.mapRenderer = iface.mapCanvas().mapRenderer()

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'splineplugin_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

    def initGui(self):
        self.settingsAction = QAction( QCoreApplication.translate("Spline", "Settings" ), self.iface.mainWindow() )
        self.settingsAction.setObjectName("splineAction")
        self.settingsAction.triggered.connect(self.openSettings)

        self.iface.addPluginToVectorMenu(u"Digitize Spline", self.settingsAction)

        self.spline = SplineTool(self.iface)


    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginVectorMenu(u"Digitize Spline", self.settingsAction )
        del self.spline # removes its action from toolbar

    def run(self):
        pass

    def openSettings(self):
        # button signals in SettingsDialog were not working on Win7/64
        # if SettingsDialog was created with iface.mainWindow() as parent
        #self.settingsDialog = SettingsDialog(self.iface.mainWindow())
        self.settingsDialog = SettingsDialog()
        self.settingsDialog.changed.connect( self.spline.settingsChanged )
        self.settingsDialog.show()
        

