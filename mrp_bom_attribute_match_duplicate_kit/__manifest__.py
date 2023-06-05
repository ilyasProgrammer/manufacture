# Copyright 2023 Ooops. (https://www.ooops404.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    "name": "MRP BOM Attribute Match Duplicate Kit",
    "summary": "Duplicate product with MRP BOMs",
    "version": "14.0.1.0.0",
    "author": "Ooops, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/manufacture",
    "category": "MRP",
    "license": "AGPL-3",
    "depends": ["mrp_bom_attribute_match"],
    "data": [
        "data/action_data.xml",
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
}
