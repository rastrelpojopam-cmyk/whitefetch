Name:           whitefetch
Version:        1.0.0
Release:        3%{?dist}
Summary:        Custom system information fetch tool written in Python

License:        MIT
URL:            https://github.com
BuildArch:      noarch

Requires:       python3
Requires:       python3-psutil

%description
A lightweight and beautiful system information fetch tool optimized for Fedora Linux.

%prep
cp %{_sourcedir}/whitefetch .

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 whitefetch %{buildroot}%{_bindir}/whitefetch

%files
# Ключевое исправление: принудительно задаем права 755 (запуск для всех)
%attr(0755, root, root) %{_bindir}/whitefetch

%changelog
* Wed Jul 01 2026 Artem <rastrelpojopam@gmail.com> - 1.0.0-2
- Fix global execution permissions for all users
