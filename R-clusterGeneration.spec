#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-clusterGeneration
Version  : 1.3.4
Release  : 8
URL      : https://cran.r-project.org/src/contrib/clusterGeneration_1.3.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/clusterGeneration_1.3.4.tar.gz
Summary  : Random Cluster Generation (with Specified Degree of Separation)
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n clusterGeneration

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552756518

%install
export SOURCE_DATE_EPOCH=1552756518
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library clusterGeneration
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library clusterGeneration
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library clusterGeneration
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  clusterGeneration || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/clusterGeneration/DESCRIPTION
/usr/lib64/R/library/clusterGeneration/INDEX
/usr/lib64/R/library/clusterGeneration/Meta/Rd.rds
/usr/lib64/R/library/clusterGeneration/Meta/features.rds
/usr/lib64/R/library/clusterGeneration/Meta/hsearch.rds
/usr/lib64/R/library/clusterGeneration/Meta/links.rds
/usr/lib64/R/library/clusterGeneration/Meta/nsInfo.rds
/usr/lib64/R/library/clusterGeneration/Meta/package.rds
/usr/lib64/R/library/clusterGeneration/NAMESPACE
/usr/lib64/R/library/clusterGeneration/NEWS
/usr/lib64/R/library/clusterGeneration/R/clusterGeneration
/usr/lib64/R/library/clusterGeneration/R/clusterGeneration.rdb
/usr/lib64/R/library/clusterGeneration/R/clusterGeneration.rdx
/usr/lib64/R/library/clusterGeneration/help/AnIndex
/usr/lib64/R/library/clusterGeneration/help/aliases.rds
/usr/lib64/R/library/clusterGeneration/help/clusterGeneration.rdb
/usr/lib64/R/library/clusterGeneration/help/clusterGeneration.rdx
/usr/lib64/R/library/clusterGeneration/help/paths.rds
/usr/lib64/R/library/clusterGeneration/html/00Index.html
/usr/lib64/R/library/clusterGeneration/html/R.css
