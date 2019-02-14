# Model report for file:///tmp/top-repos-quality-repos-68x3i7pl/axios HEAD 21ae22dbd3ae3d3a55d9efd4eead3dd7fb6d8e6e

### Dump

```json
{'created_at': datetime.datetime(2019, 2, 12, 21, 48, 19, 124220),
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
 'uuid': 'dc1c48bc-b84d-404e-84de-e3e5144f92f3',
 'version': [1]}
style.format.analyzer.FormatAnalyzer/[1] file:///tmp/top-repos-quality-repos-68x3i7pl/axios 21ae22dbd3ae3d3a55d9efd4eead3dd7fb6d8e6e

# javascript
18 rules, avg.len. 6.7
## train
PPCR: 0.875035
### report
macro
{'f1-score': 0.8137352096931474,
 'precision': 0.8219688912959071,
 'recall': 0.8068928105986117,
 'support': 21735}
micro
{'f1-score': 0.9657234874626179,
 'precision': 0.9657234874626179,
 'recall': 0.9657234874626179,
 'support': 21735}
weighted
{'f1-score': 0.9640737087732655,
 'precision': 0.9627334445673768,
 'recall': 0.9657234874626179,
 'support': 21735}
### report_full
macro
{'f1-score': 0.6551969490532417,
 'precision': 0.8219688912959071,
 'recall': 0.598655703771243,
 'support': 24839}
micro
{'f1-score': 0.9013612745308542,
 'precision': 0.9657234874626179,
 'recall': 0.8450420709368333,
 'support': 24839}
weighted
{'f1-score': 0.8833770234384309,
 'precision': 0.9570861464210941,
 'recall': 0.8450420709368333,
 'support': 24839}
## test
PPCR: 0.884716
### report
macro
{'f1-score': 0.8106457951151123,
 'precision': 0.8621534167608198,
 'recall': 0.7845405590395175,
 'support': 5065}
micro
{'f1-score': 0.9707798617966437,
 'precision': 0.9707798617966437,
 'recall': 0.9707798617966437,
 'support': 5065}
weighted
{'f1-score': 0.9699022124967746,
 'precision': 0.971113544516339,
 'recall': 0.9707798617966437,
 'support': 5065}
### report_full
macro
{'f1-score': 0.658684311702217,
 'precision': 0.8621534167608198,
 'recall': 0.6001679485449457,
 'support': 5725}
micro
{'f1-score': 0.9113994439295644,
 'precision': 0.9707798617966437,
 'recall': 0.8588646288209607,
 'support': 5725}
weighted
{'f1-score': 0.8923777175086901,
 'precision': 0.9722505133114787,
 'recall': 0.8588646288209607,
 'support': 5725}
```

## javascript
### Summary
18 rules, avg.len. 6.7

