# Week 1 — Setup and Troubleshooting

Follow the [Week 1 Google Doc](https://docs.google.com/document/d/1ooopqDUiiGSvQ9Zh6pKobe8IPoPcbLI4XPvaCYBKjCQ/edit?usp=drivesdk) for the *learning*. Use this file to run the code.

## Prerequisites
- Python **3.10 or 3.11** recommended
- Git + a terminal (VS Code terminal is fine)
- No GPU necessary

## 1. Clone and enter the repository
```bash
git clone https://github.com/dishaiit09-beep/GameSense-WiDS-6.0.git
cd GameSense-WiDS-6.0
```

## 2. Create a virtual environment
```bash
python -m venv .venv
```
**Windows PowerShell:** `.venv\Scripts\Activate.ps1`

**macOS/Linux:** `source .venv/bin/activate`

If Windows uses the Python launcher, replace `python` with `py -3.11` for the creation step. If PowerShell blocks activation, run `.venv\Scripts\python.exe` directly instead of changing machine-wide security settings.

## 3. Install
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-week1.txt
python -m pip install -e .
```

## 4. Inspect the game
```bash
python scripts/week01_inspect_env.py
```
Expected: numerical observation, action space of size 2. Actions: 0 = do nothing, 1 = flap.

## 5. Run and plot the shared random baseline
```bash
python scripts/week01_random_agent.py --episodes 20 --seed 42
python scripts/week01_plot_results.py --csv results/week01/random_baseline.csv
```
Outputs: `results/week01/random_baseline.csv`, `results/week01/random_baseline.png`.

If you have a desktop graphical session and want to watch the bird, optionally run:
```bash
python scripts/week01_random_agent.py --episodes 1 --render
```

## 6. Tests
```bash
python -m pytest -q
```

## Common issues
- **No module named flappy_bird_gymnasium:** activate your virtual environment and reinstall requirements.
- **No module named gamesense:** run `python -m pip install -e .` from the repository root.
- **No CSV to plot:** first run `week01_random_agent.py`.
- **Window does not open:** omit `--render`; the non-visual experiment works in a headless environment.
- **Unsupported Python / package install fails:** try Python 3.10 or 3.11 in a fresh environment and copy the exact error to a GitHub issue.

> Note: The code is unit-tested, but full Flappy Bird execution still needs verification on a laptop with the third-party game package installed.
