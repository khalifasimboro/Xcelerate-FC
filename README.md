# Xcelerate FC

### Football Possession Inference | More Than a Hack 2027

**From player proximity to football-aware temporal modeling.**

Xcelerate FC is our submission to the **More Than a Hack 2027** challenge, organized by Metrica Sports.

Our objective is to infer which team controls the ball throughout a football match using automatic player and ball tracking, tactical events, spatial relationships, and temporal modeling.

Rather than treating possession as an independent classification problem at every frame, we model it as a continuous football process involving ball control, passes, challenges, turnovers, and stoppages.

**Team members**

- KAMBIRE Eric
- LARAISSE Hamza
- BELEMCOABGA Falleiz Rostem
- BATIONO Max Dieudonné Nathan
- SIMBORO Rydouane

**Repository:** https://github.com/khalifasimboro/Xcelerate-FC

**Technical report:** [Xcelerate FC.pdf](report/Xcelerate%20FC.pdf)

---

## 1. The Challenge

We analyze the FC Barcelona vs Athletic Club match provided for the competition.

The tactical video contains **199,319 frames at 25 FPS**.

Each frame receives one of four labels:

| Label | Meaning |
|---|---|
| `H` | FC Barcelona in possession |
| `A` | Athletic Club in possession |
| `D` | Dead ball or play stopped |
| `X` | Outside the evaluated period or abstention |

The competition's primary ranking metric is **spellF1**, which evaluates complete possession intervals rather than isolated frames.

Predicted and reference possessions are matched using temporal Intersection over Union (IoU), averaged at thresholds of 0.3, 0.4, 0.5, 0.6 and 0.7.

Per-frame macroF1 and transition metrics provide complementary diagnostics.

Official challenge documentation:

