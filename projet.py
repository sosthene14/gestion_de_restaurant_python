# Ces deux lignes importent les modules sys et datetime pour être utilisés dans le programme.
import sys
import datetime

# Ceci est un dictionnaire qui contient des articles de fast-food avec leurs noms et leurs prix respectifs.
fast_food = {
    1: ['Hamburger', 2500],
    2: ['Les Deluxe Potatoes', 3000],
    3: ['Chicken McNuggets', 1500]
}
# Ceci est un dictionnaire qui contient les options de plat du jour avec leurs noms et leurs prix respectifs.
menu_day_food = {
    1: ["Sandwichs poulet au curry", 3500],
    2: ["Bircher aux flocons d’avoine et aux fruits", 5000],
    3: ["Brioche au sucre fourrée à la crème", 4000],
    4: ["Chaussons aux pommes", 2000]
}
dictionnary_for_foods_name = {}
# Ceci est un tuple qui contient les options de menu disponibles pour l'utilisateur.
menu_option = ("1- Plat du jour", "2- Fast Food", "3- Caisse", "4- Quitter")
menu_option_size = len(menu_option)

# Ceci définit le choix d'utilisateur par défaut sur 0.

default_user_choice = 0

# Ces deux lignes stockent la longueur de la liste fast_food
# et menu_day_food, qui est le nombre d'articles de nourriture dans chacun des dictionnaires.
size_fast_food_list = len(fast_food)
size_menu_day_food = len(menu_day_food)
user_command_available = 0


# Ceci est la fonction main_menu qui affiche les options de menu en boucle et appelle la fonction get_user_input.

def main_menu():
    for i in menu_option:
        print(i)
    get_user_input()


# Ceci est la fonction interval_of_user_choice qui prend en entrée un début et une fin
# et renvoie une plage de valeurs entre start et end.

def interval_of_user_choice(start, end):
    return range(start, end)


# affiche un message d'erreur lorsque l'utilisateur saisit
# une option non valide et appelle la fonction passée en argument.

def action_if_error(function):
    print("Choix erroné,veuillez reesayer")
    function()


# définit l'intervalle de choix pour les options du menu et demande à l'utilisateur de faire son choix.
# Si le choix n'est pas un nombre ou n'est pas dans l'intervalle, il affiche un message d'erreur et demande à nouveau.

def define_interval_for_choices(end_intervale, increment):
    global default_user_choice
    interval = interval_of_user_choice(1, end_intervale + increment + 1)
    user_input = input("Veuillez faire votre choix :\n")
    while not user_input.isdigit() or int(user_input) not in interval:
        print("Choix erroné ")
        user_input = input("Reeseyer ")
    default_user_choice = int(user_input)
    return True


# appelle la fonction define_interval_for_choices pour définir l'intervalle de choix et renvoie interface_to_go.
def get_user_input():
    if define_interval_for_choices(menu_option_size, 1):
        return interface_to_go(int(default_user_choice))


# prend en charge les choix de l'utilisateur en fonction de la valeur de choice.
# S'il choisit 1, il charge le dictionnaire menu_day_food et appelle la fonction menu_of_the_day.
# S'il choisit 2, il charge le dictionnaire fast_food et appelle également la fonction menu_of_the_day.
# S'il choisit 3, il appelle la fonction caisse.
# Si l'utilisateur choisit 4, le programme quitte en affichant un message "A Bientôt".
def interface_to_go(choice):
    global dictionnary_for_foods_name, user_command_available
    if choice == 1:
        dictionnary_for_foods_name = menu_day_food
        user_command_available = size_menu_day_food
        menu_of_the_day()
    elif choice == 2:
        dictionnary_for_foods_name = fast_food
        user_command_available = size_fast_food_list
        menu_of_the_day()
    elif choice == 3:
        caisse()
    else:
        sys.exit(print("A Bientot"))


# La fonction menu_of_the_day() affiche le menu du jour et permet à l'utilisateur de sélectionner
# un plat. La fonction appelle define_interval_for_choices() pour valider l'entrée
# de l'utilisateur, puis appelle menu_of_the_day_choice() avec le choix sélectionné.

