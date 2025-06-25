Name:           vop
Version:        1.4.0 
Release:        1%{?dist}
Summary: The vop password generator       

Group: Utilities
License: Apache-2.0       
URL: https://github.com/MatthewBuchananAstley/vop            
Source0: %{name}-%{version}.tar.gz 
Packager: Matthew Buchanan Astley - <mbastley@gmail.com,matthewbuchanan@astley.nl>      

#BuildRequires:
#Requires: python3      
BuildArch: noarch

%description
The vop password generator provides modern quantum safe passwords. Modern passwords need to have at least one uppercase, a lowercase and a special character or more and be of sufficient length. The option of selecting a password from a list of passwords further increases the security.  

%prep
%setup -q

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp %{name} $RPM_BUILD_ROOT/%{_bindir}
cp pw $RPM_BUILD_ROOT/%{_bindir}
cp t3 $RPM_BUILD_ROOT/%{_bindir}
cp Password_entropy_verifier.py $RPM_BUILD_ROOT/%{_bindir}

# --- NEW ADDITIONS FOR SBOM AND CHECKSUM ---

# Create a dedicated directory for SBOM files
# It's common practice to put metadata like SBOMs under /usr/share/doc/<package_name>/sbom/
mkdir -p %{buildroot}%{_docdir}/%{name}/sbom

# Define the desired final filenames for clarity
# This assumes your repo name is 'vop', so the SBOM would be 'vop-sbom.spdx.json'
# Adjust if your GitHub Action is using a different base name for the SBOM.
# E.g., if it uses 'list-fs-files-sbom.spdx.json', use that here instead.
%define sbom_json_filename %{name}-sbom.spdx.json
%define sbom_sha256_filename %{name}-sbom.spdx.json.sha256

# Copy the SBOM JSON file from the _manifest/spdx_2.2/ directory within the source tree
# and rename it to the desired final name in the RPM.
# IMPORTANT: This assumes _manifest/spdx_2.2/manifest.spdx.json exists in your source tarball.
install -p -m 644 _manifest/spdx_2.2/manifest.spdx.json %{buildroot}%{_docdir}/%{name}/sbom/%{sbom_json_filename}

# Copy the SHA256 checksum file.
# IMPORTANT: This assumes _manifest/spdx_2.2/manifest.spdx.json.sha256 exists in your source tarball.
install -p -m 644 _manifest/spdx_2.2/manifest.spdx.json.sha256 %{buildroot}%{_docdir}/%{name}/sbom/%{sbom_sha256_filename}

# --- END NEW ADDITIONS ---


%files
%{_bindir}/%{name}
%{_bindir}/pw
%{_bindir}/t3
%{_bindir}/Password_entropy_verifier.py

%license LICENCE.md 
%doc CHANGELOG.md COPYRIGHT.md README.md SECURITY.md

# --- NEW ADDITIONS TO %files ---
# Declare the SBOM directory as documentation
%docdir %{_docdir}/%{name}/sbom

# List the SBOM files to be included in the package
%{_docdir}/%{name}/sbom/%{sbom_json_filename}
%{_docdir}/%{name}/sbom/%{sbom_sha256_filename}
# --- END NEW ADDITIONS ---

%changelog
* Wed Jun 18 2025 Matthew Buchanan Astley <matthewbuchanan@astley.nl, mbastley@gmail.com>
- 
