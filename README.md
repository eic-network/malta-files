# malta-files

Journalists working with EIC.network dug into hundreds of thousands of
documents that show how Malta operates a tax system where companies pay
the lowest tax on profits in the EU. Part of the data that was used for
this research is the public Malta Registry of Companies.

We have re-arranged, cleaned and made searchable in new ways the public
information contained in the register.

For more information about Malta Files investigation, see : https://eic.network/projects/malta-files

Keep in mind that the data we make available is only for information
purposes and does not indicate any illegal activity. For any current and
official status go to the Malta Registry of Companies here
http://rocsupport.mfsa.com.mt/pages/SearchCompanyInformation.aspx


# technical information

The files in this repository were produced by scraping, using [this code](
https://github.com/eic-network/malta-roc-scraper).
They are organized as follows:

* the raw data we scraped from the web is in the [companies](./companies) directory
  * each file is named after a company ID as found in the registry
  * each company contains all the details in the companies list, plus the extra information from the lookup information
* the script [extract-people.py](./extract_people.py) is used by calling `python ./extract_people.py`
  * this iterates over the companies data and extracts all entities (people and companies) that are declared as involved parties (e.g. shareholders)
  * the results are placed in the [entities](./entities) directory
    * there are two files (CSV and JSON) with **all** the results grouped together
    * the two directories ([csv](./entities/csv) and [json](./entities/json)) contain the same results, but grouped by nationality and in separate files
