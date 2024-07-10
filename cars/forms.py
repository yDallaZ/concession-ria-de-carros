from django import forms
from cars.models import Brand, Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
    
    def clean_value(self):
        value = self.cleaned_data['value']
        if value < 20000:
         self.add_error('value', 'valor mínimo do carro deve ser de R$20.000')
        return value
    
    def clean_factory_year(self):
       factory_year = self.cleaned_data['factory_year']
       if factory_year < 1975:
          self.add_error('factory_year', 'ano de fabricação deve ser maior que 1975')
       return factory_year 
        

       

