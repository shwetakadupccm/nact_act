import pandas as pd
import re
import datetime

nact_act_rupali = pd.read_excel('D:\\Shweta\\HER2_TNBC\\rupalis_data\\HER2_799_for_Rupali_sk.xlsx')
tnbc_nact_act_rupali = pd.read_excel('D:\\Shweta\\HER2_TNBC\\rupalis_data\\TNBC_799_for_Rupali_sk.xlsx')

def change_format_of_drug_date(sx_df, dt_str = 'Sx Date'):
    dts = []
    for sx_dt in sx_df[dt_str]:
        print(sx_dt)
        match = re.search('\d{2}.\d{2}.\d{4}', str(sx_dt))
        print(match)
        if match is not None:
            dt = datetime.datetime.strptime(match.group(), '%d.%m.%Y').date()
            dts.append(str(dt))
        else:
            dts.append(sx_dt)
    return dts

dts = change_format_of_drug_date(nact_act_rupali, 'Date of drug prescription')

def change_format_of_sx_date(sx_df, dt_str = 'Sx Date'):
    dts = []
    for sx_dt in sx_df[dt_str]:
        print(sx_dt)
        match = re.search('\d{2}.\d{2}.\d{4}', str(sx_dt))
        print(match)
        if match is not None:
            dt = datetime.datetime.strptime(match.group(), '%d.%m.%Y').date()
            dts.append(str(dt))
        else:
            dts.append(sx_dt)
    return dts

def separated_nact_act_data(df, drug_dt_str = 'Date of drug prescription', sx_dt_str = 'surgery_date_from_ffpe',
                            drugs_given_str = 'drugs given'):
    drug_dt_cleaned = change_format_of_drug_date(df, drug_dt_str)
    sx_dt_cleaned = change_format_of_sx_date(df, sx_dt_str)
    pre_sx_dates = []
    post_sx_dates = []
    nact_drugs = []
    act_drugs = []

    for i in range(len(df)):
        print(i)
        drug_dt = drug_dt_cleaned[i]
        print(drug_dt)
        sx_dt = sx_dt_cleaned[i]
        print(sx_dt)
        if drug_dt < sx_dt:
            drugs_given = df[drugs_given_str][i]
            print(drugs_given)
            pre_sx_dates.append(drug_dt)
            post_sx_dates.append('NA')
            nact_drugs.append(drugs_given)
            act_drugs.append('data_not_available')
        elif drug_dt > sx_dt:
            drugs_given = df[drugs_given_str][i]
            print(drugs_given)
            post_sx_dates.append(drug_dt)
            pre_sx_dates.append('NA')
            act_drugs.append(drugs_given)
            nact_drugs.append('data_not_available')
        else:
            nact_drugs.append('data_not_available')
            act_drugs.append('data_not_available')
            pre_sx_dates.append('date_not_available')
            post_sx_dates.append('data_not_available')

    df['date_of_pre_sx_drug_given'] = pre_sx_dates
    df['date_of_post_sx_drug_given'] = post_sx_dates
    df['cleaned_sx_date'] = sx_dt_cleaned
    df['nact_drugs'] = nact_drugs
    df['act_drugs'] = act_drugs
    return df

df = separated_nact_act_data(tnbc_nact_act_rupali, drug_dt_str = 'Date of drug prescription', sx_dt_str = 'surgery_date',
                            drugs_given_str = 'drugs given_cleaned')

df.to_excel('D:\\Shweta\\HER2_TNBC\\2021_06_08_script_output_df\\2021_07_08_nact_act_data_separated_for_tnbc_sk.xlsx',
            index = False)

df_her2 = separated_nact_act_data(nact_act_rupali, drug_dt_str = 'Date of drug prescription', sx_dt_str = 'surgery_date_from_ffpe',
                            drugs_given_str = 'drugs given_cleaned')

df_her2.to_excel('D:\\Shweta\\HER2_TNBC\\2021_06_08_script_output_df\\2021_07_08_nact_act_data_separated_for_her2_sk.xlsx',
            index = False)

