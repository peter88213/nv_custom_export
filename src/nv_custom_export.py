"""novelibre plugin for template-based export of the final document. 

Requires Python 3.6+
Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_custom_export
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""
import webbrowser

from nvlib.controller.plugin.plugin_base import PluginBase
from nvcustomexport.custom_export_service import CustomExportService


class Plugin(PluginBase):
    """Template plugin class."""
    VERSION = '@release'
    API_VERSION = '5.23'
    DESCRIPTION = 'Custom template-based export for the final document'
    URL = 'https://github.com/peter88213/nv_custom_export'

    HELP_URL = 'https://peter88213.github.io/nv_custom_export/help/'

    def install(self, model, view, controller):
        """Install the plugin.
        
        Positional arguments:
            model -- reference to the novelibre main model instance.
            view -- reference to the novelibre main view instance.
            controller -- reference to the novelibre main controller instance.

        Extends the superclass method.
        """
        super().install(model, view, controller)

        # Add an entry to the Help menu.
        self._ui.helpMenu.add_command(
            label='nv_custom_export Online help',
            command=self.open_help,
        )

        # Start the service.
        self.customExportService = CustomExportService(model, view, controller)

    def on_open(self):
        """Actions to be performed after a project is opened."""
        self.customExportService.set_custom_templates()

    def open_help(self):
        webbrowser.open(self.HELP_URL)

