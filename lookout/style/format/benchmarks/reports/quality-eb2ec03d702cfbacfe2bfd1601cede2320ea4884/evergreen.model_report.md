# Model report for file:///tmp/top-repos-quality-repos-tp_t08ml/evergreen HEAD ba22d511dad83c072842e47801ef42697d142f7c

### Dump

```json
{'created_at': datetime.datetime(2019, 2, 13, 7, 32, 3, 678375),
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
 'uuid': '5a99202a-8a64-4219-9cb5-1a2ce2200eb7',
 'version': [1]}
style.format.analyzer.FormatAnalyzer/[1] file:///tmp/top-repos-quality-repos-tp_t08ml/evergreen ba22d511dad83c072842e47801ef42697d142f7c

# javascript
66 rules, avg.len. 10.6
## train
PPCR: 0.925939
### report
macro
{'f1-score': 0.7261015793207852,
 'precision': 0.758198201358468,
 'recall': 0.7029785989799299,
 'support': 77877}
micro
{'f1-score': 0.9513078315805693,
 'precision': 0.9513078315805693,
 'recall': 0.9513078315805693,
 'support': 77877}
weighted
{'f1-score': 0.9484458894121365,
 'precision': 0.9477801107792525,
 'recall': 0.9513078315805693,
 'support': 77877}
### report_full
macro
{'f1-score': 0.6593704942410873,
 'precision': 0.758198201358468,
 'recall': 0.6047007817009906,
 'support': 84106}
micro
{'f1-score': 0.9147256193551173,
 'precision': 0.9513078315805693,
 'recall': 0.8808527334554015,
 'support': 84106}
weighted
{'f1-score': 0.9054430443211353,
 'precision': 0.9448831817946555,
 'recall': 0.8808527334554015,
 'support': 84106}
## test
PPCR: 0.934698
### report
macro
{'f1-score': 0.6761568158963345,
 'precision': 0.7439654387003994,
 'recall': 0.6425245930948427,
 'support': 18350}
micro
{'f1-score': 0.9348228882833788,
 'precision': 0.9348228882833788,
 'recall': 0.9348228882833788,
 'support': 18350}
weighted
{'f1-score': 0.9283622572792619,
 'precision': 0.9306277528405075,
 'recall': 0.9348228882833788,
 'support': 18350}
### report_full
macro
{'f1-score': 0.6043194048400633,
 'precision': 0.7439654387003994,
 'recall': 0.5550260454913067,
 'support': 19632}
micro
{'f1-score': 0.9032699699857827,
 'precision': 0.9348228882833788,
 'recall': 0.8737775061124694,
 'support': 19632}
weighted
{'f1-score': 0.8858778240293925,
 'precision': 0.9287674199793878,
 'recall': 0.8737775061124694,
 'support': 19632}
```

## javascript
### Summary
66 rules, avg.len. 10.6

| | |
|-|-|
|Min support|96|
|Max support|26659|
|Min confidence|0.8057757616043091|
|Max confidence|0.9997504949569702|

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
                     'min_samples_split': 190,
                     'n_estimators': 10,
                     'prune_attributes': True,
                     'prune_branches_algorithms': ['reduced-error'],
                     'prune_dataset_ratio': 0.2,
                     'top_down_greedy_budget': [False, 0.5]}}
