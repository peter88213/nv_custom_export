[Project homepage](https://github.com/peter88213/nv_custom_export) > [Index](../) > Help

---

A [novelibre](https://github.com/peter88213/novelibre/) plugin providing a custom template-based export for the final document.


**User guide**

This page refers to the latest `nv_custom_export
<https://github.com/peter88213/nv_custom_export/>`__ release.
You can open it with **Help > nv_custom_export Online help**.

---

**Important**

The *nv_custom_export* plugin processes text files to generate code according to the 
[OpenDocument XML file format](https://en.wikipedia.org/wiki/OpenDocument_technical_specification#content.xml). 
I highly recommend that you familiarize yourself with this XML format before creating your 
own templates. If you do something wrong, *novelibre* may generate a text document that cannot 
be opened by OpenOffice/LibreOffice. In an emergency, simply delete your self-generated 
template files or uninstall the *nv_custom_export* plugin via the Plugin manager. 

The best way to get started is to experiment with the examples provided (see below).

---


## Configuration

Configuration is done by providing your custom template files either globally
or locally in a template folder. 
If there is no template folder at all, the *novelibre* default templates are applied.
 

### Global templates

Optional global templates are applied to all of your *novelibre* projects
that have no local templates (see below).

Place a subfolder named `nv_custom_export` in your *novelibre* installation  directory.
It contains all template files to be applied. 
The best way is to copy the provided sample template files (see below) and customize 
them with a text editor according to your needs.


### Local templates

Optional local templates are used prior to global templates, if any.

Place a subfolder named `nv_custom_export` in your project directory.
It contains all template files to be applied to this project. 
The best way is to copy the provided sample template files (see below) and customize 
them with a text editor according to your needs.


## Examples

The installation includes a directory named `nv_custom_export_sample` containing several 
subdirectories with example templates for different purposes. 
Please refer to the included README files for documentation.


# Reference

## Templates

### Project level templates

- `header.txt`

### Chapter level templates

- `part_template.txt`(part header; applied to all "normal" parts)
- `chapter_template.txt`(chapter header; applied to all "normal" chapters)
- `part_end_template.txt`(part footer; applied to all "normal" parts)
- `chapter_end_template.txt`(chapter footer; applied to all "normal" chapters)


### Section level templates

- `section_template.txt`(applied to "normal" sections within "normal" chapters)
- `appended_section_template.txt`(optional; applied to "normal" sections that are appended to the previous one)
- `first_section_template.txt`(optional; applied  to "normal" sections at the beginning of the chapter)
- `section_divider.txt`(lead sections, beginning from the second in chapter)


## Placeholders

### Syntax

There are two options:

1.  `$Placeholder` - If the placeholder is followed by a character that
    is clearly recognizable as a separator, e.g. a blank.
2.  `${Placeholder}` - If the placeholder is followed by a character
    that is not recognizable as a separator.

### "Project template" placeholders

-   `$Title` - Project title
-   `$Desc` - Project description consisting of ready-formatted paragraphs
-   `$AuthorName` - Author\'s name
-   `$Language` - Language code acc. to ISO 639-1
-   `$Country` - Country code acc. to ISO 3166-2
-   `$CustomPlotProgress` - Custom "Plot progress" field title
-   `$CustomCharacterization` - Custom "Characterization" field title
-   `$CustomWorldBuilding` - Custom "World building" field title
-   `$CustomGoal` - Custom "Goal" field title
-   `$CustomConflict` - Custom "Conflict" field title
-   `$CustomOutcome` - Custom "Outcome" field title
-   `$CustomChrBio` - Custom character "Bio" field title
-   `$CustomChrGoals` - Custom character "Goals" field title

### "Chapter template" placeholders

-   `$ID` - Chapter ID,
-   `$ChapterNumber` - Chapter number (in sort order),
-   `$Title` - Chapter title
-   `$Desc` - Chapter description consisting of ready-formatted paragraphs
-   `$Epigraph` - Epigraph consisting of ready-formatted paragraphs
-   `$EpigraphSrc` - Epigraph source
-   `$Notes` - Chapter notes consisting of ready-formatted paragraphs
-   `$ProjectName` - URL-coded file name without suffix and extension
-   `$ProjectPath` - URL-coded fpath to the project directory
-   `$Language` - Language code acc. to ISO 639-1
-   `$Country` - Country code acc. to ISO 3166-2
-   `$ManuscriptSuffix` - File name suffix of the manuscript

### "Section template" placeholders

-   `$ID` - Section ID,
-   `$SectionNumber` - Section number (in sort order),
-   `$Title` - Section title
-   `$Desc` - Section description consisting of ready-formatted paragraphs
-   `$WordCount` - Section word count
-   `$WordsTotal` - Accumulated word count including the current section
-   `$Status` - Section status (Outline, Draft etc.)
-   `$SectionContent` - Section content consisting of ready-formatted paragraphs
-   `$Date` - Specific section date (YYYY-MM-DD)
-   `$Time` - Time section begins: (hh:mm)
-   `$OdsTime` - Time section begins: (PThhHmmMssS)
-   `$Day` - Day section begins
-   `$ScDate` - Date or day (localized)
-   `$DateYear` - Year
-   `$DateMonth` - Month (number)
-   `$DateDay` - Day (number)
-   `$DateWeekday` - Day of the week (name)
-   `$MonthName` - Month (name)
-   `$LastsDays` - Amount of time section lasts: days
-   `$LastsHours` - Amount of time section lasts: hours
-   `$LastsMinutes` - Amount of time section lasts: minutes
-   `Duration` - Combination of days and hours and minutes
-   `$Scene` - The sections\'s kind of scene, if any
-   `$Goal` - The section protagonist\'s goal consisting of ready-formatted paragraphs
-   `$Conflict` - The section conflict consisting of ready-formatted paragraphs
-   `$Outcome` - The section outcome consisting of ready-formatted paragraphs
-   `$Tags` - Comma-separated list of section tags
-   `$Characters` - Comma-separated list of characters assigned to the
    section
-   `$Viewpoint` - Viewpoint character
-   `$Locations` - Comma-separated list of locations assigned to the
    section
-   `$Items` - Comma-separated list of items assigned to the section
-   `$Notes` - Section notes consisting of ready-formatted paragraphs
-   `$ProjectName` - URL-coded file name without suffix and extension
-   `$ProjectPath` - URL-coded fpath to the project directory
-   `$Language` - Language code acc. to ISO 639-1
-   `$Country` - Country code acc. to ISO 3166-2
-   `$ManuscriptSuffix` - File name suffix of the manuscript
-   `$SectionsSuffix` - File name suffix of the section descriptions
-   `$CustomPlotProgress` - Custom "Plot progress" field title
-   `$CustomCharacterization` - Custom "Characterization" field title
-   `$CustomWorldBuilding` - Custom "World building" field title
-   `$CustomGoal` - Custom "Goal" field title
-   `$CustomConflict` - Custom "Conflict" field title
-   `$CustomOutcome` - Custom "Outcome" field title

