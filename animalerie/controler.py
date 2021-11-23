# import models as Model


class Controler:
    def check():
        return None


# def nourrir(id_animal):
#     if Model.lit_etat(id_animal) is not None:
#         if Model.lit_etat(id_animal) != 'affame':
#             print('Desole,', id_animal, "n'a pas faim...")
#             return False
#         elif Model.verif_dispo('mangeoire') != 'libre':
#             occupant = Model.cherche_occupant('mangeoire')
#             print('Desole, la mangeoire est occupee par', occupant)
#             return False
#         else:
#             Model.change_etat(id_animal, 'repus')
#             Model.change_lieu(id_animal, 'mangeoire')
#             return True
#     else:
#         print("Desole,", id_animal, "n'est pas un animal connu")
#         return False

# def divertir(id_animal):
#     if Model.lit_etat(id_animal) is not None:
#         if Model.lit_etat(id_animal) != 'repus':
#             print('Desole,', id_animal, "n'est pas en etat de faire du sport.")
#             return False
#         elif Model.verif_dispo('roue') != 'libre':
#             occupant = Model.cherche_occupant('roue')
#             print('Desole, la roue est occupee par', occupant)
#             return False
#         else:
#             Model.change_etat(id_animal, 'fatigue')
#             Model.change_lieu(id_animal, 'roue')
#             return True
#     else:
#         print("Desole,", id_animal, "n'est pas un animal connu")
#         return False

# def coucher(id_animal):
#     if Model.lit_etat(id_animal) is not None:
#         if Model.lit_etat(id_animal) != 'fatigue':
#             print('Desole,', id_animal, "n'est pas fatigue.")
#             return False
#         elif Model.verif_dispo('nid') != 'libre':
#             occupant = Model.cherche_occupant('nid')
#             print('Desole, le nid est occupe par', occupant)
#             return False
#         else:
#             Model.change_etat(id_animal, 'endormi')
#             Model.change_lieu(id_animal, 'nid')
#             return True
#     else:
#         print("Desole,", id_animal, "n'est pas un animal connu")
#         return False


# def reveiller(id_animal):
#     if Model.lit_etat(id_animal) is not None:
#         if Model.lit_etat(id_animal) != 'endormi':
#             print('Desole,', id_animal, "ne dort pas.")
#             return False
#         else:
#             Model.change_etat(id_animal, 'affame')
#             Model.change_lieu(id_animal, 'litière')
#             return True
#     else:
#         print("Desole,", id_animal, "n'est pas un animal connu")
#         return False

