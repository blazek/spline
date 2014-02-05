# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SplinePlugin
                             -------------------
        begin                : 2014-02-5
        copyright            : (C) 2013 by Radim Blažek
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
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "Spline"


def description():
    return "Digitize spline curves"


def version():
    return "Version 0.1"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "2.0"

def author():
    return "Radim Blazek"

def email():
    return "radim.blazek@gmail.com"

def classFactory(iface):
    from splineplugin import SplinePlugin
    return SplinePlugin(iface)
