# Model report for file:///tmp/top-repos-quality-repos-g8bg943w/express HEAD b4eb1f59d39d801d7365c86b04500f16faeb0b1c

### Dump

```json
{'created_at': datetime.datetime(2019, 2, 12, 22, 1, 17, 414562),
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
 'uuid': '1e79b483-3c2f-464e-bb63-24deb82e2635',
 'version': [1]}
style.format.analyzer.FormatAnalyzer/[1] file:///tmp/top-repos-quality-repos-g8bg943w/express b4eb1f59d39d801d7365c86b04500f16faeb0b1c

# javascript
40 rules, avg.len. 8.2
## train
PPCR: 0.959797
### report
macro
{'f1-score': 0.9395820727667125,
 'precision': 0.9531924781353951,
 'recall': 0.9273121788075175,
 'support': 69138}
micro
{'f1-score': 0.9614683676126009,
 'precision': 0.9614683676126009,
 'recall': 0.9614683676126009,
 'support': 69138}
weighted
{'f1-score': 0.9608921248713054,
 'precision': 0.96140589779903,
 'recall': 0.9614683676126009,
 'support': 69138}
### report_full
macro
{'f1-score': 0.9016721210345119,
 'precision': 0.9531924781353951,
 'recall': 0.860953373566757,
 'support': 72034}
micro
{'f1-score': 0.9417448219193609,
 'precision': 0.9614683676126009,
 'recall': 0.9228142266152095,
 'support': 72034}
weighted
{'f1-score': 0.9394225094965968,
 'precision': 0.9604223029454134,
 'recall': 0.9228142266152095,
 'support': 72034}
## test
PPCR: 0.942590
### report
macro
{'f1-score': 0.9272904697932166,
 'precision': 0.9449483940611751,
 'recall': 0.9112931089390367,
 'support': 14711}
micro
{'f1-score': 0.954387873020189,
 'precision': 0.954387873020189,
 'recall': 0.954387873020189,
 'support': 14711}
weighted
{'f1-score': 0.9536549784093341,
 'precision': 0.9544522036735851,
 'recall': 0.954387873020189,
 'support': 14711}
### report_full
macro
{'f1-score': 0.886099834715725,
 'precision': 0.9449483940611751,
 'recall': 0.8408727441511196,
 'support': 15607}
micro
{'f1-score': 0.9261824658618643,
 'precision': 0.954387873020189,
 'recall': 0.8995963349778945,
 'support': 15607}
weighted
{'f1-score': 0.9232460721049308,
 'precision': 0.9529358571682635,
 'recall': 0.8995963349778945,
 'support': 15607}
```

## javascript
### Summary
40 rules, avg.len. 8.2

