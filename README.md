# Xcelerate FC | More Than a Hack 2027

**Team:** KAMBIRE Eric, LARAISSE Hamza, BELEMCOABGA Falleiz Rostem, BATIONO Max Dieudonné Nathan, SIMBORO Rydouane.

**Challenge:** predict H (Barcelona), A (Athletic Club), D (ball not in play) or X (ungraded) for each of **199,319 frames** of the competition video at **25 FPS**. The official ranking metric is **spellF1**, which matches H/A possession intervals across temporal IoU thresholds 0.3–0.7. Per-frame macroF1 is reported separately.

## What is in this pull request?

| Path | Contents |
|---|---|
| [`notebooks/xcelerate-fc.ipynb`](notebooks/xcelerate-fc.ipynb) | Complete Kaggle notebook, 47 cells: M1–M4 experiments, external checks, TabICLv2 screening, final CSV and frame/timecode divergence diagnostics. Outputs are **cleared** because they may contain derived private match material. |
| [`report/Xcelerate FC.pdf`](report/Xcelerate%20FC.pdf) | Seven-page English technical report. |
| [`report/Xcelerate FC.tex`](report/Xcelerate%20FC.tex) | XeLaTeX report source with two external-validation charts in `report/figures/`. |
| [`requirements.txt`](requirements.txt) | Python compatibility constraints; NumPy is pinned to the observed Kaggle version. Exact package freeze from the Kaggle runtime is still recommended. |
| [`docs/DATA_ACCESS.md`](docs/DATA_ACCESS.md) | Private data access and safe sharing policy. |
| [`scripts/validate_submission.py`](scripts/validate_submission.py) | Local CSV integrity and SHA-256 verification, with instructions for running the **official validator**. |

## Our development sequence

1. **M1, frame-wise geometry.** Parse automatic ATD player/ball tracking, XML team association and Smart Tagging. Compare a nearest-player baseline with H/A/D observation scores and Viterbi.
2. **M2, temporal persistence.** Compare baseline penalties `(13,10,7)` to `switch_strong` `(23,17,11)` and temperature scaling. Choose hypotheses using different **external** matches.
3. **M3, football control cues.** Add exclusive sustained last-controller memory (1.8 m, 5 frames, 10 s expiry), tentative duel and ball-acceleration evidence, safe interpolation of short missing-ball segments, and multi-scale score fusion. Check each change by ablation on the same five external matches.
4. **M4, experimental D and foundation model.** Compare a physically motivated D V2 to the classic score, and screen TabICLv2 against HistGradientBoosting on externally-labelled H/A examples. **Neither full temporal TabICL CV nor external D-recall validation has been completed; these branches are not included in the selected final model.**
5. **Lock, test once, export.** Select `fusion_control_multiscale` on five development matches; score it once on a fresh external match; then export a `frame,label` CSV. The supplied public five-minute competition labels are for **pipeline checking only**, never tuning or model selection.

### Results from the executed Kaggle notebook

| Check | Measurement |
|---|---:|
| Five external development matches, mean H/A **proxy** spellF1 | **0.4823** (SD 0.0178) |
| External H/A macroF1, development mean | 0.8200 |
| Fresh external holdout 2017461, H/A proxy spellF1 | 0.4078 |
| Public five-minute diagnostic, official spellF1 | 0.4108 (not model selection) |
| Public diagnostic, F1_D | 0.0000 |
| Submitted prediction, H/A spells (complete video) | 356 |

**Interpretation:** External SkillCorner labels are only known H/A portions, **not full dead-ball annotations**, and the external proxy spellF1 is not the competition's private score. Public five-minute metrics are not a leaderboard. No labels from the competition match were used for training or tuning.

## Reproduction on Kaggle

