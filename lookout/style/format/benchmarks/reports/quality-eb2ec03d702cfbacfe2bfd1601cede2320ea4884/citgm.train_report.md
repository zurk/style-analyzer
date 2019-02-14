# Train report for javascript / file:///tmp/top-repos-quality-repos-eof7hnjl/citgm HEAD 0c4c7ccdd1cad8ce9506e34ca523787ba18cafe2

### Classification report

PPCR: 0.806

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.985| 0.997| 0.981| 0.991| 0.983| 11646| 11846| 0.983 |
| `␣` | 0.987| 0.968| 0.623| 0.977| 0.764| 3593| 5581| 0.644 |
| `'` | 1.000| 1.000| 1.000| 1.000| 1.000| 1628| 1628| 1.000 |
| `⏎␣⁺␣⁺` | 0.977| 0.960| 0.772| 0.969| 0.862| 626| 779| 0.804 |
| `⏎␣⁻␣⁻` | 1.000| 0.963| 0.634| 0.981| 0.776| 482| 732| 0.658 |
| `⏎` | 0.000| 0.000| 0.000| 0.000| 0.000| 49| 1366| 0.036 |
| `⏎⏎` | 0.000| 0.000| 0.000| 0.000| 0.000| 5| 442| 0.011 |
| `micro avg` | 0.987| 0.987| 0.795| 0.987| 0.880| 18029| 22374| 0.806 |
| `macro avg` | 0.707| 0.698| 0.573| 0.703| 0.626| 18029| 22374| 0.806 |
| `weighted avg` | 0.984| 0.987| 0.795| 0.985| 0.839| 18029| 22374| 0.806 |

### Confusion matrix

|refusal|  ∅| ␣| '| ⏎| ⏎␣⁺␣⁺| ⏎␣⁻␣⁻| ⏎⏎| 
|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |
|200 |11616 |24 |0 |0 |6 |0 |0 |
|1988 |111 |3477 |0 |0 |5 |0 |0 |
|0 |0 |0 |1628 |0 |0 |0 |0 |
|1317 |33 |15 |0 |0 |1 |0 |0 |
|153 |17 |8 |0 |0 |601 |0 |0 |
|250 |16 |0 |0 |0 |2 |464 |0 |
|437 |5 |0 |0 |0 |0 |0 |0 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|
| lib/lookup.js | 21 |
| test/test-lookup.js | 21 |
| lib/common-args.js | 20 |
| bin/citgm-all.js | 20 |
| lib/match-conditions.js | 15 |
| bin/citgm.js | 14 |
| lib/out.js | 13 |
| lib/reporter/tap.js | 11 |
| lib/citgm.js | 10 |
| test/test-match-conditions.js | 9 |

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\u0027": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 1628}, "macro avg": {"f1-score": 0.7025143589618804, "precision": 0.7069246159995831, "recall": 0.6982655012940139, "support": 18029}, "micro avg": {"f1-score": 0.9865217150146985, "precision": 0.9865217150146985, "recall": 0.9865217150146985, "support": 18029}, "weighted avg": {"f1-score": 0.9849993351019407, "precision": 0.9835916654630353, "recall": 0.9865217150146985, "support": 18029}, "\u2205": {"f1-score": 0.9909571745435933, "precision": 0.9845736565519579, "recall": 0.9974240082431737, "support": 11646}, "\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 49}, "\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 5}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.9685737308622079, "precision": 0.9772357723577236, "recall": 0.9600638977635783, "support": 626}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.9809725158562368, "precision": 1.0, "recall": 0.9626556016597511, "support": 482}, "\u2423": {"f1-score": 0.9770970914711254, "precision": 0.9866628830874007, "recall": 0.9677150013915947, "support": 3593}},
  "cl_report_full": {"\u0027": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 1628}, "macro avg": {"f1-score": 0.6263596612511562, "precision": 0.7069246159995831, "recall": 0.5727103571476136, "support": 22374}, "micro avg": {"f1-score": 0.8804296710640299, "precision": 0.9865217150146985, "recall": 0.7949405560025029, "support": 22374}, "weighted avg": {"f1-score": 0.8389105279407109, "precision": 0.9069049679401066, "recall": 0.7949405560025029, "support": 22374}, "\u2205": {"f1-score": 0.9825748604297072, "precision": 0.9845736565519579, "recall": 0.9805841634306939, "support": 11846}, "\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 1366}, "\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 442}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.8622668579626973, "precision": 0.9772357723577236, "recall": 0.7715019255455713, "support": 779}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.7759197324414716, "precision": 1.0, "recall": 0.6338797814207651, "support": 732}, "\u2423": {"f1-score": 0.7637561779242175, "precision": 0.9866628830874007, "recall": 0.6230066296362659, "support": 5581}},
  "ppcr": 0.8058013765978368
}
```
</details>
