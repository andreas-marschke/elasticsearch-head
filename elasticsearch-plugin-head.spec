%define debug_package %{nil}
%define base_install_dir %{_javadir}/%{name}
%define site_install_dir %{base_install_dir}/plugins/head/_site
# Avoid running brp-java-repack-jars
%define __os_install_post %{nil}

Name:           elasticsearch-plugin-head
Version:        1.0git.afced97
Release:        1%{?dist}
Summary:        ElasticSearch plugin to use Head

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://github.com/Aconex/elasticsearch-head

Source0:                https://github.com/downloads/andreas-marschke/elasticsearch-head/elasticsearch-plugin-head-1.0~git-afced97.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       elasticsearch >= 0.19

%description
A web front end for an elastic search cluster.

%prep
rm -fR %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
cd %{name}-%{version}
%{__mkdir} -p plugins
unzip %{SOURCE0} -d plugins/head

%build
true

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}
%{__mkdir} -p %{buildroot}/%{site_install_dir}
%{__mkdir} -p %{buildroot}/%{site_install_dir}/lib
%{__mkdir} -p %{buildroot}/%{site_install_dir}/lib/es
%{__mkdir} -p %{buildroot}/%{site_install_dir}/lib/es/test
%{__mkdir} -p %{buildroot}/%{site_install_dir}/lib/es/test/index_generators
%{__mkdir} -p %{buildroot}/%{site_install_dir}/lib/es/images
%{__mkdir} -p %{buildroot}/%{site_install_dir}/lib/dateRangeParser
%{__mkdir} -p %{buildroot}/%{site_install_dir}/lib/jsacx
%{__mkdir} -p %{buildroot}/%{site_install_dir}/lib/jsacx/test
%{__mkdir} -p %{buildroot}/%{site_install_dir}/lib/jsacx/test/functional
%{__mkdir} -p %{buildroot}/%{site_install_dir}/lib/jsacx/src
%{__mkdir} -p %{buildroot}/%{site_install_dir}/lib/jsacx/src/images
%{__mkdir} -p %{buildroot}/%{site_install_dir}/lib/graphael
%{__mkdir} -p %{buildroot}/%{site_install_dir}/lib/nohtml
%{__mkdir} -p %{buildroot}/%{site_install_dir}/lib/lang
%{__install} -D -m 755 plugins/head/index.html -t %{buildroot}/%{site_install_dir}/
%{__install} -D -m 755 plugins/head/README.textile -t %{buildroot}/%{site_install_dir}/
%{__install} -D -m 755 plugins/head/LICENCE -t %{buildroot}/%{site_install_dir}/
%{__install} -D -m 755 plugins/head/lib/es/widgets.js -t %{buildroot}/%{site_install_dir}/lib/es/
%{__install} -D -m 755 plugins/head/lib/es/test/browserTest.html -t %{buildroot}/%{site_install_dir}/lib/es/
%{__install} -D -m 755 plugins/head/lib/es/test/index_generators/twitter_river.sh -t %{buildroot}/%{site_install_dir}/lib/es/test/index_generators/
%{__install} -D -m 755 plugins/head/lib/es/test/index_generators/delete_all_indices.sh -t %{buildroot}/%{site_install_dir}/lib/es/test/index_generators/
%{__install} -D -m 755 plugins/head/lib/es/test/index_generators/conflictingField.sh -t %{buildroot}/%{site_install_dir}/lib/es/test/index_generators/
%{__install} -D -m 755 plugins/head/lib/es/test/index_generators/twitter_feed.sh -t %{buildroot}/%{site_install_dir}/lib/es/test/index_generators/
%{__install} -D -m 755 plugins/head/lib/es/core.js -t %{buildroot}/%{site_install_dir}/lib/es/
%{__install} -D -m 755 plugins/head/lib/es/images/expando.png -t %{buildroot}/%{site_install_dir}/lib/es/images/
%{__install} -D -m 755 plugins/head/lib/es/images/loading.gif -t %{buildroot}/%{site_install_dir}/lib/es/images/
%{__install} -D -m 755 plugins/head/lib/es/images/favicon.png -t %{buildroot}/%{site_install_dir}/lib/es/images/
%{__install} -D -m 755 plugins/head/lib/es/es.css -t %{buildroot}/%{site_install_dir}/lib/es/
%{__install} -D -m 755 plugins/head/lib/dateRangeParser/date-range-parser.js -t %{buildroot}/%{site_install_dir}/lib/dateRangeParser/
%{__install} -D -m 755 plugins/head/lib/jsacx/test/functional/PanelTest.html -t %{buildroot}/%{site_install_dir}/lib/jsacx/test/functional/
%{__install} -D -m 755 plugins/head/lib/jsacx/test/functional/menuButtonTest.html -t %{buildroot}/%{site_install_dir}/lib/jsacx/test/functional/
%{__install} -D -m 755 plugins/head/lib/jsacx/src/jsacx-widgets.js -t %{buildroot}/%{site_install_dir}/lib/jsacx/src/
%{__install} -D -m 755 plugins/head/lib/jsacx/src/jquery.js -t %{buildroot}/%{site_install_dir}/lib/jsacx/src/
%{__install} -D -m 755 plugins/head/lib/jsacx/src/jsacx-widgets.css -t %{buildroot}/%{site_install_dir}/lib/jsacx/src/
%{__install} -D -m 755 plugins/head/lib/jsacx/src/jsacx-data.js -t %{buildroot}/%{site_install_dir}/lib/jsacx/src/
%{__install} -D -m 755 plugins/head/lib/jsacx/src/jsacx.js -t %{buildroot}/%{site_install_dir}/lib/jsacx/src/
%{__install} -D -m 755 plugins/head/lib/jsacx/src/images/menu-button.gif -t %{buildroot}/%{site_install_dir}/lib/jsacx/src/images/
%{__install} -D -m 755 plugins/head/lib/jsacx/src/jsacx-fields.js -t %{buildroot}/%{site_install_dir}/lib/jsacx/src/
%{__install} -D -m 755 plugins/head/lib/nohtml/jquery.acx-nohtml.js -t %{buildroot}/%{site_install_dir}/lib/nohtml/
%{__install} -D -m 755 plugins/head/lib/lang/en_strings.js -t %{buildroot}/%{site_install_dir}/lib/lang/

%files
%defattr(-,root,root,-)
%dir %{base_install_dir}/plugins/head
%{base_install_dir}/plugins/head/*

%changelog
* Tue Aug 14 2012 Andreas Marschke 1.0git.afced97
- Initial package

