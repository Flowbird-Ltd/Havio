# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Contact(models.Model):
    _inherit = "res.partner"

    type = fields.Selection(
        [
            ('contact', 'Contact'),
            ('invoice', 'Invoice Address'),
            ('delivery', 'Delivery Address'),
            ('other', 'Other Address'),
            ("private", "Private Address"),
            ("site", "Site Address")
         ], string='Address Type',
        default='contact',
        help="Invoice & Delivery addresses are used in sales orders. "
             "Private addresses are only visible by authorized users."
    )
