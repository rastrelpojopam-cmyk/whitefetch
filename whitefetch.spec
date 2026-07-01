Name:           whitefetch
Version:        1.0.0
Release:        6%{?dist}
Summary:        Custom system information fetch tool written in Python

License:        MIT
URL:            https://github.com
# Указываем имя нашего архива
Source0:        whitefetch-1.0.0.tar.gz
BuildArch:      noarch

Requires:       python3
Requires:       python3-psutil

%description
A lightweight and beautiful system information fetch tool optimized for Fedora Linux.

%prep
# Этот макрос автоматически распакует наш tar.gz в облаке Copr
%setup -q -c

%install
mkdir -p %{buildroot}%{_bindir}
# Устанавливаем распакованный файл скрипта
install -p -m 755 whitefetch %{buildroot}%{_bindir}/whitefetch

%files
%attr(0755, root, root) %{_bindir}/whitefetch

%changelog
* Wed Jul 01 2026 Artem <rastrelpojopam@gmail.com> - 1.0.0-6
- Switch to standard tarball source for Copr compatibility
