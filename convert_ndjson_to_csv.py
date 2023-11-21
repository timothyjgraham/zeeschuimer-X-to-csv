import json
import csv
import sys

def convert_ndjson_to_csv(ndjson_file, csv_file):
    headers = [
        'tweet_text', 'creation_date', 'tweet_id', 'language', 'user_id', 
        'user_name', 'favorite_count', 'retweet_count', 'reply_count', 
        'quote_count', 'media_url', 'media_type', 'hashtag', 'mention', 
        'url', 'screen_name', 'verified', 'account_creation_date', 
        'default_profile', 'default_profile_image', 'followers_count'
    ]

    with open(ndjson_file, 'r') as file, open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)

        for line in file:
            data = json.loads(line)

            legacy = data.get('data', {}).get('legacy', {})
            user = data.get('data', {}).get('core', {}).get('user_results', {}).get('result', {}).get('legacy', {})

            row = [
                legacy.get('full_text', ''),
                legacy.get('created_at', ''),
                legacy.get('id_str', ''),
                legacy.get('lang', ''),
                legacy.get('user_id_str', ''),
                legacy.get('name', ''),
                legacy.get('favorite_count', ''),
                legacy.get('retweet_count', ''),
                legacy.get('reply_count', ''),
                legacy.get('quote_count', ''),
                '; '.join([m.get('media_url_https', '') for m in legacy.get('extended_entities', {}).get('media', [])]),
                '; '.join([m.get('type', '') for m in legacy.get('extended_entities', {}).get('media', [])]),
                '; '.join([h.get('text', '') for h in legacy.get('entities', {}).get('hashtags', [])]),
                '; '.join([m.get('screen_name', '') for m in legacy.get('entities', {}).get('user_mentions', [])]),
                '; '.join([u.get('expanded_url', '') for u in legacy.get('entities', {}).get('urls', [])]),
                user.get('screen_name', ''),
                user.get('is_blue_verified', ''),
                user.get('created_at', ''),
                user.get('default_profile', ''),
                user.get('default_profile_image', ''),
                user.get('followers_count', '')
            ]

            writer.writerow(row)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_ndjson_file> <output_csv_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_ndjson_to_csv(input_file, output_file)
    print(f"Conversion complete. CSV file saved as: {output_file}")

