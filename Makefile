run:
	python3 app.py


AUTOSTART_FILE := $(HOME)/.config/autostart/wathiq.desktop
GIT_VERSION := $(shell git describe --abbrev --dirty --always --tags)
install_startup:
	cp wathiq.desktop "$(AUTOSTART_FILE)"
	sed -i "s|<WATHIQ_DIR>|$(PWD)|g" "$(AUTOSTART_FILE)"
	sed -i "s|<VERSION>|$(GIT_VERSION)|g" "$(AUTOSTART_FILE)"
	chmod 664 "$(AUTOSTART_FILE)"
