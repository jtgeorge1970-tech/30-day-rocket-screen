"""Compatibility entry point for the durable daily pipeline.

The former downloader permanently skipped completed symbols and recorded failed
attempts as completed. Use the SSOT daily pipeline instead; it refreshes dates,
retains failed symbols for retry and persists research predictions and outcomes.
The scheduled workflow owns restore/push verification of the state branch.
"""
from ofts.daily import main

if __name__ == "__main__":
    main()
