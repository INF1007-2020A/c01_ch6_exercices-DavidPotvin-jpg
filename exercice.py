#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> bool:
    if values is None:
        # TODO: Demander les valeurs ici
        values = [input("Enter ...") for _ in range(10)]
        return values == sorted(values)

    return False


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: Demander les mots ici
        mot1 = list(input("Enter the first word : ")).sort()
        mot2 = list(input("Enter the second word : ")).sort()
        if mot1 == mot2:
            return True

    return False


def contains_doubles(items: list) -> bool:
    return len(items) != len(set(items))

def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    max_sum = 0
    best_student = ''
    best_average = 0.0
    for student, notes in student_grades:
        print(student, notes)
        # if sum(notes) > max_sum:
        #     max_sum = sum(notes)
        #     best_student = student
        #     best_average = sum(notes)/len(notes)
    return {best_student : best_average}


def histogram(sentence: str) -> tuple:
    # TODO: Créer l'histogramme a l'aide d'un dictionnaire
    #       Afficher l'histogramme et les lettres les plus fréquentes
    #       Retourner l'histogramme et le tableau de lettres

    return {}, []


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données
    nom_recette = input("Enter the name of the recipe : ")
    ingredients = input("Quels ingredient contient la recette ? : ")
    return {nom_recette: ingredients}


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    nom_recette = input("Enter the name of the recipe : ")
    if nom_recette in ingredients:
        print(f"{nom_recette} contient {ingredients[nom_recette]}")




def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    #name, result = best_grades(grades)
    #print(f"{name} a la meilleure moyenne: {result}")
    
    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