- [Competition repository](https://github.com/metrica-sports/more-than-a-hack-2027)
- [Evaluation protocol](https://github.com/metrica-sports/more-than-a-hack-2027/blob/main/EVALUATION.md)
- [Competition rules](https://github.com/metrica-sports/more-than-a-hack-2027/blob/main/RULES.md)
- [Submission requirements](https://github.com/metrica-sports/more-than-a-hack-2027/blob/main/SUBMISSION.md)

## 2. Our Approach

Our development followed four successive research stages.

### M1. Geometric Baseline

We first investigated whether possession could be inferred from the player closest to the ball.

We reconstructed spatial features from the supplied automatic tracking and combined them with tactical information.

The first approach used:

- Distance between the ball and nearby players
- Team identification and player tracking
- Tactical event indicators
- An initial dead-ball score

We then introduced a Viterbi decoder to obtain temporally consistent predictions.

This established our baseline HMM-inspired model.

**Key observation:** Proximity alone cannot reliably identify possession. A defending player can approach the ball during a pass without gaining control.

### M2. Temporal Continuity

We next focused on possession fragmentation.

Our second stage investigated stronger transition penalties in the Viterbi decoder, especially between Barcelona and Athletic Club.

The `switch_strong` configuration penalizes unnecessary possession changes and improves the continuity of predicted intervals.

We compared several penalty configurations on external football matches rather than optimizing against the competition's public five-minute annotations.

This stage demonstrated that **temporal structure matters as much as frame-level classification**.

### M3. Football-Aware Ball Control and Model Fusion

We extended the temporal model with rules reflecting how possession works in football.

A genuine possession change should be supported by evidence of ball control, not merely a change in the closest player.

Our experiments introduced:

**Last-controller memory.** A sustained, sufficiently close ball interaction supports the last controlling team over a limited time.

**Contested-ball reasoning.** During duels or uncertain ball interactions, the decoder can preserve the previous possession until stronger evidence supports a turnover.

**Ball-touch candidates.** Ball acceleration and proximity provide additional evidence of possible player interactions.

**Missing-ball handling.** Short gaps are interpolated where possible, while longer gaps remain uncertain.

**Multiscale temporal evidence.** We combine information across short and longer time windows to reduce noise and preserve possession continuity.

These mechanisms led to our selected model:

### `fusion_control_multiscale`

The final H/A inference model combines ball-control evidence, spatial observations, multiscale temporal smoothing, and Viterbi decoding with strong transition penalties.

Each component was compared through external-match experiments and ablation tests.

### M4. Dead-Ball Modeling and Tabular Foundation Models

We also explored two additional research directions.

**Dead-Ball V2**

Our experimental detector incorporates physical and tactical evidence such as ball exits, restart preparation, active-play signals and temporary stoppage memory.

It improves the interpretability of dead-ball decisions, but external data did not provide sufficient positive dead-ball annotations to validate its recall reliably.

For that reason, this branch was not selected as the primary submission model.

**TabICLv2**

We investigated a pretrained Tabular Foundation Model using external football tracking features.

TabICLv2 was compared against nearest-player physics and HistGradientBoosting on externally labeled H/A examples.

The screening results were encouraging. However, a complete temporal spellF1 validation was not performed, so TabICLv2 was not incorporated into the selected submission.

## 3. Experimental Validation

We evaluated our approaches using the public [SkillCorner Open Data](https://github.com/SkillCorner/opendata) collection.

These are **independent football matches**, not the Barcelona vs Athletic Club competition match.

Five matches were used for development and leave-one-match-out validation:

`1886347`, `1899585`, `1925299`, `1996435`, `2006229`

An additional match, `2017461`, was reserved for a final external evaluation of the selected model.

SkillCorner tracking is sampled at approximately 10 Hz, compared with 25 FPS for the competition video.

Its available possession labels support H/A evaluation on annotated intervals. Unlabeled intervals are **not treated as dead-ball ground truth**.

### External evaluation results

| Model | Mean H/A proxy spellF1 |
|---|---:|
| Baseline HMM | 0.4004 |
| `switch_strong` | 0.4501 |
| `control_strong` | 0.4815 |
| **`fusion_control_multiscale`** | **0.4823** |

The selected model also achieved:

| Evaluation | Result |
|---|---:|
| Five-match external proxy spellF1, mean | **0.4823** |
| Five-match standard deviation | 0.0178 |
| Five-match external H/A macroF1 | 0.8200 |
| Reserved external match proxy spellF1 | 0.4078 |
| Reserved external match H/A macroF1 | 0.7426 |

The decrease on the reserved match illustrates the remaining sensitivity to differences in tracking quality, match dynamics and observation coverage.

The external proxy spellF1 is not identical to the competition's official full-match metric.

### Competition data diagnostic

After selecting the model through external evaluation, we performed a pipeline check on the organizers' public five-minute ground-truth window.

| Metric | Result |
|---|---:|
| Official public-window spellF1 | 0.4108 |
| Official public-window macroF1 | 0.5076 |
| Public-window F1 for D | 0.0000 |
| Predicted possessions in public window | 20 |

**The five-minute public ground truth was not used for training, hyperparameter tuning or model selection.**

The official full-match ground truth is private and was not accessible to our team.

## 4. Final Prediction

Our selected submission model is:

**`fusion_control_multiscale`**

The model produces one label per video frame.

The executed Kaggle pipeline generated:

| Property | Value |
|---|---:|
| Total frames | 199,319 |
| H frames | 92,388 |
| A frames | 61,942 |
| D frames | 4,527 |
| X frames | 40,462 |
| Predicted H/A possessions | 356 |

The required submission format is:

```csv
frame,label
0,X
1,X
2,X
```

The complete output must contain exactly 199,319 data rows, with consecutive frame indices from 0 to 199318.

The submission filename is **`Xcelerate FC.csv`**.

The generated file must be validated before submission using the organizers' official validator.

## 5. Repository Structure

```text
Xcelerate-FC/
├── notebooks/
│   └── xcelerate-fc.ipynb
├── report/
│   ├── Xcelerate FC.pdf
│   ├── Xcelerate FC.tex
│   └── figures/
├── docs/
│   └── DATA_ACCESS.md
├── scripts/
│   └── validate_submission.py
├── requirements.txt
├── .gitignore
└── README.md
```

- **[`notebooks/xcelerate-fc.ipynb`](notebooks/xcelerate-fc.ipynb)**: Main reproducible research notebook documenting data loading, M1–M4 experiments, TabICLv2 screening, model selection and submission export. Outputs are cleared to prevent redistribution of derived private match material.
- **[`report/Xcelerate FC.pdf`](report/Xcelerate%20FC.pdf)**: Complete technical report describing our methodology, football modeling principles, validation results and team contributions.
- **[`report/Xcelerate FC.tex`](report/Xcelerate%20FC.tex)**: LaTeX source for the report, accompanied by evaluation figures in [`report/figures/`](report/figures/).
- **[`docs/DATA_ACCESS.md`](docs/DATA_ACCESS.md)**: Data access policy, Kaggle dataset authorization procedure and competition compliance guidelines.
- **[`scripts/validate_submission.py`](scripts/validate_submission.py)**: Verification script for output dimensions, schema, label validity and reference SHA-256 integrity.
- **[`requirements.txt`](requirements.txt)**: Core dependencies and library versions for reproducing experiments.

## 6. Reproducing Our Results

Our development and final execution were performed using **Kaggle Notebooks**.

### Step 1. Obtain the competition data

The original competition data is restricted.

For authorized team members or reviewers, we maintain a private Kaggle dataset:

**[Xcelerate FC competition dataset](https://www.kaggle.com/datasets/erickambire/bar-data)**

Access must be granted by the dataset owner and comply with the competition's data license.

The dataset includes the tracking and tagging assets required by the notebook. The private dataset is not redistributed through GitHub.

Authorized organizers who already hold the original competition bundle may also supply the required files locally.

See [Data Access](docs/DATA_ACCESS.md).

### Step 2. Configure Kaggle

Create a Kaggle notebook and import:

`notebooks/xcelerate-fc.ipynb`

Attach the private competition dataset using Kaggle's **Add Input** functionality.

For external validation, the notebook retrieves publicly accessible SkillCorner match data.

Enable Kaggle Internet access if these public resources and optional TabICL model weights have not already been cached.

A GPU is recommended for optional TabICLv2 experiments, but the selected classical temporal model does not require it.

### Step 3. Install dependencies

Use a compatible Python environment with the packages listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

The main computational stack includes NumPy, pandas, SciPy, scikit-learn, Numba and Matplotlib.

TabICLv2 and PyTorch are optional dependencies for the foundation-model experiment.

### Step 4. Run the notebook

Execute the notebook sequentially.

The main experimental configuration uses:

```python
SEED = 2027

DEV_IDS = [
    1886347,
    1899585,
    1925299,
    1996435,
    2006229
]

FRESH_HOLDOUT = 2017461

RUN_TABICL_FULL_CV = False
MODEL_TO_EXPORT = "AUTO"
```

The notebook compares models on external matches, selects the eligible candidate, applies the selected model to the competition data and exports the final predictions.

The original completed run selected `fusion_control_multiscale`.

### Step 5. Validate the submission

The generated CSV is saved as:

```text
/kaggle/working/Xcelerate.csv
```

Rename or copy it to:

```text
Xcelerate FC.csv
```

Run the local verification and the official competition validator:

```bash
python scripts/validate_submission.py "Xcelerate FC.csv"
```

Official validator:

```bash
python evaluation/validate_submission.py "Xcelerate FC.csv"
```

The second command requires the organizers' evaluation code.

The SHA-256 checksum of our original Kaggle-generated prediction file is:

```text
6ae8a607a3c27bb96ec8da12b7e64326fb44765e8801ceb04f6844c21aa92c58
```

An independently reproduced output should be checked against this reference. A differing checksum requires investigation before submission.

## 7. Data Usage and Competition Compliance

Our pipeline follows the official rules:

- All predictions are generated algorithmically.
- No manual possession labels were created for the supplied competition match.
- No private full-match ground truth was used.
- The public five-minute ground truth was used only for pipeline diagnostics.
- External SkillCorner labels were used only on other matches.
- No private tracking, video, tactical XML or derived frame-level tracking is redistributed in this public repository.
- **Pre-existing repository assets:** The legacy root file `Données-Prediction Baseline.csv` committed in earlier repository revisions contains derived tracking features from the competition video. In accordance with the competition data license, repository administrators should evaluate removing or untracking this legacy file from public history to ensure strict licensing compliance.

Our public code is intended to be inspectable and reproducible by authorized reviewers with access to the original assets.

## 8. Limitations and Future Work

Three limitations remain important:

1. **Dead-ball inference.** The selected model performs poorly on D in the public diagnostic. Full dead-ball validation requires an independent external dataset with reliable play-stoppage annotations.
2. **Domain shift.** SkillCorner broadcast tracking differs from the competition's automatic tracking. Performance on a reserved external match was lower than the development average.
3. **Temporal foundation models.** TabICLv2 improved H/A classification in initial external screening, but a full possession-level temporal validation remains necessary.

Future work will focus on accurate stoppage and restart detection, more reliable ball-control evidence, improved handling of long tracking gaps, and full temporal integration of pretrained tabular models.

## 9. Technical Report

Our methodology, experimental progression, football assumptions, validation results and limitations are documented in:

**[Xcelerate FC — Technical Report](report/Xcelerate%20FC.pdf)**

The LaTeX source is available in [report/Xcelerate FC.tex](report/Xcelerate%20FC.tex).

## 10. Acknowledgments

We thank **Metrica Sports** for organizing More Than a Hack 2027 and providing the technical assets and evaluation framework.

We also acknowledge **SkillCorner** for its publicly available football tracking dataset, used for external experimentation.

---

**Xcelerate FC | More Than a Hack 2027**

*Football intelligence through geometry, temporal reasoning and evidence-based model selection.*
