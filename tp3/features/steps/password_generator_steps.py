from behave import *
from password_generator import PasswordGenerator
import re

@when('je génère un mot de passe par défaut')
def step_impl(context):
    generator = PasswordGenerator()
    context.password = generator.generate_default()

@then('je dois obtenir un mot de passe de {length:d} caractères')
def step_impl(context, length):
    assert len(context.password) == length

@then('le mot de passe doit contenir au moins {count:d} caractères spéciaux')
def step_impl(context, count):
    special_chars = sum(1 for c in context.password if c in "!@#$%^&*()_+-=[]{}|;:,.<>?")
    assert special_chars >= count

@then('le mot de passe doit contenir au moins {count:d} chiffres')
def step_impl(context, count):
    digits = sum(1 for c in context.password if c.isdigit())
    assert digits >= count

@then('le mot de passe doit contenir au moins {count:d} lettres majuscules')
def step_impl(context, count):
    uppercase = sum(1 for c in context.password if c.isupper())
    assert uppercase >= count

@when('je génère un mot de passe avec les exigences suivantes')
def step_impl(context):
    generator = PasswordGenerator()
    row = context.table[0]
    requirements = {
        'min_length': int(row['longueur_min']),
        'min_special_chars': int(row['caracteres_speciaux_min']),
        'min_numbers': int(row['chiffres_min']),
        'min_uppercase': int(row['majuscules_min']),
        'exclude_similar': row['exclure_similaires'] == 'true',
        'exclude_ambiguous': row['exclure_ambigus'] == 'true'
    }
    context.password = generator.generate_custom(requirements)

@when('je génère un mot de passe mémorable')
def step_impl(context):
    generator = PasswordGenerator()
    context.password = generator.generate_memorable()

@then('je dois obtenir un mot de passe contenant {count:d} mots')
def step_impl(context, count):
    # On compte le nombre de groupes de caractères séparés par des caractères spéciaux
    words = re.split('[#$%&@]', context.password)
    assert len(words) == count

@then('les mots doivent être séparés par des caractères spéciaux')
def step_impl(context):
    assert any(c in context.password for c in ['#', '$', '%', '&', '@'])

@then('certains caractères doivent être remplacés par des chiffres')
def step_impl(context):
    assert any(c.isdigit() for c in context.password)

@given('un mot de passe "{password}"')
def step_impl(context, password):
    context.password = password

@when('je vérifie les exigences suivantes')
def step_impl(context):
    generator = PasswordGenerator()
    row = context.table[0]
    context.requirements = {
        'min_length': int(row['longueur_min']),
        'min_special_chars': int(row['caracteres_speciaux_min']),
        'min_numbers': int(row['chiffres_min']),
        'min_uppercase': int(row['majuscules_min'])
    }
    context.result = generator.verify_requirements(context.password, context.requirements)

@then('la vérification doit retourner {expected}')
def step_impl(context, expected):
    expected_bool = expected.lower() == 'vrai'
    assert context.result == expected_bool, f"Expected {expected_bool} but got {context.result}"