"""
Lab 07 entry point.

This file simply imports and exposes the functions you implemented
in lab07_contact_book.py so that the CI workflow can find them.
"""

from lab07_contact_book import save_contacts_to_json, load_contacts_from_json
from lab07_api_client import get_api_data

# Optional: small sanity check when run directly
if __name__ == "__main__":
    print("Lab 07 loaded successfully.")
