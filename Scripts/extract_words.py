import argparse
from pathlib import Path


def extract_words(input_path: Path) -> list[str]:
    lines = input_path.read_text(encoding="utf-8").splitlines()
    words: list[str] = []
    for line in lines:
        if not line.strip():
            continue
        word = line.split("\t", 1)[0].strip()
        if word:
            words.append(word)
    return words


def default_output_path(input_path: Path, output_dir: Path) -> Path:
    return output_dir / f"{input_path.stem}-单词.txt"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("/Users/pengyu/Documents/Github Project/english-vocabulary/5 考研-乱序.txt"),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("/Users/pengyu/Documents/Github Project/english-vocabulary/clean"),
    )
    args = parser.parse_args()

    input_path: Path = args.input
    output_dir: Path = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = default_output_path(input_path, output_dir)

    words = extract_words(input_path)
    output_path.write_text("\n".join(words) + "\n", encoding="utf-8")
    print(output_path)


if __name__ == "__main__":
    main()
