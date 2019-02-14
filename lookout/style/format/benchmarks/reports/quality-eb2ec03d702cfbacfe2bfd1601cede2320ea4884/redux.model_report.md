# Model report for file:///tmp/top-repos-quality-repos-pfwm2g26/redux HEAD 902484ed735d38aec06683c847810a7218d8dba2

### Dump

```json
{'created_at': datetime.datetime(2019, 2, 13, 7, 26, 27, 624406),
 'dependencies': [],
 'environment': {'packages': [['ConfigArgParse', '0.13.0'],
                              ['Jinja2', '2.10'],
                              ['MarkupSafe', '1.1.0'],
                              ['PyYAML', '3.13'],
                              ['Pympler', '0.5'],
                              ['SQLAlchemy', '1.2.10'],
                              ['SQLAlchemy-Utils', '0.33.3'],
                              ['asdf', '2.3.1'],
                              ['bblfsh', '2.12.7'],
                              ['cachetools', '2.0.1'],
                              ['certifi', '2018.11.29'],
                              ['chardet', '3.0.4'],
                              ['clint', '0.5.1'],
                              ['dulwich', '0.19.10'],
                              ['grpcio', '1.18.0'],
                              ['grpcio-tools', '1.18.0'],
                              ['humanfriendly', '4.16.1'],
                              ['humanize', '0.5.1'],
                              ['idna', '2.8'],
                              ['jsonschema', '2.6.0'],
                              ['lookout-sdk', '0.4.1'],
                              ['lookout-sdk-ml', '0.9.0'],
                              ['lz4', '2.1.6'],
                              ['modelforge', '0.9.3'],
                              ['numpy', '1.16.0'],
                              ['pip', '19.0.1'],
                              ['protobuf', '3.6.1'],
                              ['psycopg2-binary', '2.7.5'],
                              ['pygtrie', '2.3'],
                              ['python-dateutil', '2.7.5'],
                              ['python-igraph', '0.7.1.post6'],
                              ['requests', '2.21.0'],
                              ['requirements-parser', '0.2.0'],
                              ['scikit-learn', '0.20.1'],
                              ['scikit-optimize', '0.5.2'],
                              ['scipy', '1.2.0'],
                              ['semantic-version', '2.6.0'],
                              ['setuptools', '40.7.1'],
                              ['six', '1.12.0'],
                              ['stringcase', '1.2.0'],
                              ['tabulate', '0.8.2'],
                              ['tqdm', '4.31.1'],
                              ['urllib3', '1.24.1'],
                              ['xxhash', '1.3.0']],
                 'platform': 'Linux-4.15.15-coreos-x86_64-with-Ubuntu-18.04-bionic',
                 'python': '3.6.7 (default, Oct 22 2018, 11:32:17) \n'
                           '[GCC 8.2.0]'},
 'model': 'code-format',
 'uuid': '55e54244-f215-472e-bbd2-2e7ab1431e93',
 'version': [1]}
style.format.analyzer.FormatAnalyzer/[1] file:///tmp/top-repos-quality-repos-pfwm2g26/redux 902484ed735d38aec06683c847810a7218d8dba2

# javascript
32 rules, avg.len. 7.6
## train
PPCR: 0.866531
### report
macro
{'f1-score': 0.7824561452997806,
 'precision': 0.7921545546169372,
 'recall': 0.7740894605459306,
 'support': 27703}
micro
{'f1-score': 0.9409450240046204,
 'precision': 0.9409450240046204,
 'recall': 0.9409450240046204,
 'support': 27703}
weighted
{'f1-score': 0.938825777552121,
 'precision': 0.9371996084759944,
 'recall': 0.9409450240046204,
 'support': 27703}
### report_full
macro
{'f1-score': 0.6861081863992443,
 'precision': 0.7921545546169372,
 'recall': 0.6195638417943949,
 'support': 31970}
micro
{'f1-score': 0.8736614549293651,
 'precision': 0.9409450240046204,
 'recall': 0.8153581482639976,
 'support': 31970}
weighted
{'f1-score': 0.8667119192105429,
 'precision': 0.935868620418472,
 'recall': 0.8153581482639976,
 'support': 31970}
## test
PPCR: 0.884812
### report
macro
{'f1-score': 0.7726190408899389,
 'precision': 0.7831186061096012,
 'recall': 0.7632191326967451,
 'support': 8127}
micro
{'f1-score': 0.9451212009351544,
 'precision': 0.9451212009351544,
 'recall': 0.9451212009351544,
 'support': 8127}
weighted
{'f1-score': 0.9441836611197779,
 'precision': 0.9435796910794239,
 'recall': 0.9451212009351544,
 'support': 8127}
### report_full
macro
{'f1-score': 0.6711917591816221,
 'precision': 0.7831186061096012,
 'recall': 0.6071821767089823,
 'support': 9185}
micro
{'f1-score': 0.8873613678373382,
 'precision': 0.9451212009351544,
 'recall': 0.836254763200871,
 'support': 9185}
weighted
{'f1-score': 0.8787361985149855,
 'precision': 0.9384575754429347,
 'recall': 0.836254763200871,
 'support': 9185}
```

