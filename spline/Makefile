#/***************************************************************************
# SplinePlugin
# 
#        begin                : 2013-10-02
#        copyright            : (C) 2013 by Radim Blažek
#        email                : radim.blazek@gmail.com
# ***************************************************************************/
# 
#/***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# ***************************************************************************/

# CONFIGURATION
PLUGIN_UPLOAD = $(CURDIR)/plugin_upload.py

# Makefile for a PyQGIS plugin 

# translation
SOURCES = __init__.py splineplugin.py
#TRANSLATIONS = i18n/splineplugin_en.ts
TRANSLATIONS = 

# global

PLUGINNAME = spline

PY_FILES = splineplugin.py __init__.py

EXTRAS = icon.png metadata.txt

PACKAGE_FILES = icon.png __init__.py metadata.txt resources_rc.py settingsdialog.py splineplugin.py spline.py splinetool.py ui_settingsdialog.py utils.py

UI_FILES = ui_settingsdialog.py

RESOURCE_FILES = resources_rc.py

HELP = help/build/html

default: compile

compile: $(UI_FILES) $(RESOURCE_FILES) 

%_rc.py : %.qrc $(EXTRAS)
	pyrcc4 -o $*_rc.py  $<

%.py : %.ui
	pyuic4 -o $@ $<

%.qm : %.ts
	lrelease $<

# The deploy  target only works on unix like operating system where
# the Python plugin directory is located at:
# $HOME/.qgis2/python/plugins
deploy: compile doc transcompile
	mkdir -p $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)
	cp -vf $(PY_FILES) $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)
	cp -vf $(UI_FILES) $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)
	cp -vf $(RESOURCE_FILES) $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)
	cp -vf $(EXTRAS) $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)
	cp -vfr i18n $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)
	cp -vfr $(HELP) $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)/help

# The dclean target removes compiled python files from plugin directory
# also delets any .svn entry
dclean:
	find $(HOME)/.qgis2/python/plugins/$(PLUGINNAME) -iname "*.pyc" -delete
	find $(HOME)/.qgis2/python/plugins/$(PLUGINNAME) -iname ".svn" -prune -exec rm -Rf {} \;

# The derase deletes deployed plugin
derase:
	rm -Rf $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)

# The zip target deploys the plugin and creates a zip file with the deployed
# content. You can then upload the zip file on http://plugins.qgis.org
zip: deploy dclean 
	rm -f $(PLUGINNAME).zip
	cd $(HOME)/.qgis2/python/plugins; zip -9r $(CURDIR)/$(PLUGINNAME).zip $(PLUGINNAME)

# Create a zip package of the plugin named $(PLUGINNAME).zip. 
# This requires use of git (your plugin development directory must be a 
# git repository).
# To use, pass a valid commit or tag as follows:
#   make package VERSION=Version_0.3.2
#package: compile
#		rm -f $(PLUGINNAME).zip
#		git archive --prefix=$(PLUGINNAME)/ -o $(PLUGINNAME).zip $(VERSION)
#		echo "Created package: $(PLUGINNAME).zip"

# How to add directory path in zip?
# To use, pass a version which has to be given to zip and help:
#   make package VERSION=0.1.0
package: compile
	rm -f spline*.zip
	rm -rf spline/
	mkdir spline
	cp $(PACKAGE_FILES) spline/
	#mkdir -p spline/help/build/
	#cp -r help/build/html spline/help/build/
	#cp -r help/build/html ../release/help.$(VERSION)
	zip -9r ../release/spline.$(VERSION).zip spline/
	rm -rf spline/
	echo "Created package: ../release/spline.$(VERSION).zip"
	echo "Created help: ../release/help.$(VERSION)"

upload: zip
	$(PLUGIN_UPLOAD) $(PLUGINNAME).zip

# transup
# update .ts translation files
transup:
	pylupdate4 Makefile

# transcompile
# compile translation files into .qm binary format
transcompile: $(TRANSLATIONS:.ts=.qm)

# transclean
# deletes all .qm files
transclean:
	rm -f i18n/*.qm

clean:
	rm $(UI_FILES) $(RESOURCE_FILES)

# build documentation with sphinx
doc: 
	cd help; make html
