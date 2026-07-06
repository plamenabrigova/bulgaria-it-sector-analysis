from src.clean import clean_stats, clean_cloud_adop
from src.export import export_datasets
from src.config import FILES, RAW_FOLDER


def main():
    datasets = {}
    for name, filename in FILES.items():
        datasets[name] = clean_stats(RAW_FOLDER / filename)

    datasets['cloud_adoption'] = clean_cloud_adop(
        RAW_FOLDER / 'Cloud computing services by size class of enterprise.tsv'
    )

    export_datasets(datasets)


if __name__ == '__main__':
    main()


