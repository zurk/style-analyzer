# Model report for file:///tmp/top-repos-quality-repos-i7sl73u3/atom HEAD 108b23210759a8c5b2f51ac99659be5dc31a7371

### Dump

```json
{'created_at': datetime.datetime(2019, 2, 13, 8, 26, 31, 74767),
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
 'uuid': 'a9d3d3d1-30e8-40fb-adba-991dff5a8e42',
 'version': [1]}
style.format.analyzer.FormatAnalyzer/[1] file:///tmp/top-repos-quality-repos-i7sl73u3/atom 108b23210759a8c5b2f51ac99659be5dc31a7371

# javascript
87 rules, avg.len. 9.7
## train
PPCR: 0.976672
### report
macro
{'f1-score': 0.7319736143697753,
 'precision': 0.7527966585880623,
 'recall': 0.7163695496085275,
 'support': 491983}
micro
{'f1-score': 0.9798163757690814,
 'precision': 0.9798163757690814,
 'recall': 0.9798163757690814,
 'support': 491983}
weighted
{'f1-score': 0.9785179724125145,
 'precision': 0.9778056060973562,
 'recall': 0.9798163757690814,
 'support': 491983}
### report_full
macro
{'f1-score': 0.7035946564745841,
 'precision': 0.7527966585880623,
 'recall': 0.6719040767768543,
 'support': 503734}
micro
{'f1-score': 0.9682530277177149,
 'precision': 0.9798163757690814,
 'recall': 0.9569594269991702,
 'support': 503734}
weighted
{'f1-score': 0.9658141153634934,
 'precision': 0.9774244987819124,
 'recall': 0.9569594269991702,
 'support': 503734}
## test
PPCR: 0.967604
### report
macro
{'f1-score': 0.7152439440702101,
 'precision': 0.7308659535531228,
 'recall': 0.7043112657784939,
 'support': 118276}
micro
{'f1-score': 0.9657834218269133,
 'precision': 0.9657834218269133,
 'recall': 0.9657834218269133,
 'support': 118276}
weighted
{'f1-score': 0.9635311192429606,
 'precision': 0.962186059099845,
 'recall': 0.9657834218269133,
 'support': 118276}
### report_full
macro
{'f1-score': 0.6824299522073655,
 'precision': 0.7308659535531228,
 'recall': 0.650920409695101,
 'support': 122236}
micro
{'f1-score': 0.9498819185737094,
 'precision': 0.9657834218269133,
 'recall': 0.9344955659543833,
 'support': 122236}
weighted
{'f1-score': 0.9457246415416063,
 'precision': 0.9614715949762503,
 'recall': 0.9344955659543833,
 'support': 122236}
```

## javascript
### Summary
87 rules, avg.len. 9.7

| | |
|-|-|
|Min support|91|
|Max support|65414|
|Min confidence|0.807692289352417|
|Max confidence|0.9998457431793213|

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
                     'min_samples_leaf': 91,
                     'min_samples_split': 239,
                     'n_estimators': 10,
                     'prune_attributes': True,
                     'prune_branches_algorithms': ['reduced-error'],
                     'prune_dataset_ratio': 0.2,
                     'top_down_greedy_budget': [False, 0.5]}}
