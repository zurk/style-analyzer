# Model report for file:///tmp/top-repos-quality-repos-eof7hnjl/citgm HEAD 0c4c7ccdd1cad8ce9506e34ca523787ba18cafe2

### Dump

```json
{'created_at': datetime.datetime(2019, 2, 13, 7, 29, 30, 366810),
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
 'uuid': 'ff173857-66e9-407f-a7a3-3b32ff1b9700',
 'version': [1]}
style.format.analyzer.FormatAnalyzer/[1] file:///tmp/top-repos-quality-repos-eof7hnjl/citgm 0c4c7ccdd1cad8ce9506e34ca523787ba18cafe2

# javascript
18 rules, avg.len. 5.8
## train
PPCR: 0.919154
### report
macro
{'f1-score': 0.9090542856009318,
 'precision': 0.9299536071465208,
 'recall': 0.8952925774198351,
 'support': 18998}
micro
{'f1-score': 0.9581534898410359,
 'precision': 0.9581534898410359,
 'recall': 0.9581534898410359,
 'support': 18998}
weighted
{'f1-score': 0.9572264500725183,
 'precision': 0.9575296556121758,
 'recall': 0.9581534898410359,
 'support': 18998}
### report_full
macro
{'f1-score': 0.7695671529533156,
 'precision': 0.9299536071465208,
 'recall': 0.711912135673454,
 'support': 20669}
micro
{'f1-score': 0.9177906068016235,
 'precision': 0.9581534898410359,
 'recall': 0.8806908897382554,
 'support': 20669}
weighted
{'f1-score': 0.9003941416786094,
 'precision': 0.951997447907228,
 'recall': 0.8806908897382554,
 'support': 20669}
## test
PPCR: 0.935879
### report
macro
{'f1-score': 0.9177003158481648,
 'precision': 0.9326147063043205,
 'recall': 0.9115932804823628,
 'support': 4656}
micro
{'f1-score': 0.9583333333333334,
 'precision': 0.9583333333333334,
 'recall': 0.9583333333333334,
 'support': 4656}
weighted
{'f1-score': 0.957485338918992,
 'precision': 0.9594623415297354,
 'recall': 0.9583333333333334,
 'support': 4656}
### report_full
macro
{'f1-score': 0.8012442276984103,
 'precision': 0.9326147063043205,
 'recall': 0.7417638925366431,
 'support': 4975}
micro
{'f1-score': 0.9265912158654345,
 'precision': 0.9583333333333334,
 'recall': 0.8968844221105527,
 'support': 4975}
weighted
{'f1-score': 0.9145276639705315,
 'precision': 0.957509274595832,
 'recall': 0.8968844221105527,
 'support': 4975}
```

## javascript
### Summary
18 rules, avg.len. 5.8

| | |
|-|-|
|Min support|100|
|Max support|7700|
|Min confidence|0.8125|
|Max confidence|0.9995429515838623|

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
                     'min_samples_split': 237,
                     'n_estimators': 10,
                     'prune_attributes': True,
                     'prune_branches_algorithms': ['reduced-error'],
                     'prune_dataset_ratio': 0.2,
                     'top_down_greedy_budget': [False, 0.5]}}
```

### Rules

| rule number | description |
|----:|:-----|
| 1 | `  -1.internal_type = StringLiteral<br>⇒ y = '<br>Confidence: 1.000. Support: 1094.` |
| 2 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ +1.internal_type = StringLiteral<br>⇒ y = ␣<br>Confidence: 0.905. Support: 300.` |
| 3 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,}<br>	∧ -2.label not in {<space>}<br>	∧ +1.internal_type = StringLiteral<br>⇒ y = '<br>Confidence: 0.918. Support: 1115.` |
| 4 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.998. Support: 329.` |
| 5 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +5.reserved = function<br>⇒ y = ⏎⏎<br>Confidence: 0.874. Support: 115.` |
| 6 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {;}<br>	∧ -3.length ≥ 2<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles in {VARIABLE}<br>⇒ y = ␣<br>Confidence: 0.997. Support: 778.` |
| 7 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles in {LITERAL} and not in {VARIABLE}<br>⇒ y = ⏎<br>Confidence: 0.841. Support: 186.` |
| 8 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles not in {LITERAL, VARIABLE}<br>⇒ y = ␣<br>Confidence: 0.963. Support: 613.` |
| 9 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, ;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles in {OPERATOR} and not in {VARIABLE}<br>⇒ y = ␣<br>Confidence: 0.909. Support: 630.` |
| 10 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles not in {OPERATOR, VARIABLE}<br>⇒ y = ⏎␣⁺␣⁺<br>Confidence: 0.962. Support: 433.` |
| 11 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, ;, {}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = {<br>	∧ ^1.roles not in {OPERATOR, VARIABLE}<br>⇒ y = ␣<br>Confidence: 0.956. Support: 422.` |
| 12 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = const<br>	∧ +1.internal_type not in {StringLiteral}<br>⇒ y = ␣<br>Confidence: 0.999. Support: 354.` |
| 13 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = function<br>	∧ +1.internal_type not in {StringLiteral}<br>⇒ y = ␣<br>Confidence: 0.812. Support: 280.` |
| 14 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = :<br>	∧ +1.internal_type not in {StringLiteral}<br>⇒ y = ␣<br>Confidence: 0.981. Support: 183.` |
| 15 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, const, function}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ ^1.roles not in {OPERATOR, VARIABLE}<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.843. Support: 169.` |
| 16 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = if<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>⇒ y = ␣<br>Confidence: 0.995. Support: 100.` |
| 17 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, const, function, if, {}<br>	∧ -2.label in {<-space>}<br>	∧ -4.diff_col ≥ 1<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {{, }}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {OPERATOR, VARIABLE}<br>⇒ y = ∅<br>Confidence: 0.975. Support: 417.` |
| 18 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, const, function, if, {}<br>	∧ -2.label not in {<-space>}<br>	∧ -4.diff_col ≥ 1<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {{, }}<br>	∧ ^1.roles not in {OPERATOR, VARIABLE}<br>⇒ y = ∅<br>Confidence: 0.965. Support: 7700.` |

<details>
    <summary>Machine-readable report</summary>
```json
{"javascript": {"avg_rule_len": 5.833333333333333, "max_conf": 0.9995429515838623, "max_support": 7700, "min_conf": 0.8125, "min_support": 100, "num_rules": 18}}
```
</details>
