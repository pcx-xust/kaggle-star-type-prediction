from pathlib import Path
import shutil

import kagglehub


COMPETITION_NAME = "playground-series-s6e6"
RAW_DATA_DIR = Path("data/raw")


def main():
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    download_path = Path(kagglehub.competition_download(COMPETITION_NAME))
    print(f"KaggleHub download path: {download_path}")

    for item in download_path.iterdir():
        if item.is_file():
            target_path = RAW_DATA_DIR / item.name
            shutil.copy2(item, target_path)
            print(f"Copied: {item.name} -> {target_path}")

    print(f"Competition files are available in: {RAW_DATA_DIR.resolve()}")


if __name__ == "__main__":
    main()
