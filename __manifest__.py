{
    'name': 'Hospital Management System',
    'version': '1.0',
    'category': 'Healthcare',
    'author': 'Harsh',
    'depends': ['base','sale'],
    'data': [
        'views/hospital_menu.xml',
        'views/hospital_patient_views.xml',
        'views/hospital_physician_views.xml',
        'security/ir.model.access.csv',
        'views/hospital_specialty_views.xml',
        'data/hospital_treatment_actions.xml',
        'views/hospital_treatment_views.xml',
        'wizard/hospital_treatment_wizard_views.xml',
        'views/sale_order_views.xml',
        'views/hospital_diagnosis_views.xml',
        'views/hospital_disease_views.xml',
        'data/hospital_treatment_sequence.xml',
        'report/report_template.xml',
        'report/report_action.xml',

    ],
    'installable': True,
    'application': True,
}

