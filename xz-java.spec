%global pkg_name xz-java
%{?scl:%scl_package %{pkg_name}}
%{?java_common_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.3
Release:        3.12%{?dist}
Summary:        Java implementation of XZ data compression
BuildArch:      noarch

License:        Public Domain
URL:            http://tukaani.org/xz/java.html
Source0:        http://tukaani.org/xz/xz-java-%{version}.zip

BuildRequires:  %{?scl_prefix}javapackages-tools
BuildRequires:  %{?scl_prefix}ant

%description
A complete implementation of XZ data compression in Java.

It features full support for the .xz file format specification version 1.0.4,
single-threaded streamed compression and decompression, single-threaded
decompression with limited random access support, raw streams (no .xz headers)
for advanced users, including LZMA2 with preset dictionary.

%package javadoc
Summary:        Javadocs for %{pkg_name}

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -q -c -n %{pkg_name}-%{version}

%build
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
# During documentation generation the upstream build.xml tries to download
# package-list from oracle.com. Create a dummy package-list to prevent that.
mkdir -p extdoc && touch extdoc/package-list

ant maven
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - <<"EOF"}
set -e -x
# jar
install -dm 755 %{buildroot}%{_javadir}
install -m 644 build/jar/xz.jar %{buildroot}%{_javadir}/%{pkg_name}.jar
ln -sf %{pkg_name}.jar %{buildroot}%{_javadir}/xz.jar
# javadoc
install -dm 755 %{buildroot}%{_javadocdir}
cp -R build/doc %{buildroot}%{_javadocdir}/%{name}
# pom
install -dm 755 %{buildroot}%{_mavenpomdir}
install -pm 644 build/maven/xz-%{version}.pom %{buildroot}/%{_mavenpomdir}/JPP-%{pkg_name}.pom
%add_maven_depmap JPP-%{pkg_name}.pom %{pkg_name}.jar
%{?scl:EOF}

%files -f .mfiles
%doc COPYING README THANKS
%{_javadir}/%{pkg_name}.jar
%{_javadir}/xz.jar

%files javadoc
%doc COPYING
%{_javadocdir}/%{name}

%changelog
* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.3-3.12
- Mass rebuild 2015-01-13

* Fri Jan 09 2015 Michal Srb <msrb@redhat.com> - 1.3-3.11
- Mass rebuild 2015-01-09

* Tue Dec 16 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-3.10
- Migrate requires and build-requires to rh-java-common

* Mon Dec 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-3.9
- Mass rebuild 2014-12-15

* Mon Dec 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-3.8
- Rebuild for rh-java-common collection

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-3.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-3.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-3.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-3.4
- Remove requires on java

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-3.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-3.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-3.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.3-3
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-2
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Tue May 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-1
- Update to upstream version 1.3

* Tue Jan 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-1
- Update to upstream version 1.2

* Thu Jan 3 2013 Krzysztof Daniel <kdaniel@redhat.com> 1.1-2
- Add patch for OSGi Manifest.

* Fri Aug 17 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-1
- Update to upstream version 1.1

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-3
- Install xz.jar symlink

* Thu Apr 5 2012 Mikolaj Izdebski <mizdebsk@redhat.com> 1.0-2
- Fix issues found during package review
- Include missing COPYING files.
- Add missing RPM group.
- Comment on touching package-list.

* Wed Apr 4 2012 Mikolaj Izdebski <mizdebsk@redhat.com> 1.0-1
- Initial packaging.
