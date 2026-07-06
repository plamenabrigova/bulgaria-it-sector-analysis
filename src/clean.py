import pandas as pd
from src.config import RAW_FOLDER, EU27, NACE_FILTER, CLOUD_SIZE_EMP, CLOUD_INDIC_IS


def _melt_and_clean(geo, df):
    # Shared melt and flag-stripping logic for all datasets.
    year_cols = df.columns[1:]
    df_long = pd.concat([geo, df[year_cols]], axis=1)
    df_long = df_long.melt(id_vars=['geo'],
                           var_name='year',
                           value_name='raw_value')

    df_long['value'] = (df_long['raw_value']
                        .str.strip()
                        .str.extract(r'^([\d.]+)'))

    df_long['value'] = pd.to_numeric(df_long['value'], errors='coerce')
    df_long['year'] = df_long['year'].str.strip().astype(int)

    df_clean = df_long.dropna(subset=['value'])
    return df_clean[df_clean['geo'].isin(EU27)].reset_index(drop=True)


def clean_stats(filepath):
    # Clean datasets with 3-part composite key: freq, nace_r2, geo
    df = pd.read_table(filepath)

    key_col = df.columns[0]
    keys = df[key_col].str.split(',', expand=True)
    keys.columns = ['freq', 'nace_r2', 'geo']

    mask = keys['nace_r2'] == NACE_FILTER
    keys = keys[mask].reset_index(drop=True)
    df = df[mask].reset_index(drop=True)

    geo = keys['geo']
    geo.name = 'geo'

    return _melt_and_clean(geo, df)


def clean_cloud_adop(filepath):
    # Cleans cloud adoption dataset with 6-part composite key
    df = pd.read_table(filepath)

    key_col = df.columns[0]
    keys = df[key_col].str.split(',', expand=True)
    keys.columns = ['freq', 'size_emp', 'nace_r2', 'indic_is', 'unit', 'geo']

    mask = (keys['size_emp'] == CLOUD_SIZE_EMP) & (keys['indic_is'] == CLOUD_INDIC_IS)
    keys = keys[mask].reset_index(drop=True)
    df = df[mask].reset_index(drop=True)

    geo = keys['geo']
    geo.name = 'geo'

    return _melt_and_clean(geo, df)
