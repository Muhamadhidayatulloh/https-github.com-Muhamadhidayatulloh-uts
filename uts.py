# Data
company_detail_list = [
    {
        'name': 'Company 1',
        'domain': 'Retail',
        'country': 'United States'
    },
    {
        'name': 'Company 2',
        'domain': 'Technology',
        'country': 'United Kingdom'
    },
    {
        'name': 'Company 3',
        'domain': 'Healthcare',
        'country': 'United States'
    }
]

employee_detail_list = [
    {
        'name': 'EMP-0001',
        'first_name': 'John',
        'last_name': 'Doe',
        'full_name': 'John Doe',
        'company': 'Company 1',
        'nationality': 'Australia'
    },
    {
        'name': 'EMP-0002',
        'first_name': 'Tom',
        'last_name': 'Smith',
        'full_name': 'Tom Smith',
        'company': 'Company 2',
        'nationality': 'United States'
    },
    {
        'name': 'EMP-0003',
        'first_name': 'Andrew',
        'last_name': 'Sebastian',
        'full_name': 'Andrew Sebastian',
        'company': 'Company 3',
        'nationality': 'United States'
    },
    {
        'name': 'EMP-0005',
        'first_name': 'Ying Han',
        'last_name': 'Tan',
        'full_name': 'Ying Han Tan',
        'company': 'Company 1',
        'nationality': 'Australia'
    },
    {
        'name': 'EMP-0015',
        'first_name': 'Kenneth',
        'last_name': 'Ng',
        'full_name': 'Kenneth Ng',
        'company': 'Company 3',
        'nationality': 'United States'
    },
    {
        'name': 'EMP-0018',
        'first_name': 'Rubby',
        'last_name': 'Lee',
        'full_name': 'Rubby Lee',
        'company': 'Company 2',
        'nationality': 'Hong Kong'
    },
    {
        'name': 'EMP-0017',
        'first_name': 'Robert',
        'last_name': 'White',
        'full_name': 'Robert White',
        'company': 'Company 1',
        'nationality': 'United Kingdom'
    }
]

# Tugas 1: Mendapatkan daftar semua perusahaan dan mengurutkan berdasarkan nama perusahaan dalam urutan terbalik
def get_sorted_companies(company_detail_list):
    sorted_companies = sorted(company_detail_list, key=lambda x: x['name'], reverse=True)
    return [{"name": company['name']} for company in sorted_companies]

# Tugas 2: Mencetak semua nilai domain di setiap perusahaan
def print_company_domains(company_detail_list):
    for company in company_detail_list:
        print(f"{company['name']}: {company['domain']} ({company['country']})")

# Tugas 3: Menampilkan daftar semua karyawan berdasarkan domain perusahaan
def list_employees_by_domain(employee_detail_list, company_detail_list):
    domain_employees = {}
    company_domain_map = {company['name']: company['domain'] for company in company_detail_list}
    
    for employee in employee_detail_list:
        company = employee['company']
        domain = company_domain_map[company]
        if domain not in domain_employees:
            domain_employees[domain] = []
        domain_employees[domain].append(employee['full_name'])
    
    return domain_employees

# Tugas 4: Fungsi yang mengembalikan karyawan dengan negara perusahaannya
def get_employees_with_company_country(employee_detail_list, company_detail_list):
    company_country_map = {company['name']: company['country'] for company in company_detail_list}
    employees_with_country = []

    for employee in employee_detail_list:
        company = employee['company']
        country = company_country_map[company]
        employees_with_country.append({
            "full_name": employee['full_name'],
            "company": company,
            "country": country
        })

    return employees_with_country

# Tugas 5: Fungsi yang mengembalikan perusahaan dengan jumlah karyawan berdasarkan kewarganegaraan
from collections import defaultdict

def get_employee_nationality_count(employee_detail_list):
    company_nationality_count = defaultdict(lambda: defaultdict(int))
    
    for employee in employee_detail_list:
        company = employee['company']
        nationality = employee['nationality']
        company_nationality_count[company][nationality] += 1
    
    result = []
    for company, nationalities in company_nationality_count.items():
        result.append({
            "company": company,
            "employee_nationality": dict(nationalities)
        })
    
    return result

# Contoh pemanggilan fungsi
sorted_companies = get_sorted_companies(company_detail_list)
print(sorted_companies)

print("\nDomains:")
print_company_domains(company_detail_list)

print("\nEmployees by Domain:")
print(list_employees_by_domain(employee_detail_list, company_detail_list))

print("\nEmployees with Company Country:")
print(get_employees_with_company_country(employee_detail_list, company_detail_list))

print("\nEmployee Nationality Count:")
print(get_employee_nationality_count(employee_detail_list))
