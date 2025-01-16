.PHONY: major minor patch

major:
	./scripts/increment_version.sh major

minor:
	./scripts/increment_version.sh minor

patch:
	./scripts/increment_version.sh patch