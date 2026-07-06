from src.config import CLEAN_FOLDER, YEAR_MIN, YEAR_MAX


def export_datasets(datasets: dict) -> None:

    # Create the clean folder if it does not exist yet
    CLEAN_FOLDER.mkdir(parents=True, exist_ok=True)

    for name, df in datasets.items():

        # Drop raw_value
        if 'raw_value' in df.columns:
            df = df.drop(columns=['raw_value'])

        # Filter to the analysis year range
        df = df.query('@YEAR_MIN <= year <= @YEAR_MAX').copy()

        # Add a metric label column so datasets can be stacked in Tableau
        # if needed without losing track of which metric each row belongs to
        df['metric'] = name

        # Export
        output_path = CLEAN_FOLDER / f'{name}.csv'
        df.to_csv(output_path, index=False)

        print(f"Exported {name}.csv — {len(df)} rows, "
              f"{df['geo'].nunique()} countries, "
              f"{df['year'].min()}–{df['year'].max()}")