```

### Rules

| rule number | description |
|----:|:-----|
| 1 | `  -1.reserved = ,<br>	∧ ^1.roles in {BINARY, LIST}<br>⇒ y = ⏎<br>Confidence: 1.000. Support: 37474.` |
| 2 | `  •••start_col ≥ 70<br>	∧ -1.reserved = ,<br>	∧ ^1.roles in {LIST} and not in {BINARY}<br>	∧ ^2.roles in {ASSIGNMENT}<br>⇒ y = ⏎<br>Confidence: 0.884. Support: 735.` |
| 3 | `  •••start_col ≥ 70<br>	∧ -1.reserved = ,<br>	∧ ^1.roles in {LIST} and not in {BINARY}<br>	∧ ^2.roles not in {ASSIGNMENT}<br>⇒ y = ␣<br>Confidence: 0.918. Support: 577.` |
| 4 | `  •••start_col ≤ 69<br>	∧ -1.reserved = ,<br>	∧ -2.reserved = }<br>	∧ ^1.roles in {LIST} and not in {BINARY}<br>⇒ y = ⏎<br>Confidence: 0.916. Support: 231.` |
| 5 | `  •••start_col ≤ 69<br>	∧ -1.reserved = ,<br>	∧ -2.reserved not in {}}<br>	∧ -4.roles not in {LITERAL}<br>	∧ +1.length ≥ 13<br>	∧ ^1.roles in {LIST} and not in {BINARY}<br>	∧ ^2.roles not in {DECLARATION}<br>⇒ y = ⏎<br>Confidence: 0.810. Support: 92.` |
| 6 | `  •••start_col ≤ 63<br>	∧ -1.reserved = ,<br>	∧ -2.reserved not in {}}<br>	∧ -4.roles not in {LITERAL}<br>	∧ +1.length ≥ 13<br>	∧ ^1.roles in {LIST} and not in {BINARY}<br>	∧ ^2.roles not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.895. Support: 700.` |
| 7 | `  •••start_col ≤ 69<br>	∧ -1.reserved = ,<br>	∧ -2.reserved not in {}}<br>	∧ -4.roles not in {LITERAL}<br>	∧ +1.length ≤ 12<br>	∧ ^1.roles in {LIST} and not in {BINARY}<br>	∧ ^2.roles not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.984. Support: 5282.` |
| 8 | `  -1.reserved not in {,}<br>	∧ ^1.roles in {LIST}<br>	∧ ^2.roles in {BINARY}<br>⇒ y = '<br>Confidence: 0.999. Support: 18235.` |
| 9 | `  -1.internal_type = StringLiteral<br>	∧ -1.reserved not in {,}<br>	∧ ^1.roles in {LIST}<br>	∧ ^2.roles not in {BINARY}<br>⇒ y = '<br>Confidence: 0.999. Support: 724.` |
| 10 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,}<br>	∧ +1.internal_type = StringLiteral<br>	∧ ^1.roles in {LIST}<br>	∧ ^2.roles not in {BINARY}<br>⇒ y = '<br>Confidence: 0.992. Support: 448.` |
| 11 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,}<br>	∧ -5.label in {<-space>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles in {LIST}<br>	∧ ^2.roles not in {BINARY}<br>⇒ y = ⏎␣⁺␣⁺<br>Confidence: 0.976. Support: 105.` |
| 12 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,}<br>	∧ -2.length ≥ 3<br>	∧ -5.label not in {<-space>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ ^1.roles in {LIST}<br>	∧ ^2.roles not in {BINARY}<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.984. Support: 92.` |
| 13 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,}<br>	∧ -2.length ≤ 3<br>	∧ -5.label not in {<-space>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ ^1.roles in {LIST}<br>	∧ ^2.roles not in {BINARY}<br>⇒ y = ∅<br>Confidence: 0.943. Support: 220.` |
| 14 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,}<br>	∧ -5.label not in {<-space>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ ^1.roles in {LIST}<br>	∧ ^2.roles not in {BINARY}<br>⇒ y = ∅<br>Confidence: 0.988. Support: 5040.` |
| 15 | `  -1.internal_type = StringLiteral<br>	∧ ^1.roles in {IDENTIFIER} and not in {LIST}<br>⇒ y = '<br>Confidence: 0.989. Support: 701.` |
| 16 | `  -1.internal_type not in {StringLiteral}<br>	∧ ^1.roles in {IDENTIFIER} and not in {LIST}<br>⇒ y = ∅<br>Confidence: 0.997. Support: 65414.` |
| 17 | `  -1.internal_type = StringLiteral<br>	∧ ^1.roles not in {IDENTIFIER, LIST}<br>⇒ y = '<br>Confidence: 0.960. Support: 9344.` |
| 18 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ +1.roles in {STRING}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER, LIST}<br>⇒ y = '<br>Confidence: 0.957. Support: 5835.` |
| 19 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ +1.roles not in {STRING}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER, LIST}<br>⇒ y = ∅<br>Confidence: 0.992. Support: 13050.` |
| 20 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ +1.roles in {MAP}<br>	∧ +1.length ≥ 2<br>	∧ +4.reserved = }<br>	∧ ^1.internal_type not in {ObjectProperty}<br>	∧ ^1.roles not in {IDENTIFIER, LIST}<br>⇒ y = ∅<br>Confidence: 0.964. Support: 480.` |
| 21 | `  •••start_col ≤ 66<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ -4.diff_col ≥ 18<br>	∧ -4.label not in {<space>}<br>	∧ +1.roles in {MAP}<br>	∧ +1.length ≥ 2<br>	∧ +3.length ≥ 4<br>	∧ +4.reserved not in {}}<br>	∧ ^1.internal_type not in {ObjectProperty}<br>	∧ ^1.roles not in {LIST}<br>⇒ y = ∅<br>Confidence: 0.849. Support: 96.` |
| 22 | `  •••start_col ≤ 66<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ -4.label not in {<space>}<br>	∧ +1.roles in {MAP}<br>	∧ +1.length ≥ 2<br>	∧ +3.length ≤ 3<br>	∧ +4.reserved not in {}}<br>	∧ ^1.internal_type not in {ObjectProperty}<br>	∧ ^1.roles not in {LIST}<br>⇒ y = ∅<br>Confidence: 0.893. Support: 425.` |
| 23 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ +1.roles not in {MAP}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER, LIST}<br>⇒ y = ⏎␣⁺␣⁺<br>Confidence: 0.959. Support: 6743.` |
| 24 | `  •••start_col ≥ 14<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = )<br>	∧ +1.length ≥ 2<br>	∧ +5.length ≥ 4<br>	∧ ^1.roles in {BLOCK} and not in {IDENTIFIER, LIST}<br>⇒ y = ⏎<br>Confidence: 0.860. Support: 4850.` |
| 25 | `  •••start_col ≥ 14<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = )<br>	∧ +1.length ≥ 2<br>	∧ +5.length ≤ 3<br>	∧ ^1.roles in {BLOCK} and not in {IDENTIFIER, LIST}<br>	∧ ^2.roles not in {CALL}<br>⇒ y = ⏎<br>Confidence: 0.856. Support: 1083.` |
| 26 | `  •••start_col ≥ 14<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = )<br>	∧ +1.reserved = const<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type = Program<br>	∧ ^1.roles not in {BLOCK, IDENTIFIER, LIST}<br>⇒ y = ⏎<br>Confidence: 0.863. Support: 435.` |
| 27 | `  •••start_col ≥ 14<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = )<br>	∧ +1.reserved not in {const}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type = Program<br>	∧ ^1.roles not in {BLOCK, IDENTIFIER, LIST}<br>⇒ y = ⏎⏎<br>Confidence: 0.815. Support: 116.` |
| 28 | `  •••start_col ≥ 14<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = )<br>	∧ +1.length ≥ 2<br>	∧ +2.roles not in {COMMENT}<br>	∧ ^1.roles not in {BLOCK, IDENTIFIER, LIST}<br>⇒ y = ␣<br>Confidence: 0.944. Support: 796.` |
| 29 | `  •••start_col ≤ 13<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = )<br>	∧ +1.length ≥ 2<br>	∧ +3.internal_type not in {Identifier}<br>	∧ ^1.roles not in {IDENTIFIER, LIST}<br>⇒ y = ⏎⏎<br>Confidence: 0.973. Support: 1426.` |
| 30 | `  -1.internal_type = CommentLine<br>	∧ -1.reserved not in {(, ), {}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type = File<br>	∧ ^1.roles not in {IDENTIFIER, LIST}<br>⇒ y = ⏎<br>Confidence: 0.985. Support: 3852.` |
| 31 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {(, ), {}<br>	∧ +1.roles in {COMMENT}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type = File<br>	∧ ^1.roles not in {LIST}<br>⇒ y = ∅<br>Confidence: 1.000. Support: 3241.` |
| 32 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {(, ), {}<br>	∧ +1.length ≥ 2<br>	∧ +2.length ≥ 21<br>	∧ ^1.internal_type = File<br>	∧ ^1.roles not in {IDENTIFIER, LIST}<br>⇒ y = ⏎⏎<br>Confidence: 0.938. Support: 684.` |
| 33 | `  -1.diff_col ≤ 8<br>	∧ -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {(, ), {}<br>	∧ +1.length ≥ 2<br>	∧ +2.length ≤ 20<br>	∧ ^1.internal_type = File<br>	∧ ^1.roles not in {IDENTIFIER, LIST}<br>⇒ y = ␣<br>Confidence: 0.817. Support: 238.` |
| 34 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label in {<space>}<br>	∧ -1.reserved not in {(, ), {}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {File}<br>	∧ ^1.roles not in {IDENTIFIER, LIST}<br>⇒ y = '<br>Confidence: 0.986. Support: 3140.` |
| 35 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved = }<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type = IfStatement<br>	∧ ^1.roles not in {IDENTIFIER, LIST}<br>⇒ y = ␣<br>Confidence: 0.999. Support: 433.` |
| 36 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved = }<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {File, IfStatement}<br>	∧ ^1.roles in {LITERAL} and not in {IDENTIFIER, LIST}<br>⇒ y = ∅<br>Confidence: 0.998. Support: 259.` |
| 37 | `  •••start_col ≤ 5<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved = }<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {File, IfStatement}<br>	∧ ^1.roles not in {IDENTIFIER, LIST, LITERAL}<br>⇒ y = ⏎⏎<br>Confidence: 0.967. Support: 1184.` |
| 38 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ), {, }}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {File}<br>	∧ ^1.roles in {INCOMPLETE, LITERAL} and not in {IDENTIFIER, LIST}<br>⇒ y = ∅<br>Confidence: 0.996. Support: 844.` |
| 39 | `  •••start_col ≥ 52<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ), {, }}<br>	∧ -2.roles in {MAP}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {File}<br>	∧ ^1.roles in {LITERAL} and not in {IDENTIFIER, INCOMPLETE, LIST}<br>⇒ y = ␣<br>Confidence: 0.994. Support: 240.` |
| 40 | `  •••start_col ≥ 52<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ), {, }}<br>	∧ -2.roles not in {MAP}<br>	∧ +1.length ≥ 10<br>	∧ ^1.internal_type not in {File}<br>	∧ ^1.roles in {LITERAL} and not in {IDENTIFIER, INCOMPLETE, LIST}<br>⇒ y = ⏎<br>Confidence: 0.830. Support: 91.` |
| 41 | `  •••start_col ≤ 51<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ), {, }}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {File}<br>	∧ ^1.roles in {LITERAL} and not in {IDENTIFIER, INCOMPLETE, LIST}<br>	∧ ^2.roles in {LITERAL} and not in {MAP}<br>⇒ y = ␣<br>Confidence: 0.810. Support: 297.` |
| 42 | `  •••start_col ≤ 51<br>	∧ -1.diff_offset ≥ 2<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(, ), {, }}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {File}<br>	∧ ^1.roles in {LITERAL} and not in {IDENTIFIER, LIST}<br>	∧ ^2.roles not in {LITERAL}<br>⇒ y = '<br>Confidence: 0.808. Support: 91.` |
| 43 | `  •••start_col ≤ 51<br>	∧ -1.diff_offset ≤ 2<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ), {, }}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {File}<br>	∧ ^1.roles in {LITERAL} and not in {IDENTIFIER, INCOMPLETE, LIST}<br>	∧ ^2.roles not in {LITERAL}<br>⇒ y = ⏎<br>Confidence: 0.844. Support: 1085.` |
| 44 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = [<br>	∧ +1.internal_type = StringLiteral<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {File}<br>	∧ ^1.roles not in {IDENTIFIER, LIST, LITERAL}<br>⇒ y = '<br>Confidence: 0.924. Support: 465.` |
| 45 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved = [<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {File}<br>	∧ ^1.roles not in {IDENTIFIER, LIST, LITERAL}<br>⇒ y = ∅<br>Confidence: 0.960. Support: 565.` |
| 46 | `  •••start_col ≥ 25<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ), [, {, }}<br>	∧ +1.length ≥ 2<br>	∧ +5.reserved not in {=}<br>	∧ ^1.internal_type = BlockStatement<br>	∧ ^1.roles not in {IDENTIFIER, LIST, LITERAL}<br>⇒ y = ⏎<br>Confidence: 0.852. Support: 1497.` |
| 47 | `  •••start_col ≤ 24<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ), [, {, }}<br>	∧ -4.label in {<space>}<br>	∧ +1.length ≥ 2<br>	∧ +5.reserved not in {=}<br>	∧ ^1.internal_type = BlockStatement<br>	∧ ^1.roles not in {IDENTIFIER, LIST, LITERAL}<br>⇒ y = ⏎<br>Confidence: 0.854. Support: 195.` |
| 48 | `  •••start_col ≤ 18<br>	∧ -1.diff_col ≥ 3<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ), [, {, }}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type = BlockStatement<br>	∧ ^1.roles not in {IDENTIFIER, LIST, LITERAL}<br>⇒ y = ␣<br>Confidence: 0.981. Support: 2549.` |
| 49 | `  •••start_col ≤ 18<br>	∧ -1.diff_col ≤ 2<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ), [, {, }}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type = BlockStatement<br>	∧ ^1.roles not in {LIST, LITERAL}<br>⇒ y = ∅<br>Confidence: 0.841. Support: 179.` |
| 50 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ), [, {, }}<br>	∧ -2.diff_line = 0<br>	∧ -2.diff_offset ≥ 3<br>	∧ -2.reserved = (<br>	∧ -4.diff_offset ≥ 6<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {BlockStatement, File}<br>	∧ ^1.roles not in {IDENTIFIER, LIST, LITERAL}<br>⇒ y = ␣<br>Confidence: 0.944. Support: 619.` |
| 51 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ), [, {, }}<br>	∧ -2.diff_line = 0<br>	∧ -2.diff_offset ≤ 2<br>	∧ -2.reserved = (<br>	∧ -4.diff_offset ≥ 6<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {BlockStatement, File}<br>	∧ ^1.roles not in {LIST, LITERAL}<br>⇒ y = ∅<br>Confidence: 0.998. Support: 286.` |
| 52 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ), [, {, }}<br>	∧ -2.diff_line = 0<br>	∧ -2.reserved not in {(}<br>	∧ -4.diff_offset ≥ 6<br>	∧ +1.roles in {EXPRESSION}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {BlockStatement, File}<br>	∧ ^1.roles not in {IDENTIFIER, LIST, LITERAL}<br>⇒ y = ␣<br>Confidence: 0.978. Support: 17218.` |
| 53 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ), [, {, }}<br>	∧ -2.diff_line = 0<br>	∧ -2.reserved not in {(}<br>	∧ -4.diff_offset ≥ 6<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 8<br>	∧ ^1.internal_type not in {BlockStatement, File}<br>	∧ ^1.roles not in {IDENTIFIER, LIST, LITERAL}<br>⇒ y = ␣<br>Confidence: 0.903. Support: 3191.` |
| 54 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ), [, {, }}<br>	∧ -2.reserved = (<br>	∧ -4.diff_offset ≤ 5<br>	∧ +1.roles in {EXPRESSION}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {BlockStatement, File}<br>	∧ ^1.roles not in {LIST, LITERAL}<br>⇒ y = ∅<br>Confidence: 0.997. Support: 160.` |
| 55 | `  •••start_col ≤ 5<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ), [, {, }}<br>	∧ -4.diff_offset ≤ 5<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {BlockStatement, File}<br>	∧ ^1.roles not in {LIST, LITERAL}<br>⇒ y = ∅<br>Confidence: 0.997. Support: 167.` |
| 56 | `  -1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = =<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER, LIST}<br>⇒ y = ␣<br>Confidence: 0.994. Support: 9356.` |
| 57 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ +1.reserved = {<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER, LIST}<br>⇒ y = ∅<br>Confidence: 0.999. Support: 723.` |
| 58 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(}<br>	∧ +1.reserved = {<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER, LIST}<br>⇒ y = ␣<br>Confidence: 0.981. Support: 7996.` |
| 59 | `  •••start_col ≥ 39<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.roles in {EXPRESSION}<br>	∧ -4.label not in {<space>}<br>	∧ +1.reserved = }<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER, LIST}<br>⇒ y = ∅<br>Confidence: 0.937. Support: 959.` |
| 60 | `  •••start_col ≤ 38<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.roles in {EXPRESSION}<br>	∧ +1.reserved = }<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles in {DECLARATION} and not in {IDENTIFIER, LIST}<br>⇒ y = ∅<br>Confidence: 0.935. Support: 162.` |
| 61 | `  •••start_col ≤ 38<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.roles in {EXPRESSION}<br>	∧ +1.reserved = }<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {DECLARATION, EXPRESSION, IDENTIFIER, LIST}<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.852. Support: 795.` |
| 62 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {]}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ +1.reserved = }<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles in {EXPRESSION, MAP} and not in {IDENTIFIER, LIST}<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.867. Support: 147.` |
| 63 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {]}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ +1.reserved = }<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {EXPRESSION, IDENTIFIER, LIST}<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.953. Support: 6029.` |
| 64 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ +1.reserved not in {{, }}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER, LIST}<br>⇒ y = ␣<br>Confidence: 0.973. Support: 2344.` |
| 65 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = if<br>	∧ +1.reserved not in {{, }}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER, LIST}<br>⇒ y = ␣<br>Confidence: 1.000. Support: 1780.` |
| 66 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, if}<br>	∧ -1.roles in {NAME}<br>	∧ +1.reserved not in {}}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER, LIST}<br>⇒ y = ␣<br>Confidence: 0.994. Support: 1695.` |
| 67 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = :<br>	∧ +1.reserved not in {}}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.999. Support: 894.` |
| 68 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :, if}<br>	∧ +1.reserved = )<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles in {OPERATOR} and not in {LIST}<br>⇒ y = ∅<br>Confidence: 0.996. Support: 341.` |
| 69 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :, if}<br>	∧ +1.reserved = ]<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles in {OPERATOR} and not in {LIST}<br>⇒ y = ∅<br>Confidence: 0.997. Support: 166.` |
| 70 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :, if}<br>	∧ -1.roles in {IDENTIFIER}<br>	∧ +1.reserved = (<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles in {OPERATOR} and not in {LIST}<br>⇒ y = ∅<br>Confidence: 0.995. Support: 99.` |
| 71 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, if}<br>	∧ -1.roles not in {IDENTIFIER}<br>	∧ +1.reserved = (<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles in {OPERATOR} and not in {IDENTIFIER, LIST}<br>⇒ y = ␣<br>Confidence: 0.887. Support: 190.` |
| 72 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, if}<br>	∧ +1.reserved not in {(, ), }}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles in {OPERATOR} and not in {IDENTIFIER, LIST}<br>⇒ y = ␣<br>Confidence: 0.896. Support: 1356.` |
| 73 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,}<br>	∧ +1.internal_type = StringLiteral<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER, LIST, OPERATOR}<br>⇒ y = '<br>Confidence: 0.914. Support: 532.` |
| 74 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = const<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.997. Support: 151.` |
| 75 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, if}<br>	∧ -5.reserved = const<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER, LIST}<br>⇒ y = ␣<br>Confidence: 0.956. Support: 148.` |
| 76 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles in {IDENTIFIER}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.996. Support: 124.` |
| 77 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, if}<br>	∧ -5.length ≥ 21<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {IDENTIFIER}<br>	∧ +1.length ≤ 1<br>	∧ +4.reserved = ><br>	∧ ^1.roles not in {IDENTIFIER, LIST}<br>⇒ y = ␣<br>Confidence: 0.957. Support: 199.` |
| 78 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, const, if}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {IDENTIFIER}<br>	∧ +1.length ≤ 1<br>	∧ +4.reserved = ><br>	∧ ^1.roles not in {LIST, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.930. Support: 838.` |
| 79 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, const, if}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {(, =, {, }}<br>	∧ +1.roles not in {IDENTIFIER}<br>	∧ +1.length ≤ 1<br>	∧ +3.reserved = {<br>	∧ ^1.roles not in {LIST, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.977. Support: 547.` |
| 80 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, const, if}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {IDENTIFIER}<br>	∧ +1.length ≤ 1<br>	∧ +3.reserved not in {{}<br>	∧ ^1.roles in {IF} and not in {LIST, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.931. Support: 3707.` |
| 81 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, const, if}<br>	∧ -1.length ≤ 2<br>	∧ -3.reserved = }<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {IDENTIFIER}<br>	∧ +1.length ≤ 1<br>	∧ +3.reserved not in {{}<br>	∧ ^1.roles not in {IF, LIST, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.926. Support: 411.` |
| 82 | `  •••start_col ≥ 13<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, const, if}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {IDENTIFIER}<br>	∧ +1.length ≤ 1<br>	∧ +3.reserved not in {{}<br>	∧ ^1.roles not in {IF, LIST, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.992. Support: 56344.` |
| 83 | `  •••start_col ≤ 12<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, if}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = (<br>	∧ +1.roles not in {IDENTIFIER}<br>	∧ +1.length ≤ 1<br>	∧ +3.internal_type = Identifier<br>	∧ ^1.roles not in {IDENTIFIER, IF, LIST}<br>⇒ y = ␣<br>Confidence: 0.906. Support: 207.` |
| 84 | `  •••start_col ≤ 12<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, const, if}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {(, =, {, }}<br>	∧ +1.roles not in {IDENTIFIER}<br>	∧ +1.length ≤ 1<br>	∧ +3.internal_type = Identifier<br>	∧ +3.reserved not in {{}<br>	∧ ^1.roles not in {IF, LIST, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.956. Support: 215.` |
| 85 | `  •••start_col ≤ 12<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, const, if}<br>	∧ -1.roles in {EXPRESSION}<br>	∧ -1.length ≥ 3<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {IDENTIFIER}<br>	∧ +1.length ≤ 1<br>	∧ +3.internal_type not in {Identifier}<br>	∧ +3.reserved not in {{}<br>	∧ ^1.roles not in {IF, LIST, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.999. Support: 665.` |
| 86 | `  •••start_col ≤ 12<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, const, if}<br>	∧ -1.length ≤ 2<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {IDENTIFIER}<br>	∧ +1.length ≤ 1<br>	∧ +3.internal_type not in {Identifier}<br>	∧ +3.reserved not in {{}<br>	∧ ^1.roles not in {IF, LIST, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.991. Support: 4153.` |
| 87 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, if}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.length = 0<br>	∧ ^1.roles not in {IDENTIFIER, LIST, OPERATOR}<br>⇒ y = ⏎<br>Confidence: 0.985. Support: 170.` |

<details>
    <summary>Machine-readable report</summary>
```json
{"javascript": {"avg_rule_len": 9.655172413793103, "max_conf": 0.9998457431793213, "max_support": 65414, "min_conf": 0.807692289352417, "min_support": 91, "num_rules": 87}}
```
</details>
