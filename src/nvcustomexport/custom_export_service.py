"""Provide a class for the custom template-based export service.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""


class CustomExportService:

    TEMPLATES = dict(
        _fileHeader='header.xml',
        _partTemplate='part_template.xml',
        _partEndTemplate='part_end_template.xml',
        _chapterTemplate='chapter_template.xml',
        _chapterEndTemplate='chapter_end_template.xml',
        _sectionTemplate='section_template.xml',
        _firstSectionTemplate='first_section_template.xml',
        _sectionDivider='section_divider.xml',
         )

    def set_custom_templates(self, model):
        exportClass = model.nvService.final_document_class()
        exportClass._firstSectionTemplate = '''<text:p text:style-name="Heading_20_6">$Viewpoint</text:p>\n'
$SectionContent
    '''

