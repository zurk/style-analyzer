# Model report for file:///tmp/top-repos-quality-repos-44ftc19l/reveal.js HEAD 0b3e7839ebf4ed8b6c180aca0abafa28c67aee6d

### Dump

```json
{'created_at': datetime.datetime(2019, 2, 12, 21, 33, 44, 491037),
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
 'uuid': '7c08abae-ec7b-42be-9f22-264c7a719d32',
 'version': [1]}
style.format.analyzer.FormatAnalyzer/[1] file:///tmp/top-repos-quality-repos-44ftc19l/reveal.js 0b3e7839ebf4ed8b6c180aca0abafa28c67aee6d

# javascript
34 rules, avg.len. 11.3
## train
PPCR: 0.807112
### report
macro
{'f1-score': 0.7125498209654305,
 'precision': 0.7161028277497957,
 'recall': 0.7152867692770889,
 'support': 42283}
micro
{'f1-score': 0.955324835040087,
 'precision': 0.955324835040087,
 'recall': 0.955324835040087,
 'support': 42283}
weighted
{'f1-score': 0.9523323208331298,
 'precision': 0.9510145883394417,
 'recall': 0.955324835040087,
 'support': 42283}
### report_full
macro
{'f1-score': 0.5673467216191073,
 'precision': 0.7161028277497957,
 'recall': 0.51449249089462,
 'support': 52388}
micro
{'f1-score': 0.8533553041586125,
 'precision': 0.955324835040087,
 'recall': 0.7710544399480798,
 'support': 52388}
weighted
{'f1-score': 0.8364528009427759,
 'precision': 0.9421976190941532,
 'recall': 0.7710544399480798,
 'support': 52388}
## test
PPCR: 0.793419
### report
macro
{'f1-score': 0.618568401219514,
 'precision': 0.5861306385097839,
 'recall': 0.6855598104069249,
 'support': 8584}
micro
{'f1-score': 0.9538676607642125,
 'precision': 0.9538676607642125,
 'recall': 0.9538676607642125,
 'support': 8584}
weighted
{'f1-score': 0.9534857209375979,
 'precision': 0.9559673666218621,
 'recall': 0.9538676607642125,
 'support': 8584}
### report_full
macro
{'f1-score': 0.4873172467200101,
 'precision': 0.5861306385097839,
 'recall': 0.4594339623322762,
 'support': 10819}
micro
{'f1-score': 0.8439931969283101,
 'precision': 0.9538676607642125,
 'recall': 0.756816711341159,
 'support': 10819}
weighted
{'f1-score': 0.8263640253154507,
 'precision': 0.9451567918037124,
 'recall': 0.756816711341159,
 'support': 10819}
```

## javascript
### Summary
34 rules, avg.len. 11.3

