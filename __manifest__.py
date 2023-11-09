{
    'name': "contact_travel",
    'version': '1.0',
    'depends': ['base'],
    'author': "maroua",
    'category': 'Uncategorized',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'views/contact_views.xml',
        'views/show_voyage_views.xml',
    ],
    # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
    'license': 'AGPL-3',
    'installable': True,
}