## javascript
### Summary
32 rules, avg.len. 7.6

| | |
|-|-|
|Min support|91|
|Max support|3720|
|Min confidence|0.834967315196991|
|Max confidence|0.9995437860488892|

### Configuration

```json
{'feature_extractor': {'cutoff_label_support': 80,
                       'debug_parsing': False,
                       'label_composites': '<cut>',
                       'left_features': ['length',
                                         'diff_offset',
                                         'diff_col',
                                         'diff_line',
                                         'internal_type',
                                         'label',
                                         'reserved',
                                         'roles'],
                       'left_siblings_window': 5,
                       'no_labels_on_right': True,
                       'node_features': ['start_line', 'start_col'],
                       'parent_features': ['internal_type', 'roles'],
                       'parents_depth': 2,
                       'return_sibling_indices': False,
                       'right_features': ['length', 'internal_type', 'reserved', 'roles'],
                       'right_siblings_window': 5,
                       'select_features_number': 500,
                       'selected_features': '<cut>'},
 'line_length_limit': 500,
 'lines_ratio_train_trigger': 0.2,
 'lower_bound_instances': 500,
 'optimizer': {'base_model_name_categories': ['sklearn.ensemble.RandomForestClassifier',
                                              'sklearn.tree.DecisionTreeClassifier'],
               'cv': 3,
               'max_depth_categories': [None, 5, 10],
               'max_features_categories': [None, 'auto'],
               'min_samples_leaf_max': 120,
               'min_samples_leaf_min': 90,
               'min_samples_split_max': 240,
               'min_samples_split_min': 180,
               'n_iter': 50,
               'n_jobs': -1},
 'overall_size_limit': 5242880,
 'random_state': 42,
 'test_dataset_ratio': 0.2,
 'trainable_rules': {'attribute_similarity_threshold': 0.98,
                     'base_model_name': 'sklearn.tree.DecisionTreeClassifier',
                     'confidence_threshold': 0.8,
                     'min_samples_leaf': 90,
                     'min_samples_split': 180,
                     'n_estimators': 10,
                     'prune_attributes': True,
                     'prune_branches_algorithms': ['reduced-error'],
                     'prune_dataset_ratio': 0.2,
                     'top_down_greedy_budget': [False, 0.5]}}
```

### Rules

