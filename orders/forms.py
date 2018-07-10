from django import forms
from django.contrib.auth.models import User
from orders.models import Order, Template, Profile
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.contrib.auth.forms import UserCreationForm

class PlaceOrderForm(forms.Form):
	outputOrg=forms.CharField(max_length=1000, label='',widget=forms.TextInput(attrs={'placeholder': 'Название организации', 'class': 'form-control'}))
	outputContact=forms.CharField(max_length=1000, label='', widget=forms.TextInput(attrs={'placeholder': 'ФИО контактного лица', 'class': 'form-control'}))
	outputNumber=forms.CharField(max_length=1000, label='', widget=forms.TextInput(attrs={'placeholder': 'Номер контактного лица', 'class': 'form-control'}))
	outputAdress=forms.CharField(max_length=1000, label='', widget=forms.TextInput(attrs={'placeholder': 'Адрес', 'class': 'form-control'}))

	inputOrg=forms.CharField(max_length=1000,label="",widget=forms.TextInput(attrs={'placeholder': 'Название организации', 'class': 'form-control'}))
	inputContact=forms.CharField(max_length=1000,label="", widget=forms.TextInput(attrs={'placeholder': 'ФИО контактного лица', 'class': 'form-control'}))
	inputNumber=forms.CharField(max_length=1000,label="", widget=forms.TextInput(attrs={'placeholder': 'Номер контактного лица', 'class': 'form-control'}))
	inputAdress=forms.CharField(max_length=1000,label="", widget=forms.TextInput(attrs={'placeholder': 'Адрес', 'class': 'form-control'}))

	cargoDescription=forms.CharField(required=False,max_length=1000,label="", widget=forms.TextInput(attrs={'placeholder': 'Опишите товар', 'class': 'form-control'}))
	weight=forms.IntegerField(required=False,label="",widget=forms.TextInput(attrs={'placeholder': 'Вес(кг)', 'class': 'form-control'}))
	comments=forms.CharField(required=False,max_length=2000,label="", widget=forms.Textarea(attrs={'placeholder': 'Комментарии', 'class': 'form-control', 'style':'resize: none;'}))
	attach1=forms.FileField(required=False,widget=forms.FileInput(attrs={'style':'display: none;', 'accept': "image/*,application/pdf"}))
	attach2=forms.FileField(required=False,widget=forms.FileInput(attrs={'style':'display: none;', 'accept': "image/*,application/pdf"}))
	attach3=forms.FileField(required=False,widget=forms.FileInput(attrs={'style':'display: none;', 'accept': "image/*,application/pdf"}))
	attach4=forms.FileField(required=False,widget=forms.FileInput(attrs={'style':'display: none;', 'accept': "image/*,application/pdf"}))

class OrderForm(forms.ModelForm):
	class Meta:
		model=Order
		fields=['outputOrg','outputContact','outputNumber','outputAdress',
		'inputOrg','inputContact','inputNumber','inputAdress','cargoDescripton','weight',
		'comments','attach1',
		'attach2','attach3','attach4', 'comments']
		widgets={
			'outputOrg' : forms.TextInput(attrs={'placeholder': 'Название организации', 'class': 'form-control','id': 'outputOrganization'}),
			'outputContact' : forms.TextInput(attrs={'placeholder': 'ФИО контакта', 'class': 'form-control','id': 'outputContact'}),
			'outputNumber' : forms.TextInput(attrs={'placeholder': 'Телефон контактного лица', 'class': 'form-control','id': 'outputNumber'}),
			'outputAdress' : forms.TextInput(attrs={'placeholder': 'Адрес', 'class': 'form-control','id': 'outputAdress'}),
			'inputOrg' : forms.TextInput(attrs={'placeholder': 'Название организации', 'class': 'form-control','id': 'inputOrganization'}),
			'inputContact' : forms.TextInput(attrs={'placeholder': 'ФИО контакта', 'class': 'form-control','id': 'inputContact'}),
			'inputNumber' : forms.TextInput(attrs={'placeholder': 'Телефон контактного лица', 'class': 'form-control','id': 'inputNumber'}),
			'inputAdress' : forms.TextInput(attrs={'placeholder': 'Адрес', 'class': 'form-control','id': 'inputAdress'}),
			'cargoDescripton' : forms.TextInput(attrs={'placeholder': 'Опишите товар(Реагенты, мед сырье...)', 'class': 'form-control'}),
			'weight' : forms.NumberInput(attrs={'placeholder': 'Вес в кг', 'class': 'form-control'}),
			'attach1' : forms.FileInput(attrs={'style':'display: none;', 'accept': "image/*,application/pdf", 'onchange': '$("#kartinka1").attr("class","glyphicon glyphicon-ok")'}),
			'attach2' : forms.FileInput(attrs={'style':'display: none;', 'accept': "image/*,application/pdf", 'onchange': '$("#kartinka2").attr("class","glyphicon glyphicon-ok")'}),
			'attach3' : forms.FileInput(attrs={'style':'display: none;', 'accept': "image/*,application/pdf", 'onchange': '$("#kartinka3").attr("class","glyphicon glyphicon-ok")'}),
			'attach4' : forms.FileInput(attrs={'style':'display: none;', 'accept': "image/*,application/pdf", 'onchange': '$("#kartinka4").attr("class","glyphicon glyphicon-ok")'}),
			'comments' : forms.Textarea(attrs={'placeholder':'Напишите сюда любые комментарии, которые могут понадобится логисту или водителю(Нужны грузчики, хрупкий груз, температурный режим)', 'class': 'form-control', 'style': 'resize: none;'})
		}

