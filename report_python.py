from odoo import models, fields , api


class ReportTreatment(models.AbstractModel):
    _name = 'report.zydus_hospital.action_report_treatment'
    _description = 'Zydus Hospital Treatment Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['hospital.treatment'].browse(docids)

        return {
            'doc_ids': docids,
            'doc_model': 'hospital.treatment',
            'docs': docs,

        }