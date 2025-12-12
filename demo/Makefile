.PHONY: serve
serve: demo
	uv run sigal serve --browser

.PHONY: demo
demo: clean
	uv run sigal build

.PHONY: clean
clean:
	rm -rf output