def menu_of_the_day():
    print(f"{'*' * 20} Plats du jour {'*' * 20}")
    for i in dictionnary_for_foods_name:
        print(f"{i} -  {dictionnary_for_foods_name[i][0]} -- {dictionnary_for_foods_name[i][1]} FCFA")
    print(f"{len(dictionnary_for_foods_name) + 1} -  Retour")

    if define_interval_for_choices(len(dictionnary_for_foods_name), 1):
        return menu_of_the_day_choice(default_user_choice)


# La fonction menu_of_the_day_choice() vérifie si le menu sélectionné est du fast-food ou non.
# S'il ne l'est pas, elle demande à l'utilisateur s'il veut voir les détails du plat qu'il a choisi.
# Si oui, elle appelle show_foods_details(). Si non, elle appelle ask_for_command().
# Si le menu sélectionné est du fast-food, elle appelle directement ask_for_command().

def menu_of_the_day_choice(choice):
    global default_user_choice
    if dictionnary_for_foods_name != fast_food:
        if choice == 1:
            default_user_choice = 1
            yes_or_no_foods_details()
        elif choice == 2:
            default_user_choice = 2
            yes_or_no_foods_details()
        elif choice == 3:
            default_user_choice = 3
            yes_or_no_foods_details()
        elif choice == 4:
            default_user_choice = 4
            yes_or_no_foods_details()
        elif len(dictionnary_for_foods_name) + 1:
            main_menu()
    else:
        if choice == 1:
            default_user_choice = 1
            ask_for_command()
        elif choice == 2:
            default_user_choice = 2
            ask_for_command()
        elif choice == 3:
            default_user_choice = 3
            ask_for_command()
        else:
            main_menu()


# La fonction yes_or_no_foods_details() demande à l'utilisateur s'il veut voir les détails
# du plat qu'il a choisi. Si l'utilisateur répond "oui", elle appelle show_foods_details().
# Si l'utilisateur répond "non",
# elle appelle ask_for_command(). Si l'entrée est invalide, elle répète la question.

def yes_or_no_foods_details():
    details = input("Voulez vous voir les détails de ce plat ? o/n\n").lower()
    if details == "o":
        show_foods_details()
    elif details == "n":
        ask_for_command()
    else:
        print("choix erroné, veuillez reeseyer")
        yes_or_no_foods_details()


# La fonction open_file_where_food_details_are() ouvre le fichier
# listOfFood.txt et retourne le contenu divisé par le séparateur "***".

def open_file_where_food_details_are():
    with open('listOfFood.txt', 'r', encoding='UTF-8') as food_file:
        file = food_file.read()
        list_food = file.split("***")
        return list_food


# La fonction show_foods_details() affiche les détails du plat sélectionné par l'utilisateur
# en appelant la fonction open_file_where_food_details_are().
# Elle appelle ensuite la fonction ask_for_command() pour demander à l'utilisateur s'il souhaite commander.
def show_foods_details():
    print(open_file_where_food_details_are()[default_user_choice - 1])
    ask_for_command()


# La fonction ask_for_command() demande à l'utilisateur s'il souhaite commander en utilisant
# la fonction input(). Si l'utilisateur répond "o", la fonction check_command_availability() est
# appelée. Si l'utilisateur répond "n", la fonction menu_of_the_day() est appelée. Si la réponse n'est pas valide,
# la fonction action_if_error() est appelée avec la fonction ask_for_command() en argument.

def ask_for_command():
    command = input("Voulez vous commander ? o/n\n").lower()
    if command == "o":
        check_command_availability()
    elif command == "n":
        menu_of_the_day()
    else:
        action_if_error(ask_for_command())


# La fonction check_command_availability() vérifie si l'utilisateur peut commander un nouveau plat.
# Si c'est possible, la fonction initialise_command() est appelée.
# Si ce n'est pas le cas, un message d'erreur est affiché et la fonction main_menu() est appelée

def check_command_availability():
    if user_command_available > 0:
        initialise_command()
    else:
        print("Désolé, Vous avez atteint votre nombre maximal de commandes")
        main_menu()


# Les variables total_cost et total_cost_list sont déclarées pour enregistrer
# le coût total des commandes. La variable command_number est déclarée pour enregistrer le nombre de plats commandés.

