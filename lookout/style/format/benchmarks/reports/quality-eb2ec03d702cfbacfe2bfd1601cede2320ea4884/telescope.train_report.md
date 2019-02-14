# Train report for javascript / file:///tmp/top-repos-quality-repos-w_xek5jl/telescope HEAD 534030114f47696fe3f3b08ea7ca49467428f2af

### Classification report

PPCR: 0.227

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `'` | 1.000| 1.000| 1.000| 1.000| 1.000| 203| 203| 1.000 |
| `∅` | 0.000| 0.000| 0.000| 0.000| 0.000| 0| 411| 0.000 |
| `␣` | 0.000| 0.000| 0.000| 0.000| 0.000| 0| 189| 0.000 |
| `⏎` | 0.000| 0.000| 0.000| 0.000| 0.000| 0| 93| 0.000 |
| `macro avg` | 0.250| 0.250| 0.250| 0.250| 0.250| 203| 896| 0.227 |
| `weighted avg` | 1.000| 1.000| 0.227| 1.000| 0.227| 203| 896| 0.227 |
| `micro avg` | 1.000| 1.000| 0.227| 1.000| 0.369| 203| 896| 0.227 |

### Confusion matrix

|refusal|  ∅| '| ␣| ⏎| 
|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |
|411 |0 |0 |0 |0 |
|0 |0 |203 |0 |0 |
|189 |0 |0 |0 |0 |
|93 |0 |0 |0 |0 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\u0027": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 203}, "macro avg": {"f1-score": 0.25, "precision": 0.25, "recall": 0.25, "support": 203}, "micro avg": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 203}, "weighted avg": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 203}, "\u2205": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 0}, "\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 0}, "\u2423": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 0}},
  "cl_report_full": {"\u0027": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 203}, "macro avg": {"f1-score": 0.25, "precision": 0.25, "recall": 0.25, "support": 896}, "micro avg": {"f1-score": 0.36942675159235666, "precision": 1.0, "recall": 0.2265625, "support": 896}, "weighted avg": {"f1-score": 0.2265625, "precision": 0.2265625, "recall": 0.2265625, "support": 896}, "\u2205": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 411}, "\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 93}, "\u2423": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 189}},
  "ppcr": 0.2265625
}
```
</details>
