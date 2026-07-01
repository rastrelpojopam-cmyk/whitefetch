Name:           whitefetch
Version:        1.0.0
Release:        4%{?dist}
Summary:        Custom system information fetch tool written in Python

License:        MIT
URL:            https://github.com
BuildArch:      noarch

Requires:       python3
Requires:       python3-psutil

%description
A lightweight and beautiful system information fetch tool optimized for Fedora Linux.

%prep
# Для GitHub-репозиториев секцию подготовки оставляем пустой, файлы уже на месте
%build

%install
mkdir -p %{buildroot}%{_bindir}
# Файл whitefetch уже находится в рабочей папке сборщика, просто устанавливаем его
install -p -m 755 whitefetch %{buildroot}%{_bindir}/whitefetch

%files
%attr(0755, root, root) %{_bindir}/whitefetch

%changelog
* Wed Jul 01 2026 Artem <rastrelpojopam@gmail.com> - 1.0.0-4
- Fix cloud build paths for Fedora Copr
