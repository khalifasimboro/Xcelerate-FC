# Private data access (Xcelerate FC)

The competition match assets are private under the More Than a Hack 2027 data licence. Our Kaggle dataset is **not** a public mirror:

**Dataset:** https://www.kaggle.com/datasets/erickambire/bar-data

A visitor with only this URL may not be able to view or download it. To share with an **authorized competitor/reviewer**, the dataset owner can navigate to **Kaggle → Dataset → Settings → Sharing**, search for their Kaggle username and invite them with **Can view** permission. Granting access should be conditional on the competition organizer's licence/authorization; Kaggle access must not bypass these conditions. The Kaggle owner must approve the request; GitHub collaborators are not automatically Kaggle dataset collaborators.

The repository contains only source code, the reproducibility procedure, and aggregate externally validated metrics. It intentionally excludes private ATD TXT, XML, videos, frame-level tracking exports, homography, generated full-match tables and private ground-truth data.

In Kaggle, add the dataset under **Add Input** after authorization. The notebook searches, in order, `MTAH_DATA_DIR`, `/kaggle/input/datasets/erickambire/bar-data`, `/kaggle/input/bar-data`, and dataset files discovered under `/kaggle/input/`. It expects these filenames:

```
BAR-ATH_tactical_atd.txt
BAR-ATH_tactical_atd.xml
BAR-ATH_tactical_smart_tagging.xml
```

`BAR-ATH_tactical_homography.csv` is optional for the present code path. A private competition public-GT CSV can be mounted for **diagnostic checks only**. Any private data access must be agreed with the owner. If access cannot be granted, the notebook's code and scientific methodology remain inspectable, but the exact final CSV cannot be independently rebuilt from the public GitHub repository alone. Organizers already entitled to the original bundle may supply it locally by setting `MTAH_DATA_DIR`.

The public SkillCorner open data is independent from the competition match. The external IDs and source are recorded in `README.md` and the notebook.
