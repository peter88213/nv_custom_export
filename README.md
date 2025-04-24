# nv_custom_export

The [novelibre](https://github.com/peter88213/novelibre/) Python program helps authors organize novels.  

The user can provide custom export templates either locally in the project folder, or globally in the installation folder. 
*novelibre* shall import the templates and apply them for the final document export.
 

### Project level templates

- `header.xml`

### Chapter level templates

- `part_template.xml`(part header; applied to all "normal" parts)
- `chapter_template.xml`(chapter header; applied to all "normal" chapters)
- `part_end_template.xml`(part footer; applied to all "normal" parts)
- `chapter_end_template.xml`(chapter footer; applied to all "normal" chapters)



### Section level templates

- `section_template.xml`(applied to "normal" sections within "normal" chapters)
- `first_section_template.xml`(applied  to sections at the beginning of the chapter)
- `section_divider.xml`(lead sections, beginning from the second in chapter)


![Screenshot](docs/Screenshots/screen01.png)

## Requirements

- [novelibre](https://github.com/peter88213/novelibre/) version 5.22+

## Download and install

### Default: Executable Python zip archive

Download the latest release [nv_custom_export_v0.1.0.pyzw](https://github.com/peter88213/nv_custom_export/raw/main/dist/nv_custom_export_v0.1.0.pyzw)

- Launch *nv_custom_export_v0.1.0.pyzw* by double-clicking (Windows/Linux desktop),
- or execute `python nv_custom_export_v0.1.0.pyzw` (Windows), resp. `python3 nv_custom_export_v0.1.0.pyzw` (Linux) on the command line.

#### Important

Many web browsers recognize the download as an executable file and offer to open it immediately. 
This starts the installation.

However, depending on your security settings, your browser may 
initially  refuse  to download the executable file. 
In this case, your confirmation or an additional action is required. 
If this is not possible, you have the option of downloading 
the zip file. 


### Alternative: Zip file

The package is also available in zip format: [nv_custom_export_v0.1.0.zip](https://github.com/peter88213/nv_custom_export/raw/main/dist/nv_custom_export_v0.1.0.zip)

- Extract the *nv_custom_export_v0.1.0* folder from the downloaded zipfile "nv_custom_export_v0.1.0.zip".
- Move into this new folder and launch *setup.pyw* by double-clicking (Windows/Linux desktop), 
- or execute `python setup.pyw` (Windows), resp. `python3 setup.pyw` (Linux) on the command line.

---

[Changelog](docs/changelog.md)

## Usage

See the [online manual](docs/usage.md)

---

## License

This is Open Source software, and the *nv_custom_export* plugin is licensed under GPLv3. See the
[GNU General Public License website](https://www.gnu.org/licenses/gpl-3.0.en.html) for more
details, or consult the [LICENSE](https://github.com/peter88213/nv_custom_export/blob/main/LICENSE) file.
