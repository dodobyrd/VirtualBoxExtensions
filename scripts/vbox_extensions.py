#!/usr/bin/python2.7
"""
Adds VirtualBox plugin listing
"""
import os
import sys
import CoreFoundation

"""
We had a request to find a particular plugin for VirtualBox
which requires a license. To appropriately determine an
accurate number, we've added an additional module to munkireport
"""

extension_pack_list = []

def get_virtualbox_plugins():
    #VirtualBox stores its plugins within the application bundle
    vbox_plugin_folder = "/Applications/VirtualBox.app/Contents/MacOS/ExtensionPacks"
    #List the contents of the directory
    virtualbox_plugins = os.listdir(vbox_plugin_folder)
    #let us know if you found anything
    print "Found %i in plugin folder" % len(virtualbox_plugins)
    for plugin in virtualbox_plugins:
        extension_pack_list.append(plugin)

def main():
    '''Main'''
    # Create cache dir if it does not exist
    cachedir = '%s/cache' % os.path.dirname(os.path.realpath(__file__))
    if not os.path.exists(cachedir):
        os.makedirs(cachedir)

    # Skip manual check
    if len(sys.argv) > 1:
        if sys.argv[1] == 'manualcheck':
            print 'Manual check: skipping'
            exit(0)

    # Get any existing virtualbox_plugins
    get_virtualbox_plugins()

    # Write results to cache
    extension_packs_file = open(os.path.join(cachedir, 'virtualbox_plugins.txt'), 'w+')
    for plugin in extension_pack_list:
        extension_packs_file.write(plugin)
        extension_packs_file.write('\n')
    extension_packs_file.close()

if __name__ == "__main__":
    main()