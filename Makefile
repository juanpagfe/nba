# A Makefile for commands I run frequently:

clean:
	rm -rf dist
	rm -rf nba.egg-info
	rm -rf nba/__pycache__

build: clean
	poetry build

install: clean build
	rm dist/nba-*-py2*
	pip3 install dist/nba-*
