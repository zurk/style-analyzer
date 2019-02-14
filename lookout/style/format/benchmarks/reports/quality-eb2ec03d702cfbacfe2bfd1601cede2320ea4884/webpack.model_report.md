# Model report for file:///tmp/top-repos-quality-repos-jaqd5njd/webpack HEAD babe736cfa1ef7e8014ed32ba4a4ec38049dce14

### Dump

```json
{'created_at': datetime.datetime(2019, 2, 13, 3, 46, 9, 686088),
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
 'uuid': 'c1967020-5e0f-42a6-b3d4-57de3855c1db',
 'version': [1]}
style.format.analyzer.FormatAnalyzer/[1] file:///tmp/top-repos-quality-repos-jaqd5njd/webpack babe736cfa1ef7e8014ed32ba4a4ec38049dce14

# javascript
105 rules, avg.len. 10.7
## train
PPCR: 0.956476
### report
macro
{'f1-score': 0.5773209778827113,
 'precision': 0.6091252078977358,
 'recall': 0.5539801832314049,
 'support': 297551}
micro
{'f1-score': 0.9489566494483299,
 'precision': 0.9489566494483299,
 'recall': 0.9489566494483299,
 'support': 297551}
weighted
{'f1-score': 0.945397681210028,
 'precision': 0.9431055489609866,
 'recall': 0.9489566494483299,
 'support': 297551}
### report_full
macro
{'f1-score': 0.5418387337587361,
 'precision': 0.6091252078977358,
 'recall': 0.4998603867810614,
 'support': 311091}
micro
{'f1-score': 0.9278459258480355,
 'precision': 0.9489566494483299,
 'recall': 0.9076540304926854,
 'support': 311091}
weighted
{'f1-score': 0.9207632504268907,
 'precision': 0.9383431859208821,
 'recall': 0.9076540304926854,
 'support': 311091}
## test
PPCR: 0.952919
### report
macro
{'f1-score': 0.5238497363544362,
 'precision': 0.5441566858176586,
 'recall': 0.5072100160230938,
 'support': 73835}
micro
{'f1-score': 0.9491298164826979,
 'precision': 0.9491298164826979,
 'recall': 0.9491298164826979,
 'support': 73835}
weighted
{'f1-score': 0.9471782389965299,
 'precision': 0.9468246091568036,
 'recall': 0.9491298164826979,
 'support': 73835}
### report_full
macro
{'f1-score': 0.4942413295366392,
 'precision': 0.5441566858176586,
 'recall': 0.4582352465388781,
 'support': 77483}
micro
{'f1-score': 0.9262480339417649,
 'precision': 0.9491298164826979,
 'recall': 0.9044435553605307,
 'support': 77483}
weighted
{'f1-score': 0.9225204492044803,
 'precision': 0.9459637516994337,
 'recall': 0.9044435553605307,
 'support': 77483}
```

## javascript
### Summary
105 rules, avg.len. 10.7

