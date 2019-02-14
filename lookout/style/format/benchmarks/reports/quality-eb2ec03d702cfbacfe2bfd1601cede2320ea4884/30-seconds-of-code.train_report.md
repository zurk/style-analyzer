# Train report for javascript / file:///tmp/top-repos-quality-repos-tnww86x5/30-seconds-of-code HEAD 3a122c9cfcbdc091227879a06a32bc67ccd0d35d

### Classification report

PPCR: 0.868

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.947| 0.996| 0.953| 0.971| 0.950| 36816| 38486| 0.957 |
| `␣` | 0.950| 0.873| 0.544| 0.910| 0.692| 11051| 17746| 0.623 |
| `'` | 1.000| 1.000| 1.000| 1.000| 1.000| 6252| 6252| 1.000 |
| `⏎` | 0.910| 0.838| 0.798| 0.873| 0.851| 3078| 3233| 0.952 |
| `⏎␣⁻␣⁻` | 0.999| 0.812| 0.775| 0.896| 0.873| 1713| 1795| 0.954 |
| `⏎␣⁺␣⁺` | 1.000| 0.795| 0.682| 0.886| 0.811| 1640| 1911| 0.858 |
| `⏎⏎` | 0.000| 0.000| 0.000| 0.000| 0.000| 111| 455| 0.244 |
| `micro avg` | 0.954| 0.954| 0.828| 0.954| 0.886| 60661| 69878| 0.868 |
| `macro avg` | 0.829| 0.759| 0.679| 0.791| 0.739| 60661| 69878| 0.868 |
| `weighted avg` | 0.952| 0.954| 0.828| 0.952| 0.872| 60661| 69878| 0.868 |

### Confusion matrix

|refusal|  ∅| ␣| '| ⏎| ⏎␣⁺␣⁺| ⏎␣⁻␣⁻| ⏎⏎| 
|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |
|1670 |36670 |146 |0 |0 |0 |0 |0 |
|6695 |1381 |9651 |0 |19 |0 |0 |0 |
|0 |0 |0 |6252 |0 |0 |0 |0 |
|155 |181 |317 |0 |2580 |0 |0 |0 |
|271 |293 |42 |0 |0 |1304 |1 |0 |
|82 |183 |7 |0 |132 |0 |1391 |0 |
|344 |8 |0 |0 |103 |0 |0 |0 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|
| scripts/web.js | 231 |
| scripts/util.js | 96 |
| scripts/tdd.js | 52 |
| scripts/localize.js | 41 |
| scripts/rollup.js | 38 |
| test/hexToRGB/hexToRGB.js | 35 |
| test/colorize/colorize.js | 34 |
| scripts/analyze.js | 32 |
| scripts/tag.js | 32 |
| scripts/extract.js | 30 |

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\u0027": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 6252}, "macro avg": {"f1-score": 0.7907849872152053, "precision": 0.8294900636084204, "recall": 0.7592433185556662, "support": 60661}, "micro avg": {"f1-score": 0.9536275366380376, "precision": 0.9536275366380376, "recall": 0.9536275366380376, "support": 60661}, "weighted avg": {"f1-score": 0.9516602777481179, "precision": 0.9523511376841955, "recall": 0.9536275366380376, "support": 60661}, "\u2205": {"f1-score": 0.9709791876290844, "precision": 0.9471536315735096, "recall": 0.9960343328987397, "support": 36816}, "\u23ce": {"f1-score": 0.8728010825439784, "precision": 0.9103740296400847, "recall": 0.8382066276803118, "support": 3078}, "\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 111}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.8858695652173914, "precision": 1.0, "recall": 0.7951219512195122, "support": 1640}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.89597423510467, "precision": 0.9992816091954023, "recall": 0.812025685931115, "support": 1713}, "\u2423": {"f1-score": 0.9098708400113132, "precision": 0.9496211748499459, "recall": 0.8733146321599855, "support": 11051}},
  "cl_report_full": {"\u0027": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 6252}, "macro avg": {"f1-score": 0.7394573888184405, "precision": 0.8294900636084204, "recall": 0.6788529866033083, "support": 69878}, "micro avg": {"f1-score": 0.8862945173473061, "precision": 0.9536275366380376, "recall": 0.8278428117576347, "support": 69878}, "weighted avg": {"f1-score": 0.8722736772593703, "precision": 0.9474238209444655, "recall": 0.8278428117576347, "support": 69878}, "\u2205": {"f1-score": 0.9499753892386207, "precision": 0.9471536315735096, "recall": 0.9528140102894559, "support": 38486}, "\u23ce": {"f1-score": 0.8505027196307895, "precision": 0.9103740296400847, "recall": 0.7980204144757191, "support": 3233}, "\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 455}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.8111975116640746, "precision": 1.0, "recall": 0.6823652537938252, "support": 1911}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.8729212425478508, "precision": 0.9992816091954023, "recall": 0.7749303621169916, "support": 1795}, "\u2423": {"f1-score": 0.691604858647748, "precision": 0.9496211748499459, "recall": 0.5438408655471656, "support": 17746}},
  "ppcr": 0.8680986862818054
}
```
</details>
