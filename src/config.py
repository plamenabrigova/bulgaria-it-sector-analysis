from pathlib import Path

# Project root
ROOT = Path(__file__).resolve().parent.parent

# Data folders
RAW_FOLDER = ROOT / 'data' / 'raw'
CLEAN_FOLDER = ROOT / 'data' / 'clean'

# Raw file names
FILES = {
    'it_in_total':    'Percentage of the ICT sector personnel in total employment.tsv',
    'it_gross_value': 'Percentage of the ICT sector in Gross value added.tsv',
    'it_change_value': 'Percentage change of value added by ICT sector at current prices.tsv',
}

# Datasets that use the simple 3-part composite key (freq, nace_r2, geo)
# cloud_adoption is excluded because it has a 6-part key and requires its own cleaning function
SIMPLE_FILES = {k: v for k, v in FILES.items() if k != 'cloud_adoption'}

GEO_CODE_FIXES = {
    "EL": "GR",  # Eurostat uses EL for Greece; standardize to ISO GR
}

# EU27 country codes
EU27 = ['AT', 'BE', 'BG', 'CY', 'CZ', 'DE', 'DK', 'EE', 'ES', 'FI',
        'FR', 'GR', 'HR', 'HU', 'IE', 'IT', 'LT', 'LU', 'LV', 'MT',
        'NL', 'PL', 'PT', 'RO', 'SE', 'SI', 'SK']

COUNTRY_NAMES = {
    "AT": "Austria", "BE": "Belgium", "BG": "Bulgaria", "CZ": "Czech Republic",
    "DE": "Germany", "DK": "Denmark", "EE": "Estonia", "GR": "Greece",
    "ES": "Spain", "FI": "Finland", "FR": "France", "HR": "Croatia",
    "HU": "Hungary", "IE": "Ireland", "IT": "Italy", "LT": "Lithuania",
    "LV": "Latvia", "MT": "Malta", "NL": "Netherlands", "PL": "Poland",
    "PT": "Portugal", "RO": "Romania", "SE": "Sweden", "SI": "Slovenia",
    "SK": "Slovakia",
}

# NACE Rev.2 activity filter applied to the three simple datasets
# C_ICT: ICT occupations across all economic sectors (persons employed in ICT roles
# regardless of which industry they work in). The raw files also contain G-U_ICT
# (ICT occupations in services sectors only) and ICT (a broader aggregate).
# C_ICT is selected for consistency and cross-country comparability.
NACE_FILTER = 'C_ICT'

# Cloud adoption dimension filters
# size_emp GE10: enterprises with 10 or more employees — the broadest comparable
# size class available and the Eurostat standard for enterprise ICT surveys.
# Excludes micro-enterprises (under 10 employees) which are surveyed inconsistently
# across EU member states.
CLOUD_SIZE_EMP = 'GE10'

# indic_is E_CC: enterprises purchasing any paid cloud computing service.
# The dataset also contains breakdowns by cloud service type (e.g. E_CC1_B for
# basic services, E_CC1_S for software, E_CC1_I for infrastructure) but E_CC
# is the top-level indicator covering all cloud adoption, which is most suitable
# for cross-country comparison.
CLOUD_INDIC_IS = 'E_CC'

# unit PC_ENT: percentage of enterprises — the only unit available in this dataset.
# Values represent the share of enterprises in a given country and size class
# that purchased at least one cloud computing service in the reference year.
CLOUD_UNIT = 'PC_ENT'

# Analysis year range — the window where Bulgaria has continuous data across
# all four datasets. Cloud adoption data is only collected in odd years by Eurostat,
# so some years will have gaps in that dataset within this range.
YEAR_MIN = 2014
YEAR_MAX = 2023
