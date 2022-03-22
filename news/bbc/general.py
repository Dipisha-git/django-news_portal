from . models import CompanySettings


def data_pass(request):
    data = {
        'companyData': CompanySettings.objects.first()
    }
    return data
