from odoo import _, api, fields, models
from odoo.exceptions import AccessError

class MaterialMaterial(models.Model):
    _name = 'material.material'
    _description = 'Material Material'


    code = fields.Char('Material Code',required=True)
    name = fields.Char('Material Name',required=True)
    type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton'),
    ], string='Material Type',required=True)
    buy_price = fields.Monetary('Buy Price',required=True)
    currency_id = fields.Many2one('res.currency', string='Currency',default=lambda self:self.env.user.company_id.currency_id,required=True)
    supplier_id = fields.Many2one('res.partner', string='Supplier',required=True)

    @api.onchange('buy_price')
    def _onchange_buy_price(self):
        if self.buy_price < 100:
            raise AccessError(_("Buy Price tidak boleh kurang dari 100"))

    @api.constrains("buy_price")
    def check_buy_price():
        for i in self:
            if i.buy_price < 100:
                raise AccessError(_("Buy Price tidak boleh kurang dari 100"))
