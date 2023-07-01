.PHONY: ruffinstall
ruffinstall:
	pip install --upgrade pip
	pip install --upgrade --upgrade-strategy eager -r requirements-ruff.txt

.PHONY: devinstall
devinstall:
	pip install --upgrade pip
	pip install --upgrade --upgrade-strategy eager --editable .[dev]

.PHONY: test
test: rufftest

.PHONY: rufftest
rufftest:
	ruff .

.PHONY: clean
clean:
	rm -rf dist

.PHONY: publish
publish:
	flit publish

.PHONY: demo
demo:
	make -C demo/ demo
