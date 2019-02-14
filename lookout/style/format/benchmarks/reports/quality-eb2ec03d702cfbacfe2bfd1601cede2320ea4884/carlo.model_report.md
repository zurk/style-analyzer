# Model report for file:///tmp/top-repos-quality-repos-b15drnka/carlo HEAD b8ce2bca042c757b13fc82a3e059980342ddd9a8

### Dump

```json
{'created_at': datetime.datetime(2019, 2, 13, 7, 24, 6, 387641),
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
 'uuid': '31490c40-076b-4599-898b-5af107072156',
 'version': [1]}
style.format.analyzer.FormatAnalyzer/[1] file:///tmp/top-repos-quality-repos-b15drnka/carlo b8ce2bca042c757b13fc82a3e059980342ddd9a8

# javascript
49 rules, avg.len. 5.9
## train
PPCR: 0.853738
### report
macro
{'f1-score': 0.44076240604129596,
 'precision': 0.43663666128804657,
 'recall': 0.44614576655833266,
 'support': 10962}
micro
{'f1-score': 0.9122422915526364,
 'precision': 0.9122422915526364,
 'recall': 0.9122422915526364,
 'support': 10962}
weighted
{'f1-score': 0.8976385371648288,
 'precision': 0.8838436878962479,
 'recall': 0.9122422915526364,
 'support': 10962}
### report_full
macro
{'f1-score': 0.4034770920049626,
 'precision': 0.43663666128804657,
 'recall': 0.38096667047921523,
 'support': 12840}
micro
{'f1-score': 0.8402655239055541,
 'precision': 0.9122422915526364,
 'recall': 0.778816199376947,
 'support': 12840}
weighted
{'f1-score': 0.7925399856639289,
 'precision': 0.8095955057737784,
 'recall': 0.778816199376947,
 'support': 12840}
## test
PPCR: 0.866466
### report
macro
{'f1-score': 0.4647709202274904,
 'precision': 0.47045660749322793,
 'recall': 0.45977076721224386,
 'support': 1726}
micro
{'f1-score': 0.906720741599073,
 'precision': 0.906720741599073,
 'recall': 0.906720741599073,
 'support': 1726}
weighted
{'f1-score': 0.8932926545904529,
 'precision': 0.8806819230369507,
 'recall': 0.906720741599073,
 'support': 1726}
### report_full
macro
{'f1-score': 0.4176111047332086,
 'precision': 0.47045660749322793,
 'recall': 0.38575369685394206,
 'support': 1992}
micro
{'f1-score': 0.8418504572350727,
 'precision': 0.906720741599073,
 'recall': 0.7856425702811245,
 'support': 1992}
weighted
{'f1-score': 0.7966695118646263,
 'precision': 0.81382728804914,
 'recall': 0.7856425702811245,
 'support': 1992}
```

## javascript
### Summary
49 rules, avg.len. 5.9

| | |
|-|-|
|Min support|134|
|Max support|2763|
|Min confidence|0.8026556968688965|
|Max confidence|0.9993403553962708|

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
                     'base_model_name': 'sklearn.ensemble.RandomForestClassifier',
                     'confidence_threshold': 0.8,
                     'min_samples_leaf': 90,
                     'min_samples_split': 181,
                     'n_estimators': 10,
                     'prune_attributes': True,
                     'prune_branches_algorithms': ['reduced-error'],
                     'prune_dataset_ratio': 0.2,
                     'top_down_greedy_budget': [False, 0.5]}}
