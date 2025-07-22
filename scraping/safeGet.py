async def safe_get(locator, attr: str = None) -> str:
    """
    Récupère de manière sécuritaire le contenu texte ou un attribut d’un locator.
    Si l’élément n’existe pas ou l’attribut est manquant, retourne "-".
    """
    if await locator.count() == 0:
        return "-"
    if attr:
        return await locator.get_attribute(attr) or "-"
    return (await locator.text_content() or "-").strip()
