# -*- coding: utf-8 -*-
# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields

class ZitcomEvent(models.Model):
    _name = "zitcom.event"

    # Attribut name sur chaque objet d'Odoo
    # https://www.odoo.com/documentation/10.0/reference/orm.html#fields
    name = fields.Char("title", required=True)
    