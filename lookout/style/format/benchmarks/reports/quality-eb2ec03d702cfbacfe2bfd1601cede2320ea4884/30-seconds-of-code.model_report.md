# Model report for file:///tmp/top-repos-quality-repos-tnww86x5/30-seconds-of-code HEAD 3a122c9cfcbdc091227879a06a32bc67ccd0d35d

### Dump

```json
{'created_at': datetime.datetime(2019, 2, 13, 7, 39, 18, 678663),
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
 'uuid': 'd180c4e1-693e-4a37-a0ab-0e9c4339c621',
 'version': [1]}
style.format.analyzer.FormatAnalyzer/[1] file:///tmp/top-repos-quality-repos-tnww86x5/30-seconds-of-code 3a122c9cfcbdc091227879a06a32bc67ccd0d35d

# javascript
19 rules, avg.len. 6.1
## train
PPCR: 0.980390
### report
macro
{'f1-score': 0.9241638811089905,
 'precision': 0.9656978814914231,
 'recall': 0.8897503466817707,
 'support': 43595}
micro
{'f1-score': 0.9684367473334098,
 'precision': 0.9684367473334098,
 'recall': 0.9684367473334098,
 'support': 43595}
weighted
{'f1-score': 0.9677004335603978,
 'precision': 0.9684968719833342,
 'recall': 0.9684367473334098,
 'support': 43595}
### report_full
macro
{'f1-score': 0.9158508529982635,
 'precision': 0.9656978814914231,
 'recall': 0.873975307342871,
 'support': 44467}
micro
{'f1-score': 0.958847175853376,
 'precision': 0.9684367473334098,
 'recall': 0.9494456563294128,
 'support': 44467}
weighted
{'f1-score': 0.9579970813474764,
 'precision': 0.9682291961524386,
 'recall': 0.9494456563294128,
 'support': 44467}
## test
PPCR: 0.980688
### report
macro
{'f1-score': 0.9074168243510136,
 'precision': 0.9536975446712449,
 'recall': 0.8705466965608393,
 'support': 10969}
micro
{'f1-score': 0.9596134561035646,
 'precision': 0.9596134561035646,
 'recall': 0.9596134561035646,
 'support': 10969}
weighted
{'f1-score': 0.9587270777391586,
 'precision': 0.9595981657693784,
 'recall': 0.9596134561035646,
 'support': 10969}
### report_full
macro
{'f1-score': 0.9001747615731152,
 'precision': 0.9536975446712449,
 'recall': 0.8566945021667062,
 'support': 11185}
micro
{'f1-score': 0.9502572898799314,
 'precision': 0.9596134561035646,
 'recall': 0.9410818059901654,
 'support': 11185}
weighted
{'f1-score': 0.9492760654866815,
 'precision': 0.9593671251759149,
 'recall': 0.9410818059901654,
 'support': 11185}
```

## javascript
### Summary
19 rules, avg.len. 6.1

| | |
|-|-|
|Min support|98|
|Max support|16167|
|Min confidence|0.8706293702125549|
|Max confidence|0.9997541904449463|

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
| 1 | `  -1.internal_type = StringLiteral<br>⇒ y = '<br>Confidence: 1.000. Support: 2034.` |
| 2 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ +1.internal_type = StringLiteral<br>⇒ y = ␣<br>Confidence: 0.926. Support: 237.` |
| 3 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = :<br>	∧ +1.internal_type = StringLiteral<br>⇒ y = ␣<br>Confidence: 0.995. Support: 98.` |
| 4 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,}<br>	∧ -2.label not in {<space>}<br>	∧ +1.internal_type = StringLiteral<br>⇒ y = '<br>Confidence: 0.990. Support: 2025.` |
| 5 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.995. Support: 887.` |
| 6 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ -4.length ≥ 9<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>⇒ y = ⏎⏎<br>Confidence: 0.916. Support: 257.` |
| 7 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ -4.length ≤ 8<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>⇒ y = ⏎<br>Confidence: 0.938. Support: 1315.` |
| 8 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ +1.internal_type not in {StringLiteral}<br>⇒ y = ␣<br>Confidence: 0.923. Support: 2133.` |
| 9 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, ;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = =<br>⇒ y = ␣<br>Confidence: 1.000. Support: 1723.` |
| 10 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, ;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = {<br>⇒ y = ␣<br>Confidence: 0.923. Support: 1295.` |
| 11 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ -3.reserved = ><br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {}<br>⇒ y = ⏎␣⁺␣⁺<br>Confidence: 0.999. Support: 808.` |
| 12 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ -3.reserved not in {>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles in {EXPRESSION}<br>	∧ ^1.roles in {EXPRESSION}<br>⇒ y = ␣<br>Confidence: 0.916. Support: 161.` |
| 13 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, ;, {}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles in {EXPRESSION}<br>	∧ ^1.roles in {EXPRESSION, OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.871. Support: 143.` |
| 14 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, ;, {}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles in {EXPRESSION}<br>	∧ ^1.roles in {DECLARATION, EXPRESSION}<br>⇒ y = ␣<br>Confidence: 0.875. Support: 100.` |
| 15 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, ;, {}<br>	∧ -3.reserved not in {>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {}<br>	∧ +1.roles in {EXPRESSION}<br>	∧ ^1.roles in {EXPRESSION} and not in {DECLARATION, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.966. Support: 3470.` |
| 16 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, ;}<br>	∧ -3.reserved not in {>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {}<br>	∧ +1.roles in {EXPRESSION}<br>	∧ +4.roles in {CALLEE}<br>	∧ ^1.roles not in {EXPRESSION}<br>⇒ y = ∅<br>Confidence: 0.990. Support: 245.` |
| 17 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, ;}<br>	∧ -3.reserved not in {>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles in {EXPRESSION}<br>	∧ +4.roles not in {CALLEE}<br>	∧ ^1.roles not in {EXPRESSION}<br>⇒ y = ␣<br>Confidence: 0.918. Support: 1508.` |
| 18 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, ;}<br>	∧ -1.roles in {IDENTIFIER}<br>	∧ -3.reserved not in {>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.984. Support: 279.` |
| 19 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, ;}<br>	∧ -3.reserved not in {>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.974. Support: 16167.` |

<details>
    <summary>Machine-readable report</summary>
```json
{"javascript": {"avg_rule_len": 6.052631578947368, "max_conf": 0.9997541904449463, "max_support": 16167, "min_conf": 0.8706293702125549, "min_support": 98, "num_rules": 19}}
```
</details>
