%{?scl:%scl_package xz-java}
%{!?scl:%global pkg_name %{name}}
%{!?maven_scl:%global maven_scl_prefix  %{nil}}

Name:           %{?scl_prefix}xz-java
Version:        1.5
Release:        1.bootstrap1.2%{?dist}
Summary:        Java implementation of XZ data compression
License:        Public Domain
URL:            http://tukaani.org/xz/java.html
BuildArch:      noarch

Source0:        http://tukaani.org/xz/xz-java-%{version}.zip

BuildRequires:  jpackage-utils
BuildRequires:  	java-1.7.0-openjdk-devel
BuildRequires:  %{maven_scl_prefix}ant

Requires:       jpackage-utils
Requires:       java

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
%setup -q -c %{pkg_name}-%{version}

%build
scl enable %{scl} - <<"EOF"
unset ANT_HOME
# During documentation generation the upstream build.xml tries to download
# package-list from oracle.com. Create a dummy package-list to prevent that.
mkdir -p extdoc && touch extdoc/package-list

ant maven
EOF

%install
scl enable %{scl} - <<"EOF"
# jar
install -dm 755 %{buildroot}%{_javadir}
install -m 644 build/jar/xz.jar %{buildroot}%{_javadir}/%{pkg_name}.jar
ln -sf %{pkg_name}.jar %{buildroot}%{_javadir}/xz.jar
# javadoc
install -dm 755 %{buildroot}%{_javadocdir}
cp -R build/doc %{buildroot}%{_javadocdir}/%{pkg_name}
# pom
install -dm 755 %{buildroot}%{_mavenpomdir}
install -pm 644 build/maven/xz-%{version}.pom %{buildroot}/%{_mavenpomdir}/JPP-%{pkg_name}.pom
%add_maven_depmap
EOF

%files -f .mfiles
%doc COPYING README THANKS
%{_javadir}/xz.jar

%files javadoc
%doc COPYING
%{_javadocdir}/%{pkg_name}

%changelog
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
