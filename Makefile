# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Makefile faylining eng oxiriga qo'shing (E'tibor bering: buyruq boshidagi bo'shliqlar TAB tugmasi bilan qo'yilishi shart)
pdf-build:
	make simplepdf
	cp "build/simplepdf/SarhadNGFW.pdf" source/_static/SarhadNGFW.pdf
	make html
	@echo "========================================================="
	@echo " PDF muvaffaqiyatli yaratildi va HTMLga ulandi!"
	@echo "========================================================="