.PHONY: demo clean dist

demo:
	make -C demo/ demo

clean:
	-rm -rf dist/*
	-rm -rf build/*

dist:
	python setup.py sdist bdist_wheel
