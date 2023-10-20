# from app.models import InformationFormUpdate
# from django.shortcuts import render, redirect
# from app.app_views import user_authenticate
#
#
# def edit_profile(request):
#     context_var = user_authenticate.user_authenticate(request)
#
#     if request.method == "POST":
#         form = InformationFormUpdate(request.POST)
#         if form.is_valid():
#             # form.fields.save()
#             return redirect('profile', permanent=True)
#     else:
#         form = InformationFormUpdate()
#     context_var.update({'form': form})
#     return render(request, 'app/edit_profile.html', context=context_var)
