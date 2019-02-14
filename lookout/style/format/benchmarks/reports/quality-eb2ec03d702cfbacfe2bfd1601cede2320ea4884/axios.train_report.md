# Train report for javascript / file:///tmp/top-repos-quality-repos-68x3i7pl/axios HEAD 21ae22dbd3ae3d3a55d9efd4eead3dd7fb6d8e6e

### Classification report

PPCR: 0.998

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.982| 0.994| 0.994| 0.988| 0.988| 13806| 13816| 0.999 |
| `␣` | 0.969| 0.955| 0.955| 0.962| 0.962| 3873| 3873| 1.000 |
| `'` | 0.999| 1.000| 1.000| 1.000| 1.000| 2692| 2692| 1.000 |
| `⏎␣⁻␣⁻` | 0.991| 0.959| 0.959| 0.975| 0.975| 804| 804| 1.000 |
| `⏎⏎` | 0.977| 0.946| 0.946| 0.961| 0.961| 222| 222| 1.000 |
| `⏎` | 0.000| 0.000| 0.000| 0.000| 0.000| 57| 58| 0.983 |
| `⏎␣⁺␣⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 27| 27| 1.000 |
| `"` | 0.000| 0.000| 0.000| 0.000| 0.000| 2| 34| 0.059 |
| `macro avg` | 0.615| 0.607| 0.607| 0.611| 0.611| 21483| 21526| 0.998 |
| `weighted avg` | 0.978| 0.982| 0.980| 0.980| 0.978| 21483| 21526| 0.998 |
| `micro avg` | 0.982| 0.982| 0.980| 0.982| 0.981| 21483| 21526| 0.998 |

### Confusion matrix

|refusal|  ∅| ␣| '| ⏎| ⏎␣⁺␣⁺| ⏎␣⁻␣⁻| ⏎⏎| "| 
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |0 |
|10 |13728 |78 |0 |0 |0 |0 |0 |0 |
|0 |167 |3700 |0 |0 |0 |6 |0 |0 |
|0 |0 |0 |2692 |0 |0 |0 |0 |0 |
|1 |27 |24 |0 |0 |0 |1 |5 |0 |
|0 |18 |9 |0 |0 |0 |0 |0 |0 |
|0 |27 |6 |0 |0 |0 |771 |0 |0 |
|0 |9 |3 |0 |0 |0 |0 |210 |0 |
|32 |0 |0 |2 |0 |0 |0 |0 |0 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|
| lib/adapters/http.js | 33 |
| lib/adapters/xhr.js | 29 |
| test/specs/requests.spec.js | 28 |
| lib/core/dispatchRequest.js | 23 |
| karma.conf.js | 21 |
| examples/server.js | 19 |
| lib/utils.js | 18 |
| lib/helpers/buildURL.js | 14 |
| lib/helpers/cookies.js | 13 |
| test/specs/progress.spec.js | 12 |

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\"": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 2}, "\u0027": {"f1-score": 0.9996286669142221, "precision": 0.9992576095025983, "recall": 1.0, "support": 2692}, "macro avg": {"f1-score": 0.6107027283015923, "precision": 0.6147307560586028, "recall": 0.6068229045573844, "support": 21483}, "micro avg": {"f1-score": 0.9822184983475306, "precision": 0.9822184983475306, "recall": 0.9822184983475306, "support": 21483}, "weighted avg": {"f1-score": 0.9801947415214941, "precision": 0.978259853807239, "recall": 0.9822184983475306, "support": 21483}, "\u2205": {"f1-score": 0.9882657836008928, "precision": 0.9822552947910704, "recall": 0.9943502824858758, "support": 13806}, "\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 57}, "\u23ce\u23ce": {"f1-score": 0.9610983981693363, "precision": 0.9767441860465116, "recall": 0.9459459459459459, "support": 222}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 27}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.9747155499367889, "precision": 0.9910025706940874, "recall": 0.9589552238805971, "support": 804}, "\u2423": {"f1-score": 0.9619134277914987, "precision": 0.9685863874345549, "recall": 0.9553317841466563, "support": 3873}},
  "cl_report_full": {"\"": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 34}, "\u0027": {"f1-score": 0.9996286669142221, "precision": 0.9992576095025983, "recall": 1.0, "support": 2692}, "macro avg": {"f1-score": 0.6106582790993218, "precision": 0.6147307560586028, "recall": 0.6067329409027009, "support": 21526}, "micro avg": {"f1-score": 0.9812364853867794, "precision": 0.9822184983475306, "recall": 0.9802564340797175, "support": 21526}, "weighted avg": {"f1-score": 0.9784675930741294, "precision": 0.9767620083753984, "recall": 0.9802564340797175, "support": 21526}, "\u2205": {"f1-score": 0.9879101899827288, "precision": 0.9822552947910704, "recall": 0.9936305732484076, "support": 13816}, "\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 58}, "\u23ce\u23ce": {"f1-score": 0.9610983981693363, "precision": 0.9767441860465116, "recall": 0.9459459459459459, "support": 222}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 27}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.9747155499367889, "precision": 0.9910025706940874, "recall": 0.9589552238805971, "support": 804}, "\u2423": {"f1-score": 0.9619134277914987, "precision": 0.9685863874345549, "recall": 0.9553317841466563, "support": 3873}},
  "ppcr": 0.9980024156833597
}
```
</details>
