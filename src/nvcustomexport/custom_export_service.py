"""Provide a class for the custom template-based export service.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_custom_export
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os

from nvcustomexport.nvcustomexport_globals import INSTALL_DIR
from nvcustomexport.nvcustomexport_globals import TEMPLATE_FOLDER
from nvlib.controller.services.service_base import ServiceBase


class CustomExportService(ServiceBase):

    def __init__(self, model, view, controller):
        super().__init__(model, view, controller)
        self.templateDir = None
        self.exportClass = self._mdl.nvService.final_document_class()
        self.defaultAppendedSectionTemplate = self.exportClass._appendedSectionTemplate
        self.defaultFileHeader = self.exportClass._fileHeader
        self.defaultPartTemplate = self.exportClass._partTemplate
        self.defaultPartEndTemplate = self.exportClass._partEndTemplate
        self.defaultChapterTemplate = self.exportClass._chapterTemplate
        self.defaultChapterEndTemplate = self.exportClass._chapterEndTemplate
        self.defaultSectionTemplate = self.exportClass._sectionTemplate
        self.defaultFirstSectionTemplate = self.exportClass._firstSectionTemplate
        self.defaultSectionDivider = self.exportClass._sectionDivider

    def set_template_dir(self):
        """Set the templateDir instance variable.
        
        First look for a template folder in the project directory.
        It there is none, look in the novelibre installation directory.
        Note: This is a separate method, so it can be overridden by superclasses.
        """
        try:
            self.templateDir = f'{os.path.dirname(self._mdl.prjFile.filePath)}/{TEMPLATE_FOLDER}'
        except:
            self.templateDir = ''
        if not os.path.isdir(self.templateDir):
            self.templateDir = f'{INSTALL_DIR}/{TEMPLATE_FOLDER}'

    def set_custom_templates(self):
        """Override class constants of the export class.
        
        Replace the template class constants of the export class 
        with custom templates, if any. Otherwise, reset them to default.
        """
        self.set_template_dir()
        self.exportClass._appendedSectionTemplate = self.get_template_str('appended_section_template.txt', self.defaultAppendedSectionTemplate)
        self.exportClass._fileHeader = self.get_template_str('header.txt', self.defaultFileHeader)
        self.exportClass._partTemplate = self.get_template_str('part_template.txt', self.defaultPartTemplate)
        self.exportClass._partEndTemplate = self.get_template_str('part_end_template.txt', self.defaultPartEndTemplate)
        self.exportClass._chapterTemplate = self.get_template_str('chapter_template.txt', self.defaultChapterTemplate)
        self.exportClass._chapterEndTemplate = self.get_template_str('chapter_end_template.txt', self.defaultChapterEndTemplate)
        self.exportClass._sectionTemplate = self.get_template_str('section_template.txt', self.defaultSectionTemplate)
        self.exportClass._firstSectionTemplate = self.get_template_str('first_section_template.txt', self.defaultFirstSectionTemplate)
        self.exportClass._sectionDivider = self.get_template_str('section_divider.txt', self.defaultSectionDivider)

    def get_template_str(self, fileName, defaultStr):
        """Return a template string.
        
        Return the string read from the file specified by fileName, if any. 
        Otherwise return defaultStr.
        """
        templateStr = defaultStr
        templateFile = os.path.join(self.templateDir, fileName)
        if os.path.isfile(templateFile):
            try:
                with open(templateFile, 'r', encoding='utf-8') as f:
                    templateStr = f.read()
            except Exception as ex:
                self._ui.show_error(
                    title='nv_custom_export plugin',
                    message=f'Cannot load custom template: {os.path.normpath(templateFile)}',
                    detail=str(ex),
                    )
        return templateStr

