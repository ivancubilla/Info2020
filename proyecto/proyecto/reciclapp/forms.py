from django import forms

material = (
    ("1", "Metal"),
    ("2", "Bombilla de Luz"),
    ("3", "Escombro"),
    ("4", "Carton"),
    ("5", "Vidrio"),
    ("6", "Madera"),
    ("7", "Desechos Electronicos"),
    ("8", "Baterias"),
)
locali = (
    ('1', 'Resistencia'),
    ('2', 'Barranqueras'),
    ('3', 'P.R.Saenz Peña'),
    ('4', 'Charata'),
    ('5', 'Fontana'),
    ('6', 'Las Breñas'),
    ('7', 'Villa Angela'),
    ('8', 'Castelli')
)


class PublicarForm(forms.Form):
    campomateriales = forms.ChoiceField(choices=material)
    imagen = forms.ImageField()
    peso_aprox = forms.IntegerField()
    campolocalidades = forms.ChoiceField(choices=locali)
