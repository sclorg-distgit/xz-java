%{?scl:%scl_package xz-java}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}xz-java
Version:        1.6
Release:        3.1%{?dist}
Summary:        Java implementation of XZ data compression
License:        Public Domain
URL:            http://tukaani.org/xz/java.html
BuildArch:      noarch

Source0:        http://tukaani.org/xz/xz-java-%{version}.zip

BuildRequires:  %{?scl_prefix}javapackages-local
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
%setup -n %{pkg_name}-%{version} -q -c %{pkg_name}-%{version}

%mvn_file : %{pkg_name} xz

%build
# During documentation generation the upstream build.xml tries to download
# package-list from oracle.com. Create a dummy package-list to prevent that.
mkdir -p extdoc && touch extdoc/package-list

ant maven

%install
%mvn_artifact build/maven/xz-%{version}.pom build/jar/xz.jar

%mvn_install -J build/doc

%files -f .mfiles
%doc COPYING README THANKS

%files javadoc -f .mfiles-javadoc
%doc COPYING

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 1.6-3.1
- Automated package import and SCL-ization

* Tue Mar 21 2017 Michael Simacek <msimacek@redhat.com> - 1.6-3
- Install with XMvn

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 28 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-1
- Update to upstream version 1.6

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-2
- Use .mfiles generated during build

* Mon Mar 10 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.5-1
- Update to upstream version 1.5

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-2
- Use Requires: java-headless rebuild (#1067528)

* Mon Sep 23 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-1
- Update to upstream version 1.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

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
