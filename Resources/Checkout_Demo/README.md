# Checkout Demo (AI-3: Fix a failing test suite)

The store's checkout pricing has five failing tests. Get them passing.

The pricing rules from the product team are at the top of `checkout.py`.

## Setup

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Windows (PowerShell): use `python -m venv .venv` and `.venv\Scripts\Activate.ps1`, then the same commands.

## Rules for this round

- Fix the **code**, not the tests. If you believe a test is wrong, say why and point to the pricing rule that proves it before you touch it.
- Read and explain every change your AI tool makes before you accept it.
