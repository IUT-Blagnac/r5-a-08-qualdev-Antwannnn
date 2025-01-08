import secrets
import string
import random
import re
from typing import List, Dict

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        self.similar_chars = "il1Lo0O"
        self.ambiguous_chars = "{}[]()/\'\"~,;:.<>"
        self.common_words = [
            "correct", "horse", "battery", "staple", "rainbow", "sunshine",
            "butterfly", "mountain", "ocean", "forest", "dragon", "phoenix"
        ] 

    def generate_default(self) -> str:
        """Génère un mot de passe par défaut de 16 caractères"""
        return self.generate_custom({
            'min_length': 16,
            'min_special_chars': 2,
            'min_numbers': 2,
            'min_uppercase': 2,
            'exclude_similar': False,
            'exclude_ambiguous': False
        })

    def generate_custom(self, requirements: Dict) -> str:
        """Génère un mot de passe selon des exigences spécifiques"""
        available_chars = self.lowercase
        password_chars = []
        length = requirements.get('min_length', 16)

        if requirements.get('exclude_similar', False):
            available_chars = ''.join(c for c in available_chars 
                                    if c not in self.similar_chars)
        if requirements.get('exclude_ambiguous', False):
            available_chars = ''.join(c for c in available_chars 
                                    if c not in self.ambiguous_chars)

        if requirements.get('min_uppercase', 0):
            password_chars.extend(secrets.choice(self.uppercase) 
                                for _ in range(requirements['min_uppercase']))
        if requirements.get('min_numbers', 0):
            password_chars.extend(secrets.choice(self.digits) 
                                for _ in range(requirements['min_numbers']))
        if requirements.get('min_special_chars', 0):
            password_chars.extend(secrets.choice(self.special_chars) 
                                for _ in range(requirements['min_special_chars']))

        remaining_length = length - len(password_chars)
        password_chars.extend(secrets.choice(available_chars) 
                            for _ in range(remaining_length))

        random.shuffle(password_chars)
        return ''.join(password_chars)

    def generate_memorable(self) -> str:
        """Génère un mot de passe mémorable basé sur des mots"""
        words = random.sample(self.common_words, 4)
        
        substitutions = {'a': '4', 'e': '3', 'i': '1', 'o': '0'}
        for i, word in enumerate(words):
            for old, new in substitutions.items():
                if random.random() < 0.3:  # 30% de chance de substitution
                    word = word.replace(old, new)
            words[i] = word

        separators = ['#', '$', '%', '&', '@']
        return ''.join(word + random.choice(separators) for word in words[:-1]) + words[-1]

    def verify_requirements(self, password: str, requirements: Dict) -> bool:
        """Vérifie si le mot de passe répond aux exigences"""
        if len(password) < requirements.get('min_length', 16):
            return False
        
        special_count = sum(1 for c in password if c in self.special_chars)
        if special_count < requirements.get('min_special_chars', 0):
            return False
            
        number_count = sum(1 for c in password if c.isdigit())
        if number_count < requirements.get('min_numbers', 0):
            return False
            
        upper_count = sum(1 for c in password if c.isupper())
        if upper_count < requirements.get('min_uppercase', 0):
            return False
            
        return True 