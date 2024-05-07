from argparse import ArgumentParser

from sentiment_analysis import sentiment_analysis


def main(file_path: str) -> None:
    """
    Main function that reads from a file and prints the sentiment analysis
    result for each line.
    :param file_path: Path to the file containing texts for sentiment analysis.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        results = sentiment_analysis(lines)
        for line, result in zip(lines, results):
            print(f"The sentiment of the text '{line.strip()}' is: {result}")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = ArgumentParser(
        description="Perform sentiment analysis on text from a file."
    )
    parser.add_argument(
        "file_path", type=str, help="Path to the file containing text."
    )
    args = parser.parse_args()

    main(args.file_path)
