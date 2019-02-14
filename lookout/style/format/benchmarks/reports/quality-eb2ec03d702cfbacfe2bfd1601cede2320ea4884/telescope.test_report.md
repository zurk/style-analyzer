# Test report for javascript / file:///tmp/top-repos-quality-repos-w_xek5jl/telescope HEAD 534030114f47696fe3f3b08ea7ca49467428f2af

### Classification report

PPCR: 0.553

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.801| 1.000| 0.627| 0.890| 0.703| 121| 193| 0.627 |
| `␣` | 0.000| 0.000| 0.000| 0.000| 0.000| 24| 63| 0.381 |
| `'` | 1.000| 1.000| 0.846| 1.000| 0.917| 22| 26| 0.846 |
| `⏎` | 0.000| 0.000| 0.000| 0.000| 0.000| 6| 31| 0.194 |
| `macro avg` | 0.450| 0.500| 0.368| 0.472| 0.405| 173| 313| 0.553 |
| `weighted avg` | 0.688| 0.827| 0.457| 0.749| 0.510| 173| 313| 0.553 |
| `micro avg` | 0.827| 0.827| 0.457| 0.827| 0.588| 173| 313| 0.553 |

### Confusion matrix

|refusal|  ∅| '| ␣| ⏎| 
|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |
|72 |121 |0 |0 |0 |
|4 |0 |22 |0 |0 |
|39 |24 |0 |0 |0 |
|25 |6 |0 |0 |0 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\u0027": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 22}, "macro avg": {"f1-score": 0.4724264705882353, "precision": 0.45033112582781454, "recall": 0.5, "support": 173}, "micro avg": {"f1-score": 0.8265895953757225, "precision": 0.8265895953757225, "recall": 0.8265895953757225, "support": 173}, "weighted avg": {"f1-score": 0.7494474668480109, "precision": 0.687631589021169, "recall": 0.8265895953757225, "support": 173}, "\u2205": {"f1-score": 0.8897058823529412, "precision": 0.8013245033112583, "recall": 1.0, "support": 121}, "\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 6}, "\u2423": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 24}},
  "cl_report_full": {"\u0027": {"f1-score": 0.9166666666666666, "precision": 1.0, "recall": 0.8461538461538461, "support": 26}, "macro avg": {"f1-score": 0.4050387596899225, "precision": 0.45033112582781454, "recall": 0.36827421283379835, "support": 313}, "micro avg": {"f1-score": 0.588477366255144, "precision": 0.8265895953757225, "recall": 0.45686900958466453, "support": 313}, "weighted avg": {"f1-score": 0.5099252049434084, "precision": 0.5771745339906481, "recall": 0.45686900958466453, "support": 313}, "\u2205": {"f1-score": 0.7034883720930233, "precision": 0.8013245033112583, "recall": 0.6269430051813472, "support": 193}, "\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 31}, "\u2423": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 63}},
  "ppcr": 0.5527156549520766
}
```
</details>