class TemplateForm(forms.ModelForm):
	class Meta:
		model=Template
		fields=['name','organization','contact','number','adress']
		widgets={
		'name' : forms.TextInput(attrs={'placeholder': 'Название шаблона', 'class': 'form-control'}),
		'organization' : forms.TextInput(attrs={'placeholder': 'Название организации', 'class': 'form-control'}),
		'contact' : forms.TextInput(attrs={'placeholder': 'ФИО контактного лица', 'class': 'form-control'}),
		'number' : forms.TextInput(attrs={'placeholder': 'Телефон контактного лица', 'class': 'form-control'}),
		'adress' : forms.TextInput(attrs={'placeholder': 'Адрес', 'class': 'form-control'})
		}
		error_messages={
				'unique': "Шаблон с таким названием уже существует",
		}

class RegistrationForm(UserCreationForm):
	pass

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = {
		'username'
		}
	# error_messages = {
	# 	'password_mismatch': _("The two password fields didn't match"),
	# }
	# password1 = forms.CharField(label=_("Password"),
	# 	widget=forms.PasswordInput)
	# password2 = forms.CharField(label=_("Password povtor"),
	# 	widget=forms.PasswordInput,
	# 	help_text=_("Enter the same password as above, for verification"))


	# class Meta:
	# 	model = User
	# 	fields = {
	# 	'username',
	# 	'password1',
	# 	'password2'
	# 	}

	# def save(self, commit=True):
	# 	user = super(RegistrationForm, self).save(commit=False)
	# 	# user.first_name = cleaned_data('first_name')
	# 	# user.last_name = cleaned_data('last_name')
	# 	# user.email = cleaned_data('email')

	# 	if commit:
	# 		user.save()

	# 	return user

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = {
		'family_name',
		'first_name',
		'last_name',
		'email',
		'phone_number',
		'inside_number',
		}

	# def clean_name(self):
	# 	data=self.cleaned_data
	# 	name=data.get('name')
	# 	objects=Template.objects.filter(name=name)
	# 	if len(objects)>0:
	# 		raise ValidationError('fuck')
	# 	return None

	# def clean(self):
	# 	cleaned_data=self.cleaned_data

	# 	name=cleaned_data.get('name')
	# 	objects=Template.objects.filter(name=name)

	# 	if len(objects) > 0:
	# 		raise ValidationError("fuck")

	# 	return self.cleaned_data

	# def clean(self):
	# 	cleaned_data=self.cleaned_data

	# 	field=cleaned_data.get('name')

	# 	objects=Template.objects.filter(name=field)

	# 	if len(objects) > 0:
	# 		msg="Шаблон с таким именем уже существует"
	# 		self._errors["field"]=self.error_class([msg])
	# 		# del cleaned_data["field"]
	# 		raise ValidationError(msg)

	# 	return cleaned_data

