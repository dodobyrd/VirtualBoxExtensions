#!/bin/bash

# vbox_plugins controller
CTL="${BASEURL}index.php?/module/vbox_plugins/"

# Get the scripts in the proper directories
"${CURL[@]}" "${CTL}get_script/vbox_plugins.sh" -o "${MUNKIPATH}preflight.d/vbox_plugins.sh"

# Check exit status of curl
if [ $? = 0 ]; then
	# Make executable
	chmod a+x "${MUNKIPATH}preflight.d/vbox_plugins.sh"

	# Set preference to include this file in the preflight check
	setreportpref "vbox_plugins" "${CACHEPATH}vbox_plugins.txt"

else
	echo "Failed to download all required components!"
	rm -f "${MUNKIPATH}preflight.d/vbox_plugins.sh"

	# Signal that we had an error
	ERR=1
fi
