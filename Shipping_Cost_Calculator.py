# Shipping Cost Calculator

def get_positive_float(prompt):
    """Demande à l'utilisateur une valeur flottante positive avec validation."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Erreur : La valeur doit être positive ou nulle. Veuillez réessayer.")
                continue
            return value
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")
        except EOFError:
            print("\nEntrée interrompue. Programme terminé.")
            exit(0)

## Input package weight and shipping rate with validation
weight = get_positive_float("Enter the package weight in kilograms: ")
rate = get_positive_float("Enter the shipping rate per kilogram: ")

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost:.2f} USD")