| rule number | description |
|----:|:-----|
| 1 | `  ^1.roles in {IDENTIFIER}<br>⇒ y = ∅<br>Confidence: 0.972. Support: 3283.` |
| 2 | `  -1.internal_type = StringLiteral<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = '<br>Confidence: 0.960. Support: 1016.` |
| 3 | `  •••start_col ≤ 34<br>	∧ -1.diff_col ≤ 17<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.length ≥ 3<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.952. Support: 1800.` |
| 4 | `  •••start_col ≤ 34<br>	∧ -1.diff_col ≤ 3<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.length ≥ 3<br>	∧ -3.length ≥ 3<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.912. Support: 97.` |
| 5 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = :<br>	∧ -1.length ≤ 2<br>	∧ +1.internal_type = StringLiteral<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.997. Support: 166.` |
| 6 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {:}<br>	∧ -1.length ≤ 2<br>	∧ +1.internal_type = StringLiteral<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = '<br>Confidence: 0.873. Support: 1044.` |
| 7 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ -1.length ≤ 2<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ∅<br>Confidence: 0.935. Support: 828.` |
| 8 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ -1.length ≤ 2<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles in {UNANNOTATED} and not in {IDENTIFIER}<br>⇒ y = ∅<br>Confidence: 0.931. Support: 138.` |
| 9 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ -1.length ≤ 2<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ +2.reserved = }<br>	∧ ^1.roles not in {IDENTIFIER, UNANNOTATED}<br>⇒ y = ␣<br>Confidence: 0.932. Support: 168.` |
| 10 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ -1.length ≤ 2<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ +2.reserved not in {,, }}<br>	∧ ^1.roles not in {IDENTIFIER, UNANNOTATED}<br>⇒ y = ⏎␣⁺␣⁺<br>Confidence: 0.863. Support: 845.` |
| 11 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(, {}<br>	∧ -1.length ≤ 2<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type = JSXElement<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ∅<br>Confidence: 0.999. Support: 361.` |
| 12 | `  •••start_col ≥ 9<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(, {}<br>	∧ -1.length ≤ 2<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {JSXElement}<br>	∧ ^1.roles in {DECLARATION} and not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.929. Support: 651.` |
| 13 | `  •••start_col ≥ 9<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(, {}<br>	∧ -1.length ≤ 2<br>	∧ -2.roles in {KEY}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {JSXElement}<br>	∧ ^1.roles not in {DECLARATION, IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.999. Support: 355.` |
| 14 | `  •••start_col ≥ 9<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(, :, {}<br>	∧ -1.length ≤ 2<br>	∧ -2.label not in {<space>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type = ObjectExpression<br>	∧ ^1.roles not in {DECLARATION, IDENTIFIER}<br>⇒ y = ⏎<br>Confidence: 0.880. Support: 454.` |
| 15 | `  •••start_col ≥ 9<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(, ,, :, {}<br>	∧ -1.length ≤ 2<br>	∧ -2.label not in {<space>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = import<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {JSXElement, ObjectExpression}<br>	∧ ^1.roles not in {DECLARATION, EXPRESSION, IDENTIFIER}<br>⇒ y = ⏎<br>Confidence: 0.929. Support: 246.` |
| 16 | `  •••start_col ≥ 9<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(, ,, :, {}<br>	∧ -1.length ≤ 2<br>	∧ -2.label not in {<space>}<br>	∧ -2.roles in {IMPORT}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {import}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {JSXElement, ObjectExpression}<br>	∧ ^1.roles not in {DECLARATION, EXPRESSION, IDENTIFIER}<br>⇒ y = ⏎⏎<br>Confidence: 0.995. Support: 91.` |
| 17 | `  •••start_col ≤ 8<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(, {}<br>	∧ -1.length ≤ 2<br>	∧ -2.diff_offset ≤ 2<br>	∧ -3.diff_col ≥ 1<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {JSXElement}<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ⏎⏎<br>Confidence: 0.835. Support: 306.` |
| 18 | `  •••start_col ≤ 8<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(, {}<br>	∧ -1.length ≤ 2<br>	∧ -3.diff_col = 0<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {JSXElement}<br>⇒ y = ∅<br>Confidence: 0.997. Support: 172.` |
| 19 | `  -1.internal_type = JSXIdentifier<br>	∧ +1.reserved = =<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ∅<br>Confidence: 0.997. Support: 152.` |
| 20 | `  -1.internal_type not in {JSXIdentifier, StringLiteral}<br>	∧ +1.reserved = =<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 1.000. Support: 1096.` |
| 21 | `  -1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles in {DECLARATION} and not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.942. Support: 250.` |
| 22 | `  -1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles in {UNANNOTATED} and not in {DECLARATION, IDENTIFIER}<br>⇒ y = ∅<br>Confidence: 0.886. Support: 127.` |
| 23 | `  -1.internal_type not in {StringLiteral}<br>	∧ -5.label not in {<space>}<br>	∧ +1.reserved = }<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {DECLARATION, IDENTIFIER, UNANNOTATED}<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.853. Support: 751.` |
| 24 | `  -1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = {<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles in {UNANNOTATED} and not in {IDENTIFIER}<br>⇒ y = ∅<br>Confidence: 0.920. Support: 181.` |
| 25 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ +1.reserved = {<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER, UNANNOTATED}<br>⇒ y = ∅<br>Confidence: 0.997. Support: 146.` |
| 26 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(}<br>	∧ +1.reserved = {<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER, UNANNOTATED}<br>⇒ y = ␣<br>Confidence: 0.923. Support: 1016.` |
| 27 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.roles in {EXPRESSION}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ∅<br>Confidence: 0.959. Support: 3720.` |
| 28 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ +1.reserved = (<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.846. Support: 596.` |
| 29 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ +1.reserved not in {(, =, {, }}<br>	∧ +1.roles in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ∅<br>Confidence: 0.849. Support: 96.` |
| 30 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ +1.reserved not in {(, =, {, }}<br>	∧ +1.roles in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.843. Support: 359.` |
| 31 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -2.roles not in {LITERAL}<br>	∧ +1.reserved = ><br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ +2.length ≥ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ∅<br>Confidence: 0.995. Support: 680.` |
| 32 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -2.roles not in {LITERAL}<br>	∧ +1.reserved = )<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>⇒ y = ∅<br>Confidence: 0.950. Support: 910.` |

<details>
    <summary>Machine-readable report</summary>
```json
{"javascript": {"avg_rule_len": 7.59375, "max_conf": 0.9995437860488892, "max_support": 3720, "min_conf": 0.834967315196991, "min_support": 91, "num_rules": 32}}
```
</details>
