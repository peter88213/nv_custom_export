"""Provide a class for the custom template-based export service.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
from pathlib import Path
from tkinter import messagebox


class CustomExportService:

    def __init__(self, model):
        self._mdl = model
        self.templateDir = None
        self.exportClass = self._mdl.nvService.final_document_class()
        self.defaultFileHeader = self.exportClass._fileHeader
        self.defaultPartTemplate = self.exportClass._partTemplate
        self.defaultPartEndTemplate = self.exportClass._partEndTemplate
        self.defaultChapterTemplate = self.exportClass._chapterTemplate
        self.defaultChapterEndTemplate = self.exportClass._chapterEndTemplate
        self.defaultSectionTemplate = self.exportClass._sectionTemplate
        self.defaultFirstSectionTemplate = self.exportClass._firstSectionTemplate
        self.defaultSectionDivider = self.exportClass._sectionDivider

    def set_template_dir(self):
        self.templateDir = f'{os.path.dirname(self._mdl.prjFile.filePath)}/nv_custom_export'
        if not os.path.isdir(self.templateDir):
            try:
                homeDir = str(Path.home()).replace('\\', '/')
                self.templateDir = os.path.join(homeDir, '.novx/nv_custom_export')
            except:
                return

            if not os.path.isdir(self.templateDir):
                return

    def set_custom_templates(self):
        self.set_template_dir()
        self.exportClass._fileHeader = self.get_template_text('header.txt', self.defaultFileHeader)
        self.exportClass._partTemplate = self.get_template_text('part_template.txt', self.defaultPartTemplate)
        self.exportClass._partEndTemplate = self.get_template_text('part_end_template.txt', self.defaultPartEndTemplate)
        self.exportClass._chapterTemplate = self.get_template_text('chapter_template.txt', self.defaultChapterTemplate)
        self.exportClass._chapterEndTemplate = self.get_template_text('chapter_end_template.txt', self.defaultChapterEndTemplate)
        self.exportClass._sectionTemplate = self.get_template_text('section_template.txt', self.defaultSectionTemplate)
        self.exportClass._firstSectionTemplate = self.get_template_text('first_section_template.txt', self.defaultFirstSectionTemplate)
        self.exportClass._sectionDivider = self.get_template_text('section_divider.txt', self.defaultSectionDivider)

    def get_template_text(self, fileName, default):
        templateText = default
        templateFile = os.path.join(self.templateDir, fileName)
        if os.path.isfile(templateFile):
            try:
                with open(templateFile, 'r', encoding='utf-8') as f:
                    templateText = f.read()
            except Exception as ex:
                messagebox.showerror(
                    title='nv_custom_export plugin',
                    message=f'Cannot load custom template: {os.path.normpath(templateFile)}',
                    detail=str(ex),
                    )
        return templateText

