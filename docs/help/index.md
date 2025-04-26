[Project homepage](https://github.com/peter88213/nv_custom_export) > [Index](../) > Help

---

A [novelibre](https://github.com/peter88213/novelibre/) plugin providing a custom template-based export for the final document.


**User guide**

This page refers to the latest `nv_custom_export
<https://github.com/peter88213/nv_custom_export/>`__ release.
You can open it with **Help > nv_custom_export Online help**.


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
- `first_section_template.txt`(applied  to sections at the beginning of the chapter)
- `section_divider.txt`(lead sections, beginning from the second in chapter)


## Placeholders

### Syntax

There are two options:

1.  `$Placeholder` - If the placeholder is followed by a character that
    is clearly recognizable as a separator, e.g. a blank.
2.  `${Placeholder}` - If the placeholder is followed by a character
    that is not recognizable as a separator.

### \"Project template\" placeholders

-   `$Title` - Project title
-   `$Desc` - Project description
-   `$AuthorName` - Author\'s name
-   `$Language` - Language code acc. to ISO 639-1
-   `$Country` - Country code acc. to ISO 3166-2
-   `$CustomPlotProgress` - Custom \"Plot progress\" field title
-   `$CustomCharacterization` - Custom \"Characterization\" field title
-   `$CustomWorldBuilding` - Custom \"World building\" field title
-   `$CustomGoal` - Custom \"Goal\" field title
-   `$CustomConflict` - Custom \"Conflict\" field title
-   `$CustomOutcome` - Custom \"Outcome\" field title
-   `$CustomChrBio` - Custom character \"Bio\" field title
-   `$CustomChrGoals` - Custom character \"Goals\" field title

### \"Chapter template\" placeholders

-   `$ID` - Chapter ID,
-   `$ChapterNumber` - Chapter number (in sort order),
-   `$Title` - Chapter title
-   `$Desc` - Chapter description
-   `$Epigraph` - Epigraph
-   `$EpigraphSrc` - Epigraph source
-   `$Notes` - Chapter notes
-   `$ProjectName` - URL-coded file name without suffix and extension
-   `$ProjectPath` - URL-coded fpath to the project directory
-   `$Language` - Language code acc. to ISO 639-1
-   `$Country` - Country code acc. to ISO 3166-2
-   `$ManuscriptSuffix` - File name suffix of the manuscript

### \"Section template\" placeholders

-   `$ID` - Section ID,
-   `$SectionNumber` - Section number (in sort order),
-   `$Title` - Section title
-   `$Desc` - Section description
-   `$WordCount` - Section word count
-   `$WordsTotal` - Accumulated word count including the current section
-   `$Status` - Section status (Outline, Draft etc.)
-   `$SectionContent` - Section content
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
-   `$Goal` - The section protagonist\'s goal
-   `$Conflict` - The section conflict
-   `$Outcome` - The section outcome
-   `$Tags` - Comma-separated list of section tags
-   `$Characters` - Comma-separated list of characters assigned to the
    section
-   `$Viewpoint` - Viewpoint character
-   `$Locations` - Comma-separated list of locations assigned to the
    section
-   `$Items` - Comma-separated list of items assigned to the section
-   `$Notes` - Section notes
-   `$ProjectName` - URL-coded file name without suffix and extension
-   `$ProjectPath` - URL-coded fpath to the project directory
-   `$Language` - Language code acc. to ISO 639-1
-   `$Country` - Country code acc. to ISO 3166-2
-   `$ManuscriptSuffix` - File name suffix of the manuscript
-   `$SectionsSuffix` - File name suffix of the section descriptions
-   `$CustomPlotProgress` - Custom \"Plot progress\" field title
-   `$CustomCharacterization` - Custom \"Characterization\" field title
-   `$CustomWorldBuilding` - Custom \"World building\" field title
-   `$CustomGoal` - Custom \"Goal\" field title
-   `$CustomConflict` - Custom \"Conflict\" field title
-   `$CustomOutcome` - Custom \"Outcome\" field title

