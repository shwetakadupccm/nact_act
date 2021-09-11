import pandas as pd
import itertools
import re

cols_to_be_curated = 'drugs given'
nact_act_drug_dict = {'paclitaxel': ['paclitaxel', 'pacli', 'paclitaxel '],
                      'docetaxel': ['docetaxel', 'doce', 'docetare', 'docetere'],
                      'doxurubicin': ['doxurubicin', 'doxorubicin', 'doxo', 'doxoru'],
                      'cyclophosphamide': ['cyclophosphamide', 'cyclophospamide', 'cycloph', 'cyclophos', 'cylopho',
                                           'cylophos', 'cyclopho', 'cyclop', 'cyclo', 'cyclophosm', 'endoxan'],
                      'epirubicin': ['epirubicin', 'epirubi', 'epiru'],
                      'carboplatin': ['carboplatin', 'carbo', 'carbokem'],
                      'fluorouracil': ['fluorouracil', 'fluracil', 'flurarcil', 'fluracil'],
                      'gemcitabine': ['gemcitabine', 'gem'],
                      'cisplatin': 'cisplatin',
                      'trastuzumab': ['trastuzumab', 'transtuzumab', 'trastu', 'transtu', 'herceptin',
                                      'only trastu purchase bill'],
                      'T-DM1(trastuzumab_derivative': ['kadcyla'],
                      'harmonal_tablet': 'harmonal tablet',
                      'NA': ['na', 'nan']
                      }

def get_value_from_key(vocab_dict, value):
    id_pos = [value in value_list for value_list in (vocab_dict.values())]
    key_reqd = list(itertools.compress(vocab_dict.keys(), id_pos))
    return key_reqd

def cleaned_and_get_key_value(defined_dict_variable, val):
    split_val = val.split('+')
    lst = []
    for value in split_val:
        cleaned_value = re.sub('[^a-zA-Z]', '', value)
        cleaned_value = cleaned_value.lower()
        key_reqd = get_value_from_key(defined_dict_variable, cleaned_value)
        if key_reqd is not None:
            key_reqd_str = '; '.join(key_reqd)
            lst.append(key_reqd_str)
            while ('' in lst):
                lst.remove('')
        else:
            lst.append(key_reqd)
    return lst

def nact_act_drug_data_cleaning(nact_act_data):
    cols_nact_act = nact_act_data.columns
    key_values_all = []
    for col in cols_nact_act:
        col_dat = nact_act_data[col]
        if col == 'drugs given':
            print(col)
            key_values = []
            for value in col_dat:
                cleaned_value = str(value)
                cleaned_value = cleaned_value.lower()
                key_reqd = get_value_from_key(nact_act_drug_dict, cleaned_value)
                if len(key_reqd) != 0:
                    key_values.append(', '.join([str(elem) for elem in key_reqd]))
                    print(key_reqd)
                else:
                    key_reqd = cleaned_and_get_key_value(nact_act_drug_dict, value)
                    key_values.append(', '.join([str(elem) for elem in key_reqd]))
            nact_act_data[col + '_cleaned' ] = key_values
    return key_values_all, nact_act_data

tnbc_nact_act = pd.read_excel('D:\\Shweta\\HER2_TNBC\\rupalis_data\\TNBC_799_for_Rupali_sk.xlsx')
her2_nact_act = pd.read_excel('D:\\Shweta\\HER2_TNBC\\rupalis_data\\HER2_799_for_Rupali_sk.xlsx')

nact_act_data_tnbc = nact_act_drug_data_cleaning(tnbc_nact_act)
tnbc_nact_act.to_excel('D:\\Shweta\\HER2_TNBC\\rupalis_data\\TNBC_799_for_Rupali_sk.xlsx', index=False)

nact_act_data_her2 = nact_act_drug_data_cleaning(her2_nact_act)
her2_nact_act.to_excel('D:\\Shweta\\HER2_TNBC\\rupalis_data\\HER2_799_for_Rupali_sk.xlsx', index=False)

