#!/usr/bin/env python3
"""Check the FINAL CSV; official organizer validator remains the authority."""
from __future__ import annotations
import sys, pathlib, hashlib, pandas as pd, numpy as np
N=199319
EXPECTED="6ae8a607a3c27bb96ec8da12b7e64326fb44765e8801ceb04f6844c21aa92c58"

def main(path):
    p=pathlib.Path(path)
    if not p.is_file():raise FileNotFoundError(p)
    d=pd.read_csv(p,dtype={"label":"object"})
    assert d.columns.tolist()==["frame","label"],f"columns={d.columns.tolist()}"
    assert len(d)==N,f"rows={len(d)}"
    assert np.array_equal(d.frame.to_numpy(),np.arange(N)),"frames not 0..199318"
    assert d.label.notna().all(),"missing labels"
    labels=d.label.astype(str).str.strip().str.upper().to_numpy()
    assert np.isin(labels,["H","A","D","X"]).all(),"invalid labels"
    assert np.all(labels[:11185]=="X")
    assert np.all(labels[90652:110808]=="X")
    assert np.all(labels[110808:113742]=="D")
    assert np.all(labels[190198:]=="X")
    sha=hashlib.sha256(p.read_bytes()).hexdigest()
    nsp=int(np.sum(np.isin(labels,["H","A"]) & np.r_[True,labels[1:]!=labels[:-1]]))
    print("FORMAT OK",p,"SHA256",sha)
    print("Labels:",dict(zip(*np.unique(labels,return_counts=True))))
    print("Predicted H/A spells:",nsp)
    print("MATCHES_EXECUTED_REFERENCE_SHA256:",sha==EXPECTED)
    print("Next: python evaluation/validate_submission.py",str(p))

if __name__=="__main__":
    if len(sys.argv)!=2:sys.exit("Usage: python scripts/validate_submission.py 'Xcelerate FC.csv'")
    main(sys.argv[1])
