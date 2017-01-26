# -*- coding: utf-8 -*-
# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Zit.com",
    "summary": "Zit.com custom odoo module",
    "version": "10.0.1.0.0",
    "category": "Uncategorized",
    "website": "https://zit.com/",
    "author": "Jean-Martial <jean-martial@zitcom.fr>",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
        "crm",
        "l10n_fr",
    ],
    "data": [
        "views/zitcom_event_views.xml",
        "data/users.xml",
        "data/company.xml",
    ],
    "demo": [
    ],
}