| | |
|-|-|
|Min support|91|
|Max support|41762|
|Min confidence|0.8036649227142334|
|Max confidence|0.9996068477630615|

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
| 1 | `  -1.internal_type = StringLiteral<br>	∧ ^1.roles in {IDENTIFIER}<br>⇒ y = "<br>Confidence: 0.933. Support: 710.` |
| 2 | `  -1.internal_type not in {StringLiteral}<br>	∧ -3.internal_type = StringLiteral<br>	∧ +1.reserved not in {}}<br>	∧ +4.length ≥ 9<br>	∧ ^1.roles in {IDENTIFIER}<br>⇒ y = ⏎<br>Confidence: 0.809. Support: 123.` |
| 3 | `  -1.internal_type not in {StringLiteral}<br>	∧ -3.internal_type = StringLiteral<br>	∧ +1.reserved not in {}}<br>	∧ +4.length ≤ 8<br>	∧ ^1.roles in {IDENTIFIER}<br>⇒ y = ∅<br>Confidence: 0.854. Support: 544.` |
| 4 | `  -1.internal_type not in {StringLiteral}<br>	∧ -3.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {}}<br>	∧ ^1.roles in {IDENTIFIER}<br>⇒ y = ∅<br>Confidence: 0.987. Support: 41762.` |
| 5 | `  •••start_line = 255<br>	∧ -1.internal_type = StringLiteral<br>	∧ -5.diff_offset ≥ 22<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = "<br>Confidence: 0.881. Support: 934.` |
| 6 | `  •••start_line = 255<br>	∧ -1.internal_type = StringLiteral<br>	∧ -5.diff_offset ≤ 21<br>	∧ ^1.roles in {LITERAL} and not in {IDENTIFIER}<br>⇒ y = "<br>Confidence: 0.939. Support: 107.` |
| 7 | `  •••start_line ≤ 254<br>	∧ -1.internal_type = StringLiteral<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = "<br>Confidence: 0.976. Support: 9194.` |
| 8 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ -2.reserved = )<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ⏎␣⁺␣⁺<br>Confidence: 0.815. Support: 224.` |
| 9 | `  •••start_line ≤ 45<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ -2.reserved not in {)}<br>	∧ +1.length ≥ 2<br>	∧ +2.reserved not in {,, }}<br>	∧ ^1.internal_type = FunctionDeclaration<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ⏎⇥⁺<br>Confidence: 0.843. Support: 143.` |
| 10 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = {<br>	∧ -2.reserved not in {)}<br>	∧ +1.length ≥ 2<br>	∧ +2.reserved not in {,, }}<br>	∧ ^1.internal_type not in {FunctionDeclaration}<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ⏎⇥⁺<br>Confidence: 0.956. Support: 7534.` |
| 11 | `  •••start_line ≤ 254<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ +1.internal_type = StringLiteral<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = "<br>Confidence: 0.930. Support: 4414.` |
| 12 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ -4.diff_offset ≥ 24<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≤ 19<br>	∧ +2.reserved = )<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ∅<br>Confidence: 0.987. Support: 336.` |
| 13 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ -4.diff_offset ≤ 23<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≤ 19<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ∅<br>Confidence: 0.954. Support: 9596.` |
| 14 | `  •••start_col ≥ 11<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles in {SCOPE} and not in {IDENTIFIER}<br>⇒ y = ⏎<br>Confidence: 0.877. Support: 5327.` |
| 15 | `  •••start_col ≤ 10<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ -4.reserved not in {;}<br>	∧ +1.roles in {CALL}<br>	∧ +1.length ≥ 2<br>	∧ +3.roles not in {STRING}<br>	∧ ^1.roles in {SCOPE} and not in {IDENTIFIER}<br>⇒ y = ⏎<br>Confidence: 0.886. Support: 136.` |
| 16 | `  •••start_col ≤ 8<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ -4.reserved not in {;}<br>	∧ -5.diff_offset ≥ 11<br>	∧ +1.roles not in {CALL}<br>	∧ +1.length ≥ 2<br>	∧ +3.roles not in {STRING}<br>	∧ ^1.roles in {SCOPE} and not in {IDENTIFIER}<br>⇒ y = ⏎<br>Confidence: 0.826. Support: 204.` |
| 17 | `  •••start_col ≥ 15<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ +1.length ≥ 3<br>	∧ +2.roles in {NAME}<br>	∧ ^1.roles not in {IDENTIFIER, SCOPE}<br>⇒ y = ⏎⏎<br>Confidence: 0.974. Support: 95.` |
| 18 | `  •••start_col ≥ 15<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ +1.reserved not in {export}<br>	∧ +1.length ≥ 3<br>	∧ ^1.roles in {SWITCH} and not in {IDENTIFIER, SCOPE}<br>	∧ ^2.roles not in {SCOPE}<br>⇒ y = ⏎<br>Confidence: 0.997. Support: 146.` |
| 19 | `  •••start_col ≥ 15<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ +1.reserved not in {export}<br>	∧ +1.length ≥ 3<br>	∧ +4.length ≥ 5<br>	∧ ^1.roles not in {IDENTIFIER, SCOPE}<br>	∧ ^2.roles not in {SCOPE}<br>⇒ y = ⏎<br>Confidence: 0.878. Support: 563.` |
| 20 | `  •••start_col ≤ 30<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ +1.reserved not in {export}<br>	∧ +1.length ≥ 3<br>	∧ +4.length ≤ 5<br>	∧ ^1.roles not in {IDENTIFIER, SCOPE}<br>	∧ ^2.roles not in {SCOPE}<br>⇒ y = ⏎<br>Confidence: 0.839. Support: 208.` |
| 21 | `  •••start_col ≥ 15<br>	∧ •••start_line ≤ 15<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ +1.length ≤ 2<br>	∧ ^1.roles not in {IDENTIFIER, SCOPE}<br>⇒ y = ⏎⏎<br>Confidence: 0.861. Support: 191.` |
| 22 | `  •••start_col ≤ 14<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ -3.internal_type = StringLiteral<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER, SCOPE}<br>⇒ y = ⏎<br>Confidence: 0.874. Support: 91.` |
| 23 | `  •••start_col ≤ 14<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ -3.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER, SCOPE}<br>⇒ y = ⏎⏎<br>Confidence: 0.810. Support: 965.` |
| 24 | `  •••start_line = 255<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label in {<space>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ -5.diff_offset ≥ 10<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = "<br>Confidence: 0.832. Support: 567.` |
| 25 | `  •••start_line ≤ 254<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label in {<space>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = "<br>Confidence: 0.962. Support: 3373.` |
| 26 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved = ,<br>	∧ +1.roles in {MAP}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles in {LITERAL} and not in {IDENTIFIER}<br>⇒ y = ⏎<br>Confidence: 0.945. Support: 2094.` |
| 27 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved = ,<br>	∧ -5.label in {<newline>}<br>	∧ +1.roles not in {MAP}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles in {LITERAL} and not in {IDENTIFIER}<br>⇒ y = ⏎<br>Confidence: 0.973. Support: 465.` |
| 28 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved = ,<br>	∧ -3.internal_type = StringLiteral<br>	∧ -5.label not in {<newline>}<br>	∧ +1.roles not in {MAP}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles in {LITERAL} and not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.966. Support: 249.` |
| 29 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(, ,, ;, {}<br>	∧ +1.internal_type = StringLiteral<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles in {LITERAL} and not in {IDENTIFIER}<br>⇒ y = "<br>Confidence: 0.939. Support: 189.` |
| 30 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ,, ;, {}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles in {LITERAL} and not in {IDENTIFIER}<br>⇒ y = ∅<br>Confidence: 0.970. Support: 1674.` |
| 31 | `  •••start_col ≥ 6<br>	∧ -1.internal_type = CommentLine<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles in {FILE} and not in {IDENTIFIER, LITERAL}<br>⇒ y = ⏎<br>Confidence: 0.917. Support: 809.` |
| 32 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ -4.label in {<newline>}<br>	∧ +1.roles in {EXPRESSION}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles in {FILE} and not in {IDENTIFIER, LITERAL}<br>⇒ y = ⏎<br>Confidence: 0.804. Support: 191.` |
| 33 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ -4.label not in {<newline>}<br>	∧ +1.roles in {EXPRESSION}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles in {FILE} and not in {IDENTIFIER, LITERAL}<br>⇒ y = ␣<br>Confidence: 0.874. Support: 503.` |
| 34 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {CommentLine, StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles in {FILE} and not in {IDENTIFIER, LITERAL}<br>⇒ y = ∅<br>Confidence: 0.981. Support: 1905.` |
| 35 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = [<br>	∧ +1.roles in {STRING}<br>	∧ +1.length ≤ 13<br>	∧ ^1.roles not in {FILE, IDENTIFIER, LITERAL}<br>⇒ y = "<br>Confidence: 0.832. Support: 420.` |
| 36 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label in {<newline>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {FILE, IDENTIFIER, LITERAL}<br>⇒ y = "<br>Confidence: 0.982. Support: 362.` |
| 37 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ -1.roles in {STATEMENT}<br>	∧ -2.length ≥ 3<br>	∧ -3.diff_offset ≥ 5<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {FILE, IDENTIFIER, LITERAL}<br>⇒ y = ⏎⇥⁻<br>Confidence: 0.821. Support: 109.` |
| 38 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ -1.roles in {STATEMENT}<br>	∧ -2.length ≤ 2<br>	∧ -3.diff_offset ≥ 5<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {FILE, IDENTIFIER, LITERAL}<br>⇒ y = ⏎<br>Confidence: 0.937. Support: 135.` |
| 39 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved = }<br>	∧ -3.diff_offset ≥ 5<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {BLOCK, FILE, IDENTIFIER, LITERAL}<br>⇒ y = ␣<br>Confidence: 0.936. Support: 304.` |
| 40 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ;, {, }}<br>	∧ -3.diff_offset ≥ 5<br>	∧ -3.label in {<newline>}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type = CallExpression<br>	∧ ^1.roles not in {FILE, IDENTIFIER, LITERAL}<br>⇒ y = ⏎<br>Confidence: 0.878. Support: 440.` |
| 41 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ;, {, }}<br>	∧ -3.diff_offset ≥ 5<br>	∧ -3.label not in {<newline>}<br>	∧ -4.reserved = .<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type = CallExpression<br>	∧ ^1.roles not in {FILE, LITERAL}<br>⇒ y = ∅<br>Confidence: 0.854. Support: 230.` |
| 42 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ;, {, }}<br>	∧ -3.diff_offset ≥ 5<br>	∧ -3.label not in {<newline>}<br>	∧ -4.reserved not in {.}<br>	∧ -4.roles in {CALL}<br>	∧ -5.label in {<newline>}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type = CallExpression<br>	∧ ^1.roles not in {FILE, IDENTIFIER, LITERAL}<br>⇒ y = ␣<br>Confidence: 0.965. Support: 213.` |
| 43 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ;, {, }}<br>	∧ -3.diff_offset ≥ 5<br>	∧ -3.label not in {<newline>}<br>	∧ -4.reserved not in {.}<br>	∧ -4.roles not in {CALL}<br>	∧ -5.label in {<newline>}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type = CallExpression<br>	∧ ^1.roles not in {FILE, IDENTIFIER, LITERAL}<br>⇒ y = ⏎<br>Confidence: 0.955. Support: 235.` |
| 44 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ;, {, }}<br>	∧ -3.diff_offset ≥ 5<br>	∧ -3.label not in {<newline>}<br>	∧ -4.reserved not in {.}<br>	∧ -5.label not in {<newline>}<br>	∧ +1.length ≥ 2<br>	∧ +2.length ≤ 1<br>	∧ ^1.internal_type = CallExpression<br>	∧ ^1.roles not in {FILE, IDENTIFIER, LITERAL}<br>⇒ y = ␣<br>Confidence: 0.946. Support: 2657.` |
| 45 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved = ,<br>	∧ -3.diff_offset ≥ 5<br>	∧ -3.label in {<newline>}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {CallExpression}<br>	∧ ^1.roles not in {FILE, IDENTIFIER, LITERAL}<br>⇒ y = ⏎<br>Confidence: 0.991. Support: 170.` |
| 46 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved = ,<br>	∧ -3.diff_offset ≥ 5<br>	∧ -3.label not in {<newline>}<br>	∧ -3.reserved not in {.}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {CallExpression}<br>	∧ ^1.roles not in {FILE, IDENTIFIER, LITERAL}<br>⇒ y = ␣<br>Confidence: 0.985. Support: 1210.` |
| 47 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ,, ;, {, }}<br>	∧ -3.diff_offset ≥ 5<br>	∧ +1.roles in {EXPRESSION}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {CallExpression}<br>	∧ ^1.roles not in {FILE, IDENTIFIER, LITERAL}<br>⇒ y = ␣<br>Confidence: 0.981. Support: 15828.` |
| 48 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ,, ;, {, }}<br>	∧ -3.diff_offset ≥ 5<br>	∧ +1.roles in {LITERAL} and not in {EXPRESSION}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {CallExpression}<br>	∧ ^1.roles not in {FILE, LITERAL}<br>⇒ y = ∅<br>Confidence: 0.995. Support: 101.` |
| 49 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ,, ;, {, }}<br>	∧ -3.diff_offset ≥ 5<br>	∧ +1.roles not in {EXPRESSION, LITERAL}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {CallExpression}<br>	∧ ^1.roles not in {FILE, IDENTIFIER, LITERAL, SCOPE}<br>⇒ y = ␣<br>Confidence: 0.954. Support: 4256.` |
| 50 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ;, [, {}<br>	∧ -3.diff_offset ≤ 4<br>	∧ -5.label in {<newline>}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {FILE, IDENTIFIER, LITERAL}<br>⇒ y = ∅<br>Confidence: 0.823. Support: 591.` |
| 51 | `  •••start_col ≥ 6<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ;, [, {}<br>	∧ -2.diff_offset ≥ 13<br>	∧ -3.diff_offset ≤ 4<br>	∧ -5.label not in {<newline>}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {FILE, IDENTIFIER, LITERAL}<br>⇒ y = ∅<br>Confidence: 0.945. Support: 227.` |
| 52 | `  •••start_col ≥ 6<br>	∧ •••start_line ≥ 13<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ -2.diff_offset ≤ 13<br>	∧ -3.diff_offset ≤ 4<br>	∧ -3.reserved not in {;}<br>	∧ -3.roles in {IDENTIFIER}<br>	∧ -5.label not in {<newline>}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {FILE, IDENTIFIER, LITERAL}<br>⇒ y = ␣<br>Confidence: 0.967. Support: 323.` |
| 53 | `  •••start_col ≥ 6<br>	∧ •••start_line ≥ 13<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ;, [, {}<br>	∧ -2.diff_offset ≤ 13<br>	∧ -3.diff_offset ≤ 4<br>	∧ -3.reserved not in {;}<br>	∧ -3.roles not in {IDENTIFIER}<br>	∧ -4.label in {<space>}<br>	∧ -5.diff_offset ≥ 12<br>	∧ -5.label not in {<newline>}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {FILE, IDENTIFIER, LITERAL}<br>⇒ y = ∅<br>Confidence: 0.918. Support: 104.` |
| 54 | `  •••start_col ≥ 6<br>	∧ •••start_line ≤ 12<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ -2.diff_offset ≤ 13<br>	∧ -3.diff_offset ≤ 4<br>	∧ -3.reserved not in {;}<br>	∧ -5.label not in {<newline>}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {FILE, IDENTIFIER, LITERAL}<br>⇒ y = ␣<br>Confidence: 0.916. Support: 1203.` |
| 55 | `  •••start_col ≤ 5<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label in {<newline>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = "<br>Confidence: 0.991. Support: 909.` |
| 56 | `  •••start_col ≤ 5<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved = }<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles in {STATEMENT} and not in {BLOCK, IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.984. Support: 287.` |
| 57 | `  •••start_col ≤ 5<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved = }<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER, STATEMENT}<br>⇒ y = ⏎⏎<br>Confidence: 0.890. Support: 885.` |
| 58 | `  •••start_col ≤ 5<br>	∧ •••start_line ≥ 235<br>	∧ -1.diff_col ≥ 4<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ;, {, }}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ⏎⏎<br>Confidence: 0.829. Support: 225.` |
| 59 | `  •••start_col ≤ 5<br>	∧ •••start_line ≤ 234<br>	∧ -1.diff_col ≥ 4<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ;, {, }}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ⏎<br>Confidence: 0.896. Support: 388.` |
| 60 | `  •••start_col ≤ 5<br>	∧ -1.diff_col ≤ 3<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ;, {, }}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.997. Support: 560.` |
| 61 | `  •••start_col ≤ 5<br>	∧ •••start_line ≤ 208<br>	∧ -1.diff_col ≤ 2<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved = ,<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ⏎<br>Confidence: 0.943. Support: 324.` |
| 62 | `  •••start_col ≤ 5<br>	∧ -1.diff_col ≤ 2<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<newline>, <space>}<br>	∧ -1.reserved not in {(, ,, ;, {, }}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ∅<br>Confidence: 0.961. Support: 3621.` |
| 63 | `  -1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = =<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 1.000. Support: 8902.` |
| 64 | `  -1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ +1.length ≤ 1<br>	∧ ^1.internal_type = TemplateLiteral<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ∅<br>Confidence: 0.944. Support: 597.` |
| 65 | `  -1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = }<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles in {DECLARATION} and not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.911. Support: 341.` |
| 66 | `  -1.internal_type = Identifier<br>	∧ -1.roles in {VALUE}<br>	∧ +1.reserved = }<br>	∧ +1.length ≤ 1<br>	∧ ^1.internal_type not in {TemplateLiteral}<br>	∧ ^1.roles not in {DECLARATION, IDENTIFIER}<br>⇒ y = ⏎⇥⁻<br>Confidence: 0.861. Support: 133.` |
| 67 | `  •••start_line ≤ 252<br>	∧ -1.internal_type not in {Identifier, StringLiteral}<br>	∧ +1.reserved = }<br>	∧ +1.length ≤ 1<br>	∧ +4.roles not in {BLOCK}<br>	∧ ^1.roles in {FILE} and not in {DECLARATION, IDENTIFIER}<br>	∧ ^2.internal_type not in {CallExpression}<br>⇒ y = ⏎⇥⁻<br>Confidence: 0.950. Support: 272.` |
| 68 | `  -1.internal_type not in {Identifier, StringLiteral}<br>	∧ +1.reserved = }<br>	∧ +1.length ≤ 1<br>	∧ +4.roles not in {BLOCK}<br>	∧ ^1.roles not in {DECLARATION, FILE, IDENTIFIER}<br>	∧ ^2.internal_type not in {CallExpression}<br>⇒ y = ⏎⇥⁻<br>Confidence: 0.932. Support: 7045.` |
| 69 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ +1.reserved = {<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ∅<br>Confidence: 0.912. Support: 449.` |
| 70 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(}<br>	∧ +1.reserved = {<br>	∧ +1.length ≤ 1<br>	∧ ^1.internal_type = ArrayExpression<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ⏎<br>Confidence: 0.871. Support: 151.` |
| 71 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = [<br>	∧ +1.reserved = {<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ⏎⇥⁺<br>Confidence: 0.938. Support: 105.` |
| 72 | `  •••start_line ≤ 240<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(, [}<br>	∧ +1.reserved = {<br>	∧ +1.length ≤ 1<br>	∧ ^1.internal_type = FunctionExpression<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.990. Support: 448.` |
| 73 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(, [}<br>	∧ +1.reserved = {<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.983. Support: 7210.` |
| 74 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ +1.internal_type = StringLiteral<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = "<br>Confidence: 0.924. Support: 297.` |
| 75 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ∅<br>Confidence: 0.978. Support: 1091.` |
| 76 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label in {<space>}<br>	∧ -1.reserved not in {(}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = "<br>Confidence: 0.899. Support: 658.` |
| 77 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(}<br>	∧ +1.reserved not in {{, }}<br>	∧ +1.roles in {EXPRESSION} and not in {KEY}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.865. Support: 3429.` |
| 78 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = if<br>	∧ +1.reserved not in {{, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.952. Support: 2202.` |
| 79 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {if}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ +2.roles in {EXPRESSION}<br>	∧ ^1.internal_type = BinaryExpression<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.974. Support: 1507.` |
| 80 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ -5.label in {<newline>}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ⏎<br>Confidence: 0.838. Support: 139.` |
| 81 | `  •••start_col ≥ 21<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ -5.label not in {<newline>}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.932. Support: 626.` |
| 82 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = :<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.996. Support: 572.` |
| 83 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {,, :, if}<br>	∧ -2.internal_type = StringLiteral<br>	∧ +1.reserved not in {=, {}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ +2.roles not in {EXPRESSION}<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ⏎⇥⁻<br>Confidence: 0.874. Support: 297.` |
| 84 | `  -1.internal_type = DirectiveLiteral<br>	∧ -1.reserved not in {,, :}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = "<br>Confidence: 0.998. Support: 251.` |
| 85 | `  -1.internal_type not in {DirectiveLiteral, StringLiteral}<br>	∧ -1.reserved = return<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.984. Support: 225.` |
| 86 | `  -1.internal_type not in {DirectiveLiteral, StringLiteral}<br>	∧ -1.reserved = =<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles in {VARIABLE} and not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.913. Support: 269.` |
| 87 | `  •••start_line ≤ 244<br>	∧ -1.internal_type not in {DirectiveLiteral, StringLiteral}<br>	∧ -1.reserved not in {,, :, =}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles in {VARIABLE}<br>⇒ y = ∅<br>Confidence: 0.928. Support: 104.` |
| 88 | `  -1.internal_type not in {DirectiveLiteral, StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -2.length ≥ 88<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles not in {IDENTIFIER, VARIABLE}<br>⇒ y = ⏎<br>Confidence: 0.876. Support: 133.` |
| 89 | `  -1.internal_type not in {DirectiveLiteral, StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -2.diff_col ≥ 4<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles in {OPERATOR} and not in {VARIABLE}<br>⇒ y = ∅<br>Confidence: 0.965. Support: 473.` |
| 90 | `  -1.internal_type not in {DirectiveLiteral, StringLiteral}<br>	∧ -1.reserved not in {,}<br>	∧ -2.diff_col ≤ 3<br>	∧ -3.internal_type = Identifier<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles in {OPERATOR} and not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.839. Support: 301.` |
| 91 | `  •••start_col ≥ 11<br>	∧ -1.internal_type not in {DirectiveLiteral, StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ +1.reserved = ]<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles not in {OPERATOR, VARIABLE}<br>⇒ y = ∅<br>Confidence: 0.895. Support: 769.` |
| 92 | `  •••start_col ≤ 10<br>	∧ -1.internal_type not in {DirectiveLiteral, StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ +1.reserved = ]<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles not in {IDENTIFIER, OPERATOR, VARIABLE}<br>⇒ y = ⏎⇥⁻<br>Confidence: 0.949. Support: 204.` |
| 93 | `  -1.internal_type not in {DirectiveLiteral, StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -1.roles in {EXPRESSION}<br>	∧ -2.length ≥ 4<br>	∧ +1.reserved not in {=, {}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ +2.reserved = ;<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles not in {IDENTIFIER, OPERATOR, VARIABLE}<br>⇒ y = ⏎⇥⁻<br>Confidence: 0.990. Support: 156.` |
| 94 | `  -1.internal_type not in {DirectiveLiteral, StringLiteral}<br>	∧ -1.reserved = (<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.length ≥ 4<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ +2.reserved = ;<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles not in {OPERATOR, VARIABLE}<br>⇒ y = ∅<br>Confidence: 0.999. Support: 684.` |
| 95 | `  -1.internal_type not in {DirectiveLiteral, StringLiteral}<br>	∧ -1.reserved not in {(, ), ,, :}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.length ≥ 4<br>	∧ -3.diff_offset ≥ 7<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ +2.reserved = ;<br>	∧ +5.roles in {IDENTIFIER}<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles not in {OPERATOR, VARIABLE}<br>⇒ y = ∅<br>Confidence: 0.812. Support: 157.` |
| 96 | `  -1.internal_type not in {DirectiveLiteral, StringLiteral}<br>	∧ -1.reserved not in {(, ), ,, :}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.length ≥ 4<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ +2.reserved = ;<br>	∧ +5.roles not in {IDENTIFIER}<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles not in {OPERATOR, VARIABLE}<br>⇒ y = ∅<br>Confidence: 0.814. Support: 573.` |
| 97 | `  -1.internal_type not in {DirectiveLiteral, StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.length ≤ 3<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ +2.reserved = ;<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles not in {OPERATOR, VARIABLE}<br>⇒ y = ∅<br>Confidence: 0.958. Support: 5836.` |
| 98 | `  -1.internal_type not in {DirectiveLiteral, StringLiteral}<br>	∧ -1.reserved not in {,, :, if}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.label in {<newline>}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ +2.reserved not in {;}<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles in {IF} and not in {OPERATOR, VARIABLE}<br>	∧ ^2.roles in {STATEMENT}<br>⇒ y = ∅<br>Confidence: 0.866. Support: 228.` |
| 99 | `  -1.internal_type not in {DirectiveLiteral, StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ -2.label not in {<newline>}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ +2.reserved not in {;}<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles in {IF} and not in {OPERATOR, VARIABLE}<br>	∧ ^2.roles in {STATEMENT}<br>⇒ y = ∅<br>Confidence: 0.969. Support: 4060.` |
| 100 | `  -1.internal_type not in {DirectiveLiteral, StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ +2.reserved not in {;}<br>	∧ +4.length ≤ 1<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles in {IF} and not in {OPERATOR, VARIABLE}<br>	∧ ^2.roles not in {STATEMENT}<br>⇒ y = ∅<br>Confidence: 0.828. Support: 264.` |
| 101 | `  -1.internal_type not in {DirectiveLiteral, StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -1.roles in {EXPRESSION}<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ +2.reserved not in {;}<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles not in {IF, OPERATOR, VARIABLE}<br>⇒ y = ∅<br>Confidence: 0.996. Support: 30794.` |
| 102 | `  -1.diff_col ≥ 7<br>	∧ -1.internal_type not in {DirectiveLiteral, StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -1.length ≥ 3<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ +2.reserved not in {;}<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles not in {IF, OPERATOR, VARIABLE}<br>⇒ y = ∅<br>Confidence: 0.949. Support: 1256.` |
| 103 | `  -1.diff_col ≤ 6<br>	∧ -1.internal_type not in {DirectiveLiteral, StringLiteral}<br>	∧ -1.reserved not in {,}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -1.length ≥ 3<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ +2.reserved not in {;}<br>	∧ +2.length ≥ 2<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles not in {IDENTIFIER, IF}<br>⇒ y = ␣<br>Confidence: 0.910. Support: 461.` |
| 104 | `  -1.internal_type not in {DirectiveLiteral, StringLiteral}<br>	∧ -1.reserved not in {,, :}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -1.length ≤ 2<br>	∧ -2.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ +2.reserved not in {;}<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles not in {IF, OPERATOR, VARIABLE}<br>⇒ y = ∅<br>Confidence: 0.980. Support: 19246.` |
| 105 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {if}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length = 0<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ⏎<br>Confidence: 0.873. Support: 1869.` |

<details>
    <summary>Machine-readable report</summary>
```json
{"javascript": {"avg_rule_len": 10.714285714285714, "max_conf": 0.9996068477630615, "max_support": 41762, "min_conf": 0.8036649227142334, "min_support": 91, "num_rules": 105}}
```
</details>
