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

%files
%{_bindir}/%{name}
%{_bindir}/pw
%{_bindir}/t3
%{_bindir}/Password_entropy_verifier.py

%license LICENCE.md 
%doc CHANGELOG.md COPYRIGHT.md README.md SECURITY.md


%changelog
* Wed Jun 18 2025 Matthew Buchanan Astley <matthewbuchanan@astley.nl, mbastley@gmail.com>
- 
