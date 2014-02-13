# -*- coding: latin1 -*-
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

# Initialize Qt resources from file resources.py
#from cadtools import resources

#Import own classes and tools
from spline import Spline

class SplineTool():
    
        def __init__(self, iface):
            # Save reference to the QGIS interface
            self.iface = iface
            self.canvas = self.iface.mapCanvas()
            mc = self.canvas
            self.tool = None
            self.connectedLayer = None
            
            # Create actions 
            self.action_spline = QAction(QIcon(":/plugins/spline/icon.png"), QCoreApplication.translate("spline", "Digitize Spline Curves"),  self.iface.mainWindow())
            self.action_spline.setObjectName("actionSpline")
            self.action_spline.setEnabled(False)
            self.action_spline.setCheckable(True)            
            
            # Get the tool
            self.tool = Spline(self.iface)

            # Connect to signals for button behaviour
            self.action_spline.triggered.connect(self.digitize)
            self.iface.currentLayerChanged.connect(self.layerChanged)
            self.layerChanged() # to enable when plugin is loaded

            mc.mapToolSet.connect(self.deactivate)
            
            # Add actions to the toolbar
            self.iface.addToolBarIcon(self.action_spline)
                        
        def __del__(self):
            self.disconnectLayer()
            self.iface.removeToolBarIcon(self.action_spline)
         
        def digitize(self):
            mc = self.canvas
            layer = mc.currentLayer()
            
            mc.setMapTool(self.tool)
            self.action_spline.setChecked(True)    
           
        # get current layer if it is line or polygon, otherwise None
        def getLayer(self):
            layer = self.canvas.currentLayer()
            if layer is None: return None
            if layer.type() != QgsMapLayer.VectorLayer: return None
            if not layer.geometryType() in [ QGis.Line, QGis.Polygon ]: return None
            return layer
 
        def enableAction(self):
            self.action_spline.setEnabled(False)
            layer = self.getLayer()
            if layer:
                self.action_spline.setEnabled( layer.isEditable() )
                
        def layerChanged(self):
            self.tool.deactivate()
            self.enableAction() 
            self.disconnectLayer()
            self.connectLayer( self.getLayer() )
        
        def connectLayer(self, layer):
            if layer is None: return
            self.connectedLayer = layer
            layer.editingStopped.connect(self.enableAction)
            layer.editingStarted.connect(self.enableAction)

        def disconnectLayer(self):
            if self.connectedLayer is None: return
            self.connectedLayer.editingStopped.disconnect(self.enableAction)
            self.connectedLayer.editingStarted.disconnect(self.enableAction)
            self.connectedLayer = None
            
        def deactivate(self):
            self.action_spline.setChecked(False)

        def settingsChanged(self):
            self.tool.refresh()
            
