# Train report for javascript / file:///tmp/top-repos-quality-repos-44ftc19l/reveal.js HEAD 0b3e7839ebf4ed8b6c180aca0abafa28c67aee6d

### Classification report

PPCR: 0.708

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.984| 0.979| 0.901| 0.981| 0.941| 5932| 6444| 0.921 |
| `␣` | 0.956| 0.977| 0.624| 0.966| 0.755| 3322| 5198| 0.639 |
| `'` | 0.980| 1.000| 1.000| 0.990| 0.990| 385| 385| 1.000 |
| `⏎` | 0.994| 0.920| 0.390| 0.955| 0.560| 350| 825| 0.424 |
| `⏎⇥⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 13| 318| 0.041 |
| `"` | 0.000| 0.000| 0.000| 0.000| 0.000| 8| 8| 1.000 |
| `⏎⇥⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 5| 341| 0.015 |
| `⏎⏎` | 0.000| 0.000| 0.000| 0.000| 0.000| 3| 440| 0.007 |
| `⏎⏎⇥⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 0| 88| 0.000 |
| `⏎⏎⇥⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 0| 108| 0.000 |
| `macro avg` | 0.391| 0.388| 0.292| 0.389| 0.325| 10018| 14155| 0.708 |
| `weighted avg` | 0.972| 0.974| 0.690| 0.973| 0.765| 10018| 14155| 0.708 |
| `micro avg` | 0.974| 0.974| 0.690| 0.974| 0.808| 10018| 14155| 0.708 |

### Confusion matrix

|refusal|  ∅| ␣| ⏎| '| ⏎⏎| "| ⏎⇥⁻| ⏎⇥⁺| ⏎⏎⇥⁺| ⏎⏎⇥⁻| 
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|512 |5808 |124 |0 |0 |0 |0 |0 |0 |0 |0 |
|1876 |76 |3246 |0 |0 |0 |0 |0 |0 |0 |0 |
|475 |7 |21 |322 |0 |0 |0 |0 |0 |0 |0 |
|0 |0 |0 |0 |385 |0 |0 |0 |0 |0 |0 |
|437 |1 |0 |2 |0 |0 |0 |0 |0 |0 |0 |
|0 |0 |0 |0 |8 |0 |0 |0 |0 |0 |0 |
|305 |13 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|336 |0 |5 |0 |0 |0 |0 |0 |0 |0 |0 |
|88 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|108 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|
| js/reveal.js | 111 |
| plugin/markdown/markdown.js | 22 |
| plugin/remotes/remotes.js | 20 |
| plugin/multiplex/index.js | 19 |
| plugin/notes-server/index.js | 18 |
| plugin/notes-server/client.js | 15 |
| plugin/notes/notes.js | 15 |
| plugin/zoom-js/zoom.js | 10 |
| Gruntfile.js | 9 |
| plugin/multiplex/master.js | 8 |

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\"": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 8}, "\u0027": {"f1-score": 0.9897172236503856, "precision": 0.9796437659033079, "recall": 1.0, "support": 385}, "macro avg": {"f1-score": 0.3892895602137343, "precision": 0.3912874558104109, "recall": 0.38762186416959943, "support": 10018}, "micro avg": {"f1-score": 0.9743461768816131, "precision": 0.9743461768816131, "recall": 0.9743461768816131, "support": 10018}, "weighted avg": {"f1-score": 0.9729442167217784, "precision": 0.9717336179720255, "recall": 0.9743461768816131, "support": 10018}, "\u2205": {"f1-score": 0.9813297288164229, "precision": 0.9835732430143945, "recall": 0.9790964261631827, "support": 5932}, "\u23ce": {"f1-score": 0.9554896142433236, "precision": 0.9938271604938271, "recall": 0.92, "support": 350}, "\u23ce\u21e5\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 5}, "\u23ce\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 13}, "\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 3}, "\u23ce\u23ce\u21e5\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 0}, "\u23ce\u23ce\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 0}, "\u2423": {"f1-score": 0.9663590354272105, "precision": 0.9558303886925795, "recall": 0.9771222155328115, "support": 3322}},
  "cl_report_full": {"\"": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 8}, "\u0027": {"f1-score": 0.9897172236503856, "precision": 0.9796437659033079, "recall": 1.0, "support": 385}, "macro avg": {"f1-score": 0.3246258322710197, "precision": 0.3912874558104109, "recall": 0.2916077518843602, "support": 14155}, "micro avg": {"f1-score": 0.8075952508997642, "precision": 0.9743461768816131, "recall": 0.689579653832568, "support": 14155}, "weighted avg": {"f1-score": 0.765211698111354, "precision": 0.8833361070779914, "recall": 0.689579653832568, "support": 14155}, "\u2205": {"f1-score": 0.9406429670418658, "precision": 0.9835732430143945, "recall": 0.9013035381750466, "support": 6444}, "\u23ce": {"f1-score": 0.5604873803307223, "precision": 0.9938271604938271, "recall": 0.3903030303030303, "support": 825}, "\u23ce\u21e5\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 341}, "\u23ce\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 318}, "\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 440}, "\u23ce\u23ce\u21e5\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 88}, "\u23ce\u23ce\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 108}, "\u2423": {"f1-score": 0.7554107516872237, "precision": 0.9558303886925795, "recall": 0.6244709503655252, "support": 5198}},
  "ppcr": 0.7077357824090428
}
```
</details>
