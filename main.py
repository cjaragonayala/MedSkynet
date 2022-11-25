import json

db = {
        'roe':
        {
            'hp':
            {
                'flu': {'def':'gripe comun',
                        'tto':'acetaminophen'},
                'odynophagia': {'def': 'dolor garganta',
                                'tto': 'ibuprofen'}
            }
        }
    }


print(db['roe']['hp']['flu']['def'])

