# Custom Accounting

[![Odoo version](https://img.shields.io/badge/Odoo-12.0-brightgreen.png?style=flat-square)](https://github.com/luximgroup/accounting)

## Custom accounting related modules

This repository is meant to cover accounting customizations mostly 
aimed to improve the compatibility with our other custom modules and 
real life needs of our customers.

The Slovenian account chart module uses the same name as the original 
module to ease the installation on our own infrastructure when creating 
new databases with company country as Slovenia. To override the original 
module this repository has to be placed in front of the odoo addons 
repository in the server conf file.

## Contents

**Legend:**   ☐ Todo | ☑ Done

----

### ☑ Slovenian Accounting Chart
    l10n_si
    
* Updated Chart
* Updated and upgraded taxes
* Added slovenian banks (BIC codes)

### ☑ Invoice Service Date
    l10n_si_invoice_report

* Added service date (as date in the original) and invoice creation 
  date as required in slovenian accounting standards
* Added VAT summary at the bottom of the invoice report   

### PLANNED TO DO:
#### ☐ Better usage of fiscal positions and export related statements on the report


Maintainer
----------

[![LUXIM d.o.o.](https://static.luxim.si/luxim-logo.png)](https://luxim.si)

This suite of modules is maintained by LUXIM d.o.o.

LUXIM d.o.o. is a company dedicated to the development of project tools and 
project solutions.
