# Model report for file:///tmp/top-repos-quality-repos-w_xek5jl/telescope HEAD 534030114f47696fe3f3b08ea7ca49467428f2af

### Dump

```json
{'created_at': datetime.datetime(2019, 2, 12, 21, 24, 54, 771066),
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
 'uuid': '3dccd2e7-52aa-4b2d-ad4d-f9cfdf53563a',
 'version': [1]}
style.format.analyzer.FormatAnalyzer/[1] file:///tmp/top-repos-quality-repos-w_xek5jl/telescope 534030114f47696fe3f3b08ea7ca49467428f2af

# javascript
3 rules, avg.len. 2.7
## train
PPCR: 0.566543
### report
macro
{'f1-score': 0.47750424448217316,
 'precision': 0.45872274143302183,
 'recall': 0.5,
 'support': 613}
micro
{'f1-score': 0.9135399673735726,
 'precision': 0.9135399673735726,
 'recall': 0.9135399673735726,
 'support': 613}
weighted
{'f1-score': 0.8741999185724137,
 'precision': 0.8413552672368668,
 'recall': 0.9135399673735726,
 'support': 613}
### report_full
macro
{'f1-score': 0.43368527763432224,
 'precision': 0.45872274143302183,
 'recall': 0.4114648033126294,
 'support': 1082}
micro
{'f1-score': 0.6607669616519174,
 'precision': 0.9135399673735726,
 'recall': 0.5175600739371534,
 'support': 1082}
weighted
{'f1-score': 0.5453939522955382,
 'precision': 0.5767443467445195,
 'recall': 0.5175600739371534,
 'support': 1082}
## test
PPCR: 0.552716
### report
macro
{'f1-score': 0.4724264705882353,
 'precision': 0.45033112582781454,
 'recall': 0.5,
 'support': 173}
micro
{'f1-score': 0.8265895953757225,
 'precision': 0.8265895953757225,
 'recall': 0.8265895953757225,
 'support': 173}
weighted
{'f1-score': 0.7494474668480109,
 'precision': 0.687631589021169,
 'recall': 0.8265895953757225,
 'support': 173}
### report_full
macro
{'f1-score': 0.4050387596899225,
 'precision': 0.45033112582781454,
 'recall': 0.36827421283379835,
 'support': 313}
micro
{'f1-score': 0.588477366255144,
 'precision': 0.8265895953757225,
 'recall': 0.45686900958466453,
 'support': 313}
weighted
{'f1-score': 0.5099252049434084,
 'precision': 0.5771745339906481,
 'recall': 0.45686900958466453,
 'support': 313}
```

## javascript
### Summary
3 rules, avg.len. 2.7

| | |
|-|-|
|Min support|104|
|Max support|267|
|Min confidence|0.8183520436286926|
|Max confidence|0.9961240291595459|

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
                     'max_depth': 5,
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
| 1 | `  -1.internal_type = StringLiteral<br>⇒ y = '<br>Confidence: 0.996. Support: 129.` |
| 2 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label in {<space>}<br>	∧ +1.roles in {LITERAL}<br>⇒ y = '<br>Confidence: 0.995. Support: 104.` |
| 3 | `  -1.internal_type not in {StringLiteral}<br>	∧ -2.label not in {'}<br>	∧ +1.roles not in {LITERAL}<br>	∧ +1.length ≤ 1<br>⇒ y = ∅<br>Confidence: 0.818. Support: 267.` |

<details>
    <summary>Machine-readable report</summary>
```json
{"javascript": {"avg_rule_len": 2.6666666666666665, "max_conf": 0.9961240291595459, "max_support": 267, "min_conf": 0.8183520436286926, "min_support": 104, "num_rules": 3}}
```
</details>
