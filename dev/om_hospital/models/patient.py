from  odoo import  fields , models , api, _

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patinet Records"


    name=fields.Char(string="Name",required=True,tracking=True)
    age=fields.Integer(string="Age",tracking=True)
    is_child=fields.Boolean(string="Is Child ?",tracking=True)
    notes=fields.Text(string="Notes",tracking=True)
    gender=fields.Selection([('male','Male'),('female','female'),('other','Other')],string='Gender',tracking=True)

    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 10:
            self.is_child=True
        else:
            self.is_child=False
