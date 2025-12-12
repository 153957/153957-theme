.PHONY: test
test: rufftest typingtest unittest

.PHONY: rufftest
rufftest:
	uv run ruff check .
	uv run ruff format --check .

.PHONY: typingtest
typingtest:
	uv run ty check

.PHONY: unittest
unittest:
	uv run python -m unittest

.PHONY: clean
clean:
	rm -rf dist

.PHONY: publish
publish:
	uv build
	uv publish

.PHONY: demo
demo:
	make -C demo/ demo
