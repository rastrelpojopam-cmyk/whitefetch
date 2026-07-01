Name:           whitefetch
Version:        1.0.0
Release:        5%{?dist}
Summary:        Custom system information fetch tool written in Python

License:        MIT
URL:            https://github.com/rastrelpojopam-cmyk/whitefetch
BuildArch:      noarch

Requires:       python3
Requires:       python3-psutil

%description
A lightweight and beautiful system information fetch tool optimized for Fedora Linux.

%prep
# Создаем и изолируем рабочую директорию сборщика в облаке
%autosetup -c -T
# Копируем файл из репозитория в эту директорию
cp %{_builddir}/whitefetch-%{version}/../whitefetch .

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 whitefetch %{buildroot}%{_bindir}/whitefetch

%files
%attr(0755, root, root) %{_bindir}/whitefetch

%changelog
* Wed Jul 01 2026 Artem <rastrelpojopam@gmail.com> - 1.0.0-5
- Add proper autosetup and directory setup for cloud builds
