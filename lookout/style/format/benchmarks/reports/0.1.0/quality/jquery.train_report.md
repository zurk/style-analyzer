# Train report for javascript / file:///tmp/top-repos-quality-repos-0qyyera1/jquery HEAD dae5f3ce3d2df27873d01f0d9682f6a91ad66b87

### Classification report

PPCR: 0.901

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.994| 0.993| 0.988| 0.993| 0.991| 87702| 88067| 0.996 |
| `␣` | 0.963| 0.996| 0.957| 0.979| 0.960| 50317| 52365| 0.961 |
| `␣"` | 0.992| 1.000| 1.000| 0.996| 0.996| 14651| 14651| 1.000 |
| `"␣` | 0.977| 0.990| 0.990| 0.984| 0.984| 9391| 9391| 1.000 |
| `"` | 0.988| 0.997| 0.997| 0.993| 0.993| 7456| 7456| 1.000 |
| `⏎` | 0.961| 0.759| 0.244| 0.848| 0.389| 3080| 9586| 0.321 |
| `⏎⇥⁻` | 0.919| 0.893| 0.494| 0.906| 0.643| 2364| 4276| 0.553 |
| `⏎⇥⁺` | 0.921| 0.626| 0.204| 0.745| 0.334| 1519| 4655| 0.326 |
| `⏎⏎⇥⁺` | 0.922| 0.870| 0.480| 0.895| 0.631| 270| 490| 0.551 |
| `"⏎⇥⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 221| 221| 1.000 |
| `⏎⏎` | 0.000| 0.000| 0.000| 0.000| 0.000| 176| 4913| 0.036 |
| `␣␣` | 0.000| 0.000| 0.000| 0.000| 0.000| 156| 159| 0.981 |
| `⏎⇥⁺"` | 0.000| 0.000| 0.000| 0.000| 0.000| 105| 105| 1.000 |
| `⏎⇥⁻⇥⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 40| 118| 0.339 |
| `⏎⏎⇥⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 38| 616| 0.062 |
| `macro avg` | 0.576| 0.542| 0.424| 0.556| 0.461| 177486| 197069| 0.901 |
| `weighted avg` | 0.977| 0.981| 0.884| 0.979| 0.899| 177486| 197069| 0.901 |
| `micro avg` | 0.981| 0.981| 0.884| 0.981| 0.930| 177486| 197069| 0.901 |

### Confusion matrix

