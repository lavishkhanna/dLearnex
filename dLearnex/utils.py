import csv
from users.models import CsvData  # Import the model



def import_csv_to_db(csv_file_path):
    """
    Imports data from a CSV file into the CsvData table.
    
    The CSV file must have columns for user_id, ch_id, and score.
    """
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row, if it exists

        for row in reader:
            # Ensure the data types are correct
            user_id = int(row[0])
            ch_id = int(row[1])
            score = float(row[2])

            # Create a new entry in the database
            CsvData.objects.create(
                user_id=user_id,
                ch_id=ch_id,
                score=score
            )

        print("CSV data imported successfully!")


import csv
from users.models import Channel  # Replace `your_app` with your app name




def import_csv_to_postgres(csv_file_path):
    try:
        with open(csv_file_path, 'r', encoding='utf-8', errors='replace') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row if it exists

            for row in reader:
                try:
                    # Create or update a record in the Channel table
                    Channel.objects.update_or_create(
                        channel_id=row[0],  # Use channel_id as the unique identifier
                        defaults={
                            'channel_name': row[1],
                            'channel_url': row[2],
                        }
                        
                    )
                except Exception as e:
                    print(f"Error processing row {row}: {e}")
        print("CSV data imported successfully!")
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")