```

### Rules

| rule number | description |
|----:|:-----|
| 1 | `  ^1.internal_type = MemberExpression<br>⇒ y = ∅<br>Confidence: 0.989. Support: 2308.` |
| 2 | `  -1.internal_type = StringLiteral<br>	∧ ^1.internal_type not in {MemberExpression}<br>⇒ y = '<br>Confidence: 0.811. Support: 420.` |
| 3 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ +1.roles in {STRING}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {MemberExpression}<br>⇒ y = '<br>Confidence: 0.997. Support: 158.` |
| 4 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ +1.roles not in {STRING}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {MemberExpression}<br>⇒ y = ∅<br>Confidence: 0.999. Support: 535.` |
| 5 | `  -1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = =<br>	∧ +1.length ≤ 1<br>	∧ ^1.internal_type not in {MemberExpression}<br>⇒ y = ␣<br>Confidence: 0.998. Support: 280.` |
| 6 | `  -1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = {<br>	∧ +1.length ≤ 1<br>	∧ ^1.internal_type not in {MemberExpression}<br>⇒ y = ␣<br>Confidence: 0.913. Support: 293.` |
| 7 | `  -1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.925. Support: 2702.` |
| 8 | `  ^1.roles in {QUALIFIED}<br>⇒ y = ∅<br>Confidence: 0.992. Support: 2386.` |
| 9 | `  -1.internal_type = StringLiteral<br>	∧ ^1.roles not in {QUALIFIED}<br>⇒ y = '<br>Confidence: 0.826. Support: 450.` |
| 10 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ +1.internal_type = StringLiteral<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {QUALIFIED}<br>⇒ y = '<br>Confidence: 0.997. Support: 172.` |
| 11 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {QUALIFIED}<br>⇒ y = ∅<br>Confidence: 0.999. Support: 527.` |
| 12 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.label in {<space>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ +1.internal_type = StringLiteral<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {QUALIFIED}<br>⇒ y = '<br>Confidence: 0.866. Support: 145.` |
| 13 | `  -1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = =<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {QUALIFIED}<br>⇒ y = ␣<br>Confidence: 0.998. Support: 268.` |
| 14 | `  -1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = {<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {QUALIFIED}<br>⇒ y = ␣<br>Confidence: 0.911. Support: 264.` |
| 15 | `  -1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.internal_type not in {BinaryExpression}<br>	∧ ^1.roles not in {QUALIFIED}<br>⇒ y = ∅<br>Confidence: 0.920. Support: 2679.` |
| 16 | `  -1.internal_type = StringLiteral<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^2.roles not in {INITIALIZATION}<br>⇒ y = '<br>Confidence: 0.955. Support: 302.` |
| 17 | `  ^1.roles in {IDENTIFIER}<br>⇒ y = ∅<br>Confidence: 0.993. Support: 2241.` |
| 18 | `  -1.internal_type = StringLiteral<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = '<br>Confidence: 0.820. Support: 446.` |
| 19 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ +1.roles in {STRING}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = '<br>Confidence: 0.996. Support: 134.` |
| 20 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ +1.roles not in {STRING}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ∅<br>Confidence: 0.999. Support: 556.` |
| 21 | `  -1.diff_offset ≥ 3<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(, ;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ +2.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.963. Support: 416.` |
| 22 | `  -1.diff_offset ≤ 2<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = =<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ +2.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.997. Support: 178.` |
| 23 | `  -1.diff_offset ≤ 2<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ,<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ +2.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.853. Support: 160.` |
| 24 | `  -1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = =<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.998. Support: 289.` |
| 25 | `  -1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = {<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.888. Support: 254.` |
| 26 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.roles in {EXPRESSION}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.988. Support: 1664.` |
| 27 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ +1.reserved = (<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER}<br>⇒ y = ␣<br>Confidence: 0.805. Support: 151.` |
| 28 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ +1.reserved not in {(, =, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.895. Support: 951.` |
| 29 | `  -1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {OPERATOR, QUALIFIED}<br>⇒ y = ∅<br>Confidence: 0.915. Support: 2763.` |
| 30 | `  -1.internal_type = StringLiteral<br>	∧ -1.reserved not in {;}<br>	∧ ^1.roles not in {QUALIFIED}<br>	∧ ^2.roles not in {INITIALIZATION}<br>⇒ y = '<br>Confidence: 0.954. Support: 292.` |
| 31 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ +1.internal_type = StringLiteral<br>	∧ +1.roles not in {KEY}<br>	∧ ^1.roles not in {QUALIFIED}<br>⇒ y = '<br>Confidence: 0.997. Support: 192.` |
| 32 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {;}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles in {OPERATOR} and not in {QUALIFIED}<br>⇒ y = ␣<br>Confidence: 0.844. Support: 600.` |
| 33 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {;}<br>	∧ -1.roles in {EXPRESSION}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = =<br>	∧ ^1.roles not in {OPERATOR, QUALIFIED}<br>⇒ y = ␣<br>Confidence: 0.996. Support: 142.` |
| 34 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {;}<br>	∧ -1.roles in {EXPRESSION}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=}<br>	∧ ^1.roles not in {OPERATOR, QUALIFIED}<br>⇒ y = ∅<br>Confidence: 0.958. Support: 1675.` |
| 35 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = (<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ ^1.roles not in {OPERATOR, QUALIFIED}<br>⇒ y = ∅<br>Confidence: 0.999. Support: 758.` |
| 36 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(, ;}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = ;<br>	∧ ^1.roles not in {OPERATOR, QUALIFIED}<br>⇒ y = ∅<br>Confidence: 0.999. Support: 403.` |
| 37 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.reserved = )<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.997. Support: 152.` |
| 38 | `  -1.diff_offset ≤ 1<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {IDENTIFIER, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.902. Support: 947.` |
| 39 | `  -1.internal_type = StringLiteral<br>	∧ ^1.roles not in {QUALIFIED}<br>	∧ ^2.roles not in {LITERAL}<br>⇒ y = '<br>Confidence: 0.953. Support: 308.` |
| 40 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ +2.length ≥ 2<br>	∧ +3.length ≥ 4<br>	∧ ^1.roles not in {QUALIFIED}<br>⇒ y = ∅<br>Confidence: 0.864. Support: 143.` |
| 41 | `  •••start_col ≥ 16<br>	∧ -1.internal_type not in {StringLiteral}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {OPERATOR, QUALIFIED}<br>⇒ y = ∅<br>Confidence: 0.963. Support: 2281.` |
| 42 | `  •••start_col ≤ 15<br>	∧ -1.internal_type = Identifier<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {OPERATOR, QUALIFIED}<br>⇒ y = ∅<br>Confidence: 0.998. Support: 242.` |
| 43 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ +1.internal_type not in {StringLiteral}<br>	∧ +1.length ≥ 2<br>	∧ +2.length ≤ 1<br>	∧ ^1.internal_type not in {MemberExpression}<br>⇒ y = ␣<br>Confidence: 0.803. Support: 1092.` |
| 44 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.roles in {EXPRESSION}<br>	∧ +1.reserved not in {=, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.990. Support: 1590.` |
| 45 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ +1.reserved = (<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.internal_type not in {MemberExpression}<br>⇒ y = ␣<br>Confidence: 0.823. Support: 144.` |
| 46 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ +1.reserved not in {(, =, {, }}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.895. Support: 1002.` |
| 47 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved = ;<br>	∧ +1.reserved not in {=, {}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {QUALIFIED}<br>⇒ y = ⏎␣⁻␣⁻<br>Confidence: 0.805. Support: 151.` |
| 48 | `  -1.internal_type = Identifier<br>	∧ -1.reserved not in {;}<br>	∧ -3.diff_line ≥ 1<br>	∧ +1.reserved not in {=, {}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {OPERATOR, QUALIFIED}<br>⇒ y = ∅<br>Confidence: 0.992. Support: 197.` |
| 49 | `  -1.internal_type not in {StringLiteral}<br>	∧ -1.reserved not in {;}<br>	∧ -3.diff_line = 0<br>	∧ +1.reserved not in {=, {}<br>	∧ +1.roles not in {EXPRESSION}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {OPERATOR, QUALIFIED}<br>⇒ y = ∅<br>Confidence: 0.943. Support: 2477.` |

<details>
    <summary>Machine-readable report</summary>
```json
{"javascript": {"avg_rule_len": 5.918367346938775, "max_conf": 0.9993403553962708, "max_support": 2763, "min_conf": 0.8026556968688965, "min_support": 134, "num_rules": 49}}
```
</details>
