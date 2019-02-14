# Model report for file:///tmp/top-repos-quality-repos-iqo6lp_m/storybook HEAD b28217f887af533a17cb1498887d6b4bd41bd643

### Dump

```json
{'created_at': datetime.datetime(2019, 2, 13, 8, 4, 43, 638530),
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
 'uuid': '4206bb73-ebbc-4234-adb9-0a3a6b14ede3',
 'version': [1]}
style.format.analyzer.FormatAnalyzer/[1] file:///tmp/top-repos-quality-repos-iqo6lp_m/storybook b28217f887af533a17cb1498887d6b4bd41bd643

# javascript
81 rules, avg.len. 10.2
## train
PPCR: 0.934690
### report
macro
{'f1-score': 0.81341894311845,
 'precision': 0.8487364519398577,
 'recall': 0.7873836053049393,
 'support': 145391}
micro
{'f1-score': 0.96218472945368,
 'precision': 0.96218472945368,
 'recall': 0.96218472945368,
 'support': 145391}
weighted
{'f1-score': 0.9605063923083152,
 'precision': 0.9613280107916754,
 'recall': 0.96218472945368,
 'support': 145391}
### report_full
macro
{'f1-score': 0.745989191313255,
 'precision': 0.8487364519398577,
 'recall': 0.6855450557992049,
 'support': 155550}
micro
{'f1-score': 0.9297038289897356,
 'precision': 0.96218472945368,
 'recall': 0.899344262295082,
 'support': 155550}
weighted
{'f1-score': 0.9220403681872004,
 'precision': 0.9592937591421362,
 'recall': 0.899344262295082,
 'support': 155550}
## test
PPCR: 0.934567
### report
macro
{'f1-score': 0.8013956716646514,
 'precision': 0.8417946104835219,
 'recall': 0.7732711652162993,
 'support': 36421}
micro
{'f1-score': 0.9565086076713983,
 'precision': 0.9565086076713983,
 'recall': 0.9565086076713983,
 'support': 36421}
weighted
{'f1-score': 0.9542776934543367,
 'precision': 0.9554145281941953,
 'recall': 0.9565086076713983,
 'support': 36421}
### report_full
macro
{'f1-score': 0.736278936083671,
 'precision': 0.8417946104835219,
 'recall': 0.6768231309014605,
 'support': 38971}
micro
{'f1-score': 0.9241564091680814,
 'precision': 0.9565086076713983,
 'recall': 0.8939211208334402,
 'support': 38971}
weighted
{'f1-score': 0.9155134112790402,
 'precision': 0.9526689813184609,
 'recall': 0.8939211208334402,
 'support': 38971}
```

## javascript
### Summary
81 rules, avg.len. 10.2

