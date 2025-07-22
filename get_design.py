import os
import csv
import re
import argparse

def main():
    parser = argparse.ArgumentParser(description="Scan a directory for FASTQ files and generate a CSV file with sample info.")
    parser.add_argument("-i", "--input", required=True, help="Path to the directory containing FASTQ files.")
    parser.add_argument("-o", "--output", help="Path to the output CSV file. Defaults to 'design.csv' in the input directory.")
    args = parser.parse_args()

    FASTQ_DIR = args.input
    OUTPUT_CSV = args.output if args.output else os.path.join(FASTQ_DIR, "design.csv")

    samples = {}

    PAIRED_PATTERN = re.compile(r"(.+?)_(1|2)\.fastq\.gz$")
    SINGLE_PATTERN = re.compile(r"(.+?)\.fastq\.gz$")

    for file in os.listdir(FASTQ_DIR):
        file_path = os.path.join(FASTQ_DIR, file)

        paired_match = PAIRED_PATTERN.match(file)
        single_match = SINGLE_PATTERN.match(file)

        if paired_match:
            sample, read_pair = paired_match.groups()
            if sample not in samples:
                samples[sample] = {"read_1": "", "read_2": ""}

            if read_pair == "1":
                samples[sample]["read_1"] = file_path
            elif read_pair == "2":
                samples[sample]["read_2"] = file_path

        elif single_match:
            sample = single_match.group(1)
            if sample not in samples:
                samples[sample] = {"read_1": file_path, "read_2": ""}

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["sample", "read_1", "read_2", "group", "run_accession"])

        for sample, paths in samples.items():
            writer.writerow([sample, paths["read_1"], paths["read_2"], "A", ""])

    print(f"CSV file created at {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