|refusal|  ∅| ␣| ␣"| ⏎| "␣| "| ⏎⇥⁺| ⏎⏎| ⏎⇥⁻| ⏎⏎⇥⁻| ⏎⏎⇥⁺| "⏎⇥⁻| ␣␣| ⏎⇥⁺"| ⏎⇥⁻⇥⁻| 
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|365 |87053 |635 |0 |4 |0 |0 |0 |0 |10 |0 |0 |0 |0 |0 |0 |
|2048 |138 |50113 |0 |4 |0 |0 |32 |0 |29 |0 |1 |0 |0 |0 |0 |
|0 |0 |0 |14651 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|6506 |219 |470 |0 |2339 |0 |0 |13 |0 |39 |0 |0 |0 |0 |0 |0 |
|0 |0 |0 |0 |0 |9300 |91 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|0 |0 |0 |20 |0 |0 |7436 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|3136 |112 |429 |0 |22 |0 |0 |951 |0 |0 |0 |5 |0 |0 |0 |0 |
|4737 |0 |77 |0 |28 |0 |0 |12 |0 |46 |0 |13 |0 |0 |0 |0 |
|1912 |52 |174 |0 |25 |0 |0 |1 |0 |2112 |0 |0 |0 |0 |0 |0 |
|578 |2 |0 |0 |0 |0 |0 |1 |0 |34 |0 |1 |0 |0 |0 |0 |
|220 |0 |1 |0 |12 |0 |0 |22 |0 |0 |0 |235 |0 |0 |0 |0 |
|0 |0 |0 |0 |0 |221 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|3 |0 |156 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|0 |0 |0 |105 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|78 |4 |6 |0 |1 |0 |0 |1 |0 |28 |0 |0 |0 |0 |0 |0 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|
| test/unit/event.js | 392 |
| test/unit/offset.js | 287 |
| test/unit/ajax.js | 251 |
| test/unit/core.js | 202 |
| test/unit/wrap.js | 179 |
| test/unit/css.js | 133 |
| test/unit/manipulation.js | 125 |
| test/unit/attributes.js | 76 |
| test/unit/traversing.js | 74 |
| test/unit/deferred.js | 72 |

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\"": {"f1-score": 0.99259160381766, "precision": 0.9879101899827288, "recall": 0.9973175965665236, "support": 7456}, "\"\u23ce\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 221}, "\"\u2423": {"f1-score": 0.9835025380710659, "precision": 0.976788152504989, "recall": 0.9903098711532318, "support": 9391}, "macro avg": {"f1-score": 0.5559289275866124, "precision": 0.5756417907300793, "recall": 0.5416953243619603, "support": 177486}, "micro avg": {"f1-score": 0.9814295212016723, "precision": 0.9814295212016723, "recall": 0.9814295212016723, "support": 177486}, "weighted avg": {"f1-score": 0.9788197223434328, "precision": 0.9772766813608333, "recall": 0.9814295212016723, "support": 177486}, "\u2205": {"f1-score": 0.9932908113782363, "precision": 0.9939826444393697, "recall": 0.9925999407083077, "support": 87702}, "\u23ce": {"f1-score": 0.8482320942883045, "precision": 0.9605749486652977, "recall": 0.7594155844155844, "support": 3080}, "\u23ce\u21e5\u207a": {"f1-score": 0.7452978056426331, "precision": 0.920619554695063, "recall": 0.6260697827518104, "support": 1519}, "\u23ce\u21e5\u207a\"": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 105}, "\u23ce\u21e5\u207b": {"f1-score": 0.9060489060489061, "precision": 0.9190600522193212, "recall": 0.8934010152284264, "support": 2364}, "\u23ce\u21e5\u207b\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 40}, "\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 176}, "\u23ce\u23ce\u21e5\u207a": {"f1-score": 0.8952380952380952, "precision": 0.9215686274509803, "recall": 0.8703703703703703, "support": 270}, "\u23ce\u23ce\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 38}, "\u2423": {"f1-score": 0.9789798589540722, "precision": 0.9625823553139586, "recall": 0.9959457042351492, "support": 50317}, "\u2423\"": {"f1-score": 0.9957522003602133, "precision": 0.9915403356794802, "recall": 1.0, "support": 14651}, "\u2423\u2423": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 156}},
  "cl_report_full": {"\"": {"f1-score": 0.99259160381766, "precision": 0.9879101899827288, "recall": 0.9973175965665236, "support": 7456}, "\"\u23ce\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 221}, "\"\u2423": {"f1-score": 0.9835025380710659, "precision": 0.976788152504989, "recall": 0.9903098711532318, "support": 9391}, "macro avg": {"f1-score": 0.46131982430103025, "precision": 0.5756417907300793, "recall": 0.42366114629993895, "support": 197069}, "micro avg": {"f1-score": 0.9301170722590808, "precision": 0.9814295212016723, "recall": 0.883903607365948, "support": 197069}, "weighted avg": {"f1-score": 0.8987838426001237, "precision": 0.9483158328013788, "recall": 0.883903607365948, "support": 197069}, "\u2205": {"f1-score": 0.991226721777201, "precision": 0.9939826444393697, "recall": 0.9884860390384593, "support": 88067}, "\u23ce": {"f1-score": 0.3891523167789701, "precision": 0.9605749486652977, "recall": 0.24400166910077195, "support": 9586}, "\u23ce\u21e5\u207a": {"f1-score": 0.3343881856540084, "precision": 0.920619554695063, "recall": 0.20429645542427496, "support": 4655}, "\u23ce\u21e5\u207a\"": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 105}, "\u23ce\u21e5\u207b": {"f1-score": 0.6425311834499544, "precision": 0.9190600522193212, "recall": 0.4939195509822264, "support": 4276}, "\u23ce\u21e5\u207b\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 118}, "\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 4913}, "\u23ce\u23ce\u21e5\u207a": {"f1-score": 0.6308724832214765, "precision": 0.9215686274509803, "recall": 0.47959183673469385, "support": 490}, "\u23ce\u23ce\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 616}, "\u2423": {"f1-score": 0.9597801313849043, "precision": 0.9625823553139586, "recall": 0.956994175498902, "support": 52365}, "\u2423\"": {"f1-score": 0.9957522003602133, "precision": 0.9915403356794802, "recall": 1.0, "support": 14651}, "\u2423\u2423": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 159}},
  "ppcr": 0.9006287138007499
}
```
</details>