| | |
|-|-|
|Min support|94|
|Max support|22794|
|Min confidence|0.8143631219863892|
|Max confidence|0.9996921420097351|

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
| 1 | `  -1.internal_type = StringLiteral<br>	∧ -3.internal_type = JSXIdentifier<br>⇒ y = "<br>Confidence: 0.995. Support: 299.` |
| 2 | `  -1.internal_type = StringLiteral<br>	∧ -3.internal_type not in {JSXIdentifier}<br>⇒ y = '<br>Confidence: 0.997. Support: 6055.` |
| 3 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label in {<space>}<br>	∧ +1.internal_type = StringLiteral<br>⇒ y = '<br>Confidence: 0.999. Support: 3707.` |
| 4 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ +1.internal_type = StringLiteral<br>⇒ y = '<br>Confidence: 0.964. Support: 1796.` |
| 5 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(}<br>	∧ -2.internal_type = JSXIdentifier<br>	∧ -4.length ≥ 2<br>	∧ +1.internal_type = StringLiteral<br>⇒ y = "<br>Confidence: 0.998. Support: 222.` |
| 6 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved = ,<br>	∧ -2.internal_type not in {JSXIdentifier}<br>	∧ -4.length ≥ 2<br>	∧ +1.internal_type = StringLiteral<br>⇒ y = ␣<br>Confidence: 0.968. Support: 110.` |
| 7 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(, ,}<br>	∧ -4.length ≥ 2<br>	∧ +1.internal_type = StringLiteral<br>⇒ y = '<br>Confidence: 0.828. Support: 521.` |
| 8 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label in {<newline>}<br>	∧ -1.reserved not in {(}<br>	∧ -4.length ≤ 1<br>	∧ +1.internal_type = StringLiteral<br>⇒ y = '<br>Confidence: 0.983. Support: 146.` |
| 9 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(}<br>	∧ -4.length ≤ 1<br>	∧ +1.internal_type = StringLiteral<br>	∧ ^1.roles in {UNANNOTATED}<br>⇒ y = "<br>Confidence: 0.864. Support: 99.` |
| 10 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved = ,<br>	∧ -4.length ≤ 1<br>	∧ -5.label in {<newline>}<br>	∧ +1.internal_type = StringLiteral<br>	∧ ^1.roles not in {UNANNOTATED}<br>⇒ y = ⏎<br>Confidence: 0.988. Support: 121.` |
| 11 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved = ,<br>	∧ -4.label in {'}<br>	∧ -4.length ≤ 1<br>	∧ -5.label not in {<newline>}<br>	∧ +1.internal_type = StringLiteral<br>	∧ ^1.roles not in {UNANNOTATED}<br>⇒ y = ␣<br>Confidence: 0.930. Support: 277.` |
| 12 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ,}<br>	∧ -4.length ≤ 1<br>	∧ +1.internal_type = StringLiteral<br>	∧ ^1.roles not in {UNANNOTATED}<br>⇒ y = ␣<br>Confidence: 0.977. Support: 3318.` |
| 13 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.987. Support: 1671.` |
| 14 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = import<br>⇒ y = ⏎<br>Confidence: 0.865. Support: 967.` |
| 15 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {import, }}<br>	∧ +1.length ≥ 2<br>	∧ +3.roles in {STRING}<br>	∧ ^1.roles in {STATEMENT}<br>⇒ y = ⏎⏎<br>Confidence: 0.935. Support: 314.` |
| 16 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ -3.roles in {IMPORT}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {import, }}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {STATEMENT}<br>⇒ y = ⏎⏎<br>Confidence: 0.988. Support: 447.` |
| 17 | `  •••start_col ≤ 11<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ -3.roles not in {IMPORT}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {STATEMENT}<br>⇒ y = ⏎⏎<br>Confidence: 0.899. Support: 512.` |
| 18 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {import, }}<br>	∧ +1.length ≤ 1<br>⇒ y = ⏎<br>Confidence: 0.903. Support: 539.` |
| 19 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles in {VALUE}<br>	∧ ^1.roles in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.857. Support: 297.` |
| 20 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles not in {VALUE}<br>	∧ ^1.roles in {DECLARATION, FUNCTION}<br>⇒ y = ⏎␣⁺␣⁺<br>Confidence: 0.966. Support: 865.` |
| 21 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = )<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles in {DECLARATION, FUNCTION}<br>⇒ y = ␣<br>Confidence: 0.999. Support: 787.` |
| 22 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ><br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles in {DECLARATION, FUNCTION}<br>⇒ y = ␣<br>Confidence: 0.926. Support: 605.` |
| 23 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {), ;, >, {}<br>	∧ -3.reserved = {<br>	∧ -5.diff_offset ≤ 15<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles in {DECLARATION, FUNCTION}<br>⇒ y = ␣<br>Confidence: 0.981. Support: 608.` |
| 24 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {), ;, >, {}<br>	∧ -3.reserved not in {{}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = =<br>	∧ ^1.roles in {DECLARATION, FUNCTION}<br>⇒ y = ␣<br>Confidence: 0.999. Support: 371.` |
| 25 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=}<br>	∧ ^1.roles in {DECLARATION, FUNCTION}<br>⇒ y = ␣<br>Confidence: 0.963. Support: 260.` |
| 26 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {), ,, ;, >, {}<br>	∧ -3.reserved not in {{}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ ^1.roles in {DECLARATION, FUNCTION}<br>⇒ y = ␣<br>Confidence: 0.996. Support: 136.` |
| 27 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {), ,, ;, >, {}<br>	∧ -3.reserved not in {{}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, }}<br>	∧ ^1.roles in {DECLARATION, FUNCTION}<br>⇒ y = ∅<br>Confidence: 0.965. Support: 2936.` |
| 28 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {;, {}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = ,<br>	∧ ^1.roles in {DECLARATION} and not in {FUNCTION}<br>⇒ y = ∅<br>Confidence: 0.999. Support: 408.` |
| 29 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {;, {}<br>	∧ -3.diff_col ≥ 5<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {,}<br>	∧ ^1.roles in {DECLARATION} and not in {FUNCTION}<br>⇒ y = ␣<br>Confidence: 0.978. Support: 6320.` |
| 30 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {;, {}<br>	∧ -3.diff_col ≤ 4<br>	∧ -3.reserved = =<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {,}<br>	∧ ^1.roles in {DECLARATION} and not in {FUNCTION}<br>⇒ y = ∅<br>Confidence: 0.893. Support: 211.` |
| 31 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {;, {}<br>	∧ -2.diff_offset ≤ 4<br>	∧ -3.diff_col ≤ 4<br>	∧ -3.reserved not in {=}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {,}<br>	∧ ^1.roles in {DECLARATION} and not in {FUNCTION}<br>⇒ y = ␣<br>Confidence: 0.822. Support: 582.` |
| 32 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.989. Support: 1303.` |
| 33 | `  •••start_col ≥ 33<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ -2.roles in {EXPRESSION}<br>	∧ -5.diff_offset ≤ 15<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ ^1.roles in {LITERAL} and not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.829. Support: 126.` |
| 34 | `  •••start_col ≤ 32<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ ^1.roles in {LITERAL} and not in {DECLARATION}<br>⇒ y = ⏎<br>Confidence: 0.897. Support: 1892.` |
| 35 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ -5.diff_line ≥ 1<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.length ≥ 4<br>	∧ ^1.roles not in {DECLARATION, LITERAL}<br>⇒ y = ⏎<br>Confidence: 0.937. Support: 166.` |
| 36 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ -5.diff_line = 0<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +2.length ≤ 14<br>	∧ ^1.roles not in {DECLARATION, LITERAL}<br>⇒ y = ␣<br>Confidence: 0.943. Support: 2096.` |
| 37 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = :<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.988. Support: 2865.` |
| 38 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles in {OPERATOR} and not in {DECLARATION}<br>⇒ y = ⏎␣⁺␣⁺<br>Confidence: 0.920. Support: 220.` |
| 39 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, {}<br>	∧ -4.diff_offset ≥ 6<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles in {OPERATOR} and not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.922. Support: 2542.` |
| 40 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = const<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 1.000. Support: 1624.` |
| 41 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles in {UNANNOTATED} and not in {DECLARATION, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.924. Support: 961.` |
| 42 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +2.reserved = }<br>	∧ ^1.roles not in {DECLARATION, UNANNOTATED}<br>⇒ y = ␣<br>Confidence: 0.935. Support: 544.` |
| 43 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ -3.diff_col ≤ 6<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles in {MAP}<br>	∧ +2.reserved not in {}}<br>	∧ +4.reserved = ,<br>	∧ ^1.roles not in {DECLARATION, OPERATOR, UNANNOTATED}<br>⇒ y = ⏎␣⁺␣⁺<br>Confidence: 0.814. Support: 369.` |
| 44 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ -3.diff_col ≤ 6<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles in {MAP}<br>	∧ +2.reserved not in {}}<br>	∧ +3.roles in {VALUE}<br>	∧ ^1.roles not in {DECLARATION, UNANNOTATED}<br>⇒ y = ␣<br>Confidence: 0.972. Support: 123.` |
| 45 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ -3.diff_col ≤ 6<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {}}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR, UNANNOTATED}<br>⇒ y = ⏎␣⁺␣⁺<br>Confidence: 0.958. Support: 1117.` |
| 46 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = import<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 1.000. Support: 1305.` |
| 47 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, ;, import, {}<br>	∧ -2.reserved = =<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.979. Support: 882.` |
| 48 | `  -1.internal_type = CommentLine<br>	∧ -1.reserved not in {,, :, ;, const, import, {}<br>	∧ -2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR}<br>⇒ y = ⏎<br>Confidence: 0.883. Support: 533.` |
| 49 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, const, import, {}<br>	∧ -2.reserved not in {=}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +2.reserved = ><br>	∧ ^1.internal_type = JSXElement<br>	∧ ^1.roles not in {DECLARATION, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.999. Support: 925.` |
| 50 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, const, import, {}<br>	∧ -2.reserved not in {=}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ +2.reserved = ><br>	∧ ^1.roles not in {DECLARATION, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.921. Support: 95.` |
| 51 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, ;, {}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≤ 1<br>	∧ +2.reserved = ><br>	∧ ^1.internal_type not in {JSXElement}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.957. Support: 1093.` |
| 52 | `  -1.internal_type = JSXIdentifier<br>	∧ -1.reserved not in {,, ;, {}<br>	∧ +1.internal_type = JSXIdentifier<br>	∧ +1.length ≤ 9<br>	∧ ^1.internal_type = JSXOpeningElement<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.892. Support: 429.` |
| 53 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, const, import, {}<br>	∧ -2.reserved not in {=}<br>	∧ +1.internal_type not in {JSXIdentifier, StringLiteral}<br>	∧ +2.reserved not in {>}<br>	∧ ^1.internal_type = JSXOpeningElement<br>	∧ ^1.roles not in {DECLARATION, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.904. Support: 476.` |
| 54 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved = return<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.991. Support: 476.` |
| 55 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved = export<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.999. Support: 453.` |
| 56 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, {}<br>	∧ -2.label in {<-space>}<br>	∧ -2.reserved not in {=}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles in {NAME}<br>	∧ +2.reserved not in {>}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR}<br>⇒ y = ⏎⏎<br>Confidence: 0.996. Support: 135.` |
| 57 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, ;, {}<br>	∧ -2.label not in {<-space>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles in {NAME}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.999. Support: 345.` |
| 58 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, export, {}<br>	∧ -2.label in {<newline>}<br>	∧ -2.reserved not in {=}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ +2.reserved not in {>}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR}<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.928. Support: 214.` |
| 59 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, ;, {}<br>	∧ -2.label in {<space>} and not in {<newline>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.882. Support: 387.` |
| 60 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, ;, {}<br>	∧ -2.label not in {<newline>, <space>}<br>	∧ -5.reserved = :<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.922. Support: 198.` |
| 61 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, const, import, {}<br>	∧ -2.label not in {<newline>, <space>}<br>	∧ -2.reserved not in {=}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ +2.reserved not in {>}<br>	∧ ^1.internal_type not in {JSXOpeningElement}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.848. Support: 741.` |
| 62 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, ;, {}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = {<br>	∧ ^1.roles in {IF} and not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.965. Support: 353.` |
| 63 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, ;, {}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {{, }}<br>	∧ +2.roles in {EXPRESSION}<br>	∧ ^1.internal_type = ConditionalExpression<br>	∧ ^1.roles in {IF} and not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.879. Support: 252.` |
| 64 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, const, export, import, {}<br>	∧ -2.label not in {<newline>}<br>	∧ -2.reserved not in {=}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {{, }}<br>	∧ +2.reserved not in {>}<br>	∧ ^1.internal_type not in {ConditionalExpression, JSXOpeningElement}<br>	∧ ^1.roles in {IF} and not in {DECLARATION, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.923. Support: 1325.` |
| 65 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved = if<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ ^1.roles not in {DECLARATION, IF}<br>⇒ y = ␣<br>Confidence: 0.994. Support: 263.` |
| 66 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, ;, {}<br>	∧ -3.reserved = export<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ ^1.roles not in {DECLARATION, IF}<br>⇒ y = ␣<br>Confidence: 0.998. Support: 236.` |
| 67 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, {}<br>	∧ -2.diff_offset ≤ 4<br>	∧ -2.label in {<-space>}<br>	∧ -2.reserved not in {=}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.length ≥ 2<br>	∧ +2.reserved not in {>}<br>	∧ ^1.roles not in {DECLARATION, IF, OPERATOR, VARIABLE}<br>⇒ y = ⏎⏎<br>Confidence: 0.891. Support: 426.` |
| 68 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, const, import, {}<br>	∧ -2.label in {<-space>}<br>	∧ -2.reserved not in {=}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.length ≤ 1<br>	∧ +2.reserved not in {>}<br>	∧ ^1.internal_type not in {JSXOpeningElement}<br>	∧ ^1.roles not in {DECLARATION, IF, OPERATOR, VARIABLE}<br>⇒ y = ∅<br>Confidence: 0.981. Support: 2872.` |
| 69 | `  •••start_col ≤ 42<br>	∧ -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved = ><br>	∧ -2.label not in {<-space>}<br>	∧ -2.reserved not in {=}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = )<br>	∧ +2.reserved not in {>}<br>	∧ ^1.roles not in {DECLARATION, IF, OPERATOR, VARIABLE}<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.851. Support: 198.` |
| 70 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved = ><br>	∧ -2.label not in {<-space>}<br>	∧ -2.reserved not in {=}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {), }}<br>	∧ +2.reserved not in {>}<br>	∧ ^1.internal_type not in {JSXOpeningElement}<br>	∧ ^1.roles not in {DECLARATION, IF, OPERATOR, VARIABLE}<br>⇒ y = ∅<br>Confidence: 1.000. Support: 1010.` |
| 71 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, >, const, import, {}<br>	∧ -1.roles in {EXPRESSION}<br>	∧ -2.label not in {<-space>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {>}<br>	∧ ^1.internal_type not in {JSXOpeningElement}<br>	∧ ^1.roles not in {DECLARATION, IF, OPERATOR, VARIABLE}<br>⇒ y = ∅<br>Confidence: 0.993. Support: 21511.` |
| 72 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, >, {}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -2.label not in {<-space>}<br>	∧ -2.reserved not in {=}<br>	∧ -4.diff_offset ≤ 8<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = .<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {>}<br>	∧ +5.reserved = ,<br>	∧ ^1.roles not in {DECLARATION, IF, OPERATOR, VARIABLE}<br>⇒ y = ⏎<br>Confidence: 0.854. Support: 99.` |
| 73 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, >, const, import, {}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -2.label not in {<-space>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = .<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {>}<br>	∧ +5.reserved not in {,}<br>	∧ ^1.internal_type not in {JSXOpeningElement}<br>	∧ ^1.roles not in {DECLARATION, IF, OPERATOR, VARIABLE}<br>⇒ y = ∅<br>Confidence: 0.864. Support: 921.` |
| 74 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, >, const, import, {}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -2.label not in {<-space>}<br>	∧ -3.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {MAP}<br>	∧ +1.length ≥ 17<br>	∧ +2.reserved not in {>}<br>	∧ ^1.internal_type not in {JSXOpeningElement}<br>	∧ ^1.roles not in {DECLARATION, IF, OPERATOR, VARIABLE}<br>⇒ y = ∅<br>Confidence: 0.983. Support: 146.` |
| 75 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, ;, return, {}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -2.label not in {<-space>}<br>	∧ -3.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {., }}<br>	∧ +1.roles not in {MAP}<br>	∧ +1.length ≤ 16<br>	∧ ^1.roles not in {DECLARATION, IF}<br>⇒ y = ␣<br>Confidence: 0.910. Support: 94.` |
| 76 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, >, const, import, {}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -2.label not in {<-space>}<br>	∧ -3.reserved not in {;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles in {COMMENT} and not in {MAP}<br>	∧ +2.reserved not in {>}<br>	∧ ^1.internal_type not in {JSXOpeningElement}<br>	∧ ^1.roles in {FILE} and not in {DECLARATION, IF, OPERATOR, VARIABLE}<br>⇒ y = ∅<br>Confidence: 0.996. Support: 412.` |
| 77 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, >, const, import, {}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -2.label not in {<-space>}<br>	∧ -3.reserved not in {;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = ;<br>	∧ +1.roles not in {MAP}<br>	∧ +2.reserved not in {>}<br>	∧ ^1.roles in {FILE} and not in {DECLARATION, IF, OPERATOR, VARIABLE}<br>⇒ y = ∅<br>Confidence: 0.996. Support: 113.` |
| 78 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, >, const, import, return, {}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -2.label not in {<-space>}<br>	∧ -3.reserved not in {:, ;}<br>	∧ -4.label in {<space>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {CALLEE, MAP}<br>	∧ +2.reserved not in {>}<br>	∧ ^1.internal_type not in {JSXOpeningElement}<br>	∧ ^1.roles not in {DECLARATION, IF, OPERATOR, VARIABLE}<br>	∧ ^2.roles not in {BLOCK}<br>⇒ y = ∅<br>Confidence: 0.895. Support: 1336.` |
| 79 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, >, const, import, return, {}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -2.label not in {<-space>}<br>	∧ -3.reserved not in {:, ;}<br>	∧ -4.label not in {<space>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = <<br>	∧ +1.roles not in {CALLEE, MAP}<br>	∧ +2.reserved not in {>}<br>	∧ ^1.internal_type = JSXElement<br>	∧ ^1.roles not in {DECLARATION, IF, OPERATOR, VARIABLE}<br>	∧ ^2.roles not in {BLOCK}<br>⇒ y = ∅<br>Confidence: 0.999. Support: 837.` |
| 80 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, >, const, import, return, {}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -2.label not in {<-space>}<br>	∧ -3.reserved not in {:, ;}<br>	∧ -4.label not in {<space>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {CALLEE, MAP}<br>	∧ +2.reserved not in {>}<br>	∧ ^1.internal_type not in {JSXOpeningElement}<br>	∧ ^1.roles not in {DECLARATION, IF, OPERATOR, VARIABLE}<br>	∧ ^2.roles not in {BLOCK}<br>⇒ y = ∅<br>Confidence: 0.984. Support: 22794.` |
| 81 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, {}<br>	∧ -2.reserved not in {=}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.length = 0<br>	∧ +2.reserved not in {>}<br>	∧ ^1.roles not in {DECLARATION, IF, OPERATOR, VARIABLE}<br>⇒ y = ⏎<br>Confidence: 0.964. Support: 98.` |

<details>
    <summary>Machine-readable report</summary>
```json
{"javascript": {"avg_rule_len": 10.234567901234568, "max_conf": 0.9996921420097351, "max_support": 22794, "min_conf": 0.8143631219863892, "min_support": 94, "num_rules": 81}}
```
</details>
