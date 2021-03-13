# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenUpgrade module for Odoo
#    @copyright 2015-Today: Odoo Community Association
#    @author: Stephane LE CORNEC
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

#from openupgradelib import openupgrade


#@openupgrade.migrate()
#def migrate(cr, version):
#   # because this module is renamed, we need to inforce load of this data
#    openupgrade.load_data(
#        cr, 'l10n_ar_aeroo_einvoice', 'migrations/9.0.1.2.0/mig_data.xml')

from openupgradelib import openupgrade
from odoo.modules.module import get_module_resource
import base64


@openupgrade.migrate()
def migrate(env, version):
    aeroo_report = env.ref('l10n_ar_aeroo_einvoice.action_aeroo_report_ar_einvoice', raise_if_not_found=False)
    if aeroo_report:
        default_reports = ['l10n_ar_aeroo_einvoice/einvoice_with_footer.odt', 'l10n_ar_aeroo_einvoice/einvoice.odt']
        if aeroo_report.tml_source == 'file' and aeroo_report.report_file in default_reports:
            new_background = get_module_resource('l10n_ar_aeroo_einvoice', 'einvoice.png')
            file_content = open(new_background, 'rb').read()
            aeroo_report.background_image = base64.b64encode(file_content)
