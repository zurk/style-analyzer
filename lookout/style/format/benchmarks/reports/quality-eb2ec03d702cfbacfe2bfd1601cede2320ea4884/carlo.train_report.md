# Train report for javascript / file:///tmp/top-repos-quality-repos-b15drnka/carlo HEAD b8ce2bca042c757b13fc82a3e059980342ddd9a8

### Classification report

PPCR: 0.698

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.935| 0.997| 0.930| 0.965| 0.933| 3934| 4217| 0.933 |
| `␣` | 0.979| 0.776| 0.385| 0.866| 0.552| 1029| 2078| 0.495 |
| `'` | 1.000| 1.000| 1.000| 1.000| 1.000| 307| 307| 1.000 |
| `⏎␣⁻␣⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 24| 209| 0.115 |
| `⏎` | 0.000| 0.000| 0.000| 0.000| 0.000| 15| 402| 0.037 |
| `⏎␣⁺␣⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 4| 253| 0.016 |
| `⏎⏎` | 0.000| 0.000| 0.000| 0.000| 0.000| 3| 148| 0.020 |
| `"` | 0.000| 0.000| 0.000| 0.000| 0.000| 0| 0| 0.000 |
| `micro avg` | 0.946| 0.946| 0.660| 0.946| 0.778| 5316| 7614| 0.698 |
| `macro avg` | 0.364| 0.347| 0.289| 0.354| 0.311| 5316| 7614| 0.698 |
| `weighted avg` | 0.939| 0.946| 0.660| 0.940| 0.708| 5316| 7614| 0.698 |

### Confusion matrix

|refusal|  ∅| ␣| '| ⏎| ⏎␣⁺␣⁺| ⏎␣⁻␣⁻| "| ⏎⏎| 
|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |
|283 |3922 |12 |0 |0 |0 |0 |0 |
|1049 |230 |799 |0 |0 |0 |0 |0 |
|0 |0 |0 |307 |0 |0 |0 |0 |
|387 |15 |0 |0 |0 |0 |0 |0 |
|249 |3 |1 |0 |0 |0 |0 |0 |
|185 |20 |4 |0 |0 |0 |0 |0 |
|145 |3 |0 |0 |0 |0 |0 |0 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|
| lib/color.js | 91 |
| lib/rpc.js | 59 |
| lib/find-chrome.js | 57 |
| lib/carlo.js | 43 |
| lib/intercepted_request.js | 15 |
| examples/terminal/main.js | 13 |
| examples/systeminfo/main.js | 9 |
| index.js | 1 |

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\"": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 0}, "\u0027": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 307}, "macro avg": {"f1-score": 0.35391280795421465, "precision": 0.36431689224103664, "recall": 0.34667896136593934, "support": 5316}, "micro avg": {"f1-score": 0.945823927765237, "precision": 0.945823927765237, "recall": 0.945823927765237, "support": 5316}, "weighted avg": {"f1-score": 0.9396636100477115, "precision": 0.9394849634957183, "recall": 0.945823927765237, "support": 5316}, "\u2205": {"f1-score": 0.9651778023871047, "precision": 0.9353684712616265, "recall": 0.9969496695475343, "support": 3934}, "\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 15}, "\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 3}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 4}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 24}, "\u2423": {"f1-score": 0.8661246612466125, "precision": 0.9791666666666666, "recall": 0.7764820213799806, "support": 1029}},
  "cl_report_full": {"\"": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 0}, "\u0027": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 307}, "macro avg": {"f1-score": 0.3106095106773044, "precision": 0.36431689224103664, "recall": 0.2893186733518005, "support": 7614}, "micro avg": {"f1-score": 0.7777262180974478, "precision": 0.945823927765237, "recall": 0.6603624901497241, "support": 7614}, "weighted avg": {"f1-score": 0.7075933839137128, "precision": 0.8256050928084596, "recall": 0.6603624901497241, "support": 7614}, "\u2205": {"f1-score": 0.9326991676575506, "precision": 0.9353684712616265, "recall": 0.9300450557268201, "support": 4217}, "\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 402}, "\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 148}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 253}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 209}, "\u2423": {"f1-score": 0.5521769177608846, "precision": 0.9791666666666666, "recall": 0.3845043310875842, "support": 2078}},
  "ppcr": 0.698187549251379
}
```
</details>
