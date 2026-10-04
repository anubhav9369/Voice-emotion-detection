```
Contributing

Setup

1. Clone the repo:
 ```bash

git clone https://github.com/<anubhav9369>/<Voice-emotion-detection>.git
cd <Voice-emotion-detection>

```
2. Create a virtual environment and install dependencies:
 ```bash

 python -m venv.venv
 source.venv/bin/activate # Windows:.venv\Scripts\activate
 pip install -r requirements.txt

```
3. If the project needs secrets, copy `.env.example` to `.env` and fill in your keys (never commit `.env`).

Branch naming

Branch off `main` for every change:

- `feat/<short-description>` — new features
- `fix/<short-description>` — bug fixes
- `docs/<short-description>` — docs only
- `chore/<short-description>` — maintenance, deps, configs

Example: `feat/add-shap-explanations`

Tests

- Run the suite before pushing: `pytest`
- New features and fixes should include or update tests
- All tests must pass before merge

Pull requests

1. Push your branch and open a PR against `main`
2. Describe what changed, why, and how you tested it
3. One change per PR — keep them focused
4. Link issues with `Closes #<issue-number>` where it applies

Code style

- Follow PEP 8; small functions, descriptive names
- Format with `black` and lint with `ruff` before committing (where configured)
```