total_cost = 0
total_cost_list = []
command_number = 0


# La fonction initialise_command() demande à l'utilisateur le nombre de plats qu'il souhaite
# commander en utilisant la fonction input(). Si la réponse est un nombre valide et inférieure
# ou égale au nombre de plats disponibles, la commande est effectuée avec succès et le ticket de commande est généré.
# Sinon, un message d'erreur est affiché et la fonction command_again() est appelée.
def initialise_command():
    global user_command_available, total_cost, command_number
    command_number = input("Veuillez saisir le nombre de plats que vous souhaiter commander ")
    if command_number.isdigit():
        if 1 <= int(command_number) <= user_command_available:
            print("Commande effectué avec succès")
            total_cost = (dictionnary_for_foods_name[default_user_choice][1] * int(command_number))
            total_cost_list.append(total_cost)
            command_number = int(command_number)
            user_command_available = user_command_available - int(command_number)
            generate_ticket()
            command_again()
        else:
            print("Vous ne pouvez pas commander plus de 4 plats par jour")
            command_again()
    else:
        action_if_error(initialise_command())


# La variable total_selling_list est déclarée pour enregistrer le montant total des ventes.
total_selling_list = []


# La fonction generate_ticket génère un ticket de caisse pour la commande du client.
# Elle utilise la bibliothèque datetime pour obtenir la date actuelle et l'utilise pour nommer
# le fichier de ticket avec la date et l'heure d'impression. Elle écrit les détails de la commande
# dans le fichier ticket, tels que le nom et le prix du plat commandé, le prix total et la date d'impression.
# Elle vide également la liste total_cost_list pour préparer la prochaine commande.

def generate_ticket():
    global total_cost_list, total_selling_list
    now = datetime.datetime.now()
    ticket_name = now.strftime("%d%m%Y%H%M%S.txt")
    ticket_impression_date = now.strftime("%d/%m/%Y, %H:%M:%S")
    with open(ticket_name, 'w', encoding='UTF-8') as file:
        file.write(
            f"RESTAURANT\nNom : {dictionnary_for_foods_name[default_user_choice][0]} ({command_number})"
            f" {dictionnary_for_foods_name[default_user_choice][1]} FCFA\nTotal : {sum(total_cost_list)} FCFA\n"
            f"Date d'impression : {ticket_impression_date} ...Merci")
    total_selling_list.append(sum(total_cost_list))
    generate_all_selling_ticket(ticket_name)
    total_cost_list = []


# La fonction generate_all_selling_ticket ajoute
# les détails de vente de chaque ticket de caisse à un fichier de ventes appelé ventes.txt

def generate_all_selling_ticket(ticket_name):
    with open(ticket_name, "r", encoding='UTF-8') as file:
        for i, line in enumerate(file):
            if i == 2 - 1:
                desired_line = line
                break
        with open('ventes.txt', 'a', encoding='UTF-8') as files:
            files.write(desired_line + "\n")


# La fonction caisse lit le fichier de ventes et affiche le montant total des ventes. Si le fichier de ventes
# n'existe pas, un message d'erreur est affiché indiquant qu'il n'y a pas encore eu de ventes.

def caisse():
    try:
        with open('ventes.txt', 'r', encoding='UTF-8') as files:
            selling_file = files.read()
            selling_list = selling_file.split()
            if len(selling_list) > 0:
                print(
                    f"Voici les ventes :\n{selling_file}Le Montant Total des ventes est de : {sum(total_selling_list)} FCFA")
                main_menu()
            else:
                print("Vous n'avez aucune vente pour l'instant")
                main_menu()
    except FileNotFoundError:
        print("Vous n'avez effectué aucune vente pour l'instant")
        main_menu()


# La fonction command_again demande au client s'il souhaite commander un autre plat. Si oui,
# il est redirigé vers le menu du jour. Sinon, il est redirigé vers le menu principal.
def command_again():
    command = input("Voulez vous un autre plat du jour ? o/n\n").lower()
    if command == "o":
        menu_of_the_day()
    elif command == "n":
        main_menu()
    else:
        action_if_error(initialise_command())


if __name__ == '__main__':
    main_menu()
