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
        "sale_stock",
    ],
    "data": [
        'data/settings.xml',
        'data/location.xml',
        'data/warehouse.xml',
        'data/picking.type.xml',
        'data/route.xml',
        'views/res_partner.xml',
        # Les 2 Fichiers suivant devrait-être chargé dans les données de démo
        # "(cf ci-dessous demo []), on les chages ici pour tester sans être
        # pollué par les données de démo des autres modules.
        "demo/partner.xml",
        "demo/product.xml",
        "demo/sales.xml",
    ],
    "demo": [
        # "demo/partner.xml",
        # "demo/sales.xml",
    ],
}
