def column_names_info(column_name):
    col_values_dict = 'NA'
    if column_name == 'nact_status':
        col_values_dict = {'yes': ['yes', 'nact_given', 'nact given', 'nact_and_naht_given', 'naht given', 'naht_given'],
                    'no': ['no', 'nact not given', 'nact/naht not given', 'nact_naht_not_given'],
                    'NA': 'na',
                    'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                'requires follow up'],
                    'data_not_available': ['data not available', 'data_not_available', 'nan',
                                                'data not in report', 'data_not_availabel'],
                    'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                    }

    elif column_name == 'trastuzumab_use_nact':
        col_values_dict = {'sequential': 'sequential',
                             'concurrent': 'concurrent',
                             'NA': ['na', 'nact not given', 'nact/naht not given'],
                             'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                        'requires follow up', 'not certain, requires follow-up', 'follow-up required'],
                             'data_not_available': ['data not available', 'data_not_available',
                                                'data not in report', 'data_not_availabel'],
                             'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                             }

    elif column_name == 'chemotherapy_status':
        col_values_dict = {'yes': ['act_given', 'adjuvant chemotherapy given'],
                           'no': ['adjuvant chemotherapy not given', 'nact/naht not given'],
                           'requires_follow_up': ['requires_follow_up', 'requires follow-up',
                                                  'requires follow up', 'not certain, requires follow-up',
                                                  'follow-up required'],
                           'data_not_available': ['data not available', 'data_not_available', 'nan',
                                                  'data not in report', 'data_not_availabel'],
                           'lost_to_follow_up': [' lost to follow up', 'lost to follow up']
                           }

    return col_values_dict