| | |
|-|-|
|Min support|121|
|Max support|7233|
|Min confidence|0.805343508720398|
|Max confidence|0.9995265007019043|

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
                     'min_samples_leaf': 119,
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
| 1 | `  +1.reserved not in {)}<br>	∧ ^1.internal_type = MemberExpression<br>⇒ y = ∅<br>Confidence: 0.995. Support: 7233.` |
| 2 | `  -1.label in {<space>}<br>	∧ +1.length ≥ 9<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles in {OPERATOR}<br>⇒ y = "<br>Confidence: 0.805. Support: 131.` |
| 3 | `  -1.label not in {<space>}<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved not in {)}<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles in {OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.931. Support: 5116.` |
| 4 | `  -1.internal_type = Identifier<br>	∧ +1.reserved = =<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.999. Support: 478.` |
| 5 | `  -1.internal_type = Identifier<br>	∧ -3.reserved = (<br>	∧ +1.reserved = )<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.907. Support: 275.` |
| 6 | `  -1.internal_type = Identifier<br>	∧ -2.reserved = (<br>	∧ -3.reserved not in {(}<br>	∧ +1.reserved = )<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.998. Support: 259.` |
| 7 | `  -1.internal_type = Identifier<br>	∧ +1.reserved not in {), =}<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles in {IF} and not in {OPERATOR}<br>	∧ ^2.roles in {IF}<br>⇒ y = ∅<br>Confidence: 0.954. Support: 208.` |
| 8 | `  -1.internal_type = Identifier<br>	∧ +1.reserved not in {), =}<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles not in {IF, OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.982. Support: 3971.` |
| 9 | `  -1.internal_type not in {Identifier}<br>	∧ -1.roles not in {STRING}<br>	∧ +1.reserved = ;<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.999. Support: 1842.` |
| 10 | `  -1.internal_type not in {Identifier}<br>	∧ +1.reserved = }<br>	∧ +5.reserved not in {function}<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ⏎⇥⁻<br>Confidence: 0.837. Support: 1228.` |
| 11 | `  -1.internal_type not in {Identifier}<br>	∧ -1.reserved = {<br>	∧ +1.reserved not in {;, }}<br>	∧ +2.length ≤ 15<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ⏎⇥⁺<br>Confidence: 0.829. Support: 1217.` |
| 12 | `  -1.internal_type = CommentLine<br>	∧ -1.reserved not in {{}<br>	∧ +1.reserved not in {;, }}<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ⏎<br>Confidence: 0.987. Support: 893.` |
| 13 | `  -1.internal_type not in {CommentLine, Identifier}<br>	∧ -1.reserved not in {{}<br>	∧ +1.reserved not in {;, }}<br>	∧ +1.roles in {COMMENT}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 1.000. Support: 1056.` |
| 14 | `  -1.internal_type not in {CommentLine, Identifier}<br>	∧ -1.reserved = ;<br>	∧ +1.reserved not in {;, }}<br>	∧ +1.roles not in {COMMENT}<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles in {FILE} and not in {OPERATOR}<br>⇒ y = ⏎⏎<br>Confidence: 0.900. Support: 325.` |
| 15 | `  -1.internal_type = StringLiteral<br>	∧ -1.reserved not in {;, {}<br>	∧ -3.reserved = (<br>	∧ +1.reserved not in {;, }}<br>	∧ +1.roles not in {COMMENT}<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = '<br>Confidence: 0.999. Support: 348.` |
| 16 | `  -1.internal_type not in {CommentLine, Identifier, StringLiteral}<br>	∧ -1.label in {<space>}<br>	∧ -1.reserved not in {;, {}<br>	∧ -2.reserved = (<br>	∧ +1.reserved not in {;, }}<br>	∧ +1.roles not in {COMMENT}<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = '<br>Confidence: 0.999. Support: 421.` |
| 17 | `  -1.internal_type not in {CommentLine, Identifier, StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {{}<br>	∧ +1.reserved = ,<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.993. Support: 480.` |
| 18 | `  -1.internal_type not in {CommentLine, Identifier, StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {;, {}<br>	∧ -2.label in {<-tab>}<br>	∧ +1.reserved not in {,, ;, else, }}<br>	∧ +1.roles not in {COMMENT}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ⏎⏎<br>Confidence: 0.816. Support: 562.` |
| 19 | `  -1.internal_type not in {CommentLine, Identifier, StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved = (<br>	∧ -2.diff_col ≥ 3<br>	∧ -2.internal_type = Identifier<br>	∧ -2.label not in {<-tab>}<br>	∧ -4.length ≥ 5<br>	∧ +1.internal_type = StringLiteral<br>	∧ +1.reserved not in {,, }}<br>	∧ +1.roles not in {COMMENT}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.884. Support: 382.` |
| 20 | `  -1.internal_type not in {CommentLine, Identifier, StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved = (<br>	∧ -2.diff_col ≥ 3<br>	∧ -2.internal_type not in {Identifier}<br>	∧ -2.label not in {<-tab>}<br>	∧ +1.reserved not in {,, }}<br>	∧ +1.roles not in {COMMENT}<br>	∧ +1.length ≥ 2<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.994. Support: 386.` |
| 21 | `  -1.internal_type not in {CommentLine, Identifier, StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved = (<br>	∧ -2.diff_col ≤ 2<br>	∧ -2.label not in {<-tab>}<br>	∧ +1.reserved not in {,, }}<br>	∧ +1.length ≥ 2<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.919. Support: 339.` |
| 22 | `  -1.internal_type not in {CommentLine, Identifier, StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved = (<br>	∧ -2.label not in {<-tab>}<br>	∧ +1.reserved = )<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.999. Support: 460.` |
| 23 | `  -1.internal_type not in {CommentLine, Identifier, StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved = (<br>	∧ -2.label not in {<-tab>}<br>	∧ -3.diff_offset ≤ 5<br>	∧ +1.reserved not in {), ,, }}<br>	∧ +1.length ≤ 1<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.822. Support: 121.` |
| 24 | `  •••start_col ≥ 16<br>	∧ -1.internal_type not in {CommentLine, Identifier, StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ -2.label not in {<-tab>}<br>	∧ +1.reserved not in {,, ;, }}<br>	∧ +1.roles in {KEY} and not in {COMMENT}<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ⏎<br>Confidence: 0.908. Support: 300.` |
| 25 | `  -1.diff_col ≥ 9<br>	∧ -1.diff_offset ≥ 8<br>	∧ -1.internal_type not in {CommentLine, Identifier, StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ -2.label not in {<-tab>}<br>	∧ +1.reserved not in {,, ;, }}<br>	∧ +1.roles not in {KEY}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.997. Support: 148.` |
| 26 | `  -1.diff_col ≥ 9<br>	∧ -1.diff_offset ≤ 7<br>	∧ -1.internal_type not in {CommentLine, Identifier, StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ -2.label not in {<-tab>}<br>	∧ +1.reserved not in {,, ;, }}<br>	∧ +1.roles not in {COMMENT}<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ⏎<br>Confidence: 0.864. Support: 165.` |
| 27 | `  •••start_col ≤ 5<br>	∧ -1.diff_col ≤ 8<br>	∧ -1.internal_type not in {CommentLine, Identifier, StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, {}<br>	∧ -2.label not in {<-tab>}<br>	∧ -2.length ≤ 4<br>	∧ +1.reserved = (<br>	∧ +1.roles not in {KEY}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.969. Support: 147.` |
| 28 | `  -1.diff_col ≤ 8<br>	∧ -1.internal_type not in {CommentLine, Identifier, StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ -1.roles in {EXPRESSION}<br>	∧ -2.label not in {<-tab>, <space>}<br>	∧ +1.reserved not in {(, ,, ;, }}<br>	∧ +1.roles not in {KEY}<br>	∧ +2.roles not in {COMMENT}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ∅<br>Confidence: 0.946. Support: 121.` |
| 29 | `  -1.diff_col ≤ 8<br>	∧ -1.internal_type not in {CommentLine, Identifier, StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {{}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -2.label not in {<-tab>}<br>	∧ -3.diff_offset ≥ 5<br>	∧ +1.reserved = {<br>	∧ +1.roles not in {COMMENT, KEY}<br>	∧ +2.roles not in {COMMENT}<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles in {STATEMENT} and not in {OPERATOR, VARIABLE}<br>⇒ y = ␣<br>Confidence: 0.999. Support: 658.` |
| 30 | `  -1.diff_col ≤ 8<br>	∧ -1.internal_type not in {CommentLine, Identifier, StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -2.label not in {<-tab>}<br>	∧ -2.length ≥ 3<br>	∧ -3.diff_offset ≥ 5<br>	∧ +1.reserved not in {(, ,, ;, {, }}<br>	∧ +1.roles not in {COMMENT, KEY}<br>	∧ +2.roles not in {COMMENT}<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles in {STATEMENT} and not in {OPERATOR, VARIABLE}<br>⇒ y = ␣<br>Confidence: 0.915. Support: 866.` |
| 31 | `  -1.diff_col ≤ 8<br>	∧ -1.internal_type not in {CommentLine, Identifier, StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -2.label in {<space>} and not in {<-tab>}<br>	∧ -2.length ≤ 2<br>	∧ -3.diff_offset ≥ 5<br>	∧ +1.reserved not in {(, ,, ;, {, }}<br>	∧ +1.roles not in {COMMENT, KEY}<br>	∧ +2.roles not in {COMMENT}<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles in {STATEMENT} and not in {OPERATOR, VARIABLE}<br>⇒ y = ␣<br>Confidence: 0.874. Support: 178.` |
| 32 | `  -1.diff_col ≤ 8<br>	∧ -1.internal_type not in {CommentLine, Identifier, StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -2.label not in {<-tab>}<br>	∧ -3.diff_offset ≥ 5<br>	∧ +1.reserved not in {(, ,, ;, }}<br>	∧ +1.roles not in {COMMENT, KEY}<br>	∧ +2.roles not in {COMMENT}<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles not in {OPERATOR, STATEMENT}<br>⇒ y = ␣<br>Confidence: 0.961. Support: 2803.` |
| 33 | `  -1.diff_col ≤ 8<br>	∧ -1.internal_type not in {CommentLine, Identifier, StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {{}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -2.label not in {<-tab>}<br>	∧ -3.diff_offset ≤ 4<br>	∧ +1.reserved = {<br>	∧ +1.roles not in {COMMENT, KEY}<br>	∧ +2.roles not in {COMMENT}<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles not in {OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.998. Support: 330.` |
| 34 | `  -1.diff_col ≤ 8<br>	∧ -1.internal_type not in {CommentLine, Identifier, StringLiteral}<br>	∧ -1.label not in {<space>}<br>	∧ -1.reserved not in {(, ;, {}<br>	∧ -1.roles not in {EXPRESSION}<br>	∧ -2.label not in {<-tab>}<br>	∧ -3.diff_offset ≤ 4<br>	∧ +1.reserved not in {(, ,, ;, {, }}<br>	∧ +1.roles not in {COMMENT, KEY}<br>	∧ +2.roles not in {COMMENT}<br>	∧ ^1.internal_type not in {MemberExpression}<br>	∧ ^1.roles in {EXPRESSION} and not in {OPERATOR}<br>⇒ y = ␣<br>Confidence: 0.861. Support: 350.` |

<details>
    <summary>Machine-readable report</summary>
```json
{"javascript": {"avg_rule_len": 11.323529411764707, "max_conf": 0.9995265007019043, "max_support": 7233, "min_conf": 0.805343508720398, "min_support": 121, "num_rules": 34}}
```
</details>
