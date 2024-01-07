FLASK := python3 -m flask run --host=0.0.0.0

run:
	$(FLASK) --port=5000 --no-debug

dev:
	$(FLASK) --port=5010 --debug


AUTOSTART_FILE := $(HOME)/.config/autostart/wathiq.desktop
GIT_VERSION := $(shell git describe --abbrev --dirty --always --tags)
install_startup:
	cp wathiq.desktop "$(AUTOSTART_FILE)"
	sed -i "s|<WATHIQ_DIR>|$(PWD)|g" "$(AUTOSTART_FILE)"
	sed -i "s|<VERSION>|$(GIT_VERSION)|g" "$(AUTOSTART_FILE)"
	chmod 664 "$(AUTOSTART_FILE)"
