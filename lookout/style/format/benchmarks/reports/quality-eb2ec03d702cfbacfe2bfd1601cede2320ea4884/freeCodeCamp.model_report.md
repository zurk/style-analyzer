# Model report for file:///tmp/top-repos-quality-repos-68du5go8/freeCodeCamp HEAD cf65516cce60645a417e44c4fcea7418ca920572

### Dump

```json
{'created_at': datetime.datetime(2019, 2, 13, 7, 45, 19, 734966),
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
 'uuid': '1bec7578-f2b7-4836-bebd-7f821d6a4d22',
 'version': [1]}
style.format.analyzer.FormatAnalyzer/[1] file:///tmp/top-repos-quality-repos-68du5go8/freeCodeCamp cf65516cce60645a417e44c4fcea7418ca920572

# javascript
75 rules, avg.len. 9.9
## train
PPCR: 0.919932
### report
macro
{'f1-score': 0.6916739722108969,
 'precision': 0.7213094424669705,
 'recall': 0.6687871086516974,
 'support': 94397}
micro
{'f1-score': 0.950898863311334,
 'precision': 0.950898863311334,
 'recall': 0.950898863311334,
 'support': 94397}
weighted
{'f1-score': 0.9474027648359004,
 'precision': 0.9460900025755097,
 'recall': 0.950898863311334,
 'support': 94397}
### report_full
macro
{'f1-score': 0.6109187083613987,
 'precision': 0.7213094424669705,
 'recall': 0.5503861369056202,
 'support': 102613}
micro
{'f1-score': 0.9112430841074057,
 'precision': 0.950898863311334,
 'recall': 0.8747624569986259,
 'support': 102613}
weighted
{'f1-score': 0.902004568862812,
 'precision': 0.9440339388826144,
 'recall': 0.8747624569986259,
 'support': 102613}
## test
PPCR: 0.908773
### report
macro
{'f1-score': 0.6991992041688833,
 'precision': 0.7206524250156314,
 'recall': 0.6816216274412447,
 'support': 21577}
micro
{'f1-score': 0.9547666496732632,
 'precision': 0.9547666496732632,
 'recall': 0.9547666496732632,
 'support': 21577}
weighted
{'f1-score': 0.9527869791245599,
 'precision': 0.9523217766150389,
 'recall': 0.9547666496732632,
 'support': 21577}
### report_full
macro
{'f1-score': 0.6070990874569936,
 'precision': 0.7206524250156314,
 'recall': 0.5455403718626082,
 'support': 23743}
micro
{'f1-score': 0.9091350397175638,
 'precision': 0.9547666496732632,
 'recall': 0.8676662595291244,
 'support': 23743}
weighted
{'f1-score': 0.8998325292562377,
 'precision': 0.9497465745308299,
 'recall': 0.8676662595291244,
 'support': 23743}
```

## javascript
### Summary
75 rules, avg.len. 9.9

