#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
The top level of the package contains functions to
note-align symbolic music data.
"""
import os

EXAMPLE = os.path.join(os.path.dirname(__file__), "assets/mozart_k265_var1.match")
ALIGNMENT_TRANSFORMER_CHECKPOINT = os.path.join(os.path.dirname(__file__), "assets/alignment_transformer_checkpoint.pt")
THEGLUENOTE_CHECKPOINT = os.path.join(os.path.dirname(__file__), "assets/thegluenote_mid_checkpoint.pt")

from .match import (
    AnchorPointNoteMatcher,
    AutomaticNoteMatcher,
    DualDTWNoteMatcher,
    TheGlueNoteMatcher,
)
from .match import OnlineTransformerMatcher, OnlinePureTransformerMatcher
from .evaluate import (
    fscore_alignments,
    print_fscore_alignments,
    plot_alignment,
    plot_alignment_comparison,
)

__all__ = [
    "AnchorPointNoteMatcher",
    "AutomaticNoteMatcher",
    "DualDTWNoteMatcher",
    "TheGlueNoteMatcher",
    "OnlineTransformerMatcher",
    "OnlinePureTransformerMatcher" "fscore_alignments",
    "plot_alignment_comparison",
    "plot_alignment",
]