```

### Rules

| rule number | description |
|----:|:-----|
| 1 | `  -1.label in {<space>}<br>	∧ ^1.roles in {DECLARATION}<br>⇒ y = '<br>Confidence: 0.999. Support: 879.` |
| 2 | `  -1.label not in {<space>}<br>	∧ -1.reserved = {<br>	∧ -4.length ≤ 2<br>	∧ ^1.roles in {DECLARATION}<br>⇒ y = ⏎␣⁺␣⁺<br>Confidence: 0.944. Support: 494.` |
| 3 | `  -1.label not in {<space>}<br>	∧ -1.reserved not in {{}<br>	∧ +1.reserved = ><br>	∧ ^1.roles in {DECLARATION}<br>⇒ y = ∅<br>Confidence: 0.999. Support: 394.` |
| 4 | `  -1.label not in {<space>}<br>	∧ -1.reserved not in {{}<br>	∧ +1.reserved = ,<br>	∧ ^1.roles in {DECLARATION}<br>⇒ y = ∅<br>Confidence: 0.999. Support: 343.` |
| 5 | `  -1.label not in {<space>}<br>	∧ -1.reserved not in {{}<br>	∧ +1.reserved = )<br>	∧ ^1.roles in {DECLARATION}<br>⇒ y = ∅<br>Confidence: 0.991. Support: 272.` |
| 6 | `  -1.label not in {<space>}<br>	∧ -1.reserved = (<br>	∧ +1.reserved not in {), ,, <, >}<br>	∧ ^1.roles in {DECLARATION}<br>⇒ y = ∅<br>Confidence: 0.989. Support: 136.` |
| 7 | `  -1.label not in {<space>}<br>	∧ -1.reserved not in {(, {}<br>	∧ +1.internal_type = JSXIdentifier<br>	∧ +1.reserved not in {), ,, >}<br>	∧ ^1.roles in {DECLARATION}<br>⇒ y = ∅<br>Confidence: 0.997. Support: 162.` |
| 8 | `  -1.label not in {<space>}<br>	∧ -1.reserved not in {(, {}<br>	∧ -1.roles in {KEY}<br>	∧ +1.internal_type not in {JSXIdentifier}<br>	∧ +1.reserved not in {), ,, >}<br>	∧ ^1.roles in {DECLARATION}<br>⇒ y = ∅<br>Confidence: 0.996. Support: 127.` |
| 9 | `  -1.label not in {<space>}<br>	∧ -1.reserved not in {(, {}<br>	∧ -1.roles not in {KEY}<br>	∧ -3.label not in {<newline>}<br>	∧ +1.internal_type not in {JSXIdentifier}<br>	∧ +1.reserved not in {), ,, >}<br>	∧ ^1.roles in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.971. Support: 5280.` |
| 10 | `  -1.internal_type = StringLiteral<br>	∧ -2.reserved = =<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = "<br>Confidence: 0.999. Support: 781.` |
| 11 | `  -1.internal_type = StringLiteral<br>	∧ -2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = '<br>Confidence: 1.000. Support: 2004.` |
| 12 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = :<br>	∧ +1.roles in {MAP}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.999. Support: 834.` |
| 13 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ -2.label in {<space>}<br>	∧ +1.roles in {MAP}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ⏎␣⁺␣⁺<br>Confidence: 0.817. Support: 369.` |
| 14 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ -2.label not in {<space>}<br>	∧ -5.diff_offset ≤ 14<br>	∧ +1.roles in {MAP}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.842. Support: 117.` |
| 15 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {:, {}<br>	∧ +1.internal_type = StringLiteral<br>	∧ +1.roles in {MAP}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = '<br>Confidence: 0.940. Support: 477.` |
| 16 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {:, {}<br>	∧ -3.label in {<space>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles in {MAP}<br>	∧ ^1.roles in {INCOMPLETE} and not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.938. Support: 153.` |
| 17 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {:, {}<br>	∧ -3.label in {<space>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles in {MAP}<br>	∧ ^1.roles not in {DECLARATION, INCOMPLETE}<br>⇒ y = ⏎<br>Confidence: 0.898. Support: 249.` |
| 18 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {:, {}<br>	∧ -3.label not in {<space>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles in {MAP}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ⏎<br>Confidence: 0.921. Support: 1492.` |
| 19 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label in {'}<br>	∧ +1.reserved = import<br>	∧ +1.roles not in {MAP}<br>	∧ ^1.roles not in {DECLARATION}<br>	∧ ^2.roles in {FILE}<br>⇒ y = ⏎<br>Confidence: 0.999. Support: 567.` |
| 20 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label in {'}<br>	∧ -2.roles in {IMPORT}<br>	∧ +1.reserved not in {import}<br>	∧ +1.roles not in {MAP}<br>	∧ ^1.roles not in {DECLARATION}<br>	∧ ^2.roles in {FILE}<br>⇒ y = ⏎⏎<br>Confidence: 0.997. Support: 145.` |
| 21 | `  •••start_col ≤ 21<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {'}<br>	∧ -3.diff_offset ≥ 8<br>	∧ +1.roles not in {MAP}<br>	∧ ^1.roles not in {DECLARATION}<br>	∧ ^2.roles in {FILE}<br>⇒ y = ␣<br>Confidence: 0.935. Support: 1458.` |
| 22 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {'}<br>	∧ -3.diff_offset ≤ 7<br>	∧ +1.reserved = }<br>	∧ +1.roles not in {MAP}<br>	∧ ^1.roles not in {DECLARATION}<br>	∧ ^2.roles in {FILE}<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.980. Support: 177.` |
| 23 | `  •••start_col ≤ 3<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {'}<br>	∧ -3.diff_offset ≤ 7<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {MAP}<br>	∧ +1.length ≥ 3<br>	∧ ^1.roles not in {DECLARATION}<br>	∧ ^2.roles in {FILE}<br>⇒ y = ⏎⏎<br>Confidence: 0.978. Support: 157.` |
| 24 | `  -1.diff_offset ≥ 2<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -3.label not in {<newline>}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved = =<br>	∧ ^1.roles not in {DECLARATION}<br>	∧ ^2.roles not in {FILE}<br>⇒ y = ␣<br>Confidence: 0.806. Support: 883.` |
| 25 | `  •••start_col ≥ 36<br>	∧ -1.diff_offset ≤ 1<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -2.roles in {LITERAL}<br>	∧ -5.diff_offset ≤ 18<br>	∧ +1.internal_type = JSXIdentifier<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved = =<br>	∧ ^1.roles not in {DECLARATION}<br>	∧ ^2.roles not in {FILE}<br>⇒ y = ␣<br>Confidence: 0.919. Support: 167.` |
| 26 | `  •••start_col ≥ 36<br>	∧ -1.diff_offset ≤ 1<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -2.roles not in {LITERAL}<br>	∧ +1.internal_type = JSXIdentifier<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved = =<br>	∧ ^1.roles not in {DECLARATION}<br>	∧ ^2.roles not in {FILE}<br>⇒ y = ⏎<br>Confidence: 0.809. Support: 275.` |
| 27 | `  •••start_col ≤ 35<br>	∧ -1.diff_offset ≤ 1<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ +1.internal_type = JSXIdentifier<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved = =<br>	∧ ^1.roles not in {DECLARATION}<br>	∧ ^2.roles not in {FILE}<br>⇒ y = ⏎<br>Confidence: 0.811. Support: 828.` |
| 28 | `  -1.diff_offset ≤ 1<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ +1.internal_type not in {JSXIdentifier}<br>	∧ +1.roles in {KEY} and not in {MAP}<br>	∧ +2.reserved = =<br>	∧ ^1.roles not in {DECLARATION}<br>	∧ ^2.roles not in {FILE}<br>⇒ y = ⏎⏎<br>Confidence: 0.996. Support: 131.` |
| 29 | `  -1.diff_offset ≤ 1<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -3.roles in {EXPRESSION}<br>	∧ +1.internal_type not in {JSXIdentifier}<br>	∧ +1.roles not in {KEY, MAP}<br>	∧ +2.reserved = =<br>	∧ ^1.roles not in {DECLARATION}<br>	∧ ^2.roles not in {FILE}<br>⇒ y = ␣<br>Confidence: 0.876. Support: 101.` |
| 30 | `  -1.diff_offset ≤ 1<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -3.roles not in {EXPRESSION}<br>	∧ +1.internal_type not in {JSXIdentifier}<br>	∧ +1.roles not in {KEY, MAP}<br>	∧ +2.reserved = =<br>	∧ ^1.roles not in {DECLARATION}<br>	∧ ^2.roles not in {FILE}<br>⇒ y = ∅<br>Confidence: 0.853. Support: 583.` |
| 31 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label in {<space>}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles in {OPERATOR} and not in {DECLARATION}<br>	∧ ^2.roles not in {FILE}<br>⇒ y = '<br>Confidence: 0.997. Support: 163.` |
| 32 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles in {OPERATOR} and not in {DECLARATION}<br>	∧ ^2.roles not in {FILE}<br>⇒ y = ␣<br>Confidence: 0.912. Support: 1429.` |
| 33 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = :<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR}<br>	∧ ^2.roles not in {FILE}<br>⇒ y = ␣<br>Confidence: 0.963. Support: 1176.` |
| 34 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {:}<br>	∧ -2.internal_type = JSXIdentifier<br>	∧ +1.internal_type = StringLiteral<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR}<br>	∧ ^2.roles not in {FILE}<br>⇒ y = "<br>Confidence: 0.999. Support: 749.` |
| 35 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -2.internal_type not in {JSXIdentifier}<br>	∧ +1.internal_type = StringLiteral<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR}<br>	∧ ^2.roles not in {FILE}<br>⇒ y = '<br>Confidence: 0.906. Support: 515.` |
| 36 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ +2.roles in {COMMENT}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR}<br>	∧ ^2.roles not in {FILE}<br>⇒ y = ⏎⏎<br>Confidence: 0.930. Support: 351.` |
| 37 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles in {CALL} and not in {DECLARATION}<br>	∧ ^2.roles not in {FILE}<br>⇒ y = ␣<br>Confidence: 0.820. Support: 353.` |
| 38 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = )<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles in {STATEMENT} and not in {DECLARATION, OPERATOR}<br>	∧ ^2.roles not in {FILE}<br>⇒ y = ∅<br>Confidence: 0.922. Support: 517.` |
| 39 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles in {STATEMENT} and not in {DECLARATION, OPERATOR}<br>	∧ ^2.roles not in {FILE}<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.831. Support: 257.` |
| 40 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {), }}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles in {STATEMENT} and not in {DECLARATION, OPERATOR}<br>	∧ ^2.roles not in {FILE}<br>⇒ y = ⏎␣⁺␣⁺<br>Confidence: 0.997. Support: 161.` |
| 41 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :, {}<br>	∧ -2.label in {<newline>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {), }}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles in {BLOCK, STATEMENT} and not in {DECLARATION}<br>	∧ ^2.roles not in {FILE}<br>⇒ y = ␣<br>Confidence: 0.997. Support: 158.` |
| 42 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :, {}<br>	∧ -2.label in {<newline>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {), }}<br>	∧ +1.roles not in {MAP}<br>	∧ +1.length ≤ 1<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles in {BLOCK, STATEMENT} and not in {DECLARATION}<br>	∧ ^2.roles not in {FILE}<br>⇒ y = ␣<br>Confidence: 0.935. Support: 100.` |
| 43 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR, STATEMENT}<br>	∧ ^2.roles in {TYPE} and not in {FILE}<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.957. Support: 381.` |
| 44 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {MAP}<br>	∧ +1.length ≤ 1<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles in {VARIABLE} and not in {DECLARATION, STATEMENT}<br>	∧ ^2.roles in {TYPE} and not in {FILE}<br>⇒ y = ␣<br>Confidence: 0.898. Support: 532.` |
| 45 | `  •••start_col ≥ 5<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR, STATEMENT, VARIABLE}<br>	∧ ^2.roles in {TYPE} and not in {FILE}<br>⇒ y = ∅<br>Confidence: 0.887. Support: 315.` |
| 46 | `  •••start_col ≤ 5<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR, STATEMENT, VARIABLE}<br>	∧ ^2.roles in {TYPE} and not in {FILE}<br>⇒ y = ⏎⏎<br>Confidence: 0.997. Support: 163.` |
| 47 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -4.diff_offset ≥ 5<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, STATEMENT}<br>	∧ ^2.internal_type = ExportNamedDeclaration<br>	∧ ^2.roles not in {FILE, TYPE}<br>⇒ y = ␣<br>Confidence: 0.997. Support: 161.` |
| 48 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.roles in {COMMENT}<br>	∧ -4.diff_offset ≥ 5<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR, STATEMENT}<br>	∧ ^2.roles not in {FILE, TYPE}<br>⇒ y = ⏎<br>Confidence: 0.960. Support: 136.` |
| 49 | `  -1.internal_type = CommentLine<br>	∧ -1.reserved not in {,, :}<br>	∧ -4.diff_offset ≥ 5<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR, STATEMENT}<br>	∧ ^2.roles not in {FILE, TYPE}<br>⇒ y = ⏎<br>Confidence: 0.885. Support: 143.` |
| 50 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.roles not in {COMMENT}<br>	∧ -4.diff_offset ≥ 5<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles in {UNANNOTATED} and not in {DECLARATION, OPERATOR, STATEMENT}<br>	∧ ^2.roles not in {FILE, TYPE}<br>⇒ y = ∅<br>Confidence: 0.927. Support: 1709.` |
| 51 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.roles not in {COMMENT}<br>	∧ -4.diff_offset ≥ 5<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.internal_type = JSXElement<br>	∧ ^1.roles not in {DECLARATION, OPERATOR, STATEMENT, UNANNOTATED}<br>	∧ ^2.roles not in {FILE, TYPE}<br>⇒ y = ∅<br>Confidence: 0.879. Support: 186.` |
| 52 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.roles not in {COMMENT}<br>	∧ -4.diff_offset ≥ 5<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ +2.roles in {STRING}<br>	∧ ^1.internal_type not in {JSXElement}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR, STATEMENT, UNANNOTATED}<br>	∧ ^2.roles not in {FILE, TYPE}<br>⇒ y = ∅<br>Confidence: 0.852. Support: 105.` |
| 53 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved = }<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.roles not in {COMMENT}<br>	∧ -3.diff_offset ≤ 8<br>	∧ -4.diff_offset ≥ 5<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=, >}<br>	∧ +2.roles not in {COMMENT}<br>	∧ +2.length ≥ 9<br>	∧ ^1.internal_type not in {JSXOpeningElement}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR, STATEMENT}<br>	∧ ^2.roles not in {FILE, TYPE}<br>⇒ y = ∅<br>Confidence: 0.816. Support: 177.` |
| 54 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved = }<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.roles not in {COMMENT}<br>	∧ -4.diff_offset ≥ 5<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=, >}<br>	∧ +2.roles not in {COMMENT}<br>	∧ +2.length ≤ 8<br>	∧ ^1.internal_type not in {JSXOpeningElement}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR, STATEMENT}<br>	∧ ^2.roles not in {FILE, TYPE}<br>⇒ y = ∅<br>Confidence: 0.972. Support: 834.` |
| 55 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -4.diff_offset ≥ 5<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = {<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.internal_type = File<br>	∧ ^1.roles not in {DECLARATION, STATEMENT}<br>	∧ ^2.roles not in {FILE, TYPE}<br>⇒ y = ␣<br>Confidence: 0.987. Support: 116.` |
| 56 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, }}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.label in {<space>}<br>	∧ -3.length ≥ 6<br>	∧ -4.diff_offset ≥ 5<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {{, }}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.internal_type = File<br>	∧ ^1.roles not in {DECLARATION, STATEMENT}<br>	∧ ^2.roles not in {FILE, TYPE}<br>⇒ y = ␣<br>Confidence: 0.818. Support: 96.` |
| 57 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, }}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.label in {<space>}<br>	∧ -2.roles not in {COMMENT}<br>	∧ -3.length ≤ 5<br>	∧ -4.diff_offset ≥ 5<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {{, }}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ +2.roles not in {COMMENT}<br>	∧ ^1.internal_type = File<br>	∧ ^1.roles not in {DECLARATION, OPERATOR, STATEMENT}<br>	∧ ^2.roles not in {FILE, TYPE}<br>⇒ y = ∅<br>Confidence: 0.867. Support: 124.` |
| 58 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, }}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.label not in {<space>}<br>	∧ -2.roles not in {COMMENT}<br>	∧ -4.diff_offset ≥ 5<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {{, }}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ +2.roles not in {COMMENT}<br>	∧ ^1.internal_type = File<br>	∧ ^1.roles not in {DECLARATION, OPERATOR, STATEMENT}<br>	∧ ^2.roles not in {FILE, TYPE}<br>⇒ y = ∅<br>Confidence: 0.948. Support: 1755.` |
| 59 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, >}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.roles not in {COMMENT}<br>	∧ -4.diff_offset ≥ 5<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = )<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ +2.roles not in {COMMENT}<br>	∧ ^1.internal_type not in {File}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR, STATEMENT}<br>	∧ ^2.roles not in {FILE, TYPE}<br>⇒ y = ∅<br>Confidence: 0.971. Support: 527.` |
| 60 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, }}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.roles not in {COMMENT}<br>	∧ -4.diff_offset ≥ 5<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ +2.roles not in {COMMENT}<br>	∧ ^1.internal_type not in {File}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR, STATEMENT}<br>	∧ ^2.roles not in {FILE, TYPE}<br>⇒ y = ∅<br>Confidence: 0.982. Support: 26659.` |
| 61 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -4.diff_offset ≥ 5<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles not in {MAP}<br>	∧ +1.length = 0<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR, STATEMENT}<br>	∧ ^2.roles not in {FILE, TYPE}<br>⇒ y = ⏎<br>Confidence: 0.931. Support: 167.` |
| 62 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -2.reserved = =<br>	∧ -4.diff_offset ≤ 4<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, STATEMENT}<br>	∧ ^2.roles not in {FILE, TYPE}<br>⇒ y = ␣<br>Confidence: 0.978. Support: 207.` |
| 63 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -1.length ≥ 4<br>	∧ -2.reserved not in {=}<br>	∧ -4.diff_offset ≤ 4<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, STATEMENT}<br>	∧ ^2.roles not in {FILE, TYPE}<br>⇒ y = ␣<br>Confidence: 0.982. Support: 196.` |
| 64 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -1.length ≤ 3<br>	∧ -2.reserved not in {=}<br>	∧ -4.diff_offset ≤ 4<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = =<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, STATEMENT}<br>	∧ ^2.roles not in {FILE, TYPE}<br>⇒ y = ␣<br>Confidence: 0.992. Support: 184.` |
| 65 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ -1.length ≤ 3<br>	∧ -2.reserved not in {=}<br>	∧ -4.diff_offset ≤ 4<br>	∧ +1.internal_type not in {Identifier, StringLiteral}<br>	∧ +1.reserved not in {=}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR, STATEMENT}<br>	∧ ^2.roles not in {FILE, TYPE}<br>⇒ y = ⏎␣⁺␣⁺<br>Confidence: 0.916. Support: 125.` |
| 66 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :, {}<br>	∧ -1.length ≤ 3<br>	∧ -2.reserved not in {=}<br>	∧ -4.diff_offset ≤ 4<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {=}<br>	∧ +5.reserved not in {{}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR, STATEMENT}<br>	∧ ^2.roles not in {FILE, TYPE}<br>⇒ y = ∅<br>Confidence: 0.873. Support: 981.` |

<details>
    <summary>Machine-readable report</summary>
```json
{"javascript": {"avg_rule_len": 10.590909090909092, "max_conf": 0.9997504949569702, "max_support": 26659, "min_conf": 0.8057757616043091, "min_support": 96, "num_rules": 66}}
```
</details>
