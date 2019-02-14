# Train report for javascript / file:///tmp/top-repos-quality-repos-tp_t08ml/evergreen HEAD ba22d511dad83c072842e47801ef42697d142f7c

### Classification report

PPCR: 0.819

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.964| 0.995| 0.917| 0.979| 0.940| 22458| 24367| 0.922 |
| `␣` | 0.976| 0.964| 0.701| 0.970| 0.816| 8598| 11814| 0.728 |
| `'` | 1.000| 1.000| 1.000| 1.000| 1.000| 4888| 4888| 1.000 |
| `⏎` | 0.955| 0.868| 0.442| 0.910| 0.605| 1830| 3591| 0.510 |
| `"` | 1.000| 1.000| 1.000| 1.000| 1.000| 996| 996| 1.000 |
| `⏎␣⁻␣⁻` | 0.973| 0.679| 0.289| 0.800| 0.445| 647| 1520| 0.426 |
| `⏎⏎` | 0.963| 0.987| 0.756| 0.975| 0.847| 632| 825| 0.766 |
| `⏎␣⁺␣⁺` | 0.935| 0.652| 0.269| 0.768| 0.418| 617| 1492| 0.414 |
| `⏎␣⁻␣⁻␣⁻␣⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 79| 95| 0.832 |
| `⏎␣⁺␣⁺␣⁺␣⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 5| 148| 0.034 |
| `micro avg` | 0.971| 0.971| 0.796| 0.971| 0.875| 40750| 49736| 0.819 |
| `macro avg` | 0.777| 0.714| 0.538| 0.740| 0.607| 40750| 49736| 0.819 |
| `weighted avg` | 0.969| 0.971| 0.796| 0.969| 0.856| 40750| 49736| 0.819 |

### Confusion matrix

|refusal|  ∅| ␣| ⏎| '| ⏎␣⁺␣⁺| ⏎␣⁻␣⁻| "| ⏎⏎| ⏎␣⁺␣⁺␣⁺␣⁺| ⏎␣⁻␣⁻␣⁻␣⁻| 
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|1909 |22344 |75 |36 |0 |0 |3 |0 |0 |0 |0 |
|3216 |250 |8285 |26 |0 |26 |7 |0 |4 |0 |0 |
|1761 |205 |15 |1589 |0 |1 |0 |0 |20 |0 |0 |
|0 |0 |0 |0 |4888 |0 |0 |0 |0 |0 |0 |
|875 |157 |58 |0 |0 |402 |0 |0 |0 |0 |0 |
|873 |153 |50 |5 |0 |0 |439 |0 |0 |0 |0 |
|0 |0 |0 |0 |0 |0 |0 |996 |0 |0 |0 |
|193 |0 |0 |8 |0 |0 |0 |0 |624 |0 |0 |
|143 |2 |2 |0 |0 |1 |0 |0 |0 |0 |0 |
|16 |70 |7 |0 |0 |0 |2 |0 |0 |0 |0 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|
| packages/evergreen-buttons/src/styles/ButtonAppearances.js | 50 |
| packages/evergreen-alert/src/components/Alert.js | 30 |
| packages/evergreen-table/docs/index.js | 30 |
| packages/evergreen-typography/stories/index.stories.js | 24 |
| packages/evergreen-positioner/src/components/Positioner.js | 22 |
| packages/evergreen-autocomplete/src/components/Autocomplete.js | 22 |
| packages/evergreen-table/stories/index.stories.js | 21 |
| packages/evergreen-shared-styles/src/styles/CheckboxAppearances.js | 21 |
| packages/evergreen-layers/src/components/Pane.js | 21 |
| packages/evergreen-icons/stories/index.stories.js | 20 |

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\"": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 996}, "\u0027": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 4888}, "macro avg": {"f1-score": 0.7400838663107561, "precision": 0.7765683989798567, "recall": 0.7144223763122091, "support": 40750}, "micro avg": {"f1-score": 0.9709693251533742, "precision": 0.9709693251533742, "recall": 0.9709693251533742, "support": 40750}, "weighted avg": {"f1-score": 0.968890238997212, "precision": 0.9688893357138826, "recall": 0.9709693251533742, "support": 40750}, "\u2205": {"f1-score": 0.9791625583382633, "precision": 0.9638928432768216, "recall": 0.9949238578680203, "support": 22458}, "\u23ce": {"f1-score": 0.909559244419004, "precision": 0.9549278846153846, "recall": 0.8683060109289618, "support": 1830}, "\u23ce\u23ce": {"f1-score": 0.975, "precision": 0.9629629629629629, "recall": 0.9873417721518988, "support": 632}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.7679083094555874, "precision": 0.9348837209302325, "recall": 0.6515397082658023, "support": 617}, "\u23ce\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 5}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.7996357012750456, "precision": 0.9733924611973392, "recall": 0.678516228748068, "support": 647}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 79}, "\u2423": {"f1-score": 0.9695728496196606, "precision": 0.9756241168158266, "recall": 0.9635961851593394, "support": 8598}},
  "cl_report_full": {"\"": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 996}, "\u0027": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 4888}, "macro avg": {"f1-score": 0.6071646524393206, "precision": 0.7765683989798567, "recall": 0.537537603888941, "support": 49736}, "micro avg": {"f1-score": 0.8745441283734501, "precision": 0.9709693251533742, "recall": 0.7955404535949815, "support": 49736}, "weighted avg": {"f1-score": 0.856474591010527, "precision": 0.9649990702697168, "recall": 0.7955404535949815, "support": 49736}, "\u2205": {"f1-score": 0.9398502565828216, "precision": 0.9638928432768216, "recall": 0.9169778799195634, "support": 24367}, "\u23ce": {"f1-score": 0.6047573739295908, "precision": 0.9549278846153846, "recall": 0.442495126705653, "support": 3591}, "\u23ce\u23ce": {"f1-score": 0.8472505091649695, "precision": 0.9629629629629629, "recall": 0.7563636363636363, "support": 825}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.41831425598335065, "precision": 0.9348837209302325, "recall": 0.26943699731903487, "support": 1492}, "\u23ce\u2423\u207a\u2423\u207a\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 148}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.4454591577879249, "precision": 0.9733924611973392, "recall": 0.2888157894736842, "support": 1520}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 95}, "\u2423": {"f1-score": 0.8160149709445484, "precision": 0.9756241168158266, "recall": 0.7012866091078381, "support": 11814}},
  "ppcr": 0.8193260414991154
}
```
</details>
