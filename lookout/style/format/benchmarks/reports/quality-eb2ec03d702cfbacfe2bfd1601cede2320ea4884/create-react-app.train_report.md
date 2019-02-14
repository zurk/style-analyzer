# Train report for javascript / file:///tmp/top-repos-quality-repos-qb72sltl/create-react-app HEAD 32106d216e4c31fda30ec475f9f03186d116c893

### Classification report

PPCR: 0.902

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `␣` | 0.968| 1.000| 1.000| 0.984| 0.984| 2390| 2390| 1.000 |
| `'` | 1.000| 1.000| 1.000| 1.000| 1.000| 1464| 1464| 1.000 |
| `⏎` | 0.968| 1.000| 0.986| 0.984| 0.977| 642| 651| 0.986 |
| `⏎␣⁻␣⁻` | 1.000| 0.961| 0.961| 0.980| 0.980| 380| 380| 1.000 |
| `∅` | 0.000| 0.000| 0.000| 0.000| 0.000| 38| 506| 0.075 |
| `⏎␣⁺␣⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 35| 35| 1.000 |
| `⏎⏎` | 0.000| 0.000| 0.000| 0.000| 0.000| 11| 11| 1.000 |
| `"` | 0.000| 0.000| 0.000| 0.000| 0.000| 0| 59| 0.000 |
| `macro avg` | 0.492| 0.495| 0.493| 0.493| 0.493| 4960| 5496| 0.902 |
| `weighted avg` | 0.964| 0.980| 0.884| 0.972| 0.878| 4960| 5496| 0.902 |
| `micro avg` | 0.980| 0.980| 0.884| 0.980| 0.930| 4960| 5496| 0.902 |

### Confusion matrix

|refusal|  ∅| ␣| '| ⏎| ⏎␣⁺␣⁺| ⏎␣⁻␣⁻| ⏎⏎| "| 
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |0 |
|468 |0 |38 |0 |0 |0 |0 |0 |0 |
|0 |0 |2390 |0 |0 |0 |0 |0 |0 |
|0 |0 |0 |1464 |0 |0 |0 |0 |0 |
|9 |0 |0 |0 |642 |0 |0 |0 |0 |
|0 |0 |35 |0 |0 |0 |0 |0 |0 |
|0 |0 |5 |0 |10 |0 |365 |0 |0 |
|0 |0 |0 |0 |11 |0 |0 |0 |0 |
|59 |0 |0 |0 |0 |0 |0 |0 |0 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|
| docusaurus/website/pages/en/index.js | 12 |
| packages/create-react-app/createReactApp.js | 10 |
| packages/react-scripts/config/webpack.config.prod.js | 10 |
| packages/react-scripts/config/webpack.config.dev.js | 9 |
| fixtures/browser/graphql-with-mjs/src/App.js | 6 |
| tasks/cra.js | 6 |
| packages/eslint-config-react-app/index.js | 5 |
| docusaurus/website/siteConfig.js | 4 |
| packages/react-scripts/fixtures/kitchensink/integration/webpack.test.js | 3 |
| fixtures/smoke/relative-paths/index.test.js | 3 |

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\"": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 0}, "\u0027": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 1464}, "macro avg": {"f1-score": 0.4934647284587127, "precision": 0.49209015672096046, "recall": 0.4950657894736842, "support": 4960}, "micro avg": {"f1-score": 0.9800403225806451, "precision": 0.9800403225806451, "recall": 0.9800403225806451, "support": 4960}, "weighted avg": {"f1-score": 0.9717024480686467, "precision": 0.9637359500689249, "recall": 0.9800403225806451, "support": 4960}, "\u2205": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 38}, "\u23ce": {"f1-score": 0.9839080459770114, "precision": 0.9683257918552036, "recall": 1.0, "support": 642}, "\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 11}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 35}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.9798657718120806, "precision": 1.0, "recall": 0.9605263157894737, "support": 380}, "\u2423": {"f1-score": 0.9839440098806093, "precision": 0.9683954619124797, "recall": 1.0, "support": 2390}},
  "cl_report_full": {"\"": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 59}, "\u0027": {"f1-score": 1.0, "precision": 1.0, "recall": 1.0, "support": 1464}, "macro avg": {"f1-score": 0.4926223414330474, "precision": 0.49209015672096046, "recall": 0.4933376788746059, "support": 5496}, "micro avg": {"f1-score": 0.9298010711553175, "precision": 0.9800403225806451, "recall": 0.8844614264919942, "support": 5496}, "weighted avg": {"f1-score": 0.8777496657941442, "precision": 0.8713328319629848, "recall": 0.8844614264919942, "support": 5496}, "\u2205": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 506}, "\u23ce": {"f1-score": 0.9771689497716893, "precision": 0.9683257918552036, "recall": 0.9861751152073732, "support": 651}, "\u23ce\u23ce": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 11}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 35}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.9798657718120806, "precision": 1.0, "recall": 0.9605263157894737, "support": 380}, "\u2423": {"f1-score": 0.9839440098806093, "precision": 0.9683954619124797, "recall": 1.0, "support": 2390}},
  "ppcr": 0.9024745269286754
}
```
</details>
