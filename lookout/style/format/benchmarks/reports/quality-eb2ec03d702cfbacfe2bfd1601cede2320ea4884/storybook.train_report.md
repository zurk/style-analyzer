# Train report for javascript / file:///tmp/top-repos-quality-repos-iqo6lp_m/storybook HEAD b28217f887af533a17cb1498887d6b4bd41bd643

### Classification report

PPCR: 0.854

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.975| 0.994| 0.936| 0.984| 0.955| 88091| 93519| 0.942 |
| `␣` | 0.961| 0.986| 0.862| 0.973| 0.909| 43738| 50042| 0.874 |
| `'` | 1.000| 1.000| 1.000| 1.000| 1.000| 18305| 18305| 1.000 |
| `⏎␣⁻␣⁻` | 0.979| 0.896| 0.784| 0.935| 0.871| 5455| 6233| 0.875 |
| `⏎␣⁺␣⁺` | 0.962| 0.661| 0.480| 0.784| 0.641| 4664| 6420| 0.726 |
| `⏎` | 0.972| 0.331| 0.039| 0.494| 0.076| 1348| 11335| 0.119 |
| `⏎⏎` | 0.968| 0.972| 0.265| 0.970| 0.416| 1344| 4941| 0.272 |
| `"` | 1.000| 0.992| 0.992| 0.996| 0.996| 753| 753| 1.000 |
| `⏎␣⁻␣⁻␣⁻␣⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 76| 130| 0.585 |
| `micro avg` | 0.974| 0.974| 0.832| 0.974| 0.897| 163774| 191678| 0.854 |
| `macro avg` | 0.869| 0.759| 0.595| 0.793| 0.651| 163774| 191678| 0.854 |
| `weighted avg` | 0.973| 0.974| 0.832| 0.971| 0.868| 163774| 191678| 0.854 |

### Confusion matrix

|refusal|  ∅| ␣| '| ⏎| ⏎␣⁺␣⁺| ⏎␣⁻␣⁻| ⏎⏎| "| ⏎␣⁻␣⁻␣⁻␣⁻| 
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|5428 |87568 |431 |0 |0 |47 |45 |0 |0 |0 |
|6304 |520 |43130 |0 |12 |74 |0 |2 |0 |0 |
|0 |0 |0 |18305 |0 |0 |0 |0 |0 |0 |
|9987 |557 |305 |0 |446 |0 |0 |40 |0 |0 |
|1756 |763 |819 |0 |0 |3082 |0 |0 |0 |0 |
|778 |391 |178 |0 |1 |0 |4885 |0 |0 |0 |
|3597 |29 |8 |0 |0 |0 |0 |1307 |0 |0 |
|0 |0 |0 |6 |0 |0 |0 |0 |747 |0 |
|54 |11 |5 |0 |0 |0 |59 |1 |0 |0 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|
| examples/official-storybook/stories/addon-info.stories.js | 148 |
| lib/cli/lib/detect.js | 83 |
| lib/ui/src/modules/ui/components/stories_panel/stories_tree/index.test.js | 75 |
| addons/jest/src/components/Result.js | 61 |
| lib/cli/lib/initiate.js | 60 |
| examples/official-storybook/stories/addon-knobs.stories.js | 51 |
| lib/components/src/tabs/tabs.stories.js | 51 |
| addons/info/src/components/PropVal.js | 49 |
| examples/official-storybook/stories/addon-actions.stories.js | 44 |
| addons/info/src/components/Story.js | 42 |

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\"": {"f1-score": 0.996, "precision": 1.0, "recall": 0.9920318725099602, "support": 753}, "\u0027": {"f1-score": 0.999836137207778, "precision": 0.999672328108787, "recall": 1.0, "support": 18305}, "macro avg": {"f1-score": 0.7929444869912986, "precision": 0.8685210362725813, "recall": 0.7590932810252564, "support": 163774}, "micro avg": {"f1-score": 0.9737198822767961, "precision": 0.9737198822767961, "recall": 0.9737198822767961, "support": 163774}, "weighted avg": {"f1-score": 0.971232720163301, "precision": 0.9732471042733751, "recall": 0.9737198822767961, "support": 163774}, "\u2205": {"f1-score": 0.9842971955263305, "precision": 0.9747214461425439, "recall": 0.9940629576233667, "support": 88091}, "\u23ce": {"f1-score": 0.4936358605423353, "precision": 0.971677559912854, "recall": 0.33086053412462907, "support": 1348}, "\u23ce\u23ce": {"f1-score": 0.9703043801039347, "precision": 0.9681481481481482, "recall": 0.9724702380952381, "support": 1344}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.7835261217745011, "precision": 0.9622229160162348, "recall": 0.6608061749571184, "support": 4664}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.9354653389505937, "precision": 0.9791541391060333, "recall": 0.8955087076076994, "support": 5455}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 76}, "\u2423": {"f1-score": 0.9734353488162142, "precision": 0.9610927890186292, "recall": 0.9860990443092963, "support": 43738}},
  "cl_report_full": {"\"": {"f1-score": 0.996, "precision": 1.0, "recall": 0.9920318725099602, "support": 753}, "\u0027": {"f1-score": 0.999836137207778, "precision": 0.999672328108787, "recall": 1.0, "support": 18305}, "macro avg": {"f1-score": 0.6513428011764228, "precision": 0.8685210362725813, "recall": 0.5953262590295044, "support": 191678}, "micro avg": {"f1-score": 0.8972800828241224, "precision": 0.9737198822767961, "recall": 0.8319681966631538, "support": 191678}, "weighted avg": {"f1-score": 0.8676220245517654, "precision": 0.9723604495424122, "recall": 0.8319681966631538, "support": 191678}, "\u2205": {"f1-score": 0.9551587604576839, "precision": 0.9747214461425439, "recall": 0.9363658721757077, "support": 93519}, "\u23ce": {"f1-score": 0.07563167712396132, "precision": 0.971677559912854, "recall": 0.03934715483017203, "support": 11335}, "\u23ce\u23ce": {"f1-score": 0.4155142266730249, "precision": 0.9681481481481482, "recall": 0.26452135195304594, "support": 4941}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.6405486854411306, "precision": 0.9622229160162348, "recall": 0.4800623052959502, "support": 6420}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.8706112992336482, "precision": 0.9791541391060333, "recall": 0.7837317503609819, "support": 6233}, "\u23ce\u2423\u207b\u2423\u207b\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 130}, "\u2423": {"f1-score": 0.9087844244505785, "precision": 0.9610927890186292, "recall": 0.8618760241397226, "support": 50042}},
  "ppcr": 0.8544225211031
}
```
</details>
