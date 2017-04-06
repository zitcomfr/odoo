# -*- coding: utf-8 -*-
# Copyright 2017 <pverkest@anybox.fr>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Zit.com",
    "summary": "Zit.com custom stock configuration module",
    "version": "10.0.1.0.0",
    "category": "Uncategorized",
    "website": "https://zit.com/",
    "author": "Jean-Martial <jean-martial@zitcom.fr>",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
        "sale",
        "stock",
    ],
    "data": [
        'data/settings.xml',
        'data/location.xml',
        'data/warehouse.xml',
        'data/picking.type.xml',
        'data/route.xml',
        'views/res_partner.xml',
    ],
    "demo": [
        "demo/partner.xml",
        "demo/sales.xml",
    ],
}