| | |
|-|-|
|Min support|98|
|Max support|22691|
|Min confidence|0.8328025341033936|
|Max confidence|0.9998719096183777|

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
| 1 | `  -1.roles in {STRING}<br>⇒ y = '<br>Confidence: 1.000. Support: 3904.` |
| 2 | `  -1.reserved = ,<br>	∧ -1.roles not in {STRING}<br>	∧ +1.roles in {STRING}<br>⇒ y = ␣<br>Confidence: 0.971. Support: 596.` |
| 3 | `  -1.reserved = :<br>	∧ -1.roles not in {STRING}<br>	∧ +1.roles in {STRING}<br>⇒ y = ␣<br>Confidence: 0.998. Support: 220.` |
| 4 | `  -1.reserved not in {:}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.label in {<space>}<br>	∧ +1.roles in {STRING}<br>⇒ y = ␣<br>Confidence: 0.887. Support: 208.` |
| 5 | `  -1.reserved not in {,, :}<br>	∧ -2.label not in {<space>}<br>	∧ +1.roles in {STRING}<br>⇒ y = '<br>Confidence: 0.988. Support: 3907.` |
| 6 | `  -1.reserved = ,<br>	∧ -1.roles not in {STRING}<br>	∧ +1.roles not in {STRING}<br>⇒ y = ␣<br>Confidence: 0.980. Support: 3042.` |
| 7 | `  -1.reserved not in {,}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≥ 3<br>	∧ +1.reserved = =<br>	∧ +1.roles not in {STRING}<br>⇒ y = ␣<br>Confidence: 1.000. Support: 1294.` |
| 8 | `  -1.reserved = var<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≥ 3<br>	∧ +1.roles not in {STRING}<br>⇒ y = ␣<br>Confidence: 0.999. Support: 898.` |
| 9 | `  -1.reserved not in {var}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≥ 3<br>	∧ -4.label in {<space>}<br>	∧ +1.reserved = }<br>	∧ +1.roles not in {STRING}<br>⇒ y = ␣<br>Confidence: 0.880. Support: 137.` |
| 10 | `  -1.reserved not in {,, var}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≥ 3<br>	∧ -4.internal_type not in {Identifier}<br>	∧ -4.label not in {<space>}<br>	∧ +1.reserved = }<br>	∧ +1.roles not in {STRING}<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.982. Support: 257.` |
| 11 | `  -1.reserved not in {,, var}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≥ 3<br>	∧ -4.roles in {CALLEE}<br>	∧ +1.reserved not in {=, }}<br>	∧ +1.roles not in {STRING}<br>	∧ +4.roles in {STRING}<br>⇒ y = ⏎<br>Confidence: 0.950. Support: 434.` |
| 12 | `  -1.reserved not in {,, var}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≥ 3<br>	∧ -4.roles in {CALLEE}<br>	∧ +1.reserved not in {=, }}<br>	∧ +1.roles not in {STRING}<br>	∧ +4.roles not in {STRING}<br>⇒ y = ∅<br>Confidence: 0.925. Support: 154.` |
| 13 | `  -1.reserved not in {var}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≥ 3<br>	∧ -4.roles not in {CALLEE}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {STRING}<br>	∧ ^1.roles in {OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.918. Support: 409.` |
| 14 | `  -1.internal_type = CommentLine<br>	∧ -1.reserved not in {,, var}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≥ 3<br>	∧ -4.roles not in {CALLEE}<br>	∧ +1.reserved not in {=, }}<br>	∧ +1.roles not in {STRING}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ⏎<br>Confidence: 0.833. Support: 314.` |
| 15 | `  -1.internal_type not in {CommentLine}<br>	∧ -1.reserved = if<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≥ 3<br>	∧ -4.roles not in {CALLEE}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {STRING}<br>⇒ y = ␣<br>Confidence: 0.992. Support: 196.` |
| 16 | `  -1.internal_type not in {CommentLine}<br>	∧ -1.reserved = return<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≥ 3<br>	∧ -4.roles not in {CALLEE}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {STRING}<br>⇒ y = ␣<br>Confidence: 0.997. Support: 186.` |
| 17 | `  -1.internal_type not in {CommentLine}<br>	∧ -1.reserved = :<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≥ 3<br>	∧ -4.roles not in {CALLEE}<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {STRING}<br>⇒ y = ␣<br>Confidence: 0.970. Support: 185.` |
| 18 | `  -1.internal_type not in {CommentLine}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≥ 3<br>	∧ -4.label in {<space>}<br>	∧ -4.roles not in {CALLEE}<br>	∧ +1.reserved = {<br>	∧ +1.roles not in {STRING}<br>⇒ y = ␣<br>Confidence: 0.997. Support: 197.` |
| 19 | `  -1.internal_type not in {CommentLine}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≥ 3<br>	∧ -4.label not in {<space>}<br>	∧ -4.roles not in {CALLEE}<br>	∧ +1.reserved = {<br>	∧ +1.roles not in {STRING}<br>	∧ ^1.roles in {STATEMENT}<br>⇒ y = ␣<br>Confidence: 0.905. Support: 111.` |
| 20 | `  -1.internal_type not in {CommentLine}<br>	∧ -1.reserved not in {,, :, var}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≥ 3<br>	∧ -4.label not in {<space>}<br>	∧ -4.roles not in {CALLEE}<br>	∧ -5.diff_offset ≥ 15<br>	∧ +1.reserved = {<br>	∧ +1.roles not in {STRING}<br>	∧ ^1.roles not in {OPERATOR, STATEMENT}<br>⇒ y = ∅<br>Confidence: 0.933. Support: 428.` |
| 21 | `  •••start_col ≤ 33<br>	∧ -1.internal_type not in {CommentLine}<br>	∧ -1.reserved not in {,, :, var}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≥ 3<br>	∧ -4.label not in {<space>}<br>	∧ -4.roles not in {CALLEE}<br>	∧ -5.diff_offset ≤ 14<br>	∧ +1.reserved = {<br>	∧ +1.roles not in {STRING}<br>	∧ ^1.roles not in {OPERATOR, STATEMENT}<br>⇒ y = ∅<br>Confidence: 0.888. Support: 165.` |
| 22 | `  -1.internal_type not in {CommentLine}<br>	∧ -1.reserved not in {,, ;, var}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≥ 3<br>	∧ -2.roles in {COMMENT}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {STRING}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ⏎⏎<br>Confidence: 0.835. Support: 136.` |
| 23 | `  -1.internal_type not in {CommentLine}<br>	∧ -1.reserved = new<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≥ 3<br>	∧ -4.roles not in {CALLEE}<br>	∧ +1.reserved not in {{, }}<br>	∧ +1.roles not in {STRING}<br>⇒ y = ␣<br>Confidence: 0.995. Support: 111.` |
| 24 | `  -1.internal_type not in {CommentLine}<br>	∧ -1.reserved not in {,, ;, new, var}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≥ 3<br>	∧ -4.roles not in {CALLEE}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {STRING}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles in {IF} and not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.888. Support: 353.` |
| 25 | `  -1.internal_type not in {CommentLine}<br>	∧ -1.reserved = }<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≥ 3<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {STRING}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IF, OPERATOR}<br>⇒ y = ⏎⏎<br>Confidence: 0.954. Support: 98.` |
| 26 | `  -1.internal_type not in {CommentLine}<br>	∧ -1.reserved = }<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≥ 3<br>	∧ -4.roles not in {CALLEE}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {STRING}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {OPERATOR}<br>	∧ ^2.roles not in {BLOCK}<br>⇒ y = ∅<br>Confidence: 0.999. Support: 1324.` |
| 27 | `  -1.internal_type not in {CommentLine}<br>	∧ -1.reserved not in {,, ;, var, }}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≥ 3<br>	∧ -4.roles not in {CALLEE}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {STRING}<br>	∧ ^1.roles not in {IF, OPERATOR}<br>	∧ ^2.roles not in {BLOCK}<br>⇒ y = ∅<br>Confidence: 0.993. Support: 22691.` |
| 28 | `  -1.reserved = {<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≤ 2<br>	∧ +1.roles in {KEY} and not in {STRING}<br>⇒ y = ␣<br>Confidence: 0.838. Support: 219.` |
| 29 | `  -1.reserved = {<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≤ 2<br>	∧ +1.roles not in {KEY, STRING}<br>⇒ y = ⏎␣⁺␣⁺<br>Confidence: 0.982. Support: 1799.` |
| 30 | `  -1.reserved not in {,, {}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≤ 2<br>	∧ +1.reserved = }<br>	∧ +1.roles not in {STRING}<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.961. Support: 1491.` |
| 31 | `  -1.reserved = =<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≤ 2<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {STRING}<br>⇒ y = ␣<br>Confidence: 0.999. Support: 1277.` |
| 32 | `  -1.reserved = ;<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≤ 2<br>	∧ -4.diff_col ≥ 9<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {STRING}<br>	∧ +3.length ≥ 2<br>⇒ y = ⏎⏎<br>Confidence: 0.900. Support: 874.` |
| 33 | `  •••start_col ≤ 11<br>	∧ -1.reserved = ;<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≤ 2<br>	∧ -4.diff_col ≤ 8<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {STRING}<br>	∧ +3.length ≥ 2<br>⇒ y = ⏎⏎<br>Confidence: 0.969. Support: 114.` |
| 34 | `  -1.reserved = ;<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≤ 2<br>	∧ +1.reserved not in {}}<br>	∧ +1.roles not in {STRING}<br>	∧ +3.length ≤ 1<br>⇒ y = ⏎<br>Confidence: 0.847. Support: 383.` |
| 35 | `  -1.reserved not in {,, ;, =, {}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≤ 2<br>	∧ +1.reserved = .<br>	∧ +1.roles not in {STRING}<br>⇒ y = ⏎<br>Confidence: 0.897. Support: 790.` |
| 36 | `  -1.reserved not in {,, ;, =, {}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≤ 2<br>	∧ +1.reserved not in {., }}<br>	∧ +1.roles in {CALLEE} and not in {STRING}<br>⇒ y = ⏎⏎<br>Confidence: 0.954. Support: 467.` |
| 37 | `  -1.reserved not in {;, =, {}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≤ 2<br>	∧ +1.reserved not in {., }}<br>	∧ +1.roles not in {CALLEE, STRING}<br>	∧ ^1.internal_type = BinaryExpression<br>⇒ y = ␣<br>Confidence: 0.900. Support: 205.` |
| 38 | `  -1.reserved not in {,, ;, =, {}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≤ 2<br>	∧ +1.reserved not in {., }}<br>	∧ +1.roles not in {CALLEE, STRING}<br>	∧ +1.length ≤ 2<br>	∧ +3.reserved not in {=}<br>	∧ +4.reserved = (<br>	∧ ^1.internal_type not in {BinaryExpression}<br>⇒ y = ∅<br>Confidence: 0.969. Support: 146.` |
| 39 | `  -1.reserved not in {,, ;, =, {}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≤ 2<br>	∧ -3.label in {<space>}<br>	∧ -5.diff_offset ≤ 9<br>	∧ +1.reserved not in {., }}<br>	∧ +1.roles not in {CALLEE, STRING}<br>	∧ +2.length ≥ 1<br>	∧ +3.reserved not in {=}<br>	∧ +4.reserved not in {(}<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles not in {IF}<br>⇒ y = ∅<br>Confidence: 0.922. Support: 161.` |
| 40 | `  -1.reserved not in {,, ;, =, {}<br>	∧ -1.roles not in {STRING}<br>	∧ -2.diff_offset ≤ 2<br>	∧ -3.label not in {<space>}<br>	∧ +1.reserved not in {., }}<br>	∧ +1.roles not in {CALLEE, STRING}<br>	∧ +2.length ≥ 1<br>	∧ +3.reserved not in {=}<br>	∧ +4.reserved not in {(}<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles not in {IF}<br>⇒ y = ∅<br>Confidence: 0.957. Support: 3783.` |

<details>
    <summary>Machine-readable report</summary>
```json
{"javascript": {"avg_rule_len": 8.225, "max_conf": 0.9998719096183777, "max_support": 22691, "min_conf": 0.8328025341033936, "min_support": 98, "num_rules": 40}}
```
</details>
