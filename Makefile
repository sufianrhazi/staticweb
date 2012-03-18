all:
	scripts/build.sh

setup:
	mkdir -p ./lib/python
	PYTHONPATH=./lib/python easy_install -d ./lib/python jinja2
	mkdir -p ./lib/ruby
	gem install sass --prerelease --install-dir ./lib/ruby

clean:
	rm -f www/css/*.css
	rm -f www/*.html

.PHONY: all clean setup