1. **Obtain authorized competition data.** The original Metrica bundle is available to approved competitors. We mounted it in a **private** Kaggle dataset: [erickambire/bar-data](https://www.kaggle.com/datasets/erickambire/bar-data). A link alone does not grant access. The owner can add a permitted collaborator under **Kaggle Dataset → Settings → Sharing → Add collaborator → Can view**. See [`docs/DATA_ACCESS.md`](docs/DATA_ACCESS.md).
2. Create a Kaggle notebook from [`notebooks/xcelerate-fc.ipynb`](notebooks/xcelerate-fc.ipynb). Add the approved private dataset as an input; the loader also accepts `MTAH_DATA_DIR` for a directory containing the ATD TXT/XML and Smart Tagging XML assets. Keep the competition notebook and outputs private unless licensed otherwise.
3. Use a Kaggle Python 3 environment; enable GPU if running optional TabICLv2. **Internet ON** is needed to download public SkillCorner tracking and the public TabICL checkpoint if they are not cached. Install `requirements.txt` in a fresh environment if needed. The main notebook uses imports from Kaggle's preinstalled scientific stack; validate compatibility before overwriting Kaggle's own packages.
4. Run cells in order. Required configurations: `SEED=2027`, `DEV_IDS=[1886347,1899585,1925299,1996435,2006229]`, `FRESH_HOLDOUT=2017461`, `RUN_TABICL_FULL_CV=False`, and final `MODEL_TO_EXPORT='AUTO'`.
5. The notebook writes `/kaggle/working/Xcelerate.csv`. Optionally rename it to **`Xcelerate FC.csv`** for the form. Run `python scripts/validate_submission.py "Xcelerate FC.csv"` for local checks and **run the official `evaluation/validate_submission.py` before submission**. The expected SHA-256 for the originally executed output is below. A different hash after re-execution must be explained and compared, not silently accepted.

```text
Expected output: 199319 rows; header: frame,label
Expected selected model: fusion_control_multiscale
Expected SHA256 (executed Kaggle run):
6ae8a607a3c27bb96ec8da12b7e64326fb44765e8801ceb04f6844c21aa92c58
```

### External labelled data

Source: [SkillCorner Open Data](https://github.com/SkillCorner/opendata), entirely **different matches** from the supplied Barcelona–Athletic match. Development match IDs: `1886347`, `1899585`, `1925299`, `1996435`, `2006229`. Fresh held-out match: `2017461`. Native tracking is approximately 10 Hz; possession labels are read from `possession.group` where present. Unknown intervals are unlabelled and **must never be interpreted as D ground truth**. See the notebook for the loading, temporal adaptation and match-wise split. Automatic pseudo-labels (where used in experimental branches) do not come from humans annotating the supplied match.

## Official validation and submission

- Official rules: https://github.com/metrica-sports/more-than-a-hack-2027/blob/main/RULES.md
- Metric details: https://github.com/metrica-sports/more-than-a-hack-2027/blob/main/EVALUATION.md
- Official format check: https://github.com/metrica-sports/more-than-a-hack-2027/blob/main/SUBMISSION.md
- Submit **`Xcelerate FC.csv`** and **`Xcelerate FC.pdf`**, plus the public repository URL, before **17 November 2026 23:59 CET**.
- Never commit competition tracking, tactical XML, homography, video, derived frame-level tracking, public ground truth copies, full Kaggle execution outputs, private dataset downloads, API tokens or restricted model files to this public repository.

## Compiling the technical report

With XeLaTeX and the included charts:

```bash
cd report
xelatex -interaction=nonstopmode "Xcelerate FC.tex"
```

The checked-in PDF is a convenience copy. It is not the scored possession file; the independently-generated CSV is.

## Limitations

The **selected** model has only external H/A validation. It detects too few dead-ball frames in the public diagnostic. Differences between 10 Hz SkillCorner broadcasts and 25 Hz automatic competition tracking limit transfer. The reserved external match scored below the development average. Our research branches on TabICLv2 and D V2 do not establish a fully validated H/A/D system.
