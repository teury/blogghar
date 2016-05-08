from django import forms

from allauth.account import forms as allauth_forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import StrictButton


class CustomLoginForm(allauth_forms.LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()
        self.helper = FormHelper(self)
        self.helper.col_class = False
        self.helper.form_tag = False
        self.helper.form_show_labels = True

        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = None
            del self.fields[field].widget.attrs['placeholder']

        self.helper.layout = Layout(
            'login', 'password', 'remember',
            StrictButton(
                'Sign In', type='submit', style='margin-top: 10px',
                css_class="waves-effect btn-large blue waves-light btn right"),
        )


class CustomChangePwdForm(allauth_forms.ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomChangePwdForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_show_labels = True

        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = None
            del self.fields[field].widget.attrs['placeholder']

        self.helper.layout = Layout(
            'oldpassword', 'password1', 'password2',
            StrictButton(
                'Change Password', type='submit', name='action',
                css_class='btn blue waves-effect waves-light btn-large')
        )


class CustomAddEmailForm(allauth_forms.AddEmailForm):
    def __init__(self, *args, **kwargs):
        super(CustomAddEmailForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_show_labels = True

        self.fields['email'].widget.attrs['placeholder'] = None
        self.fields['email'].label = 'Email Address'

        del self.fields['email'].widget.attrs['placeholder']

        self.helper.layout = Layout(
            'email',
            StrictButton(
                'Add Email', name='action_add', type='submit',
                css_class='btn blue btn-large white-text waves-effect waves-light')  # noqa
        )


class CustomResetPwdForm(allauth_forms.ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomResetPwdForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_show_labels = True

        del self.fields['email'].widget.attrs['placeholder']
        self.fields['email'].label = "Email Address"

        self.helper.layout = Layout(
            'email',
            StrictButton(
                'Reset My Password', type='submit',
                css_class='btn blue btn-large waves-effect waves-light')
        )
