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
    def open_travel_list(self):
        # Define the logic to open the list of travels associated with the contact
        # You can navigate to the list view of travels here
        # Example: return an action to open the list view
        action = self.env.ref('contact_travel.action_voyage_list')
        result = action.read()[0]
        result['domain'] = [('partner_id', '=', self.id)]
        return result
