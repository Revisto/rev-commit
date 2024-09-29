#!/bin/sh

install() {
    echo "Installing rev-commit..."
    pip3 install .
    echo "Installation complete."
}
uninstall() {
    echo "Uninstalling rev-commit..."
    pip3 uninstall -y rev-commit
    echo "Uninstallation complete."
}
case "$1" in
    install)
        install
        ;;
    uninstall)
        uninstall
        ;;
    *)
        echo "Usage: $0 {install|uninstall}"
        exit 1
        ;;
esac