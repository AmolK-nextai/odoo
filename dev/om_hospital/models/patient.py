from  odoo import  fields , models , api

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patinet Records"


    name=fields.Char(string="Name",required=True)
    age=fields.Integer(string="Age")
    is_child=fields.Boolean(string="Is Child ?")
    notes=fields.Text(string="Notes")
    gender=fields.Selection([('male','Male'),('female','female'),('other','Other')],string='Gender')

