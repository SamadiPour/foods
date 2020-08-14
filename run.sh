rm -r build/
rm -r dist/
rm -r *.egg-info/
python setup.py bdist_wheel
yes | python -m pip uninstall pfood
python -m pip install dist/$(ls dist/ | grep ".whl")