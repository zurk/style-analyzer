# Train report for javascript / file:///tmp/top-repos-quality-repos-pfwm2g26/redux HEAD 902484ed735d38aec06683c847810a7218d8dba2

### Classification report

PPCR: 0.992

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.973| 0.996| 0.986| 0.984| 0.980| 16697| 16858| 0.990 |
| `␣` | 0.965| 0.981| 0.981| 0.973| 0.973| 7875| 7875| 1.000 |
| `'` | 1.000| 1.000| 1.000| 1.000| 1.000| 1463| 1463| 1.000 |
| `⏎` | 0.912| 0.678| 0.672| 0.778| 0.774| 429| 433| 0.991 |
| `⏎␣⁺␣⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 193| 193| 1.000 |
| `⏎␣⁻␣⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 186| 186| 1.000 |
| `⏎⏎` | 1.000| 0.799| 0.799| 0.888| 0.888| 139| 139| 1.000 |
| `"` | 1.000| 1.000| 0.033| 1.000| 0.063| 2| 61| 0.033 |
| `micro avg` | 0.972| 0.972| 0.964| 0.972| 0.968| 26984| 27208| 0.992 |
| `macro avg` | 0.731| 0.682| 0.559| 0.703| 0.585| 26984| 27208| 0.992 |
| `weighted avg` | 0.958| 0.972| 0.964| 0.964| 0.959| 26984| 27208| 0.992 |

### Confusion matrix

|refusal|  ∅| ␣| '| ⏎| ⏎␣⁺␣⁺| ⏎␣⁻␣⁻| ⏎⏎| "| 
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |0 |
|161 |16630 |67 |0 |0 |0 |0 |0 |0 |
|0 |153 |7722 |0 |0 |0 |0 |0 |0 |
|0 |0 |0 |1463 |0 |0 |0 |0 |0 |
|4 |61 |77 |0 |291 |0 |0 |0 |0 |
|0 |76 |117 |0 |0 |0 |0 |0 |0 |
|0 |170 |16 |0 |0 |0 |0 |0 |0 |
|0 |0 |0 |0 |28 |0 |0 |111 |0 |
|59 |0 |0 |0 |0 |0 |0 |0 |2 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|
| test/createStore.spec.js | 76 |
| examples/todomvc/src/reducers/todos.spec.js | 59 |
| src/combineReducers.js | 30 |
| test/combineReducers.spec.js | 23 |
| examples/todos-flow/src/__tests__/reducers/todos.test.js | 23 |
| examples/todos/src/reducers/todos.spec.js | 21 |
| test/helpers/reducers.js | 14 |
| test/bindActionCreators.spec.js | 13 |
| examples/real-world/src/actions/index.js | 12 |
| examples/real-world/src/middleware/api.js | 12 |

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\"": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 2}, "\u0027": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 1463}, "macro avg": {"f1-score": 0.7029236038360638, "precision": 0.731335006415827, "recall": 0.6816801951350733, "support": 26984}, "micro avg": {"f1-score": 0.9716498665876074, "precision": 0.9716498665876074, "recall": 0.9716498665876074, "support": 26984}, "weighted avg": {"f1-score": 0.9642925639095843, "precision": 0.9577978424324796, "recall": 0.9716498665876074, "support": 26984}, "\u2205": {"f1-score": 0.9844022849024774, "precision": 0.973083674663546, "recall": 0.9959873031083428, "support": 16697}, "\u23ce": {"f1-score": 0.7780748663101604, "precision": 0.9122257053291536, "recall": 0.6783216783216783, "support": 429}, "\u23ce\u23ce": {"f1-score": 0.8880000000000001, "precision": 1.0, "recall": 0.7985611510791367, "support": 139}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 193}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 186}, "\u2423": {"f1-score": 0.9729116794758724, "precision": 0.9653706713339167, "recall": 0.9805714285714285, "support": 7875}},
  "cl_report_full": {"\"": {"f1-score": 0.06349206349206349, "precision": 1.0, "recall": 0.03278688524590164, "support": 61}, "\u0027": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 1463}, "macro avg": {"f1-score": 0.5847592029451605, "precision": 0.731335006415827, "recall": 0.5588062695147284, "support": 27208}, "micro avg": {"f1-score": 0.9676335990552112, "precision": 0.9716498665876074, "recall": 0.9636503969420759, "support": 27208}, "weighted avg": {"f1-score": 0.9594034748251798, "precision": 0.9579731091825997, "recall": 0.9636503969420759, "support": 27208}, "\u2205": {"f1-score": 0.9797337103805821, "precision": 0.973083674663546, "recall": 0.9864752639696287, "support": 16858}, "\u23ce": {"f1-score": 0.773936170212766, "precision": 0.9122257053291536, "recall": 0.6720554272517321, "support": 433}, "\u23ce\u23ce": {"f1-score": 0.8880000000000001, "precision": 1.0, "recall": 0.7985611510791367, "support": 139}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 193}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 186}, "\u2423": {"f1-score": 0.9729116794758724, "precision": 0.9653706713339167, "recall": 0.9805714285714285, "support": 7875}},
  "ppcr": 0.9917671273154954
}
```
</details>
