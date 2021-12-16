from django import forms

class AlumnoFormulario(forms.Form):
    nombreAlumno = forms.CharField(max_length = 40)
    apellidoAlumno = forms.CharField(max_length = 40)
    edadAlumno = forms.IntegerField()


class ProfesorFormulario(forms.Form):
    nombreProf = forms.CharField(max_length = 40)
    apellidoProf = forms.CharField(max_length = 40)
    aniosEjerciendo = forms.IntegerField()

class MateriaFormulario(forms.Form):
    nombreMateria = forms.CharField(max_length = 40)
    obligatoria = forms.BooleanField()