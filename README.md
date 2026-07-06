# Bulgaria's IT Sector: Growth, Employment and Digital Adoption (2014–2023)

A data pipeline and analysis comparing Bulgaria against EU27 peers 
across four Eurostat indicators of IT sector development.

## Datasets
All data sourced from [Eurostat](https://ec.europa.eu/eurostat):

| Dataset | Eurostat Code |
|---|---|
| ICT sector personnel in total employment | `isoc_sks_itspt` |
| ICT sector share of gross value added | `tin00074` |
| Percentage change of value added by ICT sector | `tin00074` |
| Cloud computing adoption by enterprise size | `isoc_cicce_use` |

Download the TSV exports from Eurostat and place them in `data/raw/`.

## Setup
```bash
pip install -r requirements.txt
python main.py
```

## Output
Cleaned CSVs are exported to `data/clean/`, one file per metric, 
filtered to EU27 countries for the period 2014–2023.

## Key Methodological Decisions
- NACE filter: `C_ICT` only (ICT occupations across all sectors)
- Cloud adoption: enterprises with 10+ employees (`GE10`), any cloud service (`E_CC`)
- Greece coded as `EL` per Eurostat convention, not ISO standard `GR`
- Eurostat flag characters (`b`, `e`, `p`) stripped; confidential (`:@C`) and 
  unavailable (`:`) values dropped