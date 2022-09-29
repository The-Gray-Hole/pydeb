#!/bin/bash

set -e

write_file () {
cat <<EOM >$1
$2
EOM
}

PACKAGE="{{ pydeb['package-name'] }}"
DEPENDENCIES_PATH="{{ pydeb['debian-files'] }}/var/$PACKAGE/wheels"
WHEELHOUSE="dependencies-wheels"
DEP_BUILDS="dep_dists"

mkdir -p "$DEPENDENCIES_PATH"
mkdir -p "$DEP_BUILDS"
mkdir -p "$WHEELHOUSE"

cp requirements.txt "$WHEELHOUSE"
python3 -m pip download --index-url https://pypi.python.org/simple -r "$WHEELHOUSE"/requirements.txt -d "$WHEELHOUSE"
python3 setup.py bdist_wheel -d "$WHEELHOUSE"

for FILE in $(ls -p $WHEELHOUSE | grep .tar.gz$); do
  tar -zxf "$WHEELHOUSE/$FILE" -C "$DEP_BUILDS"
  rm "$WHEELHOUSE/$FILE"
done

for PACK in $(ls -p $DEP_BUILDS | grep /); do
  cd "$DEP_BUILDS/$PACK"
  python3 setup.py bdist_wheel -d ./
  cd ../../
  cp "$DEP_BUILDS/$PACK"*.whl "$WHEELHOUSE"
done

tar -zcf "$WHEELHOUSE".tar.gz "$WHEELHOUSE"
mv "$WHEELHOUSE".tar.gz "$DEPENDENCIES_PATH"

exit 0
