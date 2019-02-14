# Train report for javascript / file:///tmp/top-repos-quality-repos-68du5go8/freeCodeCamp HEAD cf65516cce60645a417e44c4fcea7418ca920572

### Classification report

PPCR: 0.816

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.969| 0.995| 0.899| 0.982| 0.933| 53471| 59177| 0.904 |
| `␣` | 0.972| 0.979| 0.799| 0.975| 0.877| 23677| 29025| 0.816 |
| `'` | 0.981| 1.000| 1.000| 0.991| 0.991| 10869| 10869| 1.000 |
| `⏎` | 0.939| 0.869| 0.398| 0.903| 0.559| 4340| 9469| 0.458 |
| `⏎␣⁺␣⁺` | 0.956| 0.599| 0.309| 0.737| 0.467| 2269| 4396| 0.516 |
| `⏎␣⁻␣⁻` | 0.933| 0.827| 0.434| 0.877| 0.593| 2091| 3984| 0.525 |
| `⏎⏎` | 0.929| 0.796| 0.177| 0.857| 0.297| 495| 2226| 0.222 |
| `"` | 0.000| 0.000| 0.000| 0.000| 0.000| 208| 208| 1.000 |
| `⏎␣⁻␣⁻␣⁻␣⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 129| 224| 0.576 |
| `micro avg` | 0.969| 0.969| 0.790| 0.969| 0.870| 97549| 119578| 0.816 |
| `macro avg` | 0.742| 0.674| 0.446| 0.702| 0.524| 97549| 119578| 0.816 |
| `weighted avg` | 0.965| 0.969| 0.790| 0.966| 0.851| 97549| 119578| 0.816 |

### Confusion matrix

|refusal|  ∅| ␣| '| ⏎| ⏎␣⁺␣⁺| ⏎␣⁻␣⁻| ⏎⏎| "| ⏎␣⁻␣⁻␣⁻␣⁻| 
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|5706 |53193 |273 |0 |0 |1 |3 |1 |0 |0 |
|5348 |281 |23181 |0 |148 |58 |5 |4 |0 |0 |
|0 |0 |0 |10869 |0 |0 |0 |0 |0 |0 |
|5129 |393 |148 |0 |3771 |3 |0 |25 |0 |0 |
|2127 |755 |155 |0 |0 |1359 |0 |0 |0 |0 |
|1893 |258 |83 |0 |20 |0 |1730 |0 |0 |0 |
|1731 |13 |12 |0 |76 |0 |0 |394 |0 |0 |
|0 |0 |0 |208 |0 |0 |0 |0 |0 |0 |
|95 |11 |0 |0 |1 |0 |117 |0 |0 |0 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|
| api-server/public/js/calculator.js | 320 |
| api-server/common/models/user.js | 202 |
| api-server/server/utils/map.js | 69 |
| api-server/server/utils/user-stats.test.js | 64 |
| api-server/server/boot/challenge.js | 62 |
| curriculum/test/test-challenges.js | 53 |
| client/src/components/settings/Portfolio.js | 48 |
| api-server/server/boot/certificate.js | 47 |
| api-server/common/utils/ajax-stream.js | 44 |
| api-server/server/boot/settings.js | 43 |

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\"": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 208}, "\u0027": {"f1-score": 0.9905221908320423, "precision": 0.9812223526225512, "recall": 1.0, "support": 10869}, "macro avg": {"f1-score": 0.7023419123928689, "precision": 0.7421277412220041, "recall": 0.6738892803428889, "support": 97549}, "micro avg": {"f1-score": 0.9687131595403335, "precision": 0.9687131595403335, "recall": 0.9687131595403335, "support": 97549}, "weighted avg": {"f1-score": 0.9656451769864802, "precision": 0.9650103466978402, "recall": 0.9687131595403335, "support": 97549}, "\u2205": {"f1-score": 0.9816470588235293, "precision": 0.9688365146437418, "recall": 0.9948009201249275, "support": 53471}, "\u23ce": {"f1-score": 0.9025849688846338, "precision": 0.9389940239043825, "recall": 0.8688940092165899, "support": 4340}, "\u23ce\u23ce": {"f1-score": 0.8574537540805223, "precision": 0.9292452830188679, "recall": 0.795959595959596, "support": 495}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.7365853658536584, "precision": 0.956368754398311, "recall": 0.5989422653151167, "support": 2269}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.8768373035985809, "precision": 0.9326145552560647, "recall": 0.8273553323768532, "support": 2091}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 129}, "\u2423": {"f1-score": 0.9754465694628542, "precision": 0.971868187154117, "recall": 0.9790514000929171, "support": 23677}},
  "cl_report_full": {"\"": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 208}, "\u0027": {"f1-score": 0.9905221908320423, "precision": 0.9812223526225512, "recall": 1.0, "support": 10869}, "macro avg": {"f1-score": 0.5240360685537754, "precision": 0.7421277412220041, "recall": 0.44624040003435705, "support": 119578}, "micro avg": {"f1-score": 0.8704306696081094, "precision": 0.9687131595403335, "recall": 0.7902540601113918, "support": 119578}, "weighted avg": {"f1-score": 0.851099979624981, "precision": 0.9624327732082925, "recall": 0.7902540601113918, "support": 119578}, "\u2205": {"f1-score": 0.9325479264732953, "precision": 0.9688365146437418, "recall": 0.898879632289572, "support": 59177}, "\u23ce": {"f1-score": 0.5592880978865407, "precision": 0.9389940239043825, "recall": 0.3982469109726476, "support": 9469}, "\u23ce\u23ce": {"f1-score": 0.29735849056603775, "precision": 0.9292452830188679, "recall": 0.17699910152740342, "support": 2226}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.4672511603919546, "precision": 0.956368754398311, "recall": 0.3091446769790719, "support": 4396}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.5925672204144545, "precision": 0.9326145552560647, "recall": 0.4342369477911647, "support": 3984}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 224}, "\u2423": {"f1-score": 0.8767895304196531, "precision": 0.971868187154117, "recall": 0.798656330749354, "support": 29025}},
  "ppcr": 0.8157771496429109
}
```
</details>
