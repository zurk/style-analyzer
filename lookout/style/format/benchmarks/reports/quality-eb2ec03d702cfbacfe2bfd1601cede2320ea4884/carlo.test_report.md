# Test report for javascript / file:///tmp/top-repos-quality-repos-b15drnka/carlo HEAD b8ce2bca042c757b13fc82a3e059980342ddd9a8

### Classification report

PPCR: 0.866

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.926| 0.971| 0.944| 0.948| 0.935| 1138| 1171| 0.972 |
| `␣` | 0.837| 0.837| 0.760| 0.837| 0.797| 449| 495| 0.907 |
| `'` | 1.000| 0.929| 0.867| 0.963| 0.929| 56| 60| 0.933 |
| `⏎␣⁻␣⁻` | 1.000| 0.941| 0.516| 0.970| 0.681| 34| 62| 0.548 |
| `⏎` | 0.000| 0.000| 0.000| 0.000| 0.000| 21| 91| 0.231 |
| `⏎␣⁺␣⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 18| 70| 0.257 |
| `⏎⏎` | 0.000| 0.000| 0.000| 0.000| 0.000| 10| 43| 0.233 |
| `"` | 0.000| 0.000| 0.000| 0.000| 0.000| 0| 0| 0.000 |
| `micro avg` | 0.907| 0.907| 0.786| 0.907| 0.842| 1726| 1992| 0.866 |
| `macro avg` | 0.470| 0.460| 0.386| 0.465| 0.418| 1726| 1992| 0.866 |
| `weighted avg` | 0.881| 0.907| 0.786| 0.893| 0.797| 1726| 1992| 0.866 |

### Confusion matrix

|refusal|  ∅| ␣| '| ⏎| ⏎␣⁺␣⁺| ⏎␣⁻␣⁻| "| ⏎⏎| 
|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |
|33 |1105 |33 |0 |0 |0 |0 |0 |
|46 |73 |376 |0 |0 |0 |0 |0 |
|4 |2 |2 |52 |0 |0 |0 |0 |
|70 |3 |18 |0 |0 |0 |0 |0 |
|52 |8 |10 |0 |0 |0 |0 |0 |
|28 |2 |0 |0 |0 |0 |32 |0 |
|33 |0 |10 |0 |0 |0 |0 |0 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\"": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 0}, "\u0027": {"f1-score": 0.962962962962963, "precision": 1.0, "recall": 0.9285714285714286, "support": 56}, "macro avg": {"f1-score": 0.4647709202274904, "precision": 0.47045660749322793, "recall": 0.45977076721224386, "support": 1726}, "micro avg": {"f1-score": 0.906720741599073, "precision": 0.906720741599073, "recall": 0.906720741599073, "support": 1726}, "weighted avg": {"f1-score": 0.8932926545904529, "precision": 0.8806819230369507, "recall": 0.906720741599073, "support": 1726}, "\u2205": {"f1-score": 0.9480909480909481, "precision": 0.9262363788767812, "recall": 0.9710017574692443, "support": 1138}, "\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 21}, "\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 10}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 18}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.9696969696969697, "precision": 1.0, "recall": 0.9411764705882353, "support": 34}, "\u2423": {"f1-score": 0.8374164810690423, "precision": 0.8374164810690423, "recall": 0.8374164810690423, "support": 449}},
  "cl_report_full": {"\"": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 0}, "\u0027": {"f1-score": 0.9285714285714286, "precision": 1.0, "recall": 0.8666666666666667, "support": 60}, "macro avg": {"f1-score": 0.4176111047332086, "precision": 0.47045660749322793, "recall": 0.38575369685394206, "support": 1992}, "micro avg": {"f1-score": 0.8418504572350727, "precision": 0.906720741599073, "recall": 0.7856425702811245, "support": 1992}, "weighted avg": {"f1-score": 0.7966695118646263, "precision": 0.81382728804914, "recall": 0.7856425702811245, "support": 1992}, "\u2205": {"f1-score": 0.9348561759729274, "precision": 0.9262363788767812, "recall": 0.9436379163108455, "support": 1171}, "\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 91}, "\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 43}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 70}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.6808510638297872, "precision": 1.0, "recall": 0.5161290322580645, "support": 62}, "\u2423": {"f1-score": 0.7966101694915254, "precision": 0.8374164810690423, "recall": 0.7595959595959596, "support": 495}},
  "ppcr": 0.8664658634538153
}
```
</details>
