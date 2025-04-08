def elabora_testo(testo):
    """
    Questa funzione prende una stringa e restituisce la versione in MAIUSCOLO con punti esclamativi.
    """
    if not testo:
        return "Nessun testo inserito!"
    return testo.upper() + "!!!"