| | |
|-|-|
|Min support|90|
|Max support|27360|
|Min confidence|0.8018480539321899|
|Max confidence|0.9992907643318176|

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
| 1 | `  -1.internal_type = StringLiteral<br>⇒ y = '<br>Confidence: 0.973. Support: 3695.` |
| 2 | `  -1.internal_type not in {StringLiteral}<br>	∧ -2.label in {<space>}<br>	∧ -4.length ≤ 21<br>	∧ +1.internal_type = StringLiteral<br>⇒ y = ␣<br>Confidence: 0.937. Support: 1240.` |
| 3 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = :<br>	∧ -2.label not in {<space>}<br>	∧ +1.internal_type = StringLiteral<br>⇒ y = ␣<br>Confidence: 0.982. Support: 578.` |
| 4 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ -2.label not in {<space>}<br>	∧ -5.label in {<newline>}<br>	∧ +1.internal_type = StringLiteral<br>⇒ y = ⏎<br>Confidence: 0.976. Support: 233.` |
| 5 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -2.label not in {<space>}<br>	∧ +1.internal_type = StringLiteral<br>⇒ y = '<br>Confidence: 0.943. Support: 3763.` |
| 6 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +2.reserved = }<br>	∧ ^1.roles in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.950. Support: 109.` |
| 7 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +2.reserved not in {,, }}<br>	∧ ^1.roles in {DECLARATION}<br>⇒ y = ⏎␣⁺␣⁺<br>Confidence: 0.953. Support: 977.` |
| 8 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {{}<br>	∧ -2.label in {<space>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ ^1.roles in {DECLARATION, FUNCTION}<br>⇒ y = ␣<br>Confidence: 0.962. Support: 144.` |
| 9 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {{}<br>	∧ -2.label in {<space>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = =<br>	∧ ^1.roles in {DECLARATION, FUNCTION}<br>⇒ y = ␣<br>Confidence: 0.996. Support: 131.` |
| 10 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {{}<br>	∧ -2.label in {<space>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, }}<br>	∧ ^1.roles in {DECLARATION, FUNCTION}<br>⇒ y = ∅<br>Confidence: 0.953. Support: 1594.` |
| 11 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ -2.label not in {<space>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles in {DECLARATION, FUNCTION}<br>⇒ y = ∅<br>Confidence: 0.992. Support: 445.` |
| 12 | `  -1.internal_type = Identifier<br>	∧ -1.reserved not in {(, {}<br>	∧ -2.label not in {<space>}<br>	∧ +1.reserved = =<br>	∧ ^1.roles in {DECLARATION, FUNCTION}<br>⇒ y = ␣<br>Confidence: 0.997. Support: 185.` |
| 13 | `  -1.internal_type = Identifier<br>	∧ -1.reserved not in {(, {}<br>	∧ -2.label not in {<space>}<br>	∧ +1.reserved not in {=}<br>	∧ ^1.roles in {DECLARATION, FUNCTION}<br>⇒ y = ∅<br>Confidence: 0.965. Support: 609.` |
| 14 | `  -1.internal_type not in {Identifier, StringLiteral}<br>	∧ -1.reserved not in {(, {}<br>	∧ -2.label not in {<space>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≤ 3<br>	∧ ^1.roles in {DECLARATION, FUNCTION}<br>⇒ y = ␣<br>Confidence: 0.959. Support: 1633.` |
| 15 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {{}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = ,<br>	∧ ^1.roles in {DECLARATION} and not in {FUNCTION}<br>⇒ y = ∅<br>Confidence: 0.998. Support: 269.` |
| 16 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {{}<br>	∧ -3.label in {<newline>}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {,}<br>	∧ ^1.roles in {DECLARATION} and not in {FUNCTION}<br>⇒ y = ⏎<br>Confidence: 0.988. Support: 125.` |
| 17 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {{}<br>	∧ -3.diff_line ≥ 1<br>	∧ -3.label not in {<newline>}<br>	∧ -3.reserved not in {=}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {,}<br>	∧ +2.roles in {EXPRESSION}<br>	∧ ^1.roles in {DECLARATION} and not in {FUNCTION}<br>⇒ y = ␣<br>Confidence: 0.968. Support: 109.` |
| 18 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {{}<br>	∧ -3.diff_line = 0<br>	∧ -3.label not in {<newline>}<br>	∧ -3.reserved not in {=}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {,}<br>	∧ ^1.roles in {DECLARATION} and not in {FUNCTION}<br>⇒ y = ␣<br>Confidence: 0.965. Support: 3954.` |
| 19 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.930. Support: 1142.` |
| 20 | `  •••start_col ≥ 7<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {export, }}<br>	∧ +2.length ≤ 10<br>	∧ +4.reserved not in {{}<br>	∧ ^1.roles in {IF} and not in {DECLARATION}<br>⇒ y = ⏎<br>Confidence: 0.931. Support: 109.` |
| 21 | `  •••start_col ≥ 7<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {export, }}<br>	∧ +2.roles in {IMPORT}<br>	∧ +2.length ≤ 10<br>	∧ +4.reserved not in {{}<br>	∧ ^1.roles not in {DECLARATION, IF}<br>⇒ y = ⏎<br>Confidence: 0.881. Support: 214.` |
| 22 | `  •••start_col ≥ 7<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {export, }}<br>	∧ +2.length ≤ 10<br>	∧ +3.length = 0<br>	∧ +4.reserved not in {{}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ⏎<br>Confidence: 0.986. Support: 110.` |
| 23 | `  •••start_col ≤ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.length ≥ 4<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ⏎⏎<br>Confidence: 0.841. Support: 298.` |
| 24 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.internal_type = ObjectExpression<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ⏎<br>Confidence: 0.924. Support: 1500.` |
| 25 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ -5.diff_line ≥ 1<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.internal_type not in {ObjectExpression}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ⏎<br>Confidence: 0.859. Support: 514.` |
| 26 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ -2.reserved = )<br>	∧ -5.diff_line = 0<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.internal_type not in {ObjectExpression}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ⏎<br>Confidence: 0.901. Support: 176.` |
| 27 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ -2.internal_type = Identifier<br>	∧ -2.reserved not in {)}<br>	∧ -5.diff_line = 0<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.internal_type not in {ObjectExpression}<br>	∧ ^1.roles not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.920. Support: 505.` |
| 28 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ -2.internal_type not in {Identifier}<br>	∧ -2.reserved not in {)}<br>	∧ -5.diff_line = 0<br>	∧ -5.reserved = (<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.internal_type not in {ObjectExpression}<br>	∧ ^1.roles in {EXPRESSION} and not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.990. Support: 155.` |
| 29 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ -2.internal_type not in {Identifier}<br>	∧ -2.reserved not in {)}<br>	∧ -2.roles in {EXPRESSION}<br>	∧ -5.diff_line = 0<br>	∧ -5.reserved not in {(}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.internal_type not in {ObjectExpression}<br>	∧ ^1.roles in {EXPRESSION} and not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.838. Support: 102.` |
| 30 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ -2.internal_type not in {Identifier}<br>	∧ -2.reserved not in {)}<br>	∧ -5.diff_line = 0<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.internal_type not in {ObjectExpression}<br>	∧ ^1.roles not in {DECLARATION, EXPRESSION}<br>⇒ y = ⏎<br>Confidence: 0.837. Support: 95.` |
| 31 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, ;}<br>	∧ -4.diff_offset ≥ 6<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +2.roles in {EXPRESSION}<br>	∧ ^1.roles in {OPERATOR} and not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.949. Support: 1263.` |
| 32 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, ;}<br>	∧ -2.label in {<space>}<br>	∧ -4.diff_offset ≥ 6<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +2.roles not in {EXPRESSION}<br>	∧ ^1.roles in {OPERATOR} and not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.929. Support: 866.` |
| 33 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, ;}<br>	∧ -2.label not in {<space>}<br>	∧ -4.diff_offset ≥ 6<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = =<br>	∧ +2.roles not in {EXPRESSION}<br>	∧ ^1.roles in {OPERATOR} and not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.996. Support: 122.` |
| 34 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, ;}<br>	∧ -2.label not in {<space>}<br>	∧ -4.diff_offset ≥ 6<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=}<br>	∧ +1.length ≤ 2<br>	∧ +2.roles not in {EXPRESSION}<br>	∧ ^1.roles in {OPERATOR} and not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.995. Support: 96.` |
| 35 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, ;}<br>	∧ -2.label not in {<space>}<br>	∧ -4.diff_offset ≥ 6<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=}<br>	∧ +1.length ≤ 1<br>	∧ +2.roles not in {EXPRESSION}<br>	∧ ^1.roles in {OPERATOR} and not in {DECLARATION}<br>⇒ y = ∅<br>Confidence: 0.952. Support: 115.` |
| 36 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, ;}<br>	∧ -4.diff_offset ≤ 5<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.internal_type = BinaryExpression<br>	∧ ^1.roles in {OPERATOR} and not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.893. Support: 136.` |
| 37 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = :<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.987. Support: 1642.` |
| 38 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :, ;}<br>	∧ -3.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles in {EXPRESSION} and not in {DECLARATION, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.973. Support: 658.` |
| 39 | `  -1.diff_col ≥ 2<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :, ;}<br>	∧ -3.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles in {COMMENT}<br>	∧ ^1.roles not in {DECLARATION, EXPRESSION, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.995. Support: 91.` |
| 40 | `  -1.diff_col ≥ 2<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :, ;}<br>	∧ -3.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles not in {DECLARATION, EXPRESSION}<br>⇒ y = ␣<br>Confidence: 0.992. Support: 2097.` |
| 41 | `  -1.diff_col ≤ 1<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :, ;}<br>	∧ -3.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = return<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles in {STATEMENT} and not in {DECLARATION, EXPRESSION, OPERATOR}<br>⇒ y = ⏎<br>Confidence: 0.833. Support: 111.` |
| 42 | `  -1.diff_col ≤ 1<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :, ;}<br>	∧ -3.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {DECLARATION, EXPRESSION, OPERATOR, STATEMENT}<br>⇒ y = ⏎⏎<br>Confidence: 0.935. Support: 286.` |
| 43 | `  -1.diff_col ≤ 1<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :, ;}<br>	∧ -3.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {DECLARATION, EXPRESSION, OPERATOR}<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.985. Support: 99.` |
| 44 | `  -1.diff_col ≤ 1<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :, ;}<br>	∧ -3.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {DECLARATION, EXPRESSION, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.820. Support: 308.` |
| 45 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles in {UNANNOTATED} and not in {DECLARATION, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.946. Support: 661.` |
| 46 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +2.reserved = }<br>	∧ ^1.roles not in {DECLARATION, UNANNOTATED}<br>⇒ y = ␣<br>Confidence: 0.934. Support: 399.` |
| 47 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ -3.length ≤ 4<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +2.reserved not in {}}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR, UNANNOTATED}<br>⇒ y = ⏎␣⁺␣⁺<br>Confidence: 0.905. Support: 865.` |
| 48 | `  -1.internal_type = CommentLine<br>	∧ -1.reserved not in {,, :, ;, {}<br>	∧ -3.reserved not in {;}<br>	∧ ^1.roles not in {DECLARATION, OPERATOR}<br>⇒ y = ⏎<br>Confidence: 0.938. Support: 684.` |
| 49 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, {}<br>	∧ -3.reserved not in {;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +2.reserved = =<br>	∧ ^1.roles in {EXPRESSION} and not in {DECLARATION, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.939. Support: 727.` |
| 50 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, ;, {}<br>	∧ -1.length ≥ 2<br>	∧ -3.reserved not in {;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +2.reserved = =<br>	∧ ^1.roles not in {DECLARATION, EXPRESSION}<br>⇒ y = ␣<br>Confidence: 0.826. Support: 651.` |
| 51 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, {}<br>	∧ -1.length ≤ 1<br>	∧ -2.diff_offset ≥ 3<br>	∧ -3.reserved not in {;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +2.reserved = =<br>	∧ ^1.roles not in {DECLARATION, EXPRESSION, OPERATOR}<br>⇒ y = ⏎<br>Confidence: 0.802. Support: 487.` |
| 52 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, ;, {}<br>	∧ -3.reserved not in {;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = {<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles in {IF} and not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.974. Support: 398.` |
| 53 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, ;, {}<br>	∧ -3.reserved not in {;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +2.reserved not in {=}<br>	∧ +2.roles in {EXPRESSION}<br>	∧ ^1.internal_type = ConditionalExpression<br>	∧ ^1.roles in {IF} and not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.860. Support: 282.` |
| 54 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, ;, {}<br>	∧ -3.reserved not in {;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.roles in {EXPRESSION}<br>	∧ +2.reserved not in {=}<br>	∧ +2.roles not in {EXPRESSION}<br>	∧ ^1.internal_type = ConditionalExpression<br>	∧ ^1.roles in {IF} and not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.854. Support: 113.` |
| 55 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, {}<br>	∧ -3.reserved = {<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles in {IF} and not in {DECLARATION}<br>⇒ y = ␣<br>Confidence: 0.908. Support: 168.` |
| 56 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, {}<br>	∧ -3.reserved not in {;, {}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {{}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.internal_type not in {ConditionalExpression}<br>	∧ ^1.roles in {IF} and not in {DECLARATION, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.904. Support: 1335.` |
| 57 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, {}<br>	∧ -3.reserved not in {;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles in {UNANNOTATED} and not in {DECLARATION, IF, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.931. Support: 615.` |
| 58 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, {}<br>	∧ -3.reserved not in {;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ +2.reserved not in {=}<br>	∧ ^1.internal_type = TemplateLiteral<br>	∧ ^1.roles not in {DECLARATION, IF, OPERATOR, UNANNOTATED}<br>⇒ y = ∅<br>Confidence: 0.964. Support: 151.` |
| 59 | `  •••start_col ≤ 32<br>	∧ -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, :, ;, {}<br>	∧ -3.reserved not in {;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, IF, OPERATOR, UNANNOTATED}<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.898. Support: 477.` |
| 60 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, ;, {}<br>	∧ -3.reserved not in {;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles in {NAME}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, IF}<br>⇒ y = ␣<br>Confidence: 0.957. Support: 242.` |
| 61 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, ;, {}<br>	∧ -3.reserved not in {;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.internal_type = AssignmentPattern<br>	∧ ^1.roles not in {DECLARATION, IF}<br>⇒ y = ␣<br>Confidence: 0.989. Support: 231.` |
| 62 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved = import<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, IF}<br>⇒ y = ␣<br>Confidence: 0.997. Support: 149.` |
| 63 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved = return<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, IF}<br>⇒ y = ␣<br>Confidence: 0.997. Support: 144.` |
| 64 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, ;, {}<br>	∧ -2.reserved = =<br>	∧ -3.reserved not in {;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, IF}<br>⇒ y = ␣<br>Confidence: 0.951. Support: 133.` |
| 65 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, {}<br>	∧ -3.reserved = export<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, IF}<br>⇒ y = ␣<br>Confidence: 0.996. Support: 118.` |
| 66 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved = export<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +2.reserved not in {=}<br>	∧ ^1.roles not in {DECLARATION, IF}<br>⇒ y = ␣<br>Confidence: 0.995. Support: 108.` |
| 67 | `  -1.internal_type not in {CommentLine}<br>	∧ -1.reserved not in {,, :, ;, export, import, return, {}<br>	∧ -3.reserved not in {;, export}<br>	∧ +1.internal_type = JSXIdentifier<br>	∧ +1.reserved not in {}}<br>	∧ +2.reserved = ><br>	∧ ^1.roles not in {DECLARATION, IF, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.999. Support: 705.` |
| 68 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {,, ;, {}<br>	∧ -3.reserved not in {;}<br>	∧ +1.internal_type not in {JSXIdentifier, StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +2.reserved = ><br>	∧ ^1.roles not in {DECLARATION, IF}<br>⇒ y = ␣<br>Confidence: 0.805. Support: 351.` |
| 69 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved = )<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = {<br>	∧ +2.reserved not in {=, >}<br>	∧ ^1.roles not in {DECLARATION, IF}<br>⇒ y = ␣<br>Confidence: 0.994. Support: 90.` |
| 70 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved = )<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.reserved not in {=}<br>	∧ -4.diff_offset ≥ 16<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = .<br>	∧ +1.roles not in {CALLEE}<br>	∧ +2.reserved not in {=, >}<br>	∧ +4.roles not in {FUNCTION}<br>	∧ ^1.roles not in {DECLARATION, IF, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.857. Support: 122.` |
| 71 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved = )<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.reserved not in {=}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {), }}<br>	∧ +1.roles not in {CALLEE}<br>	∧ +2.reserved not in {=, >}<br>	∧ ^1.roles not in {DECLARATION, IF, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.973. Support: 2219.` |
| 72 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {), ,, :, ;, export, import, return, {}<br>	∧ -1.roles in {EXPRESSION}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.reserved not in {=}<br>	∧ -3.reserved not in {;, export}<br>	∧ -5.reserved = ;<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {CALLEE}<br>	∧ +2.reserved not in {=, >}<br>	∧ ^1.roles not in {DECLARATION, IF, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.971. Support: 542.` |
| 73 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {), ,, :, ;, export, import, return, {}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -3.reserved not in {;, export}<br>	∧ -5.reserved not in {;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {CALLEE}<br>	∧ +2.reserved = ;<br>	∧ ^1.roles not in {DECLARATION, IF, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.874. Support: 1426.` |
| 74 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved = [<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.reserved not in {=}<br>	∧ -2.length ≥ 2<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {CALLEE}<br>	∧ +2.reserved not in {=, >}<br>	∧ ^1.roles not in {DECLARATION, IF, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.965. Support: 272.` |
| 75 | `  -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.reserved not in {), ,, :, ;, import, return, {}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.reserved not in {=}<br>	∧ -3.reserved not in {;, export}<br>	∧ -5.reserved not in {;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {CALLEE}<br>	∧ +2.reserved not in {;, =, >}<br>	∧ ^1.roles not in {DECLARATION, IF, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.977. Support: 27360.` |

<details>
    <summary>Machine-readable report</summary>
```json
{"javascript": {"avg_rule_len": 9.88, "max_conf": 0.9992907643318176, "max_support": 27360, "min_conf": 0.8018480539321899, "min_support": 90, "num_rules": 75}}
```
</details>
