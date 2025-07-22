# design-csv-creator

A tool for generating design.csv files from FASTQ files for bioinformatics workflows.

## Usage

```bash
python get_design.py -i /path/to/fastq/directory [-o /path/to/output.csv]
```

**Options:**
- `-i, --input`: Path to directory containing FASTQ files (required)
- `-o, --output`: Output CSV file path (optional, defaults to `design.csv` in input directory)

**Example:**
```bash
python get_design.py -i ./data/fastq_files
```

This will scan `./data/fastq_files/` for FASTQ files and create `./data/fastq_files/design.csv` with columns:
- `sample`: Sample name (extracted from filename)
- `read_1`: Path to R1 FASTQ file
- `read_2`: Path to R2 FASTQ file (for paired-end data)
- `group`: Sample group (default: "A")
- `run_accession`: Run accession (empty by default)

**Supported file patterns:**
- Paired-end: `sample_1.fastq.gz`, `sample_2.fastq.gz`
- Single-end: `sample.fastq.gz`
