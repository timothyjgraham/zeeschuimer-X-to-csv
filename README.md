# Zeeschuimer X/Twitter converter (NDJSON to CSV)
A simple Python script to convert [Zeeschuimer](https://github.com/digitalmethodsinitiative/zeeschuimer) NDJSON data collected from X/Twitter to CSV format.

## Purpose
The `convert_ndjson_to_csv.py` script is specifically designed for converting Twitter (now known as "X") data, exported by Zeeschuimer, from an NDJSON (Newline Delimited JSON) format into a CSV (Comma-Separated Values) format. Zeeschuimer is an open-source tool for scraping data from various platforms, including Twitter (X), and typically stores data in NDJSON format.

## How It Works
The script processes each line of the Zeeschuimer NDJSON file, where each line is a JSON object representing a Twitter (X) data item. It extracts specific fields related to tweets and user information and compiles them into a CSV file, complete with a header row and subsequent data rows.

## Fields Extracted
Fields extracted from Zeeschuimer's NDJSON output include:
- Tweet information: text, creation date, ID, language, user ID, and username.
- Engagement metrics: counts of favorites, retweets, replies, and quotes.
- Media details: URLs and types.
- Social elements: hashtags, mentions, and URLs.
- User details: screen name, verification status, account creation date, profile defaults, and follower count.

## Prerequisites
- **Python 3**: Ensure Python 3 is installed. [Download Python](https://www.python.org/downloads/).
- **Zeeschuimer**: Familiarity with Zeeschuimer, especially for Twitter (X) data extraction. Visit [Zeeschuimer on GitHub](https://github.com/digitalmethodsinitiative/zeeschuimer).
- Basic understanding of terminal or command-line interface.

## How to Use
1. **Script Placement**: Save `convert_ndjson_to_csv.py` in a directory of your choice.
2. **Data File**: Have your NDJSON file from Zeeschuimer, containing Twitter (X) data, ready.
3. **Running the Script**:
   - Open your terminal or command prompt.
   - Navigate to where the script is located.
   - Run the script with:
     ```
     python3 convert_ndjson_to_csv.py <path_to_zeeschuimer_twitter_ndjson> <path_to_output_csv>
     ```
   - Replace `<path_to_zeeschuimer_twitter_ndjson>` with the path to your NDJSON file and `<path_to_output_csv>` with the desired path for the output CSV file.
4. **Output Verification**: Check the specified location for the generated CSV file after the script successfully runs.

## Example Command
```
python3 convert_ndjson_to_csv.py twitter_data.ndjson twitter_data.csv
```


## Troubleshooting
- **Python Installation**: If a 'Python not found' error occurs, verify your Python installation and PATH settings.
- **File Paths**: Double-check the paths to the NDJSON input file and the output CSV file for any errors.

## Notes
- The script is designed for Twitter (X) data structures from Zeeschuimer and may need adjustments for other data types or structures.
- Processing large datasets may require considerable memory and computational resources.

## Credit
This code is written in the Queensland University of Technology Digital Media Research Centre (DMRC). It is funded through the Australian Research Council DECRA grant scheme.
