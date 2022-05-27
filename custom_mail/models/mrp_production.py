# -*- coding: utf-8 -*-

from odoo import models,fields,api ,_

class MrpProductionInherit(models.Model):
    
    _inherit="mrp.production"
    source_id = fields.Many2one('sale.order',string="Sale order", compute='_compute_source_id', store=True)
    def send_button_mail(self):
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = ir_model_data._xmlid_lookup('custom_mail.email_template_custom')[2]
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data._xmlid_lookup('mail.email_compose_message_wizard_form')[2]
        except ValueError:
            compose_form_id = False
        # self.write({'status':'envoye'})
        ctx = {
            'default_model': 'mrp.production',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'custom_layout': "mail.mail_notification_paynow",   
            'force_email': True,
        }
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx
        }

    @api.depends('origin')
    def _compute_source_id(self):
        for production in self :
            if production.origin :
                devis_name = production.origin.split('-')[-1].strip() 
                source = self.env['sale.order'].search([('name','=', devis_name)])
                if source :
                    try :
                        production.source_id = source 
                    except Exception as e:
                        production.source_id = False
                else :
                    production.source_id = False
                