from odoo import models, fields, api

class Voyage(models.Model):
    _name = 'contact_travel.voyage'
    _description = 'Voyage Information'

    name = fields.Char(string='Voyage Name', required=True)
    depart_date = fields.Date(string='Departure Date', required=True)
    destination = fields.Char(string='Destination', required=True)
    
    # on utilise Many2many car un voyage peut etre lier a plusieurs contacts
    partner_id = fields.Many2one('res.partner', string='Contact')

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Add this method
    def open_voyage_list(self):
        # quand l'utilisateur click sur le bouton il sera deriger vers la vue contenante la liste des voyages
        action = self.env.ref('contact_travel.show_voyage_list')
        result = action.read()[0]
        result['domain'] = [('partner_id', '=', self.id)]
        return result
