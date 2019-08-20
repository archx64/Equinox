from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from blog.models import Post
from django.core.files.storage import FileSystemStorage
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from face_authenticate import face_image


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You are now able to login, {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def view_profile(request):
    return render(request, 'users/profile_view.html')


@login_required()
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'login_post': Post.objects.filter(author=request.user)
    }
    return render(request, 'users/profile.html', context)



def login_new(request):
    context = {'username': ''}

    next_request = request.GET.get('next')

    if request.method == 'POST' and 'identify' in request.POST:
        uploaded_image = request.FILES['face-image']

        fs = FileSystemStorage()
        fs.save("login.jpg", uploaded_image)

        context['username'] = face_image.main()

    if request.method == 'POST' and 'login' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_request:
                return redirect(next_request)
            return redirect('/')
    return render(request, 'users/login_new.html', context)
