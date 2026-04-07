Summary:    Official SwiftOS operating system logos and graphics
Name:       swift-os-logos
Version:    1
Release:    1%{?dist}
License:    MIT
BuildArch:  noarch

# --- SOURCES ---
Source0:    swift-os-logo.svg
Source1:    swift-os-logo-text.svg
Source2:    swift-os-logo256.png
Source3:    swift-os-logo128.png
Source4:    swift-os-logo48.png
Source5:    swift-os-logo16.png
Source6:    swift-os-logo-symbolic.svg
Source7:    swift-os-logo-white.svg
Source8:    swift-os-logo-text-white.svg
Source9:    swift-os-logo-text-color.svg
Source10:   swift-os-logo-transparent.svg

# --- CONFLICTS & COMPATIBILITY ---
Conflicts:  fedora-logos
Conflicts:  generic-logos
Provides:   system-logos = %{version}-%{release}
Provides:   fedora-logos = 44

%description
Official branding assets for the SwiftOS operating system. 
All files are namespaced with 'swift-os' to prevent conflicts 
with desktop environment icons. Legacy paths are symlinked.

%install
install -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -d %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
install -d %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -d %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -d %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -d %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps
install -d %{buildroot}%{_datadir}/pixmaps
install -d %{buildroot}%{_datadir}/fedora-logos

install -m 0644 %{SOURCE0} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/swift-os-logo.svg
install -m 0644 %{SOURCE10} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/swift-os-logo-transparent.svg
install -m 0644 %{SOURCE5} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/swift-os-logo.png
install -m 0644 %{SOURCE4} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/swift-os-logo.png
install -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/swift-os-logo.png
install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/swift-os-logo.png
install -m 0644 %{SOURCE6} %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/swift-os-logo-symbolic.svg
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/swift-os-logo-text.svg
install -m 0644 %{SOURCE9} %{buildroot}%{_datadir}/pixmaps/swift-os-logo-text-color.svg

# Create SYMBOLIC LINKS for Fedora compatibility
ln -s ../icons/hicolor/scalable/apps/swift-os-logo.svg %{buildroot}%{_datadir}/fedora-logos/fedora-logo-sprite.svg
ln -s ../pixmaps/swift-os-logo-text-color.svg %{buildroot}%{_datadir}/fedora-logos/fedora-logo-text.svg

%files
%{_datadir}/icons/hicolor/*/apps/swift-os-logo*
%{_datadir}/pixmaps/swift-os-logo*

%dir %{_datadir}/fedora-logos
%{_datadir}/fedora-logos/fedora-logo-text.svg
%{_datadir}/fedora-logos/fedora-logo-sprite.svg

%changelog
* Tue Apr 07 2026 Kamil Machowski <https://github.com/Emkamil> - 1.0.0-1
- Initial release with 'swift-os' namespace
- All system assets renamed to prevent swift-desktop icon conflicts
- Symbolic links implemented for legacy path compatibility
