# Model report for file:///tmp/top-repos-quality-repos-6seis7kt/jquery HEAD dae5f3ce3d2df27873d01f0d9682f6a91ad66b87

### Dump

```json
{'created_at': datetime.datetime(2019, 2, 12, 22, 34, 22, 706015),
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
 'uuid': '521e92bd-6cdc-44fc-9b55-a394974dc677',
 'version': [1]}
style.format.analyzer.FormatAnalyzer/[1] file:///tmp/top-repos-quality-repos-6seis7kt/jquery dae5f3ce3d2df27873d01f0d9682f6a91ad66b87

# javascript
51 rules, avg.len. 10.3
## train
PPCR: 0.949273
### report
macro
{'f1-score': 0.6259540122708561,
 'precision': 0.6762265858953419,
 'recall': 0.5933152258654816,
 'support': 173434}
micro
{'f1-score': 0.9694292929875341,
 'precision': 0.9694292929875341,
 'recall': 0.9694292929875341,
 'support': 173434}
weighted
{'f1-score': 0.9671003245144216,
 'precision': 0.9661324125002941,
 'recall': 0.9694292929875341,
 'support': 173434}
### report_full
macro
{'f1-score': 0.5611143550162816,
 'precision': 0.6762265858953419,
 'recall': 0.5094723290081786,
 'support': 182702}
micro
{'f1-score': 0.9442010917177708,
 'precision': 0.9694292929875341,
 'recall': 0.9202526518593119,
 'support': 182702}
weighted
{'f1-score': 0.9319103378472665,
 'precision': 0.9615484176881295,
 'recall': 0.9202526518593119,
 'support': 182702}
## test
PPCR: 0.953432
### report
macro
{'f1-score': 0.619814248065926,
 'precision': 0.6741300404385914,
 'recall': 0.5820899095738622,
 'support': 45964}
micro
{'f1-score': 0.9769819859020102,
 'precision': 0.9769819859020102,
 'recall': 0.9769819859020102,
 'support': 45964}
weighted
{'f1-score': 0.9753543605020158,
 'precision': 0.9751434224741818,
 'recall': 0.9769819859020102,
 'support': 45964}
### report_full
macro
{'f1-score': 0.5431422598756002,
 'precision': 0.6741300404385914,
 'recall': 0.490211346425089,
 'support': 48209}
micro
{'f1-score': 0.9536916101217972,
 'precision': 0.9769819859020102,
 'recall': 0.9314858221493912,
 'support': 48209}
weighted
{'f1-score': 0.9400625751411414,
 'precision': 0.9720422281559254,
 'recall': 0.9314858221493912,
 'support': 48209}
```

## javascript
### Summary
51 rules, avg.len. 10.3

