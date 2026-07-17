import os
import zipfile
import boto3
from datetime import datetime

# Constants
LOG_FILE = "logs/app.log"
ARCHIVE_FOLDER = "archives"
S3_BUCKET = "darnal-ec2-log-archive-2026"


def create_archive():
    """Create a timestamped ZIP archive of the log file."""

    os.makedirs(ARCHIVE_FOLDER, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_filename = f"logs_{timestamp}.zip"
    zip_path = os.path.join(ARCHIVE_FOLDER, zip_filename)

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(LOG_FILE, arcname=os.path.basename(LOG_FILE))

    print(f" Archive created: {zip_path}")

    return zip_path, zip_filename


def upload_to_s3(zip_path, zip_filename):
    """Upload the ZIP archive to Amazon S3."""

    s3 = boto3.client("s3")

    s3.upload_file(zip_path, S3_BUCKET, zip_filename)

    print(f" Uploaded '{zip_filename}' to S3 bucket '{S3_BUCKET}'")


def cleanup_archive(zip_path):
    """Delete the local ZIP archive after a successful upload."""

    os.remove(zip_path)

    print(" Local archive deleted.")


def archive_logs():
    """Main workflow."""

    if not os.path.exists(LOG_FILE):
        print(" Log file not found.")
        return

    zip_path, zip_filename = create_archive()

    upload_to_s3(zip_path, zip_filename)

    cleanup_archive(zip_path)

    print(" Log archival completed successfully.")


if __name__ == "__main__":
    archive_logs()