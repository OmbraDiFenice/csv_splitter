import csv
import argparse
from typing import Iterable
import os.path


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dest-folder', default=".")
    parser.add_argument('-r', '--rows-per-file', type=int, default=50)
    parser.add_argument('input_file')

    return parser.parse_args()


def write_to_next_csv(filepath: str,
                      header: Iterable[str],
                      input_reader: Iterable[Iterable[str]],
                      rows_per_file: int) -> None:
    with open(filepath, "w") as output_csv:
        writer = csv.writer(output_csv, input_reader.dialect)

        writer.writerow(header)
        while rows_per_file >= 0:
            writer.writerow(next(input_reader))
            rows_per_file -= 1


def split_csv(input_filepath: str,
              dest_folder: str,
              rows_per_file: int) -> None:
    filename = os.path.basename(input_filepath)

    with open(input_filepath) as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)

        try:
            counter = 0
            while True:
                counter += 1
                next_filename = os.path.join(dest_folder, f"{counter}_{filename}")
                write_to_next_csv(next_filename,
                                  header, reader,
                                  rows_per_file)
        except StopIteration:
            pass


if __name__ == "__main__":
    args = parse_args()
    split_csv(args.input_file, args.dest_folder, args.rows_per_file)
