from odoo import models, fields, api

class HospitalTreatmentWizard(models.TransientModel):
    _name = 'hospital.treatment.wizard'
    _description = 'Sales Description for Patient'

    product_ids = fields.Many2many('product.product', string='Products', required=True)
    quantity = fields.Integer(string='Quantity', default=1)
    def confirm_action(self):
        for wizard in self:
            selected_products = wizard.product_ids
            sale_order = self.env['sale.order'].create({
                'treatment_id': self.env.context.get('active_id'),
                'partner_id': self.env.context.get('active_id'),
                'order_line': [(0, 0, {
                    'product_id': product.id,
                    'name': product.name,
                    'product_uom_qty': wizard.quantity,
                    'price_unit': product.lst_price,

                }) for product in selected_products],
            })






