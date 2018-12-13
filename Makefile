current_dir = $(shell pwd)

PROJECT = style-analyzer

DOCKERFILES = Dockerfile:$(PROJECT)
DOCKER_ORG = "srcd"

# Including ci Makefile
CI_REPOSITORY ?= https://github.com/src-d/ci.git
CI_BRANCH ?= v1
CI_PATH ?= .ci
MAKEFILE := $(CI_PATH)/Makefile.main
$(MAKEFILE):
	git clone --quiet --depth 1 -b $(CI_BRANCH) $(CI_REPOSITORY) $(CI_PATH);
-include $(MAKEFILE)

check:
	! grep -R /tmp lookout/style/*/tests
	flake8 --count
	pylint lookout

docker-test:
	docker ps | grep bblfshd  # bblfsh server should be run. Try `make bblfsh-start` command.
	docker run --rm -it --network host \
		-v $(current_dir)/.git:/style-analyzer/.git \
		-v $(current_dir)/lookout/core/server:/style-analyzer/lookout/core/server \
		--entrypoint python3 -w /style-analyzer \
			srcd/style-analyzer:test -m unittest discover

bblfsh-start:
	! docker ps | grep bblfshd # bblfsh server has been run already.
	docker run -d --rm --name style_analyzer_bblfshd --privileged -p 9432\:9432 \
		bblfsh/bblfshd\:v2.10.0
	docker exec style_analyzer_bblfshd bblfshctl driver install \
		javascript docker://bblfsh/javascript-driver\:v1.2.0

REPORTS_DIR ?= reports
REPORT_VERSION ?= untagged
REPORT_DIR ?= $(REPORTS_DIR)/$(REPORT_VERSION)
SMOKE_REPORT_DIR ?= $(REPORT_DIR)/js_smoke
NOISY_REPORT_DIR ?= $(REPORT_DIR)/noisy
QUALITY_REPORT_DIR ?= $(REPORT_DIR)/quality
SMOKE_INIT ?= ./lookout/style/format/benchmarks/data/js_smoke_init.tar.xz

$(SMOKE_REPORT_DIR) $(NOISY_REPORT_DIR) $(QUALITY_REPORT_DIR):
	mkdir -p $@
report-smoke: $(SMOKE_REPORT_DIR)
	python3 -m lookout.style.format gen-smoke-dataset $(SMOKE_INIT) $(SMOKE_REPORT_DIR)/dataset \
		2>&1 | tee $(SMOKE_REPORT_DIR)/dataset_logs.txt
	python3 -m lookout.style.format eval-smoke-dataset $(SMOKE_REPORT_DIR)/dataset \
		$(SMOKE_REPORT_DIR)/report 2>&1 | tee $(SMOKE_REPORT_DIR)/report_logs.txt
report-noisy: $(NOISY_REPORT_DIR)
	python3 -m lookout.style.format quality-report-noisy -o $(NOISY_REPORT_DIR) \
		2>&1 | tee $(NOISY_REPORT_DIR)/logs.txt
report-noisy: $(NOISY_REPORT_DIR)/youfile.md
report-quality: $(QUALITY_REPORT_DIR)
	python3 -m lookout.style.format.benchmarks.top_repos_quality -o $(QUALITY_REPORT_DIR) \
		2>&1 | tee $(QUALITY_REPORT_DIR)/logs.txt
report-release: report-smoke report-noisy report-quality

.PHONY: check docker-test bblfsh-start report-smoke report-noisy report-quality report-release
