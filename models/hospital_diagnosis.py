from odoo import models, fields

class HospitalDiagnosis(models.Model):
    _name = 'hospital.diagnosis'
    _description = 'Diagnosis'

    disease_id = fields.Many2one('hospital.disease', string="Disease", required=True)
    user_id = fields.Many2one('res.users', string="patient", required=True)
    date = fields.Date(string="Date", default=fields.Date.today)
    diagnosis_type = fields.Selection(
        [('high', 'High'), ('medium', 'Medium'), ('low', 'Low')],
        string="Diagnosis Type",
        required=True
    )
    treatment_id = fields.Many2one('hospital.treatment',string="Treatment")

