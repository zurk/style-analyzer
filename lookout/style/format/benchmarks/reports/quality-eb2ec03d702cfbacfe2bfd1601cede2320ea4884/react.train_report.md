# Train report for javascript / file:///tmp/top-repos-quality-repos-znzzmvey/react HEAD 1034e26fe5e42ba07492a736da7bdf5bf2108bc6

### Classification report

PPCR: 0.940

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.971| 0.992| 0.987| 0.982| 0.979| 211123| 212146| 0.995 |
| `␣` | 0.952| 0.976| 0.936| 0.964| 0.944| 72893| 76035| 0.959 |
| `'` | 1.000| 1.000| 1.000| 1.000| 1.000| 34635| 34635| 1.000 |
| `⏎` | 0.928| 0.913| 0.524| 0.921| 0.670| 15735| 27399| 0.574 |
| `⏎␣⁺␣⁺` | 0.986| 0.693| 0.642| 0.814| 0.777| 14170| 15310| 0.926 |
| `⏎␣⁻␣⁻` | 0.986| 0.885| 0.825| 0.932| 0.898| 13908| 14925| 0.932 |
| `"` | 1.000| 1.000| 1.000| 1.000| 1.000| 2630| 2630| 1.000 |
| `⏎⏎` | 0.945| 0.835| 0.208| 0.887| 0.341| 1721| 6919| 0.249 |
| `⏎␣⁻␣⁻␣⁻␣⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 282| 400| 0.705 |
| `micro avg` | 0.969| 0.969| 0.911| 0.969| 0.939| 367097| 390399| 0.940 |
| `macro avg` | 0.863| 0.811| 0.680| 0.833| 0.734| 367097| 390399| 0.940 |
| `weighted avg` | 0.969| 0.969| 0.911| 0.968| 0.929| 367097| 390399| 0.940 |

### Confusion matrix

|refusal|  ∅| ␣| '| ⏎| ⏎␣⁺␣⁺| ⏎␣⁻␣⁻| ⏎⏎| "| ⏎␣⁻␣⁻␣⁻␣⁻| 
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|1023 |209440 |1501 |0 |0 |139 |43 |0 |0 |0 |
|3142 |877 |71168 |0 |848 |0 |0 |0 |0 |0 |
|0 |0 |0 |34635 |0 |0 |0 |0 |0 |0 |
|11664 |464 |820 |0 |14368 |0 |0 |83 |0 |0 |
|1140 |3420 |924 |0 |4 |9822 |0 |0 |0 |0 |
|1017 |1214 |316 |0 |71 |0 |12307 |0 |0 |0 |
|5198 |98 |10 |0 |176 |0 |0 |1437 |0 |0 |
|0 |0 |0 |0 |0 |0 |0 |0 |2630 |0 |
|118 |119 |12 |0 |13 |0 |138 |0 |0 |0 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|
| fixtures/attribute-behavior/src/attributes.js | 538 |
| packages/events/__tests__/ResponderEventPlugin-test.internal.js | 485 |
| scripts/bench/benchmarks/pe-no-components/benchmark.js | 466 |
| scripts/bench/benchmarks/pe-class-components/benchmark.js | 446 |
| scripts/bench/benchmarks/pe-functional-components/benchmark.js | 413 |
| packages/react/src/__tests__/ReactProfiler-test.internal.js | 350 |
| scripts/rollup/build.js | 226 |
| packages/react-reconciler/src/__tests__/ReactNewContext-test.internal.js | 215 |
| packages/react-reconciler/src/__tests__/ReactSuspenseWithNoopRenderer-test.internal.js | 195 |
| packages/react-reconciler/src/__tests__/ReactIncremental-test.internal.js | 160 |

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\"": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 2630}, "\u0027": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 34635}, "macro avg": {"f1-score": 0.8332764692499635, "precision": 0.863162635162335, "recall": 0.8105008600940784, "support": 367097}, "micro avg": {"f1-score": 0.9692451858773021, "precision": 0.9692451858773021, "recall": 0.9692451858773021, "support": 367097}, "weighted avg": {"f1-score": 0.967810266727294, "precision": 0.9687764490369339, "recall": 0.9692451858773021, "support": 367097}, "\u2205": {"f1-score": 0.9815467891413107, "precision": 0.9712844104771091, "recall": 0.9920283436669619, "support": 211123}, "\u23ce": {"f1-score": 0.9205830530193817, "precision": 0.9281653746770026, "recall": 0.9131236097870988, "support": 15735}, "\u23ce\u23ce": {"f1-score": 0.8867633446467141, "precision": 0.9453947368421053, "recall": 0.8349796629866357, "support": 1721}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.8140566076830632, "precision": 0.9860455777532376, "recall": 0.6931545518701482, "support": 14170}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.9324897711774511, "precision": 0.9855060858424087, "recall": 0.8848863963186655, "support": 13908}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 282}, "\u2423": {"f1-score": 0.9640486575817507, "precision": 0.9520675308691523, "recall": 0.9763351762171951, "support": 72893}},
  "cl_report_full": {"\"": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 2630}, "\u0027": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 34635}, "macro avg": {"f1-score": 0.7343461364819598, "precision": 0.863162635162335, "recall": 0.6801614891103428, "support": 390399}, "micro avg": {"f1-score": 0.9394293831254554, "precision": 0.9692451858773021, "recall": 0.9113932156588516, "support": 390399}, "weighted avg": {"f1-score": 0.9292865399634006, "precision": 0.9669250757975776, "recall": 0.9113932156588516, "support": 390399}, "\u2205": {"f1-score": 0.9791994913249396, "precision": 0.9712844104771091, "recall": 0.9872446334128383, "support": 212146}, "\u23ce": {"f1-score": 0.6701648825765526, "precision": 0.9281653746770026, "recall": 0.5243987006825067, "support": 27399}, "\u23ce\u23ce": {"f1-score": 0.3405616779239246, "precision": 0.9453947368421053, "recall": 0.20768897239485476, "support": 6919}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.7773337026631317, "precision": 0.9860455777532376, "recall": 0.641541476159373, "support": 15310}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.8978951592310219, "precision": 0.9855060858424087, "recall": 0.8245896147403685, "support": 14925}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 400}, "\u2423": {"f1-score": 0.943960314618068, "precision": 0.9520675308691523, "recall": 0.9359900046031433, "support": 76035}},
  "ppcr": 0.9403123471115449
}
```
</details>
