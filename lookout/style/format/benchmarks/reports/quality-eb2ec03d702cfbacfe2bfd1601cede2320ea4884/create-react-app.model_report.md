# Model report for file:///tmp/top-repos-quality-repos-qb72sltl/create-react-app HEAD 32106d216e4c31fda30ec475f9f03186d116c893

### Dump

```json
{'created_at': datetime.datetime(2019, 2, 12, 21, 44, 47, 898610),
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
 'uuid': 'c9081dd1-da19-4575-baf1-09a9ac2039d0',
 'version': [1]}
style.format.analyzer.FormatAnalyzer/[1] file:///tmp/top-repos-quality-repos-qb72sltl/create-react-app 32106d216e4c31fda30ec475f9f03186d116c893

# javascript
16 rules, avg.len. 6.3
## train
PPCR: 0.843095
### report
macro
{'f1-score': 0.7419240162573868,
 'precision': 0.7873097665920965,
 'recall': 0.7074477568921366,
 'support': 14798}
micro
{'f1-score': 0.9168806595485877,
 'precision': 0.9168806595485877,
 'recall': 0.9168806595485877,
 'support': 14798}
weighted
{'f1-score': 0.9103565500204258,
 'precision': 0.9107674763665515,
 'recall': 0.9168806595485877,
 'support': 14798}
### report_full
macro
{'f1-score': 0.6320283250930392,
 'precision': 0.7873097665920965,
 'recall': 0.5538966250597896,
 'support': 17552}
micro
{'f1-score': 0.8388253477588873,
 'precision': 0.9168806595485877,
 'recall': 0.773017319963537,
 'support': 17552}
weighted
{'f1-score': 0.8199625229727805,
 'precision': 0.9142145302424721,
 'recall': 0.773017319963537,
 'support': 17552}
## test
PPCR: 0.838166
### report
macro
{'f1-score': 0.756816996635179,
 'precision': 0.790621758964488,
 'recall': 0.7405778050023083,
 'support': 2139}
micro
{'f1-score': 0.9518466573165031,
 'precision': 0.9518466573165031,
 'recall': 0.9518466573165031,
 'support': 2139}
weighted
{'f1-score': 0.9508545375715876,
 'precision': 0.9535679904615811,
 'recall': 0.9518466573165031,
 'support': 2139}
### report_full
macro
{'f1-score': 0.6541440390054925,
 'precision': 0.790621758964488,
 'recall': 0.5938011523500553,
 'support': 2552}
micro
{'f1-score': 0.8680451929226178,
 'precision': 0.9518466573165031,
 'recall': 0.7978056426332288,
 'support': 2552}
weighted
{'f1-score': 0.852610795337575,
 'precision': 0.9523458531057258,
 'recall': 0.7978056426332288,
 'support': 2552}
```

## javascript
### Summary
16 rules, avg.len. 6.3

| | |
|-|-|
|Min support|90|
|Max support|6766|
|Min confidence|0.8245192170143127|
|Max confidence|0.9984894394874573|

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
                     'min_samples_split': 240,
                     'n_estimators': 10,
                     'prune_attributes': True,
                     'prune_branches_algorithms': ['reduced-error'],
                     'prune_dataset_ratio': 0.2,
                     'top_down_greedy_budget': [False, 0.5]}}
```

### Rules

| rule number | description |
|----:|:-----|
| 1 | `  -1.internal_type = StringLiteral<br>⇒ y = '<br>Confidence: 0.942. Support: 819.` |
| 2 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = :<br>	∧ +1.internal_type = StringLiteral<br>⇒ y = ␣<br>Confidence: 0.939. Support: 106.` |
| 3 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -2.label not in {<space>}<br>	∧ +1.internal_type = StringLiteral<br>⇒ y = '<br>Confidence: 0.914. Support: 808.` |
| 4 | `  -1.internal_type = CommentLine<br>⇒ y = ⏎<br>Confidence: 0.966. Support: 428.` |
| 5 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.internal_type = VariableDeclarator<br>	∧ ^1.roles in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.950. Support: 526.` |
| 6 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -4.diff_offset ≥ 6<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.internal_type not in {VariableDeclarator}<br>	∧ ^1.roles in {DECLARATION} and not in {FUNCTION}<br>⇒ y = ␣<br>Confidence: 0.939. Support: 106.` |
| 7 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.998. Support: 214.` |
| 8 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles in {CALL}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ⏎⏎<br>Confidence: 0.828. Support: 90.` |
| 9 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {CallExpression}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ⏎<br>Confidence: 0.900. Support: 324.` |
| 10 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {CALL, DECLARATION}<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.825. Support: 208.` |
| 11 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved = :<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.998. Support: 331.` |
| 12 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved = {<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ⏎␣⁺␣⁺<br>Confidence: 0.834. Support: 382.` |
| 13 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved = const<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.998. Support: 209.` |
| 14 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, ;, const, {}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = {<br>	∧ ^1.roles not in {DECLARATION}<br>	∧ ^2.roles in {STATEMENT}<br>⇒ y = ␣<br>Confidence: 0.946. Support: 156.` |
| 15 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, const, {}<br>	∧ -3.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {{}<br>	∧ +1.length ≤ 1<br>	∧ +2.reserved not in {>}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.846. Support: 393.` |
| 16 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, const, {}<br>	∧ -3.reserved not in {;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {{}<br>	∧ +2.reserved not in {>}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.909. Support: 6766.` |

<details>
    <summary>Machine-readable report</summary>
```json
{"javascript": {"avg_rule_len": 6.3125, "max_conf": 0.9984894394874573, "max_support": 6766, "min_conf": 0.8245192170143127, "min_support": 90, "num_rules": 16}}
```
</details>
