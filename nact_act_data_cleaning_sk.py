import pandas as pd
import itertools
import nact_act_variable_dicts as var_dict

nact_act_data = pd.read_excel('D:\\Shweta\\HER2_TNBC\\er_pr_her2_data\\2021_26_07_nact_act_her2_data_from_all_db_sk.xlsx')

cols_to_be_curated = {'nact_status': 'nact_status_dict',
                          'trastuzumab_use_nact': 'trastuzumab_use_nact_dict',
                          'chemotherapy_status': 'adjuvant_chemotherapy_status_dict',
                          }

def get_value_from_key(vocab_dict, value):
    id_pos = [value in value_list for value_list in (vocab_dict.values())]
    key_reqd = list(itertools.compress(vocab_dict.keys(), id_pos))
    return key_reqd

key_reqd = get_value_from_key(var_dict.column_names_info('nact_status'), 'yes')

def nact_act_data_cleaning(nact_act_data):
    cols_nact_act = nact_act_data.columns
    key_values_all = []
    for col in cols_nact_act:
        col_dat = nact_act_data[col]
        if col in cols_to_be_curated.keys():
            print(col)
            key_values = []
            for value in col_dat:
                cleaned_value = str(value)
                cleaned_value = cleaned_value.lower()
                key_reqd = get_value_from_key(var_dict.column_names_info(col), cleaned_value)
                key_values.append(', '.join([str(elem) for elem in key_reqd]))
                print(key_reqd)
            nact_act_data[col + '_cleaned' ] = key_values
    return key_values_all, nact_act_data

values, nact_act_data_new = nact_act_data_cleaning(nact_act_data)

nact_act_data_new.to_excel('D:\\Shweta\\HER2_TNBC\\output_df_nact_act\\2021_26_07_nact_act_cleaned_sk.xlsx', index=False)
