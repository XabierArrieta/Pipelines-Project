import os
def download_dataset():
    '''Downloads a dataset from kaggle and only keeps the csv in your data file. Beware of your own data structure:
    this creates a data directory and also moves all the .csv files next to your jupyter notebooks to it.
    Takes: url from kaggle
    Returns: a folder with the downloaded csv
    '''
    
    #Gets the name of the dataset.zip
    url = input("Introduce la url: ")
    
    #Gets the name of the dataset.zip
    endopint = url.split("/")[-1]
    user = url.split("/")[-2]
    
    #Download, decompress and leaves only the csv
    download = f"kaggle datasets download -d {user}/{endopint}; say -v Monica 'descargando'"
    decompress = f"tar -xzvf {endopint}.zip; say -v Monica 'descomprimiendo'"
    delete = f"rm -rf {endopint}.zip; say -v Monica 'borrando el zip'"
    make_directory = "mkdir data"
    lista = "ls >> archivos.txt"
    
    for i in [download, decompress, delete, make_directory, lista]:
        os.system(i)
    
    #Gets the name of the csv (you should only have one csv when running this code)
    lista_archivos = open('archivos.txt').read()
    nueva = lista_archivos.split("\n")
    
    #Moves the .csv into the data directory
    for i in nueva:
        if i.endswith(".csv"):
            move_and_delete = f"mv {i} data/dataset.csv; rm archivos.txt; say -v Monica 'moviendo el dataset'"
            return os.system(move_and_delete)





def cleaning_mad(mad):
    
    # Eliminar columnas no relevantes para el análisis.
    
    mad = .drop(['minimum_nights', 'last_review', 'reviews_per_month', 'calculated_host_listings_count', 'availability_365'], axis = 1 )
    # Contar valores nulos.

    mad.isnull().sum().sort_values(ascending=False)
    
    # Elimininar valores nulos.
    
    mad.dropna()
    
    # Eliminar valore duplicados.
    
    mad.drop_duplicates()
    
    # Mostrar distritos correctamente.

    def dist(nombre):
        if nombre == 'ChamartÃ\xadn':
            return 'Chamartin'
        elif nombre== 'TetuÃ¡n':
            return 'Tetuan'
        elif nombre == 'ChamberÃ\xad':
            return 'Chamberí'
        elif nombre == 'VicÃ¡lvaro':
            return 'nombre'
        
    # Reemplazar caracteres especiales en los barrios.
    
    def carac(nombre):
        if 'Ã¡' in nombre:
             return nombre.replace('Ã¡','á')
        elif 'Ã©' in nombre:
             return nombre.replace('Ã©','é')
        elif 'Ã\xad' in nombre: 
             return nombre.replace('Ã\xad','í')
        elif 'Ã³'in nombre:
             return nombre.replace('Ã³','ó')
        elif 'Ãº'in nombre:
             return nombre.replace('Ãº', 'ú')
        elif 'Ã¼' in nombre:
             return nombre.replace('Ã¼','ü')
        else:
             return nombre
    
        
            return mad
        
        
        
        
        
        