| | |
|-|-|
|Min support|121|
|Max support|7994|
|Min confidence|0.807692289352417|
|Max confidence|0.9983870983123779|

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
                     'min_samples_leaf': 120,
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
| 1 | `  -1.roles in {STRING}<br>⇒ y = '<br>Confidence: 0.966. Support: 1060.` |
| 2 | `  -1.reserved not in {,}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.label not in {<space>}<br>	∧ -2.reserved = :<br>	∧ +1.roles in {MAP, STRING}<br>⇒ y = '<br>Confidence: 0.888. Support: 121.` |
| 3 | `  -1.reserved not in {,}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.label not in {<space>}<br>	∧ +1.roles in {STRING} and not in {MAP}<br>⇒ y = '<br>Confidence: 0.972. Support: 924.` |
| 4 | `  -1.reserved = ;<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved = }<br>	∧ +1.roles not in {STRING}<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.988. Support: 561.` |
| 5 | `  -1.reserved = ;<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {STRING}<br>	∧ +3.internal_type = StringLiteral<br>⇒ y = ⏎⏎<br>Confidence: 0.973. Support: 165.` |
| 6 | `  -1.reserved = {<br>	∧ -1.roles not in {STRING}<br>	∧ +1.roles not in {STRING}<br>⇒ y = ⏎␣⁺␣⁺<br>Confidence: 0.897. Support: 794.` |
| 7 | `  -1.reserved not in {;, {}<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved = {<br>	∧ +1.roles not in {STRING}<br>⇒ y = ␣<br>Confidence: 0.943. Support: 844.` |
| 8 | `  -1.reserved not in {;, {}<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved not in {{}<br>	∧ +1.roles not in {STRING}<br>	∧ +2.roles in {EXPRESSION}<br>	∧ ^1.roles in {OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.983. Support: 436.` |
| 9 | `  -1.reserved not in {;, {}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.label in {<space>}<br>	∧ +1.reserved not in {{}<br>	∧ +1.roles not in {STRING}<br>	∧ +2.roles not in {EXPRESSION}<br>	∧ ^1.roles in {OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.909. Support: 302.` |
| 10 | `  -1.reserved = ,<br>	∧ -1.roles not in {STRING}<br>	∧ +1.roles not in {STRING}<br>	∧ ^1.internal_type = ObjectExpression<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ⏎<br>Confidence: 0.808. Support: 143.` |
| 11 | `  -1.reserved = ,<br>	∧ -1.roles not in {STRING}<br>	∧ +1.roles not in {STRING}<br>	∧ ^1.internal_type not in {ObjectExpression}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.964. Support: 486.` |
| 12 | `  -1.reserved not in {,, ;, {}<br>	∧ -1.roles not in {STRING}<br>	∧ +1.roles not in {STRING}<br>	∧ ^1.internal_type = VariableDeclarator<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.977. Support: 509.` |
| 13 | `  -1.reserved = function<br>	∧ -1.roles not in {STRING}<br>	∧ +1.roles not in {STRING}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.897. Support: 459.` |
| 14 | `  -1.reserved = var<br>	∧ -1.roles not in {STRING}<br>	∧ +1.roles not in {STRING}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.998. Support: 310.` |
| 15 | `  -1.reserved = :<br>	∧ -1.roles not in {STRING}<br>	∧ +1.roles not in {STRING}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.984. Support: 225.` |
| 16 | `  -1.reserved not in {,, :, ;, function, var, {}<br>	∧ -1.roles not in {COMMENT, STRING}<br>	∧ -3.diff_line ≥ 1<br>	∧ +1.reserved not in {{, }}<br>	∧ +1.roles in {COMMENT} and not in {STRING}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {VariableDeclarator}<br>	∧ ^1.roles not in {IF, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.996. Support: 141.` |
| 17 | `  -1.reserved not in {,, :, ;, function, var, {}<br>	∧ -1.roles not in {COMMENT, STRING}<br>	∧ -3.diff_line ≥ 1<br>	∧ +1.reserved not in {{, }}<br>	∧ +1.roles not in {STRING}<br>	∧ +1.length ≤ 1<br>	∧ ^1.internal_type not in {VariableDeclarator}<br>	∧ ^1.roles not in {IF, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.947. Support: 1907.` |
| 18 | `  -1.reserved not in {,, :, ;, function, var, {}<br>	∧ -1.roles not in {COMMENT, STRING}<br>	∧ -3.diff_line = 0<br>	∧ +1.reserved not in {{, }}<br>	∧ +1.roles not in {STRING}<br>	∧ ^1.internal_type not in {VariableDeclarator}<br>	∧ ^1.roles not in {IF, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.980. Support: 7994.` |

<details>
    <summary>Machine-readable report</summary>
```json
{"javascript": {"avg_rule_len": 6.722222222222222, "max_conf": 0.9983870983123779, "max_support": 7994, "min_conf": 0.807692289352417, "min_support": 121, "num_rules": 18}}
```
</details>
