#distrito.
def dist(nombre):
    if nombre == 'ChamartÃ\xadn':
        return 'Chamartin'
    elif nombre== 'TetuÃ¡n':
        return 'Tetuan'
    elif nombre == 'ChamberÃ\xad':
        return 'Chamberí'
    elif nombre == 'VicÃ¡lvaro':
        return 'nombre'
    
#barrios
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
    
        
        
        
        
        
        
        
        
        
        