| | |
|-|-|
|Min support|94|
|Max support|24017|
|Min confidence|0.8014705777168274|
|Max confidence|0.9999547600746155|

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
| 1 | `  -1.roles in {STRING}<br>⇒ y = "<br>Confidence: 1.000. Support: 10265.` |
| 2 | `  -1.label in {<space>}<br>	∧ -1.roles not in {STRING}<br>⇒ y = "<br>Confidence: 1.000. Support: 8991.` |
| 3 | `  -1.label not in {<space>}<br>	∧ -1.roles not in {STRING}<br>	∧ +2.roles in {EXPRESSION}<br>	∧ ^1.roles in {OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.960. Support: 3588.` |
| 4 | `  -1.label not in {<space>}<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved = {<br>	∧ +2.roles in {EXPRESSION}<br>	∧ ^1.roles in {LITERAL} and not in {OPERATOR}<br>⇒ y = ⏎<br>Confidence: 0.814. Support: 94.` |
| 5 | `  -1.label not in {<space>}<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved = {<br>	∧ +2.roles in {EXPRESSION}<br>	∧ ^1.roles not in {LITERAL, OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.987. Support: 2418.` |
| 6 | `  -1.label not in {<space>}<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved not in {{}<br>	∧ +2.roles in {EXPRESSION}<br>	∧ ^1.internal_type = VariableDeclarator<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.960. Support: 1031.` |
| 7 | `  -1.label not in {<space>}<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved not in {{}<br>	∧ +1.roles in {COMMENT}<br>	∧ +1.length ≥ 2<br>	∧ +2.roles in {EXPRESSION}<br>	∧ ^1.internal_type not in {VariableDeclarator}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.998. Support: 656.` |
| 8 | `  -1.label not in {<space>}<br>	∧ -1.reserved = {<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved not in {{}<br>	∧ +1.roles not in {COMMENT}<br>	∧ +1.length ≥ 2<br>	∧ +2.roles in {EXPRESSION}<br>	∧ ^1.internal_type not in {VariableDeclarator}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ⏎⇥⁺<br>Confidence: 0.908. Support: 429.` |
| 9 | `  -1.label not in {<space>}<br>	∧ -1.reserved = (<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved not in {{}<br>	∧ +1.length ≤ 1<br>	∧ +2.roles in {EXPRESSION}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.988. Support: 453.` |
| 10 | `  -1.label not in {<space>}<br>	∧ -1.reserved = if<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved not in {{}<br>	∧ +1.length ≤ 1<br>	∧ +2.roles in {EXPRESSION}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.999. Support: 415.` |
| 11 | `  -1.label not in {<space>}<br>	∧ -1.reserved not in {(, if}<br>	∧ -1.roles not in {STRING}<br>	∧ +1.length ≤ 1<br>	∧ +2.roles in {EXPRESSION}<br>	∧ ^1.internal_type = ConditionalExpression<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.977. Support: 280.` |
| 12 | `  -1.label not in {<space>}<br>	∧ -1.reserved not in {(, if}<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved = }<br>	∧ +1.length ≤ 1<br>	∧ +2.roles in {EXPRESSION}<br>	∧ ^1.internal_type not in {VariableDeclarator}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ⏎⇥⁻<br>Confidence: 0.959. Support: 157.` |
| 13 | `  -1.label not in {<space>}<br>	∧ -1.reserved = ,<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved not in {}}<br>	∧ +1.length ≤ 1<br>	∧ +2.roles in {EXPRESSION}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.884. Support: 160.` |
| 14 | `  -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ,, :, if}<br>	∧ -1.roles in {EXPRESSION} and not in {STRING}<br>	∧ +1.reserved not in {{, }}<br>	∧ +1.length ≤ 1<br>	∧ +2.roles in {EXPRESSION}<br>	∧ ^1.internal_type not in {VariableDeclarator}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.999. Support: 24017.` |
| 15 | `  -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ,, :, if}<br>	∧ -1.roles not in {EXPRESSION, STRING}<br>	∧ +1.reserved = .<br>	∧ +1.length ≤ 1<br>	∧ +2.roles in {EXPRESSION}<br>	∧ ^1.internal_type not in {VariableDeclarator}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.873. Support: 2239.` |
| 16 | `  -1.diff_offset ≤ 2<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ,, :, if}<br>	∧ -1.roles not in {EXPRESSION, STRING}<br>	∧ -4.diff_line ≥ 1<br>	∧ +1.reserved not in {{, }}<br>	∧ +1.length ≤ 1<br>	∧ +2.roles in {EXPRESSION}<br>	∧ ^1.internal_type not in {VariableDeclarator}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.993. Support: 536.` |
| 17 | `  -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ,, :, if}<br>	∧ -1.roles not in {EXPRESSION, STRING}<br>	∧ -4.diff_line = 0<br>	∧ +1.reserved not in {{, }}<br>	∧ +1.length ≤ 1<br>	∧ +2.roles in {EXPRESSION}<br>	∧ ^1.internal_type not in {VariableDeclarator}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.993. Support: 6854.` |
| 18 | `  -1.label not in {<space>}<br>	∧ -1.reserved = .<br>	∧ -1.roles not in {STRING}<br>	∧ +2.roles not in {EXPRESSION}<br>⇒ y = ∅<br>Confidence: 1.000. Support: 11055.` |
| 19 | `  -1.label not in {<space>}<br>	∧ -1.reserved = ;<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved = }<br>	∧ +2.roles not in {EXPRESSION}<br>⇒ y = ⏎⇥⁻<br>Confidence: 0.903. Support: 2241.` |
| 20 | `  -1.label not in {<space>}<br>	∧ -1.reserved = ;<br>	∧ -1.roles not in {STRING}<br>	∧ -5.label in {<newline>}<br>	∧ +1.reserved not in {}}<br>	∧ +2.roles not in {EXPRESSION}<br>	∧ ^1.roles in {STATEMENT}<br>	∧ ^2.roles in {CALLEE}<br>⇒ y = ⏎⏎<br>Confidence: 0.990. Support: 146.` |
| 21 | `  -1.label not in {<space>}<br>	∧ -1.reserved = ;<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved not in {}}<br>	∧ +2.roles not in {EXPRESSION}<br>	∧ +3.length ≥ 1<br>	∧ ^1.roles not in {STATEMENT}<br>⇒ y = ⏎⏎<br>Confidence: 0.854. Support: 884.` |
| 22 | `  -1.label not in {<space>}<br>	∧ -1.reserved = ;<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved not in {}}<br>	∧ +2.roles not in {EXPRESSION}<br>	∧ +3.length = 0<br>	∧ ^1.roles not in {STATEMENT}<br>⇒ y = ⏎<br>Confidence: 0.995. Support: 98.` |
| 23 | `  -1.label not in {<space>}<br>	∧ -1.reserved not in {., ;}<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved = ;<br>	∧ +2.roles not in {EXPRESSION}<br>⇒ y = ∅<br>Confidence: 0.981. Support: 3780.` |
| 24 | `  -1.label not in {<space>}<br>	∧ -1.reserved = if<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved = (<br>	∧ +2.roles not in {EXPRESSION}<br>⇒ y = ␣<br>Confidence: 0.997. Support: 149.` |
| 25 | `  -1.label not in {<space>}<br>	∧ -1.reserved not in {;, if}<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved = (<br>	∧ +2.roles not in {EXPRESSION}<br>⇒ y = ∅<br>Confidence: 0.978. Support: 2926.` |
| 26 | `  -1.label not in {<space>}<br>	∧ -1.reserved = {<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved not in {(}<br>	∧ +2.internal_type = CommentLine<br>	∧ +2.roles not in {EXPRESSION}<br>⇒ y = ⏎⏎⇥⁺<br>Confidence: 0.934. Support: 188.` |
| 27 | `  -1.label not in {<space>}<br>	∧ -1.reserved = {<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved not in {(}<br>	∧ +2.internal_type not in {CommentLine}<br>	∧ +2.roles not in {EXPRESSION}<br>	∧ +3.roles in {VALUE}<br>	∧ +5.length ≤ 3<br>⇒ y = ␣<br>Confidence: 0.811. Support: 257.` |
| 28 | `  -1.label not in {<space>}<br>	∧ -1.reserved = {<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved not in {(}<br>	∧ +2.internal_type not in {CommentLine}<br>	∧ +2.roles not in {EXPRESSION}<br>	∧ +3.roles not in {VALUE}<br>⇒ y = ⏎⇥⁺<br>Confidence: 0.873. Support: 2375.` |
| 29 | `  -1.diff_col ≥ 13<br>	∧ -1.label in {<newline>} and not in {<space>}<br>	∧ -1.reserved not in {., ;, {}<br>	∧ +1.reserved not in {(, ;}<br>	∧ +2.roles not in {EXPRESSION}<br>⇒ y = "<br>Confidence: 0.999. Support: 966.` |
| 30 | `  -1.diff_col ≥ 13<br>	∧ -1.internal_type = CommentLine<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {., ;, {}<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved not in {(, ;}<br>	∧ +2.roles not in {EXPRESSION}<br>⇒ y = ⏎<br>Confidence: 0.972. Support: 1302.` |
| 31 | `  -1.diff_col ≤ 12<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {., ;, {}<br>	∧ -1.roles not in {STRING}<br>	∧ +1.roles in {COMMENT}<br>	∧ +2.roles not in {EXPRESSION}<br>⇒ y = ∅<br>Confidence: 0.999. Support: 872.` |
| 32 | `  -1.diff_col ≤ 12<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {., ;, {}<br>	∧ -3.diff_line ≥ 1<br>	∧ +1.reserved not in {(, ;}<br>	∧ +1.roles in {KEY}<br>	∧ +2.roles not in {EXPRESSION}<br>⇒ y = "<br>Confidence: 0.975. Support: 99.` |
| 33 | `  -1.diff_col ≤ 12<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {., ;, {}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.roles in {NUMBER}<br>	∧ -3.diff_line = 0<br>	∧ +1.reserved not in {(, ;}<br>	∧ +1.roles in {KEY} and not in {COMMENT}<br>	∧ +2.roles not in {EXPRESSION}<br>⇒ y = ␣<br>Confidence: 0.824. Support: 173.` |
| 34 | `  •••start_col ≤ 47<br>	∧ -1.diff_col ≤ 12<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {., ;, {}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.roles not in {NUMBER}<br>	∧ -3.diff_line = 0<br>	∧ +1.reserved not in {(, ;}<br>	∧ +1.roles in {KEY}<br>	∧ +2.roles not in {EXPRESSION}<br>⇒ y = ⏎<br>Confidence: 0.862. Support: 1022.` |
| 35 | `  -1.diff_col ≤ 12<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {., ;, {}<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved = ,<br>	∧ +1.roles not in {KEY}<br>	∧ +2.roles not in {EXPRESSION}<br>⇒ y = ∅<br>Confidence: 0.985. Support: 682.` |
| 36 | `  -1.diff_col ≤ 12<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {., ;, {}<br>	∧ -1.roles in {KEY} and not in {STRING}<br>	∧ +1.reserved not in {,}<br>	∧ +1.roles not in {KEY}<br>	∧ +2.roles not in {EXPRESSION}<br>⇒ y = ∅<br>Confidence: 0.999. Support: 506.` |
| 37 | `  •••start_col ≥ 29<br>	∧ -1.diff_col ≤ 12<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {., {}<br>	∧ -1.roles not in {KEY, STRING}<br>	∧ +1.reserved = }<br>	∧ +1.roles not in {COMMENT, KEY}<br>	∧ +2.roles not in {EXPRESSION}<br>⇒ y = ␣<br>Confidence: 0.825. Support: 374.` |
| 38 | `  •••start_col ≤ 28<br>	∧ -1.diff_col ≤ 12<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {., {}<br>	∧ -1.roles not in {KEY, STRING}<br>	∧ +1.reserved = }<br>	∧ +1.roles not in {COMMENT, KEY}<br>	∧ +2.roles not in {EXPRESSION}<br>⇒ y = ⏎⇥⁻<br>Confidence: 0.925. Support: 643.` |
| 39 | `  -1.diff_col ≤ 12<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {., ;, {}<br>	∧ -1.roles not in {KEY, STRING}<br>	∧ +1.reserved not in {(, ,, ;, }}<br>	∧ +1.roles not in {COMMENT, KEY}<br>	∧ +2.roles in {COMMENT} and not in {EXPRESSION}<br>⇒ y = ⏎⏎<br>Confidence: 0.801. Support: 340.` |
| 40 | `  -1.diff_col ≤ 12<br>	∧ -1.label in {<newline>} and not in {<space>}<br>	∧ -1.reserved not in {., ;, {}<br>	∧ +1.reserved not in {(, ,, ;, }}<br>	∧ +2.roles not in {EXPRESSION}<br>⇒ y = "<br>Confidence: 0.998. Support: 233.` |
| 41 | `  -1.diff_col ≤ 12<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {., ;, {}<br>	∧ -1.roles not in {KEY, STRING}<br>	∧ +1.reserved not in {(, ,, ;, }}<br>	∧ +1.roles not in {COMMENT, KEY}<br>	∧ +2.reserved not in {=}<br>	∧ +2.roles not in {COMMENT, EXPRESSION}<br>	∧ ^1.internal_type = VariableDeclaration<br>⇒ y = ␣<br>Confidence: 0.857. Support: 607.` |
| 42 | `  -1.diff_col ≤ 12<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved = (<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved = )<br>	∧ +1.roles not in {KEY}<br>	∧ +2.roles not in {EXPRESSION}<br>⇒ y = ∅<br>Confidence: 0.998. Support: 1993.` |
| 43 | `  -1.diff_col ≤ 12<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved = (<br>	∧ -1.roles not in {KEY, STRING}<br>	∧ +1.reserved not in {(, ), ,, }}<br>	∧ +1.roles not in {COMMENT, KEY}<br>	∧ +2.roles not in {COMMENT, EXPRESSION}<br>	∧ ^1.internal_type not in {VariableDeclaration}<br>⇒ y = ␣<br>Confidence: 0.987. Support: 10636.` |
| 44 | `  -1.diff_col ≤ 12<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ., ;, {}<br>	∧ -1.roles not in {KEY, STRING}<br>	∧ -5.label in {<newline>}<br>	∧ +1.reserved not in {(, ,, ;, }}<br>	∧ +1.roles not in {COMMENT}<br>	∧ +2.roles not in {EXPRESSION}<br>	∧ ^1.internal_type = ArrayExpression<br>⇒ y = ⏎<br>Confidence: 0.904. Support: 317.` |
| 45 | `  -1.diff_col ≤ 12<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ., ;, {}<br>	∧ -1.roles not in {KEY, STRING}<br>	∧ -5.label not in {<newline>}<br>	∧ +1.reserved not in {(, ,, ;, }}<br>	∧ +1.roles not in {COMMENT, KEY}<br>	∧ +2.roles not in {COMMENT, EXPRESSION}<br>	∧ ^1.internal_type = ArrayExpression<br>⇒ y = ␣<br>Confidence: 0.914. Support: 495.` |
| 46 | `  -1.diff_col ≤ 12<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ., ;, {}<br>	∧ -1.roles not in {KEY, STRING}<br>	∧ -3.reserved = (<br>	∧ -4.diff_offset ≥ 6<br>	∧ -5.diff_offset ≥ 2<br>	∧ +1.reserved not in {(, ,, ;, }}<br>	∧ +1.roles not in {KEY}<br>	∧ +1.length ≥ 2<br>	∧ +2.roles not in {EXPRESSION}<br>	∧ ^1.internal_type not in {ArrayExpression, VariableDeclaration}<br>⇒ y = ␣<br>Confidence: 0.814. Support: 566.` |
| 47 | `  -1.diff_col ≤ 12<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ -1.roles not in {KEY, STRING}<br>	∧ -3.reserved = (<br>	∧ -4.diff_offset ≤ 5<br>	∧ +1.reserved not in {,, }}<br>	∧ +1.roles not in {KEY}<br>	∧ +1.length ≥ 2<br>	∧ +2.roles not in {EXPRESSION}<br>	∧ ^1.internal_type not in {ArrayExpression}<br>⇒ y = ∅<br>Confidence: 0.969. Support: 245.` |
| 48 | `  -1.diff_col ≤ 12<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved = }<br>	∧ -1.roles not in {EXPRESSION, KEY, STRING}<br>	∧ -5.diff_offset ≥ 2<br>	∧ +1.reserved not in {,, }}<br>	∧ +1.roles not in {KEY}<br>	∧ +1.length ≥ 2<br>	∧ +2.roles not in {EXPRESSION}<br>	∧ ^1.internal_type not in {ArrayExpression, VariableDeclaration}<br>	∧ ^1.roles not in {SCOPE}<br>⇒ y = ␣<br>Confidence: 0.909. Support: 171.` |
| 49 | `  -1.diff_col ≤ 12<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ., ;, {, }}<br>	∧ -1.roles not in {EXPRESSION, KEY, STRING}<br>	∧ -3.reserved not in {(}<br>	∧ -5.diff_offset ≥ 2<br>	∧ +1.reserved not in {(, ,, ;, }}<br>	∧ +1.roles not in {KEY}<br>	∧ +1.length ≥ 2<br>	∧ +2.roles not in {EXPRESSION}<br>	∧ ^1.internal_type not in {ArrayExpression, VariableDeclaration}<br>⇒ y = ␣<br>Confidence: 0.935. Support: 13696.` |
| 50 | `  -1.diff_col ≤ 12<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ., ;, {}<br>	∧ -1.roles not in {KEY, STRING}<br>	∧ -4.label in {<newline>}<br>	∧ -5.diff_offset ≥ 2<br>	∧ +1.reserved not in {(, ,, ;, }}<br>	∧ +1.roles not in {KEY}<br>	∧ +1.length ≤ 1<br>	∧ +2.roles not in {EXPRESSION}<br>	∧ ^1.internal_type not in {ArrayExpression, VariableDeclaration}<br>⇒ y = ␣<br>Confidence: 0.944. Support: 477.` |
| 51 | `  -1.diff_col ≤ 12<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ., ;, {}<br>	∧ -1.roles not in {KEY, STRING}<br>	∧ -4.label not in {<newline>}<br>	∧ -5.diff_offset ≥ 2<br>	∧ +1.reserved not in {(, ,, ;, }}<br>	∧ +1.roles not in {KEY}<br>	∧ +1.length ≤ 1<br>	∧ +2.roles not in {EXPRESSION}<br>	∧ ^1.internal_type not in {ArrayExpression, VariableDeclaration}<br>⇒ y = ␣<br>Confidence: 0.980. Support: 15400.` |

<details>
    <summary>Machine-readable report</summary>
```json
{"javascript": {"avg_rule_len": 10.313725490196079, "max_conf": 0.9999547600746155, "max_support": 24017, "min_conf": 0.8014705777168274, "min_support": 94, "num_rules": 51}}
```
</details>
