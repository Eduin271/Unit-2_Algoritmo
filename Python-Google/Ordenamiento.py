import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configurar las credenciales de la cuenta de servicio
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('python-sheet-379622-b4ac162ba532.json', scope)
client = gspread.authorize(creds)

# Abrir la hoja de cálculo y la hoja de trabajo deseada
sheet = client.open('Ordenamientos').sheet1

# Leer los datos de la hoja de cálculo
values = sheet.get_all_values()[1:]


# Implementar el algoritmo de ordenamiento de burbuja
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][0] > arr[j+1][0]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Implementar el algoritmo de ordenamiento por inserción
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key[0] < arr[j][0]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Implementar el algoritmo de ordenamiento por selección
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j][0] < arr[min_idx][0]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Llamar a los algoritmos de ordenamiento y escribir los datos ordenados en la hoja de cálculo
values_sorted_bubble = bubble_sort(values)
values_sorted_insertion = insertion_sort(values)
values_sorted_selection = selection_sort(values)

n = len(values_sorted_bubble)
for i in range(n):
    sheet.update_cell(i+2, 2, values_sorted_bubble[i][0])

n = len(values_sorted_insertion)
for i in range(n):
    sheet.update_cell(i+2, 3, values_sorted_insertion[i][0])

n = len(values_sorted_selection)
for i in range(n):
    sheet.update_cell(i+2, 4, values_sorted_selection[i][0])
