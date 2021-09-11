import pandas as pd

tnbc_nact_act = pd.read_excel('D:\\Shweta\\HER2_TNBC\\rupalis_data\\TNBC_799_for_Rupali_sk.xlsx')
her2_nact_act = pd.read_excel('D:\\Shweta\\HER2_TNBC\\rupalis_data\\HER2_799_for_Rupali_sk.xlsx')

tnbc_nact_act['drugs given'].unique()
her2_nact_act['drugs given'].unique()

nact_act_drug_dict = {'paclitaxel': ['paclitaxel', 'pacli'],
                      'docetaxel': ['docetaxel', 'doce', 'docetare', 'docetere'],
                      'doxurubicin': ['doxurubicin', 'doxorubicin', 'doxo', 'doxoru'],
                      'cyclophosphamide': ['cyclophosphamide', 'cyclophospamide', 'cycloph', 'cyclophos', 'cylopho',
                                           'cylophos', 'cyclopho', 'cyclop', 'cyclo', 'cyclophosm', 'endoxan'],
                      'epirubicin': ['epirubicin', 'epirubi', 'epiru'],
                      'carboplatin': ['carboplatin', 'carbo', 'carbokem'],
                      'fluorouracil': ['fluorouracil', 'fluracil', 'flurarcil', 'fluracil'],
                      'gemcitabine': ['gemcitabine', 'gem'],
                      'cisplatin': 'cisplatin',
                      'trastuzumab': ['trastuzumab', 'trastu', 'transtu', 'herceptin']
                      }